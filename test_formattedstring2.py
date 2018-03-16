from xlrd import open_workbook

spreadsheet=open_workbook('simple.xlsx')
xl_sheet = spreadsheet.sheet_by_index(0)

def PageMaker(CSEC, QUAL, TITLE, FACULTY, FACULTYPIC):
    newPage(612,792)
    leftmargin = 30
    midmargin= width()/2+leftmargin
    #PICK IMAGE
    if str(FACULTY) = "Engineering":
        IMGpath = "testimage/eng3-1.jpg"
    for pageNumber in range(1, pageCount+1):
    w, h = imageSize(path, pageNumber=pageNumber)
    newPage(w, h)
    image(path, (0, 0), pageNumber=pageNumber)
    fill(0)
    font("GiraSans-Bold", 10)
    rect(leftmargin, 560, width()-2*leftmargin, 150)
    
    textBox(str(FACULTY).upper(), (leftmargin, 700, width()/2, 50), align="left",)
    txt = FormattedString()
    
    txt.append(str(TITLE)+'\n', font="GiraSans-Bold", fontSize=40, fill=(0, 0, 0),paragraphBottomSpacing=30)
    txt.append(str(QUAL).replace(":", "")+'\n', font="GiraSans-Book", fontSize=14, fill=(0, 0, 0),paragraphBottomSpacing=30)
    
    txt.append("CSEC QUALIFICATIONS:"+'\n', font="GiraSans-Bold", fontSize=10, fill=(0, 0, 0),paragraphBottomSpacing=5)
    txt.append(str(CSEC)+'\n', font="GiraSans-Book", fontSize=10, fill=(0, 0, 0),paragraphBottomSpacing=20)
    
    txt.append("CAPE QUALIFICATIONS:"+'\n', font="GiraSans-Bold", fontSize=10, fill=(0, 0, 0),paragraphBottomSpacing=5)
    txt.append(str(CSEC), font="GiraSans-Book", fontSize=10, fill=(0, 0, 0),paragraphBottomSpacing=40)

    textBox(txt, (leftmargin, -height()/11, 3*width()/4, 3*height()/4), align="left")
    
for i in range(1, xl_sheet.nrows):
    TITLE=xl_sheet.cell(i,0).value
    FACULTY="FACULTY OF " + xl_sheet.cell(i,1).value
    QUAL=xl_sheet.cell(i,2).value
    CSEC=xl_sheet.cell(i,4).value
    PageMaker(CSEC, QUAL, TITLE, FACULTY)
