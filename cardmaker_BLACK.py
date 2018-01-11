#UK call card size
CARDWIDTH = 249.12
CARDHEIGHT = 167.04
NCARDS = 100
BOTTOMBORDER = 25

#the text we would like to draw

title = "CRISPY"
supporting = "WEB & MOBILE SOLUTIONS"

# set the font size we would like to use as a variable

txtFontSize=125
suppFontSize=7

# path to the font file

for cards in range(NCARDS):

    #create a new page

    newPage(CARDWIDTH,CARDHEIGHT)
    # draw a white background
    fill(0)

    rect(0, 0, CARDWIDTH, CARDHEIGHT)
    # create a formatted string and already provide the font and the font size - for the Title

    txt = FormattedString(font="Crispy", fontSize=txtFontSize, fill=(0.72156862745098,0.831372549019608,0.203921568627451), stroke=(0.72156862745098,0.831372549019608,0.203921568627451), strokeWidth=1.5, align="center")
    # start the loop
    for char in title:
        # calculate a random value inbetween 0 and 1000
        startvariable=randint(0, 1000)
        # set a font variation
        txt.fontVariations(wght=startvariable)
        txt.fontVariations(wdth=240)
        # add the char to the formatted string
        print startvariable #just cross-check randmised values
        txt += char
        # create an inset
        # draw in a box

    textBox(txt, (0, 10, CARDWIDTH, txtFontSize)) #does this use of txtFontSize make sense? not sure if fontSize is translated in the same canvas units

    # draw some supporting text

    suppTxt="WE DON'T DO WEBSITES."

    font("InputMono-Medium")
    fontSize(suppFontSize)
    fill(0.72156862745098,0.831372549019608,0.203921568627451)

    inset = 52 #this is so we have something to reference the text box against to centre it

    topinset = CARDHEIGHT-BOTTOMBORDER #good idea to draw the actual thing to get an idea of how the variables need to work with each other.

    textBox(suppTxt, (inset, -topinset, CARDWIDTH-inset*2, CARDHEIGHT), align="center")
    saveImage("crispybacks"+str(cards)+".pdf")

#thanks to Frederik Berlaen for helping me automate this. to get to the final version http://typemytype.com/ forum.drawbot.com