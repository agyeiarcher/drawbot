nframes=48
novals=80
transdistance=4

CANVAS=1000
ovalsize=75
padding=ovalsize*1.2
ntimes=8
totalwidth=ovalsize+padding*ntimes
        
for frame in range(nframes):
    newPage(CANVAS, CANVAS)
    fill(0)
    rect(0,0,width(),height())
    frameDuration=1/48
    translate(CANVAS/2-totalwidth/2,height()/2-ovalsize)
    phase=2*pi*frame/nframes
    for i in range(ntimes-1):
        #multiple circles
        if i%2:
            trans=transdistance*sin(phase)
        else:
            trans=transdistance*cos(phase)
        translate(padding,0)
        #up-down translation using sin(phase)
        save()
        for j in range(novals):
            opacityphase=50/novals
            opacitycount=opacityphase*j/100
            fill(1,1,1,opacitycount)
            translate(0, trans)
            oval(0,0, ovalsize, ovalsize)
        restore()
        

saveImage("circles7.gif")
