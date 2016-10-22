from tkinter import *
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler

geoL = Nominatim()
root = Tk()
Label(text="Enter Address:").pack()
loca = Entry(root, width=50)
loca.pack()
loca.insert(END,"382 cavendish Drive waterloo Ontario")
f = Figure()
a = f.add_subplot(111)

m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90, \
            llcrnrlon=-180, urcrnrlon=180, resolution='c',
            ax=a)
m.drawparallels(np.arange(-90., 91., 1.))
m.drawmeridians(np.arange(-180., 181., 1.))
m.drawcoastlines()
m.fillcontinents(color="coral",lake_color='lightblue')
m.drawmapboundary(fill_color="blue")
# m.bluemarble()

def _quit():
    root.quit()  # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent


button = Button(master=root, text='Quit', command=_quit)
button.pack(side=BOTTOM)


def get():
    a = loca.get()
    print(type(a))
    location = geoL.geocode(a)
    print(location.latitude, location.longitude)
    m.plot(x=location.longitude, y=location.latitude, marker="^", markersize=16, latlon=True)
    plt.show()
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

    loca.delete(0, END)


send = Button(root, text="send", command=get)

send.pack()
mainloop()

root.mainloop()
