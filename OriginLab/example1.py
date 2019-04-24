import PyOrigin
bookName = '[Book1]Sheet1'

# ----------------------------------------------------------------
# PyOrigin.FindWorksheet(bookName).Columns(0).SetComments('intensity')
# str = PyOrigin.FindWorksheet(bookName).Columns(0).GetComments()
# print('Show the comment in column 1: '+str)


# ----------------------------------------------------------------
# M = [1, 2, 3, 4, 5, 6]
# PyOrigin.FindWorksheet(bookName).Columns(0).SetData(M, 0)
# print(PyOrigin.FindWorksheet(bookName).Columns(0).GetData())

# Col = PyOrigin.FindWorksheet(bookName).Columns(0)
# Data = Col.GetData()
# Length = Col.GetUpperBound()

# for i in range(Length):
#     if str(Data[i]).isalpha():
#         Data[i] = 0

# Col.SetData(Data)


# ----------------------------------------------------------------
# PyOrigin.FindWorksheet(bookName).Columns(0).SetUpperBound(PyOrigin.FindWorksheet(bookName).GetRowCount()-1)
# PyOrigin.FindWorksheet(bookName).Columns(0).GetUpperBound()
# print(PyOrigin.FindWorksheet(bookName).GetRowCount())


# M = [1,2,3,4,5,6]
# Array=PyOrigin.FindWorksheet(bookName).Columns(0).GetStringArray(0,-1,0,1)
# print(Array)

# M = ['a','b','c']
# PyOrigin.FindWorksheet(bookName).Columns(0).PutStringArray(M)
# print(Array)

# Fmt=PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(0).GetFormat()
# SubFmt=PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(0).GetSubFormat()
# print('The format number is %d \nThe subformat number is %d' % (Fmt,SubFmt))

# PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(0).SetType(3)
# type = PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(0).GetType()
# if type == 0:
#     print('column 1 is designated as Y')

# PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(1).SetUnits('mC/m^2')
# ###############################     HOW TO USE Roman Symbol??????  ##############################
# print('The unit is %s' % PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(1).GetUnits())

# Column=PyOrigin.FindWorksheet('[Book1]Sheet1').Columns(0)
# #Set COlumn Additional information
# Column.SetX0(10)
# Column.SetX1(2)
# #Get COlumn Additional information
# print('The EvenX initial value is %2.2f' % Column.GetX0())
# print('The EvenX Increment is %2.2f' % Column.GetX1())

# wks = PyOrigin.WorksheetPages('Book1').Layers(1)
# Col = wks.Columns(0)
# Col.SetFormula('ran()')
# Col.ExecuteFormula()


# Create Sheet in Book1 with 5 columns
# the following code will set column formats in a new worksheet
# 1st column - Numeric (0)
# 2nd column - Text    (1)
# 3rd column - Time    (2)
# 4th column - Date    (3)
# 5th column - Text and Numeric (9)
# wks=PyOrigin.WorksheetPages('Book1').Layers(0)
# Formats="01239"
# wks.SetColFormats(Formats)
# for i in range(5):
#     col=wks.Columns(i).GetDataFormat()
#     print(i,col)

# wks=PyOrigin.WorksheetPages('Book1').Layers(0)
# Col=wks.Columns(3)
# Col.SetDigits(9)
# print('The digit number of the column is %d' % Col.GetDigits())

# wks=PyOrigin.WorksheetPages('Book1').Layers(0)
# Col=wks.Columns(1)
# Col.SetFormula('ran()')
# Col.ExecuteFormula()

# data = PyOrigin.NewDataRange()
# Sheet = PyOrigin.WorksheetPages('Book1').Layers(0)
# if data.IsValid():
#     data.Add('X', Sheet, 0, 0, -1, -1)
# gp = PyOrigin.FindGraphLayer('Graph1')
# gp.AddPlot(data, 1)


# Folder=PyOrigin.ActiveFolder()
# print('The name of the parent folder is %s' % Folder.GetName())


# Folder=PyOrigin.ActiveFolder()
# print('The pages contained in folder are:')
# for page in Folder.PageBases():
#     print(page.GetLongName())

# gl=PyOrigin.FindGraphLayer('Graph1')
# print(gl.DataPlots(2).GetName())

# Graph=PyOrigin.ActiveLayer()
# #get the demision of the legend
# print(Graph.GraphObjects('legend').GetDX(),Graph.GraphObjects('legend').GetDY())


# #active a graphs with legend
# Graph=PyOrigin.ActiveLayer()
# #Set the left margin of the object
# print('the text in object is: %s' % Graph.GraphObjects('Legend').GetText())


# gp = PyOrigin.GraphPages('Graph1')
# if gp.IsValid():
#     gp.SetHeight(8)  # set height in inch
#     print('the height of the graph page is %2.2f' % gp.GetHeight())


# gp=PyOrigin.GraphPages('Graph1')
# if gp.IsValid():
#     gp.SetPageViewMode(1)  #page view
# if  gp.GetPageViewMode()==1:
#     print('Page view')

# wks=PyOrigin.ActiveLayer()
# wksPage=wks.GetPage()
# print(wksPage.GetName())#show the name of the parent Page

# wks=PyOrigin.WorksheetPages()
# print('There are %d Workbooks in the Project' % wks.GetCount())

# wks = PyOrigin.ActiveLayer()
# index=wks.GetIndex()
# print('Current sheet index = %i' % (index))

wksPage = PyOrigin.ActivePage()
nSheetIndex = 0
wks = wksPage.Layers(nSheetIndex)
wks.SetShow(1)
if wks.GetShow():
    print('The first sheet is hide')
