import tkinter as tk
import matplotlib

from calculate import RelayEquation

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        relay = RelayEquation(2, 2, 2)
        points = relay.run()
        self.x = []
        self.y = []
        for point in points:
            self.x.append(point.x)
            self.y.append(point.y)
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
        a_text.set("a0")
        a_label = tk.Label(input_frame, textvariable=a_text)
        a_label.grid(row=1, column=2)

        a_value = tk.StringVar()
        a_value.set("2")
        self.a_entry = tk.Entry(input_frame, textvariable=a_value, justify="center")
        self.a_entry.grid(row=2, column=2)

        b_text = tk.StringVar()
        b_text.set("b0")
        b_label = tk.Label(input_frame, textvariable=b_text)
        b_label.grid(row=3, column=2)

        b_value = tk.StringVar(None)
        b_value.set("2")
        self.b_entry = tk.Entry(input_frame, textvariable=b_value, justify="center")
        self.b_entry.grid(row=4, column=2)

        n_text = tk.StringVar()
        n_text.set("n")
        n_label = tk.Label(input_frame, textvariable=n_text)
        n_label.grid(row=5, column=2)

        n_value = tk.StringVar(None)
        n_value.set("2")
        self.n_entry = tk.Entry(input_frame, textvariable=n_value, justify="center")
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
        relay = RelayEquation(a, b, n)
        points = relay.run()
        self.x = []
        self.y = []
        for point in points:
            self.x.append(point.x)
            self.y.append(point.y)
        self.replot()

    def replot(self):
        self.axes.clear()
        self.axes.grid()
        self.axes.plot(self.x, self.y)
        self.figure_canvas.draw()


if __name__ == '__main__':
    app = App()
    app.mainloop()
