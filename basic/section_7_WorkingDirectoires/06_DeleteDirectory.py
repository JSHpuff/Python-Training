import os

dir = os.path.join("C:\\", "temp", "python")

if os.paht.exists(dir):
    os.rmdir(dir)
    print(dir + ' is removed.')
