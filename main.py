# !/usr/bin/python3
import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import N, E

import matplotlib
matplotlib.use("TkAgg")

class DisplayImage:
    def __init__(self):
        self.image_file = None
        self.my_image = None
        self.label_text = None

    def show_image(self, top_wrapper, my_canvas_wrapper, label_wrapper):
        top_wrapper[0].title('Simple Image')

        #TODO make sure you change this to some other image.
        self.image_file = PhotoImage(file='/home/lisa/data/art/butterfly_lilies_print_small.gif')
        self.my_image = my_canvas_wrapper[0].create_image(700, 700, image=self.image_file)

        self.label_text = "Image: butterfly lilies"
        label_wrapper[0] = tk.Label(text=self.label_text)
        label_wrapper[0].grid(row=900, column=10, pady=5, padx=10, columnspan=10)

        my_canvas_wrapper[0].grid(row=10, column=10, pady=10, padx=10)

        print("show Image")

        top_wrapper[0].title('Simple Image')

    @staticmethod
    def hide_image(top_wrapper, my_canvas_wrapper, label_wrapper):
        top_wrapper[0].title('           ')
        label_wrapper[0] = tk.Label(text="                                                ")
        label_wrapper[0].grid(row=900, column=10, pady=5, padx=10, columnspan=10)
        print("hide Image")
        my_canvas_wrapper[0].grid_remove()


class DisplayGraph:

    @staticmethod
    def show_graph(top_wrapper, my_canvas_wrapper, label_wrapper, original_data):
        # code leveraged: http://web.cs.ucdavis.edu/~amenta/w13/canvasPlot.py
        # The window is an object of type tk
        top_wrapper[0].title('Simple Plot')

        # we put it into the root window
        my_canvas_wrapper[0] = Canvas(top_wrapper[0], width=1000, height=1000, bg='white')
        # figures out how the canvas sits in the window
        my_canvas_wrapper[0].grid(row=10, column=10, pady=10, padx=10)

        # draw x and y axes
        my_canvas_wrapper[0].create_line(100, 900, 900, 900, width=8)
        my_canvas_wrapper[0].create_line(100, 15, 100, 900, width=8)

        # markings on x axis
        for i in range(15):
            x = 100 + (i * 50)
            my_canvas_wrapper[0].create_line(x, 890, x, 900, width=2)
            my_canvas_wrapper[0].create_text(x, 920, text='%d' % (30 * i), anchor=N)

        # markings on y axis
        for i in range(22):
            y = 900 - (i * 40)
            my_canvas_wrapper[0].create_line(90, y, 100, y, width=2)
            my_canvas_wrapper[0].create_text(90, y, text='%5.1f' % (40 * i), anchor=E)

        # draw the wiggly line
        my_canvas_wrapper[0].create_line(original_data, fill='green', width=8)

        label_wrapper[0] = tk.Label(text="                                                ")
        label_wrapper[0].grid(row=900, column=10, pady=5, padx=10, columnspan=10)
        label_wrapper[0] = tk.Label(text ="Graph")
        label_wrapper[0].grid(row=900, column=10, pady=5, padx=10, columnspan=10)
        my_canvas_wrapper[0].grid()
        print("showGraph")

    @staticmethod
    def hide_graph(topWrapper, myCanvasWrapper, labelWrapper):
        labelWrapper[0] = tk.Label(text="                                                ")
        labelWrapper[0].grid(row=900, column=10, pady=5, padx=10, columnspan=10)
        myCanvasWrapper[0].grid_remove()
        print("hideGraph")


def main():

    display_graph = DisplayGraph()
    display_image = DisplayImage()
    # callback for button

    def change_canvas_callback(toggle_wrapper, my_canvas_wrapper, top_wrapper, original_data, label_wrapper):

        if toggle_wrapper[0] == 0:
            toggle_wrapper[0] = 1
            print(str(toggle_wrapper[0]))
            #display_image.hide_image(top_wrapper, my_canvas_wrapper, label_wrapper)
            display_graph.show_graph(top_wrapper, my_canvas_wrapper, label_wrapper, original_data)

        else:
            toggle_wrapper[0] = 0  # make it False
            print(str(toggle_wrapper[0]))
            display_graph.hide_graph(top_wrapper, my_canvas_wrapper, label_wrapper)
            #display_image.show_image(top_wrapper, my_canvas_wrapper, label_wrapper)

    top = tk.Tk()
    top.title("this is a test")
    top.geometry("1100x1100+50+50")

    # toggle to keep track of which canvas to show
    toggle = 0

    my_canvas = Canvas(top, bd=3, height=1000, width=1000, relief='ridge', bg='light blue')

    original_data = [(112, 112), (114, 117), (223, 226), (234, 237), (247, 249),
                    (351, 351), (361, 362), (400, 200), (550, 100)]
    label_text = "Image: blue box"
    label = tk.Label(text=label_text)

    label.grid(row=900, column=10, pady=5, padx=10, columnspan=10)
    # pass by reference the variables
    toggle_wrapper =[toggle]
    top_wrapper = [top]
    my_canvas_wrapper = [my_canvas]
    label_wrapper = [label]

    # initial default values

    run_button = tk.Button(top, activebackground='green', text="change button", fg='green', command=lambda: change_canvas_callback(toggle_wrapper, my_canvas_wrapper, top_wrapper, original_data, label_wrapper))

    my_canvas.create_image(700, 700)
    my_canvas.grid(row=10, column=10, pady=10, padx=10)

    run_button.grid(row=950, column=10, pady=5, padx=10, columnspan=10)
    print("starter part of main")
    top.after(500)
    top.mainloop()


if __name__ == '__main__':
    main()

