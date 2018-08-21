import sys
import geocoder
from webcolors import *

sys.path.append("/")

g=geocoder.ip('me')

color1=str(abs(g.lat))
color1=format(float(color1))
if len(str(color1))<=8:
    color1=format(float(color1), ".6f")
if len(str(color1))>8:
    color1=format(float(color1), ".5f")
color=str(color1)
color1=color1.replace(".","")
color1="#"+(hex(abs(int(color1)))[2:])
color1=normalize_hex(color1)

color2=str(abs(g.lng))
color2=format(float(color2))
if len(str(color2))<=8:
    color2=format(float(color2), ".6f")
if len(str(color2))>8:
    color2=format(float(color2), ".5f")
color=str(color2)
color2=color2.replace(".","")
color2="#"+(hex(abs(int(color2)))[2:])
color2=normalize_hex(color2)

print(color1, color2)

colorTuple1=hex_to_rgb(color1)
colorTuple2=hex_to_rgb(color2)

print(colorTuple1,colorTuple2)

#convert to DrawBot-friendly color values (0<1)

colornumbers1, colornumbers2=[num/255 for num in colorTuple1], [num/255 for num in colorTuple2]

linearGradient(
    (000, 000),                         # startPoint
    (900, 900),                         # endPoint
    [colornumbers1,colornumbers2],  # colors
    [0, 1]                          # locations
    )
# draw a rectangle
rect(0, 0, 1000, 1000)

saveImage("geodude.png")