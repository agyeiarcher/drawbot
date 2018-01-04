CARDWIDTH=249.12
CARDHEIGHT=167.04
#UK call card size

newPage(CARDWIDTH,CARDHEIGHT)

path = "krspy.ttf"
fontName = installFont(path)

x, y, w, h = 0, 0, CARDWIDTH, CARDHEIGHT

fill(1)
rect(0, 0, CARDWIDTH, CARDHEIGHT)

fill(0)

txtFontSize=106

txt = FormattedString(fontSize=txtFontSize)

txt.fontVariations(wdth=266)

#set initial value

txt.align ="center"
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)

#'manually' refresh startvariable value each time and append to textBox

txt.append("C", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("H", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("A", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("R", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("G", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("E", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))
startvariable=randint(0,1000)
txt.fontVariations(wght=startvariable)
txt.append("S", font=fontName, fontSize=txtFontSize, fill=(0, 0, 0))

fill(0)

text(txt, (CARDWIDTH/2, CARDHEIGHT/2-txtFontSize/3), align="center")
