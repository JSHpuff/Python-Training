import os
import uuid
import requests
import tkinter as tk
from threading import Thread
from PIL import Image, ImageTk
from tkinter import ttk


class PictureDownload(Thread):
    def __init__(self, url):
        super().__init__()
        self.picture_file = None
        self.url = url

    def run(self):
        try:
            # 建立資料夾
            os.makedirs('./assets', exist_ok=True)

            # 下載圖片
            response = requests.get(self.url)
            response.raise_for_status()

            # 隨機命名
            picture_name = str(uuid.uuid4())
            picture_file = f'./assets/{picture_name}.jpg'

            # 寫入圖片
            with open(picture_file, 'wb') as f:
                f.write(response.content)

            self.picture_file = picture_file
        except Exception as e:
            print(f"❌ Download failed: {e}")
            self.picture_file = None


class App(tk.Tk):
    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.resizable(False, False)
        self.title('Image Viewer')

        # Progress Frame
        self.progress_frame = ttk.Frame(self)
        self.progress_frame.columnconfigure(0, weight=1)
        self.progress_frame.rowconfigure(0, weight=1)

        self.pb = ttk.Progressbar(
            self.progress_frame,
            orient=tk.HORIZONTAL,
            mode='indeterminate'
        )
        self.pb.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)
        self.progress_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Picture Frame
        self.picture_frame = ttk.Frame(self)
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas = tk.Canvas(self.picture_frame, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, column=0)
        self.picture_frame.grid(row=0, column=0)

        # Button
        btn = ttk.Button(self, text='Next Picture')
        btn['command'] = self.handle_download
        btn.grid(row=1, column=0)

    def start_downloading(self):
        self.progress_frame.tkraise()
        self.pb.start(20)

    def stop_downloading(self):
        self.picture_frame.tkraise()
        self.pb.stop()

    def set_picture(self, file_path):
        try:
            pil_img = Image.open(file_path)
            resized_img = pil_img.resize((self.canvas_width, self.canvas_height), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(resized_img)
            self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        except Exception as e:
            print(f"❌ Failed to load image: {e}")

    def handle_download(self):
        self.start_downloading()

        url = 'https://picsum.photos/640/480'
        download_thread = PictureDownload(url)
        download_thread.start()

        self.monitor(download_thread)

    def monitor(self, download_thread):
        if download_thread.is_alive():
            self.after(100, lambda: self.monitor(download_thread))
        else:
            self.stop_downloading()
            if download_thread.picture_file:
                self.set_picture(download_thread.picture_file)
            else:
                print("⚠️ No image downloaded.")


if __name__ == "__main__":
    app = App(640, 480)
    app.mainloop()
