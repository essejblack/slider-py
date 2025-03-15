import tkinter as tk

class SliderApp(tk.Tk):
    def __init__(self, image_files,x,y,delay):
        tk.Tk.__init__(self)
        self.geometry("+%d+%d" % (x, y)) # self.geometry("+ {}+ {}"format(x,y))
        self.delay = delay
        self.image_files = image_files
        self.pictures = [tk.PhotoImage(file=image) for image in image_files]
        self.index = 0
        self.pictures_display = tk.Label(self)
        self.pictures_display.pack()

    def show_slides(self):
        img_obj = self.pictures[self.index]
        img_name = self.image_files[self.index]
        self.pictures_display.config(image=img_obj)
        self.title(img_name)
        self.index = (self.index + 1) % len(self.pictures)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()

    def start(self):
        self.show_slides()
        self.run()


delay = 3500
image_files = [
    '1.png',
    '2.png',
    '3.png'
]
x = 10
y = 5
app = SliderApp(image_files,x,y,delay)
app.start()