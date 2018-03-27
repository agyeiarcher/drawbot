    
#LOWERCASE PROOFS

def ControlCharLowercase():
    
    nstring = FormattedString()
    ostring = FormattedString()
    ostring.fontSize(14)
    nstring.fontSize(14)
    if fontName in installedFonts():
        nstring.font(fontName)
        ostring.font(fontName)
    else:
        print('font %s not installed' % fontName)
    
    for k in range(len(LowerCaseLetters)):
        nstring.append("nn"+LowerCaseLetters[k]+"nn")
    for l in range(len(LowerCaseLetters)):
        ostring.append("oo"+LowerCaseLetters[l]+"oo")
    
    for i in range(len(LowerCaseLetters)):
        
        ospacing=FormattedString()
        
        ospacing.fontSize(startsize*textwaterfall)
        if fontName in installedFonts():
            ospacing.font(fontName)
        else:
            print('font %s not installed' % fontName)
        ospacing.append(str(LowerCaseLetters[i])+"\n")
        
        for j in reversed(range(textwaterfall)):
            if j ==0:
                currentfontsize=startsize/2
            if j>0:
                currentfontsize=j*startsize
                
            ospacing.fontSize(currentfontsize)
            ospacing.paragraphBottomSpacing(20)
                        
            if fontName in installedFonts():
                ospacing.font(fontName)
            else:
                print('font %s not installed' % fontName)
                
            otxt = "oo"+LowerCaseLetters[i]+"oo"
            ntxt = "nn"+LowerCaseLetters[i]+"nn"
            
            ospacing.align("left")
            ospacing.append(otxt+"  "+ntxt+"\n", fill=(0, 0, 0))
        
        newPage('LetterLandscape')
        
        alltext=ospacing+"\n"+nstring+"\n"+ostring
        textBox(alltext, (margin,margin/2,width()-280,height()-margin*2))
        
        print(alltext)
