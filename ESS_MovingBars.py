nbars = 5
nframes=40
movement = 100

#position variable relates to the vertical position of the bars. Random positions are packed into a list and then used to place rectangular bars

position = [randint(-30,30)]
for k in range(nbars):
    save()
    if position[k]==0:
        position.append(randint(-30,30))
    restore()
    save()
    if position[k]<=1:
        position.append(randint(-10,30))
    if position[k]>=1:
        position.append(randint(-30,10))
    restore()

newDrawing()
    
def bars(i,j,frame,bar,barspacing):
    barwidth = width()/15
    barheight = height()/40
    distance = i*barwidth
    fill(1)
    rect(distance+j,position[bar],barwidth,barheight)

for frame in range (nframes):
    newPage(700,600)
    frameDuration(1/30)
    fill(0)
    rect(0,0, width(), height())
    fill(1)
    barwidth = width()/10
    barspacing = height()/30
    translate(width()/2-barwidth*nbars/2+barwidth/2, height()/2)
    for i in range(nbars):
        transamount=10
        bar=i
        j=i*barspacing
        save()
        if position[bar]>20:
            save()
            phase=2*pi*frame/nframes
            transamount=position[bar]
            print transamount
            translate(0,transamount*sin(phase))
            bars(i,j,frame,bar,barspacing)
            restore()
        if position[bar]<-20:
            save()
            phase=2*pi*frame/nframes
            transamount=position[bar]
            print transamount
            translate(0,transamount*sin(phase))
            bars(i,j,frame,bar,barspacing)
            restore()
        if -10<position[bar]<0:
            save()
            phase=2*pi*frame/nframes
            transamount=2*position[bar]
            print transamount
            translate(0,transamount*sin(phase))
            bars(i,j,frame,bar,barspacing)
            restore()
        if 0<position[bar]<10:
            save()
            phase=2*pi*frame/nframes
            transamount=2*position[bar]
            print transamount
            translate(0,transamount*cos(phase))
            bars(i,j,frame,bar,barspacing)
            restore()
        restore()

# saveImage("bars.gif")