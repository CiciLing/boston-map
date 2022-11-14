import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


class ExampleApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1300x1000")
        self.previous_x = self.previous_y = 0
        self.x = self.y = 0
        self.points_recorded = []
        self.canvas = tk.Canvas(self.root, width=1300, height=1000, cursor="cross")
        self.button_print = tk.Button(self.canvas, text = "Display points", command = self.print_points)
        self.button_print.place(x = 1500,y = 800)
        #self.button_print.pack(side=tk.RIGHT)
        self.button_clear = tk.Button(self.canvas, text = "Clear", command = self.clear_all)
        self.button_clear.place(x = 1500,y = 900)
        #self.button_clear.pack(side=tk.RIGHT)
        self.image = Image.open("map.png")
        self.image = self.image.resize((1300, 1000))
        self.image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.canvas.pack(anchor='nw')
        self.canvas.bind("<Motion>", self.tell_me_where_you_are)
        self.canvas.bind("<B1-Motion>", self.draw_from_where_you_are)
        self.root.mainloop()

    def clear_all(self):
        self.canvas.delete("all")

    def print_points(self):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()
        self.canvas.create_line(self.points_recorded, fill = "red")
        self.points_recorded[:] = []

    def tell_me_where_you_are(self, event):
        self.previous_x = event.x
        self.previous_y = event.y

    def draw_from_where_you_are(self, event):
        if self.points_recorded:
            self.points_recorded.pop()
            self.points_recorded.pop()

        self.x = event.x
        self.y = event.y
        self.canvas.create_line(self.previous_x, self.previous_y,
                                self.x, self.y,fill="red")
        self.points_recorded.append(self.previous_x)
        self.points_recorded.append(self.previous_y)
        self.points_recorded.append(self.x)
        self.points_recorded.append(self.x)
        self.previous_x = self.x
        self.previous_y = self.y

if __name__ == "__main__":
    app = ExampleApp()
    print(app.points_recorded)

