import tkinter as tk
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Tkinter Matplotlib Demo")

        # Prepare Data
        data = {
            'Python':   11.27,
            'C':        11.16,
            'Java':     10.46,
            'C++':      7.5,
            'C#':       5.26
        }

        languages = data.keys()
        popularity = data.values()

        # Create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # Create FigureCanvasTkAgg Object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # Create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # Create axes
        axes = figure.add_subplot()

        # Create the barchart
        axes.bar(languages,popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=1
        )

if __name__ == "__main__":

    app = App()

    app.mainloop()
