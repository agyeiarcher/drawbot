import drawBot

f= CurrentFont()
s= CurrentFont().selection

fontName = '%s-%s' % (f.info.familyName, f.info.styleName)

if s is not None:
    drawBot.newPage('Letter')
    drawBot.font(fontName)
    drawBot.fontSize(200)
    txt=str(s)
    for char in "[ ' ] ":
        txt=txt.replace(char, "")
    drawBot.textBox(txt,(100,0, drawBot.width()-60, drawBot.height()-120), align="left")
    drawBot.printImage()