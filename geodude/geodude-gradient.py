import sys
import geocoder
from webcolors import *

sys.path.append("/")

g=geocoder.ip('me')

color1=str(g.lat)
color1=color1.replace(".","")
color1=float(color1)
color1="#"+(hex(abs(int(color1)))[2:]+"0")
color1=normalize_hex(color1)

color2=str(g.lng)
color2=color2.replace(".","")
color2="#"+(hex(abs(int(color2)))[2:]+"0")
color2=normalize_hex(color2)

colorTuple1=hex_to_rgb(color1)
colorTuple2=hex_to_rgb(color2)

colornumbers1, colornumbers2=[num/255 for num in colorTuple1], [num/255 for num in colorTuple2]

linearGradient(
    (000, 000),                         # startPoint
    (900, 900),                         # endPoint
    [colornumbers1,colornumbers2],  # colors
    [0, 0.5]                          # locations
    )
# draw a rectangle
rect(0, 0, 1000, 1000)

# saveImage("geodude.png")