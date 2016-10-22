from tkinter import *
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import twitterBackend as twb
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler

geoL = Nominatim()
root = Tk()
Label(text="Enter Address:").pack()
loca = Entry(root, width=50)
loca.pack()
#loca.insert(END, "382 cavendish Drive waterloo Ontario")
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
    print(location.latitude - radius / 111, location.latitude + radius / 111)
    m.drawmeridians(np.arange(location.longitude - radius / 111, location.longitude + radius / 111, radius/222))
    m.drawparallels(np.arange(location.latitude - radius / 111, location.latitude + radius / 111, radius/222))
    print(location.latitude-radius/111, location.latitude+radius/111, radius/222)
    centers = []
    for x in np.arange(location.latitude-radius/111+radius/444, location.latitude+radius/111, radius/222):
        for y in np.arange(location.longitude-radius/111+radius/444, location.longitude+radius/111, radius/222):
            centers.append([x,y])
    averages = []
    for i in centers:
        print("i", i[0], i[1])
        averages.append(twb.getValue(i[0], i[1], radius/4))
    #c = [[0.10252100000000004, 0.10892200000000002, 0.0649, 0.05910400000000002],
         #[0.168767, 0.15290299999999998, 0.13197812500000003, 0.10168800000000001],
         #[0.16580899999999998, 0.15036900000000006, 0.16009000000000004, 0.14318699999999998],
         #[0.20729199999999995, 0.04271300000000002, 0.015431000000000002, 0.047612999999999996]]

    c = [averages[i:i + 4] for i in range(0, len(averages), 4)]

    #print(c)

    # m.drawparallels(np.arange(-90., 91., (radius)/222))
    # m.drawmeridians(np.arange(-180., 181., (radius)/222))
    m.drawcoastlines()
    #m.plot([-80, -79], [-43, -41])#, latlon = True)
    #m.fillcontinents(color="coral", lake_color='lightblue')
    m.drawmapboundary(fill_color="blue")
    #m.plot(x=location.longitude, y=location.latitude, marker="^", markersize=16, latlon=True)
    m.imshow(c, cmap='hot', interpolation='nearest')
    plt.show()

    # loc=TOP, fill=BOTH, expand=1)


send = Button(root, text="send", command=get)
send.pack()
mainloop()

root.mainloop()
