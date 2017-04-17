import csv
import sys
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import layout
from bokeh.models.widgets import Select, Slider, Div
from bokeh.models import CustomJS, ColumnDataSource, Range1d


def AccountsFunction(fName):
    # open file passed in from command line
    f = open(fName, 'r')
    reader = csv.reader(f)
    rownum = 0
    # inititalize empty lists
    dataTotalBrr = []
    dataAnnualRevenue = []
    dataNumberOfEmployees = []
    dataDandBRevenue = []
    dataDandBTotalEmployees = []
    
    # populate lists with data from the corresponding numerical data lines
    for row in reader:
        #save header row
        if rownum == 0:
            header = row
        else:
            datanew = row[3].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            dataTotalBrr.append(float(datafinal))
            
            datanew = row[4].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            dataAnnualRevenue.append(float(datafinal))
    
            datanew = row[5].replace("$", "") 
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            dataNumberOfEmployees.append(float(datafinal))
    
            datanew = row[6].replace("$", "")
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            dataDandBRevenue.append(float(datafinal))
    
            datanew = row[7].replace("$", "")
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            dataDandBTotalEmployees.append(float(datafinal))
        rownum += 1
    
    # create list with numerical data's header values
    new_head = [header[3], header[4], header[5], header[6], header[7]]
    output_file("practice.html")
    
    # create sources with each data list so it can update the sourceToDisplay
    # using the CustomJS callbacks
    source1 = ColumnDataSource(data=dict(x=dataTotalBrr, y=dataTotalBrr))
    source2 = ColumnDataSource(data=dict(x=dataAnnualRevenue, y=dataAnnualRevenue))
    source3 = ColumnDataSource(data=dict(x=dataNumberOfEmployees, y=dataNumberOfEmployees))
    source4 = ColumnDataSource(data=dict(x=dataDandBRevenue, y=dataDandBRevenue))
    source5 = ColumnDataSource(data=dict(x=dataDandBTotalEmployees, y=dataDandBTotalEmployees))
    # source to hold whichever data has been selected to be shown
    sourceToDisplay = ColumnDataSource(data=dict(x=[], y=[]))
    # initialize sourceToDisplay to initial "select" selections
    sourceToDisplay.data['x'] = source1.data['x']
    sourceToDisplay.data['y'] = source1.data['y']
    
    # initial max and min ranges
    xmin = 0
    xmax = max(dataTotalBrr)
    ymin = 0
    ymax = max(dataTotalBrr)
        
    # figure and circles for the plot
    p = figure(title="practice", x_range=[xmin, xmax], y_range=[ymin, ymax])
    p.circle(x='x', y='y', source=sourceToDisplay, size=5)
    
    # callback that takes in all the sources and assigns one to sourceToDisplay
    # based on which option is selected
    callbackx = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4,'source5':source5}, code="""
                    var v = cb_obj.value;
                    if(v == " Total BRR ") {
                        sourceToDisplay['data']['x'] = source1['data']['x'];
                    }
                    else if(v == " AnnualRevenue ") {
                        sourceToDisplay['data']['x'] = source2['data']['x'];
                    }
                    else if(v == "NumberOfEmployees") {
                        sourceToDisplay['data']['x'] = source3['data']['x'];
                    }
                    else if(v == " DandB Revenue ") {
                        sourceToDisplay['data']['x'] = source4['data']['x'];
                    }
                    else if(v == "DandB Total Employees") {
                        sourceToDisplay['data']['x'] = source5['data']['x'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    callbacky = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4,'source5':source5}, code="""
                    var v = cb_obj.value;
                    if(v == " Total BRR ") {
                        sourceToDisplay['data']['y'] = source1['data']['y'];
                    }
                    else if(v == " AnnualRevenue ") {
                        sourceToDisplay['data']['y'] = source2['data']['y'];
                    }
                    else if(v == "NumberOfEmployees") {
                        sourceToDisplay['data']['y'] = source3['data']['y'];
                    }
                    else if(v ==" DandB Revenue ") {
                        sourceToDisplay['data']['y'] = source4['data']['y'];
                    }
                    else if(v == "DandB Total Employees") {
                        sourceToDisplay['data']['y'] = source5['data']['y'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    # widgets that are select lists to choose which data to show
    selectx = Select(title="X-Value:", options=new_head, callback=callbackx)
    selecty = Select(title="Y-Value:", options=new_head, callback=callbacky)
    l = layout([[selectx, selecty], [p]])
    # show the layout with the widgets and the plot
    show(l)
    
    f.close()


def BuildingsFunction(fName):
    f = open(fName, 'r')
    reader = csv.reader(f)
    rownum = 0
    dataLatitude = []
    dataLongitude = []
    dataNetworkProximity = []
    dataEstimatedBuildCost = []
    
    for row in reader:
        #save header row
        if rownum == 0:
            header = row
        else:
            datanew = row[6].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataLatitude.append(float(datafinal))
            
            datanew = row[7].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataLongitude.append(float(datafinal))
    
            datanew = row[11].replace("$", "") 
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataNetworkProximity.append(float(datafinal))
    
            datanew = row[12].replace("$", "")
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataEstimatedBuildCost.append(float(datafinal))
        rownum += 1
    
    new_head = [header[6], header[7], header[11], header[12]]
    output_file("practice.html")
    
    source1 = ColumnDataSource(data=dict(x=dataLatitude, y=dataLatitude))
    source2 = ColumnDataSource(data=dict(x=dataLongitude, y=dataLongitude))
    source3 = ColumnDataSource(data=dict(x=dataNetworkProximity, y=dataNetworkProximity))
    source4 = ColumnDataSource(data=dict(x=dataEstimatedBuildCost, y=dataEstimatedBuildCost))
    sourceToDisplay = ColumnDataSource(data=dict(x=[], y=[]))
    #initialize sourceToDisplay
    sourceToDisplay.data['x'] = source1.data['x']
    sourceToDisplay.data['y'] = source1.data['y']
    
    #default max and min ranges
    xmin = 0
    xmax = max(dataLatitude)
    ymin = 0
    ymax = max(dataLatitude)
        
        
    p = figure(title="practice", x_range=[xmin, xmax], y_range=[ymin, ymax])
    p.circle(x='x', y='y', source=sourceToDisplay, size=5)
    
    callbackx = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4}, code="""
                    var v = cb_obj.value;
                    if(v == "Latitude") {
                        sourceToDisplay['data']['x'] = source1['data']['x'];
                    }
                    else if(v == "Longitude") {
                        sourceToDisplay['data']['x'] = source2['data']['x'];
                    }
                    else if(v == "Network Proximity") {
                        sourceToDisplay['data']['x'] = source3['data']['x'];
                    }
                    else if(v == " Estimated Build Cost ") {
                        sourceToDisplay['data']['x'] = source4['data']['x'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    callbacky = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4}, code="""
                    var v = cb_obj.value;
                    if(v == "Latitude") {
                        sourceToDisplay['data']['y'] = source1['data']['y'];
                    }
                    else if(v == "Longitude") {
                        sourceToDisplay['data']['y'] = source2['data']['y'];
                    }
                    else if(v == "Network Proximity") {
                        sourceToDisplay['data']['y'] = source3['data']['y'];
                    }
                    else if(v ==" Estimated Build Cost ") {
                        sourceToDisplay['data']['y'] = source4['data']['y'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    
    selectx = Select(title="X-Value:", options=new_head, callback=callbackx)
    selecty = Select(title="Y-Value:", options=new_head, callback=callbacky)
    l = layout([[selectx, selecty], [p]])
    show(l)
    
    f.close()


def CPQsFunction(fName):
    f = open(fName, 'r')
    reader = csv.reader(f)
    rownum = 0
    dataMRCList = []
    dataNRRList = []
    dataNPVList = []
    dataNetworkProximity = []
    
    for row in reader:
        #save header row
        if rownum == 0:
            header = row
        else:
            datanew = row[4].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataMRCList.append(float(datafinal))
            
            datanew = row[5].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataNRRList.append(float(datafinal))
    
            datanew = row[6].replace("$", "") 
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataNPVList.append(float(datafinal))
    
            datanew = row[13].replace("$", "")
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataNetworkProximity.append(float(datafinal))
        rownum += 1
    
    new_head = [header[4], header[5], header[6], header[13]]
    output_file("practice.html")
    
    source1 = ColumnDataSource(data=dict(x=dataMRCList, y=dataMRCList))
    source2 = ColumnDataSource(data=dict(x=dataNRRList, y=dataNRRList))
    source3 = ColumnDataSource(data=dict(x=dataNPVList, y=dataNPVList))
    source4 = ColumnDataSource(data=dict(x=dataNetworkProximity, y=dataNetworkProximity))
    sourceToDisplay = ColumnDataSource(data=dict(x=[], y=[]))
    #initialize sourceToDisplay
    sourceToDisplay.data['x'] = source1.data['x']
    sourceToDisplay.data['y'] = source1.data['y']
    
    #default max and min ranges
    xmin = 0
    xmax = max(dataMRCList)
    ymin = 0
    ymax = max(dataMRCList)
        
        
    p = figure(title="practice", x_range=[xmin, xmax], y_range=[ymin, ymax])
    p.circle(x='x', y='y', source=sourceToDisplay, size=5)
    
    callbackx = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4}, code="""
                    var v = cb_obj.value;
                    if(v == " X36 MRC List ") {
                        sourceToDisplay['data']['x'] = source1['data']['x'];
                    }
                    else if(v == " X36 NRR List ") {
                        sourceToDisplay['data']['x'] = source2['data']['x'];
                    }
                    else if(v == " X36 NPV List ") {
                        sourceToDisplay['data']['x'] = source3['data']['x'];
                    }
                    else if(v == "Network Proximity") {
                        sourceToDisplay['data']['x'] = source4['data']['x'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    callbacky = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4}, code="""
                    var v = cb_obj.value;
                    if(v == " X36 MRC List ") {
                        sourceToDisplay['data']['y'] = source1['data']['y'];
                    }
                    else if(v == " X36 NRR List ") {
                        sourceToDisplay['data']['y'] = source2['data']['y'];
                    }
                    else if(v == " X36 NPV List ") {
                        sourceToDisplay['data']['y'] = source3['data']['y'];
                    }
                    else if(v =="Network Proximity") {
                        sourceToDisplay['data']['y'] = source4['data']['y'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    
    selectx = Select(title="X-Value:", options=new_head, callback=callbackx)
    selecty = Select(title="Y-Value:", options=new_head, callback=callbacky)
    l = layout([[selectx, selecty], [p]])
    show(l)
    
    f.close()


def OpportunitiesFunction(fName):
    f = open(fName, 'r')
    reader = csv.reader(f)
    rownum = 0
    dataTermInMonths = []
    dataNetworkProximity = []
    
    for row in reader:
        #save header row
        if rownum == 0:
            header = row
        else:
            datanew = row[6].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataTermInMonths.append(float(datafinal))
    
            datanew = row[16].replace("$", "")
            dataneww = datanew.replace(",", "") 
            datafinal = dataneww.replace("-", "0")
            if datafinal == "":
                datafinal = 0
            dataNetworkProximity.append(float(datafinal))
        rownum += 1
    
    new_head = [header[6], header[16]]
    output_file("practice.html")
    
    source1 = ColumnDataSource(data=dict(x=dataTermInMonths, y=dataTermInMonths))
    source2 = ColumnDataSource(data=dict(x=dataNetworkProximity, y=dataNetworkProximity))
    sourceToDisplay = ColumnDataSource(data=dict(x=[], y=[]))
    #initialize sourceToDisplay
    sourceToDisplay.data['x'] = source1.data['x']
    sourceToDisplay.data['y'] = source1.data['y']
    
    #default max and min ranges
    xmin = 0
    xmax = max(dataTermInMonths)
    ymin = 0
    ymax = max(dataTermInMonths)
        
        
    p = figure(title="practice", x_range=[xmin, xmax], y_range=[ymin, ymax])
    p.circle(x='x', y='y', source=sourceToDisplay, size=5)
    
    callbackx = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2}, code="""
                    var v = cb_obj.value;
                    if(v == "Term in Months") {
                        sourceToDisplay['data']['x'] = source1['data']['x'];
                    }
                    else if(v == "Network Proximity") {
                        sourceToDisplay['data']['x'] = source2['data']['x'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    callbacky = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2}, code="""
                    var v = cb_obj.value;
                    if(v == "Term in Months") {
                        sourceToDisplay['data']['y'] = source1['data']['y'];
                    }
                    else if(v =="Network Proximity") {
                        sourceToDisplay['data']['y'] = source2['data']['y'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    
    selectx = Select(title="X-Value:", options=new_head, callback=callbackx)
    selecty = Select(title="Y-Value:", options=new_head, callback=callbacky)
    l = layout([[selectx, selecty], [p]])
    show(l)
    
    f.close()


def ServicesFunction(fName):
    f = open(fName, 'r')
    reader = csv.reader(f)
    rownum = 0
    dataTotalMRR = []
    dataNetxMRC = []
    
    for row in reader:
        #save header row
        if rownum == 0:
            header = row
        else:
            datanew = row[2].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            dataTotalMRR.append(float(datafinal))
            
            datanew = row[3].replace("$", "")
            dataneww = datanew.replace(",", "")
            datafinal = dataneww.replace("-", "0")
            dataNetxMRC.append(float(datafinal))
        rownum += 1
    
    new_head = [header[2], header[3]]
    output_file("practice.html")
    
    source1 = ColumnDataSource(data=dict(x=dataTotalMRR, y=dataTotalMRR))
    source2 = ColumnDataSource(data=dict(x=dataNetxMRC, y=dataNetxMRC))
    sourceToDisplay = ColumnDataSource(data=dict(x=[], y=[]))
    #initialize sourceToDisplay
    sourceToDisplay.data['x'] = source1.data['x']
    sourceToDisplay.data['y'] = source1.data['y']
    
    #default max and min ranges
    xmin = 0
    xmax = max(dataTotalMRR)
    ymin = 0
    ymax = max(dataTotalMRR)
        
        
    p = figure(title="practice", x_range=[xmin, xmax], y_range=[ymin, ymax])
    p.circle(x='x', y='y', source=sourceToDisplay, size=5)
    
    callbackx = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4,'source5':source5}, code="""
                    var v = cb_obj.value;
                    if(v == "Total MRR") {
                        sourceToDisplay['data']['x'] = source1['data']['x'];
                    }
                    else if(v == "Netx MRC") {
                        sourceToDisplay['data']['x'] = source2['data']['x'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    callbacky = CustomJS(args={'sourceToDisplay':sourceToDisplay,'source1':source1,'source2':source2,'source3':source3,'source4':source4,'source5':source5}, code="""
                    var v = cb_obj.value;
                    if(v == "Total MRR") {
                        sourceToDisplay['data']['y'] = source1['data']['y'];
                    }
                    else if(v == "Netx MRC") {
                        sourceToDisplay['data']['y'] = source2['data']['y'];
                    }
                    sourceToDisplay.trigger('change');
                """)
    
    selectx = Select(title="X-Value:", options=new_head, callback=callbackx)
    selecty = Select(title="Y-Value:", options=new_head, callback=callbacky)
    l = layout([[selectx, selecty], [p]])
    show(l)
    
    f.close()

# takes in argument which is the file to be visualized
in_file = sys.argv[1]
# depending on which is included in the file (as there might be variants)
# call the corresponding function defined above
if "Accounts" in in_file:
    AccountsFunction(in_file)
elif "Buildings" in in_file:
    BuildingsFunction(in_file)
elif "CPQs" in in_file:
    CPQsFunction(in_file)
elif "Opportunities" in in_file:
    OpportunitiesFunction(in_file)
elif "Services" in in_file:
    ServicesFunction(in_file)
# if none match up, print a usage statement
else:
    print("Please pass in a file that has 'Accounts', 'Buildings', 'CPQs', 'Opportunities', or 'Services' in the name.")


