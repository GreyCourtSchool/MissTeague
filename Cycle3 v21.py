from tkinter import *
from toggledFrame import *
from HDIDatabase import *

def resetGlobals():
    global countriesVar
    global continentsVar
    global yearsVar
    global subListsCheckVar

    subListsCheckVar = []
    countriesVar = []
    continentsVar = []
    yearsVar = []

def menuWindow():
    #Main Window
    menu = Tk()
    menu.geometry("720x500")
    menu.title("HDI Analysis Tool")
    menu.resizable(False, True)
    menu.configure(background="Light Grey")

       
    #Frames
    title_frame = Frame(menu)
    title_frame.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
    filter_frame = Frame(menu)
    filter_frame.grid(row=1, column=0, columnspan=2, padx=30, pady=5)
    expandable_frame = Frame(menu)
    expandable_frame.grid(row=2, column=0, columnspan=2, padx=30, pady=5)
    show_frame = Frame(menu)
    show_frame.grid(row=3, column=0, columnspan=2, padx=30, pady=5)

    #Labels
    Label(title_frame,text="HDI Menu", font=('Arial',16)).grid(row=0, column=0, padx = 10,pady=20)
    
    #Buttons
    filterCountry_button = Button(filter_frame,text="Filter Countries",width=30,command=filterCountries)
    filterCountry_button.grid(row = 0, column = 0)
    filterContinent_button = Button(filter_frame,text="Filter Continents",width=30,command=filterContinents)
    filterContinent_button.grid(row = 0, column = 1)
    filterYears_button = Button(filter_frame,text="Filter Years",width=30,command=filterYears)
    filterYears_button.grid(row = 0, column = 2)
    showData_button = Button(show_frame,text="Show Data",width=15,command=lambda: dataWindow(menu))
    showData_button.grid(row = 0, column = 0)

    resetGlobals()
    
    #Collapsable Menu
    global tables
    tables = [["HDI",["2017 HDI","Female HDI","Male HDI","2017 Rank"]],
              ["Demography",["Total Population","Median Age","Age 15-64","Age 65+","Age 0-5", "Urban Population %"]],
              ["Education",["Education Index","Government Expenditure on Education","Litracy Rate:Ages 15+","Mean Years of Schooling","Mean Years of Schooling, Male","Mean Years of Schooling, Female"]],
              ["Health",["Life Expectancy at Birth","Life Expectancy at Birth, Male","Life Expectancy at Birth, Female","Life Expectancy Index"]],
              ["Income",["Gross Domestic Product per Capita","Gross Domestic Product","Gross National Income per Capita","Income Index"]],
              ["Trade",["Exports and Imports (% of GDP)"]],
              ["Employment",["Child Labour (% of Population)","Unemployment"]]]
    dropdown = []
    sublists = []
    subListsCheck =[]
    global subListsCheckVar
    index = 0
    varCheck = 0
    for key in range(0,len(tables)):
        dropdown.append(ToggledFrame(expandable_frame, text=tables[key][0], relief="raised", borderwidth=1))
        dropdown[index].pack(fill='x', expand = 1, pady=2, padx=2,anchor="n")
        sublists.append([])
        rowRef = 0
        for item in tables[key][1]:
            subListsCheckVar.append(IntVar())
            sublists[index].append(Checkbutton(dropdown[index].sub_frame,text=item, variable=subListsCheckVar[varCheck]))
            sublists[index][rowRef].grid(row = rowRef,column = 1,pady=2, padx=2, sticky=W)
            rowRef += 1
            varCheck += 1
        index += 1
  
def reset(previousWindow):
    previousWindow.destroy()
    menuWindow()

def myfunction(event):
    global canvas
    canvas.configure(scrollregion=canvas.bbox("all"),width=700,height=500)
    
def filterCountries():
    #Filter Countries Window
    filterCount = Toplevel()
    filterCount.geometry("840x600")
    filterCount.title("Filter Countries Menu")
    filterCount.resizable(False, False)
    filterCount.configure(background="Light Grey")

    #Frames
    main_frame = Frame(filterCount)
    main_frame.grid(row=0, column = 0, padx=30, pady=5)
    
    submit_frame = Frame(filterCount)
    submit_frame.grid(row=2, column=0, columnspan = 3, padx=30, pady=5)
    global canvas
    canvas = Canvas(main_frame)
    contnet_frame =Frame(canvas)
    myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=contnet_frame,anchor='nw')
    contnet_frame.bind("<Configure>",myfunction)

    file = open("CountriesandContinent.txt","r")
    global countries
    countries = []
    for country in file:
        temp = country.split(",")
        countries.append(temp[0][1:])
        
    #Checkboxes
    global counCheckBoxL
    global counCheckBoxM
    global counCheckBoxR
    global countriesVar
    
    counCheckBoxL = []
    counCheckBoxM = []
    counCheckBoxR = []

    #Fill Left Checkbox
    for country in range(0,63):
        countriesVar.append(IntVar())            
        counCheckBoxL.append(Checkbutton(contnet_frame, text = countries[country], variable=countriesVar[country], onvalue = 1, offvalue = 0))
        counCheckBoxL[country].grid(row = country, column = 0, sticky = W)

    #Fill Middle
    index = 0
    for country in range(63,126):
        countriesVar.append(IntVar())            
        counCheckBoxM.append(Checkbutton(contnet_frame, text = countries[country], variable=countriesVar[country], onvalue = 1, offvalue = 0))
        counCheckBoxM[index].grid(row = index, column = 1, sticky = W)
        index += 1
        
    #Fill Right
    index = 0
    for country in range(126,len(countries)):
        countriesVar.append(IntVar())            
        counCheckBoxR.append(Checkbutton(contnet_frame, text = countries[country], variable=countriesVar[country], onvalue = 1, offvalue = 0))
        counCheckBoxR[index].grid(row = index, column = 2, sticky = W)
        index += 1
    
    #Buttons
    submit_button = Button(submit_frame,text="Submit",width=15,command=lambda: countriesSubmit(filterCount))
    submit_button.grid(row = 0, column = 2)
    select_button = Button(submit_frame,text="Select All",width=15,command=countriesSelectAll)
    select_button.grid(row = 0, column = 0)
    reset_button = Button(submit_frame,text="Reset",width=15,command=countriesReset)
    reset_button.grid(row = 0, column = 1)

def filterContinents():
    #Filter Continents Window
    filterCont = Toplevel()
    filterCont.geometry("400x150")
    filterCont.title("Filter Continents Menu")
    filterCont.resizable(False, False)
    filterCont.configure(background="Light Grey")

    #Frames
    left_frame = Frame(filterCont)
    left_frame.grid(row=0, column=0, padx=30, pady=5)
    right_frame = Frame(filterCont)
    right_frame.grid(row=0, column=1, padx=30, pady=5)
    submit_frame = Frame(filterCont)
    submit_frame.grid(row=2, column=0, columnspan = 2, padx=30, pady=5)

    #Checkboxes
    global contCheckBoxL
    global contCheckBoxR
    global continentsVar
    
    contCheckBoxL = []
    contCheckBoxR = []
    
    index = 0
    continentCount = 0
    global continents
    continents = ["Africa","Antarctica","Asia","Europe","North America","South America","Oceania"]
    for continent in range(len(continents)):
        continentsVar.append(IntVar())  
        if continentCount  < 4:  
            contCheckBoxL.append(Checkbutton(left_frame, text = continents[continent], variable=continentsVar[continentCount]))
            contCheckBoxL[index].grid(row = index, column = 0, sticky = W)
            if index == 3:
                index = -1
        else:
            contCheckBoxR.append(Checkbutton(right_frame, text = continents[continent], variable=continentsVar[continentCount]))
            contCheckBoxR[index].grid(row = index, column = 0, sticky = W)
        index += 1
        continentCount += 1
        
    #Buttons
    submit_button = Button(submit_frame,text="Submit",width=15,command=lambda: continentSubmit(filterCont))
    submit_button.grid(row = 0, column = 2)
    select_button = Button(submit_frame,text="Select All",width=15,command=continentSelectAll)
    select_button.grid(row = 0, column = 0)
    reset_button = Button(submit_frame,text="Reset",width=15,command=continentReset)
    reset_button.grid(row = 0, column = 1)
    
def filterYears():
    years = Toplevel()
    years.geometry("280x530")
    years.title("Filter Years")
    years.resizable(False, False)
    years.configure(background="Light Grey")

    title_frame = Frame(years)
    title_frame.grid(row=0, column=0, columnspan=2, padx=30, pady=5)
    left_frame = Frame(years)
    left_frame.grid(row=1, column=0, columnspan=1, padx=30, pady=5)
    right_frame = Frame(years)
    right_frame.grid(row=1, column=1, columnspan=1, padx=30, pady=5)
    submit_frame = Frame(years)
    submit_frame.grid(row=2, column=0, columnspan=2, padx=30, pady=5)


    Label(title_frame,text="Filter Years", font=('Arial',16)).grid(row=0, column=0, padx = 10,pady=20)

    global yCheckBoxL
    global yCheckBoxR
    global yearsVar
    
    yCheckBoxL = []
    yCheckBoxR = []
    
    index = 0
    yearCount = 0
    for year in range (1990,2004):
        yearsVar.append(IntVar())            
        yCheckBoxL.append(Checkbutton(left_frame, text = year, variable=yearsVar[yearCount]))
        yCheckBoxL[index].grid(row = index, column = 0, sticky = W)
        index += 1
        yearCount += 1

    index = 0
    for year in range (2004,2018):
        yearsVar.append(IntVar())           
        yCheckBoxR.append(Checkbutton(right_frame, text = year, variable=yearsVar[yearCount]))
        yCheckBoxR[index].grid(row = index, column = 0, sticky = W)
        index += 1
        yearCount += 1

    
    submit_button = Button(submit_frame,text="Submit",width=30,command=lambda: yearsSubmit(years))
    submit_button.grid(row = 2, column = 0)
    select_button = Button(submit_frame,text="Select All",width=30,command=yearsSelectAll)
    select_button.grid(row = 0, column = 0)
    reset_button = Button(submit_frame,text="Reset",width=30,command=yearsReset)
    reset_button.grid(row = 1, column = 0)

def countriesSubmit(previousWindow):
    previousWindow.destroy()
    
    global countriesVar
    '''
    for country in countriesVar:
        print(country.get())'''

def countriesSelectAll():
    global counCheckBoxL
    global counCheckBoxM
    global counCheckBoxR

    for box in counCheckBoxL:
        box.select()
    for box in counCheckBoxM:
        box.select()
    for box in counCheckBoxR:
        box.select()

def countriesReset():
    global counCheckBoxL
    global counCheckBoxM
    global counCheckBoxR

    for box in counCheckBoxL:
        box.deselect()
    for box in counCheckBoxM:
        box.deselect()
    for box in counCheckBoxR:
        box.deselect()
 
def continentSubmit(previousWindow):
    previousWindow.destroy()
    
    global continentsVar
    '''    
    for continent in continentsVar:
        print(continent.get())'''

def continentSelectAll():
    global contCheckBoxL
    global contCheckBoxR
   
    for box in contCheckBoxL:
        box.select()
    for box in contCheckBoxR:
        box.select()

def continentReset():
    global contCheckBoxL
    global contCheckBoxR
    for box in contCheckBoxL:
        box.deselect()
    for box in contCheckBoxR:
        box.deselect()

        
def yearsSubmit(previousWindow):       
    previousWindow.destroy()
    
    global yearsVar
    '''
    years = 1990
    for year in yearsVar:
        print(years,":",year.get())
        years+=1'''


def yearsSelectAll():
    global yCheckBoxL
    global yCheckBoxR
    for box in yCheckBoxL:
        box.select()
    for box in yCheckBoxR:
        box.select()


def yearsReset():
    global yCheckBoxL
    global yCheckBoxR
    for box in yCheckBoxL:
        box.deselect()
    for box in yCheckBoxR:
        box.deselect()

def dataWindow(previousWindow):
    previousWindow.destroy()

    global yearsVar
    global continentsVar
    global countriesVar
    global continents
    global countries
    global subListsCheckVar
    global tables

    sqlContinents = "ContinentName = "
    headers = ["Year","Country Name"]
    
    database = [["hdi",["HDI", "HDIM", "HDIF", "Rank2017"]],
                ["Demography",["TotalPop", "MedianAge", "Age1564", "Age65", "Age05", "Urban"]],
                ["Education", ["EducationIndex", "GovExpEdu", "LitRate15", "TotalSchool", "TotalSchoolM", "TotalSchoolF"]],
                ["Health", ["LEBirth", "LEBirthM", "LEBirthF", "LifeExpIndex"]],
                ["Income",["GDPperCapita", "GDPTotal", "GNIperCapita", "IncomeIndex"]],
                ["Trade",["ExImTotalGDP"]],
                ["Employment",["ChildLabour", "Unemployment"]]]
    continentCheck = 0
    for continent in continentsVar:
        if continent.get() == 1:
            continentCheck += 1
    #print("Check",continentCheck)
    
    multiple = 0
    index = 0
    for table in tables:
        attributes = 0
        for attribute in table[1]:
            if subListsCheckVar[index].get() == 1:
                attributes += 1
            index += 1 
        if attributes > 0:
            multiple += 1

    index = 0
    if multiple == 1 and continentCheck == 0:
        sqlHeaders = "SELECT YearID, CountryName"
        for table in database:
            for attribute in table[1]:
                if subListsCheckVar[index].get() == 1:
                    headers.append(attribute)
                    sqlHeaders += (", "+str(attribute))
                    tableName = table[0]
                index += 1
        sqlHeaders += (" FROM "+str(tableName))

        year = 1990
        sqlYears = "YearID = "
        for item in yearsVar:
            if item.get() == 1:
                if sqlYears == "YearID = ":
                    sqlYears += str(year)
                else:
                    sqlYears += (" OR YearID = " + str(year))
            year += 1


        index = 0
        sqlCountries = "CountryName = "
        for item in countriesVar:
            if item.get() == 1:
                if sqlCountries == "CountryName = ":
                    sqlCountries += ("\""+countries[index][:-1]+"\"")
                else:
                    sqlCountries += (" OR CountryName = \""+countries[index]+"\"")
            index +=1

        if sqlYears != "YearID = ":
            sqlHeaders += (" WHERE "+sqlYears)
            if sqlCountries != "CountryName = ":
                sqlHeaders += (" OR "+sqlCountries)
        elif sqlCountries != "CountryName = ":
            sqlHeaders += (" WHERE "+sqlCountries)
    
    elif multiple == 1 and continentCheck > 0:
        index = 0
        sqlHeaders = ""
        for table in database:
            for attribute in table[1]:
                if subListsCheckVar[index].get() == 1:
                    headers.append(attribute)
                    tableName = table[0]
                    sqlHeaders += (", "+str(tableName)+"."+str(attribute))
                index += 1
        sqlHeaders = sqlHeaders[:0]+"SELECT "+tableName+".YearID, "+tableName+".CountryName"+sqlHeaders
        index = 0
        for continent in continentsVar:
            if continent.get() == 1:
                if sqlContinents == "ContinentName = ":
                    sqlContinents += "\""+continents[index]+"\""
                else:
                    sqlContinents += (" OR ContinentName = "+"\""+continents[index]+"\"")
                index += 1
        #sqlHeaders += (" FROM "+str(tableName)+" JOIN Country ON "+str(tableName)+".CountryName == Country.CountryName WHERE Country."+sqlContinents)
        
        year = 1990
        sqlYears = tableName + ".YearID = "
        for item in yearsVar:
            if item.get() == 1:
                if sqlYears == tableName + ".YearID = ":
                    sqlYears += str(year)
                else:
                    sqlYears += (" OR "+tableName+".YearID = " + str(year))
            year += 1

        index = 0
        sqlCountries = tableName + ".CountryName = "
        for item in countriesVar:
            if item.get() == 1:
                if sqlCountries == tableName + ".CountryName = ":
                    sqlCountries += ("\""+countries[index][:-1]+"\"")
                else:
                    sqlCountries += (" OR "+tableName+".CountryName = \""+countries[index]+"\"")
            index +=1
        
        if sqlYears != (tableName + ".YearID = "):
             sqlHeaders += (" WHERE "+sqlYears)
             if sqlCountries !=(tableName + ".CountryName = "):
                    sqlHeaders += (" OR "+sqlCountries)
        if sqlCountries != (tableName + ".CountryName = "):
             sqlHeaders += (" WHERE "+sqlCountries)


        sqlHeaders += (" FROM "+str(tableName)+" INNER JOIN Country ON "+str(tableName)+".CountryName == Country.CountryName WHERE "+sqlContinents)
    
    elif multiple > 1:
        index = 0
        tableID = 0
        tableNames = []
        sqlHeaders = ""
        for table in database:
            for attribute in table[1]:
                if subListsCheckVar[index].get() == 1:
                    headers.append(attribute)
                    sqlHeaders += (", "+table[0]+"."+str(attribute))
                    if database[tableID][0] not in tableNames:
                        tableNames.append(database[tableID][0])
                index += 1
            tableID += 1
        sqlHeaders = sqlHeaders[:0]+ "SELECT "+tableNames[0]+".YearID, "+tableNames[0]+".CountryName" + sqlHeaders[0:]
        sqlHeaders += (" FROM "+str(tableNames[0]))
        for table in range(1,len(tableNames)):
            sqlHeaders += " INNER JOIN "+tableNames[table]+" ON "+tableNames[0]+".CountryName = "+tableNames[table]+".CountryName "

        if sqlContinents != "ContinentName = ":
            sqlHeaders += (" INNER JOIN Continent ON "+str(tableNames[0])+".CountryName == Continent.CountryName WHERE Continent."+sqlContinents)
        
        year = 1990
        sqlYears = tableNames[0] + ".YearID = "
        for item in yearsVar:
            if item.get() == 1:
                if sqlYears == tableNames[0] + ".YearID = ":
                    sqlYears += str(year)
                else:
                    sqlYears += (" OR "+tableNames[0]+".YearID = " + str(year))
            year += 1

        index = 0
        sqlCountries = tableNames[0] + ".CountryName = "
        for item in countriesVar:
            if item.get() == 1:
                if sqlCountries == tableNames[0] + ".CountryName = ":
                    sqlCountries += ("\""+countries[index]+"\"")
                else:
                    sqlCountries += (" OR "+tableNames[0]+".CountryName = \""+countries[index]+"\"")
            index +=1

        if sqlYears != (tableNames[0] + ".YearID = "):
             sqlHeaders += (" WHERE "+sqlYears)
             if sqlCountries != (tableNames[0] + ".CountryName = "):
                    sqlHeaders += (" AND "+sqlCountries)
        elif sqlCountries != (tableNames[0] + ".CountryName = "):
             sqlHeaders += (" WHERE "+sqlCountries)


    print(sqlHeaders)
    #sqlHeaders += " SORT BY CountryName Asc;"
    result = returnSQL(sqlHeaders)
    '''
    for row in result:
        print(row)
    '''
    
    
    #Main Window
    data = Tk()
    data.geometry("720x500")
    data.title("HDI Analysis Tool - Data Window")
    data.resizable(True, True)
    data.configure(background="Light Grey")

    #Frames
    nav_frame = Frame(data)
    nav_frame.grid(row=0, column=0, padx=30, pady=5)
    title_frame = Frame(data)
    title_frame.grid(row=1, column=0, padx=30, pady=5)
    main_frame = Frame(data)
    main_frame.grid(row=2, column=0, padx=30, pady=5)

    #scrollable Frame
    global canvas
    canvas = Canvas(main_frame)
    contnet_frame =Frame(canvas)
    myscrollbar=Scrollbar(main_frame,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=contnet_frame,anchor='nw')
    contnet_frame.bind("<Configure>",myfunction)

    #Labels
    Label(title_frame,text="HDI Data Window", font=('Arial',16)).grid(row=0, column=0, padx = 10,pady=20)
    
    tableHeaders = []
    column = 0
    #print("Headers: " , headers)
    for header in headers:
        tableHeaders.append(Label(contnet_frame,text=header, font=('Arial',13)))
        tableHeaders[column].grid(row=0, column=column, padx = 5, pady=10)
        column += 1
    tableData = []
    index = 0
    rowRef = 1
    print(len(result))
    if len(result) > 500:
        maxRows = 500
        messagebox.showerror("Error", "Too much data to show,\nonly displaying 100 results")
    else:
        maxRows = len(result)
    try:
        for row in range(maxRows):
            row = list(row)
            tableData.append([])
            column = 0
            for attribute in result[row]:
                tableData[index].append(Label(contnet_frame,text=attribute, font=('Arial',11)))
                tableData[index][column].grid(row=rowRef, column=column, padx = 2)
                column += 1
            index += 1
            rowRef += 1
    except:
        messagebox.showerror("Error", "Too much data to show,\n refine your search")

    #Button
    submit_button = Button(nav_frame,text="Main Menu",width=15,command=lambda: reset(data))
    submit_button.grid(row = 0)
    

menuWindow()
