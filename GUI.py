from tkinter import *
from geopy.geocoders import Nominatim
from numpy import arange, sin, pi
from matplotlib import pyplot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler

geoL = Nominatim()
root = Tk()
Label(text="Enter Address:").pack()
loca = Entry(root, width=50)
loca.pack()

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0, 3.0, 0.01)
s = sin(2 * pi * t)

a.plot(t, s)


canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

button = Button(master=root, text='Quit', command=_quit)
button.pack(side=BOTTOM)

mainloop()

def get():
    a = loca.get()
    print(type(a))
    location = geoL.geocode(a)
    print(location.latitude, location.longitude)


send = Button(root, text="send", command=get)
send.pack()

root.mainloop()
