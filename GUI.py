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
loca.insert(END, "382 cavendish Drive waterloo Ontario")
radius = 1000;



def _quit():
    root.quit()
    root.destroy()

f = Figure()
f.add_subplot(111)

button = Button(master=root, text='Quit', command=_quit)
button.pack(side=BOTTOM)


def get():

    a = loca.get()
    root.destroy()
    location = geoL.geocode(a)
    m = Basemap(projection='cyl', llcrnrlat=location.latitude - radius / 111,
                urcrnrlat=location.latitude + radius / 111, llcrnrlon=location.longitude - radius / 111,
                urcrnrlon=location.longitude + radius / 111, resolution='i')
    print(location.latitude, location.longitude)
    m.drawmeridians(np.arange(location.longitude - radius / 111, location.longitude + radius / 111, 1.))
    m.drawparallels(np.arange(location.latitude - radius / 111, location.latitude + radius / 111, 1.))
    # m.drawparallels(np.arange(-90., 91., (radius)/222))
    # m.drawmeridians(np.arange(-180., 181., (radius)/222))
    m.drawcoastlines()
    #m.plot([-80, -79], [-43, -41])#, latlon = True)
    m.fillcontinents(color="coral", lake_color='lightblue')
    m.drawmapboundary(fill_color="blue")
    #m.plot(x=location.longitude, y=location.latitude, marker="^", markersize=16, latlon=True)
    plt.show()
    # loca.delete(0, END)
    # canvas = FigureCanvasTkAgg(f, master=root)
    # canvas.show()
    # canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    # toolbar = NavigationToolbar2TkAgg(canvas, root)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)


send = Button(root, text="send", command=get)
send.pack()
mainloop()

root.mainloop()
