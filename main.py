import tkinter as tk
import matplotlib

from calculate import run

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        points = run(2, 2, 2)
        self.x = []
        self.y = []
        for point in points[:40]:
            self.x.append(point[0])
            self.y.append(point[1])
        self.title('Relay')

        figure = Figure(figsize=(15, 5), dpi=100)
        self.figure_canvas = FigureCanvasTkAgg(figure, self)
        toolbarFrame = tk.Frame(self)
        toolbarFrame.grid(row=3, column=1)
        NavigationToolbar2Tk(self.figure_canvas, toolbarFrame)
        self.axes = figure.add_subplot()
        self.axes.plot(self.x, self.y)
        self.axes.grid()

        self.figure_canvas.get_tk_widget().grid(row=1, column=1)

        input_frame = tk.Frame(self)
        input_frame.grid(row=1, column=2)
        a_text = tk.StringVar()
        a_text.set("Enter a")
        a_label = tk.Label(input_frame, textvariable=a_text)
        a_label.grid(row=1, column=2)

        a_value = tk.StringVar()
        a_value.set("2")
        self.a_entry = tk.Entry(input_frame, textvariable=a_value)
        self.a_entry.grid(row=2, column=2)

        label2Text = tk.StringVar()
        label2Text.set("Enter b")
        label2Dir = tk.Label(input_frame, textvariable=label2Text)
        label2Dir.grid(row=3, column=2)

        directory2 = tk.StringVar(None)
        self.b_entry = tk.Entry(input_frame, textvariable=directory2)
        self.b_entry.grid(row=4, column=2)

        label3Text = tk.StringVar()
        label3Text.set("Enter n")
        label3Dir = tk.Label(input_frame, textvariable=label3Text)
        label3Dir.grid(row=5, column=2)

        directory3 = tk.StringVar(None)
        self.n_entry = tk.Entry(input_frame, textvariable=directory3)
        self.n_entry.grid(row=6, column=2)

        plot_button = tk.Button(master=input_frame,
                                height=2,
                                width=10,
                                text="Plot")
        plot_button.config(command=self.plot)
        plot_button.grid(row=7, column=2)

    def plot(self):
        a = int(self.a_entry.get())
        b = int(self.b_entry.get())
        n = int(self.n_entry.get())
        points = run(a, b, n)
        self.x = []
        self.y = []
        for point in points[:40]:
            self.x.append(point[0])
            self.y.append(point[1])
        self.replot()

    def replot(self):
        self.axes.clear()
        self.axes.grid()
        self.axes.plot(self.x, self.y)
        self.figure_canvas.draw()


if __name__ == '__main__':
    app = App()
    app.mainloop()