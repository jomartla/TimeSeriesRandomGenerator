import tkinter as tk

from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class VisualizationFrame(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.event_num = 0
        self.visualization_matrix = []
        self.dft_matrix = []

        # Visualization frame
        self.visualization_frame = tk.Frame(self)

        self.figure = Figure(figsize=(10, 3))
        self.ax = self.figure.add_subplot(111)
        self.ax.format_coord = lambda x, y: ""

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.visualization_frame)
        self.line = None

        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="N", columnspan=2)

        self.toolbar_frame = tk.Frame(self.visualization_frame)
        self.toolbar = VisualizationFrame.CustomToolbar(self.canvas, self.toolbar_frame)
        self.toolbar.pack()
        self.toolbar_frame.grid(row=1, column=0, sticky="E")

        # Position controller frame
        self.position_controller_frame = tk.Frame(self.visualization_frame)

        # Button for previous time series
        self.button_left = tk.Button(self.position_controller_frame, text="< Previous",
                                     command=self.previous_time_series, width=15)
        self.button_left.grid(row=0, column=0, sticky="E")

        # Label for time series position in navigation
        self.label_time_series_position_text = tk.StringVar()
        self.label_time_series_position_text.set("1")

        self.label_time_series_position = tk.Label(self.position_controller_frame,
                                                   textvariable=self.label_time_series_position_text,
                                                   font=("Arial", 10))
        self.label_time_series_position.grid(row=0, column=1, sticky="N", padx=15)

        # Button for next time series
        self.button_right = tk.Button(self.position_controller_frame, text="Next >",
                                      command=self.next_time_series, width=15)
        self.button_right.grid(row=0, column=2, sticky="W")

        self.position_controller_frame.grid(row=1, column=1, sticky="W")

        self.visualization_frame.grid_forget()

    def update_time_series_visualization(self, perform_pan=False):
        self.label_time_series_position_text.set(str(self.event_num + 1))
        self.ax.clear()
        self.line, = self.ax.plot(range(1, len(self.visualization_matrix[self.event_num]) + 1),
                                  # Values
                                  self.visualization_matrix[self.event_num])
        self.line, = self.ax.plot(range(1, len(self.dft_matrix[self.event_num]) + 1),
                                  # Values
                                  self.dft_matrix[self.event_num])
        # Although f is not used, is recommended to save the result in a variable.
        # Without doing this, the garbage collector could delete the event created.
        f = zoom_factory(self.ax, self.canvas, base_scale=1.05)
        self.ax.grid(color='whitesmoke', linestyle='-', linewidth=0.5)
        if perform_pan:
            self.toolbar.pan()

        self.canvas.draw()

    def previous_time_series(self):
        if 0 <= (self.event_num - 1) < len(self.visualization_matrix):
            self.event_num -= 1
            self.update_time_series_visualization()

    def next_time_series(self):
        if 0 <= (self.event_num + 1) < len(self.visualization_matrix):
            self.event_num += 1
            self.update_time_series_visualization()

    class CustomToolbar(NavigationToolbar2Tk):
        # only display the buttons we need
        def __init__(self, canvas_, parent_):

            self.toolitems = (
                ('Pan', 'Pan axes with left mouse', 'move', 'pan'),
                (None, None, None, None),
            )

            NavigationToolbar2Tk.__init__(self, canvas_, parent_)

        def pan(self, *args):
            NavigationToolbar2Tk.pan(self)
            self.mode = ""
            self.set_message(self.mode)


def zoom_factory(ax, canvas, base_scale=1.05):
    def zoom_fun(event):
        # get the current x and y limits
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location
        if event.button == 'down':
            # deal with zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'up':
            # deal with zoom out
            scale_factor = base_scale
        else:
            # deal with something that should never happen
            scale_factor = 1
            print(event.button)
        # set new limits
        ax.set_xlim([xdata - (xdata - cur_xlim[0]) / scale_factor,
                     xdata + (cur_xlim[1] - xdata) / scale_factor])
        ax.set_ylim([ydata - (ydata - cur_ylim[0]) / scale_factor,
                     ydata + (cur_ylim[1] - ydata) / scale_factor])

        canvas.draw()  # force re-draw

    fig = ax.get_figure()  # get the figure of interest
    # attach the call back
    fig.canvas.mpl_connect('scroll_event', zoom_fun)

    # return the function
    return zoom_fun
