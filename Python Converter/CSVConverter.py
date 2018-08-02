import csv
import warnings
import itertools

__author__ = "Abdulelah Alshehri"
__email__ = "asaalshehr@gmail.com"

# Define CSV file
csvF = r"C:\Users\shehrias\Desktop\DDT\Python Converter\j.combustflame.2010.12.008_1.csv"
# Name XML file to be created
xmlFile = r'C:\Users\shehrias\Desktop\DDT\Python Converter\expData.xml'
# Read CSV file
Data = csv.reader(open(csvF))
# number of rows
rows =next(csv.reader(open(csvF)))
Rowsn = len(rows)
# XML file to be created
xmld = open(xmlFile, 'w')
# XML Declaration
xmld.write('<?xml version="1.0"?>' + "\n")

# Define File Author
fileAuthor = r'Leplat, N. and Dagaut, P. and Togbé, C. and Vandooren, J.'
# Timeshift
timeshift = r''
# comment
comment = r''
# ignitionType
target = r''
type = r''
# Define filetypDOI
fileDOI = r'10.1016/j.combustflame.2010.12.008'
# Define fileVersion major and minor
major = r'N/A'
minor = r'N/A'
# Define fileVersion major and minor
Rmajor = r'N/A'
Rminor = r'N/A'
# Experiment type
experimentType = r'Jet stirred reactor measurement'
# bibliographyLink
description = r'Numerical and experimental study of ethanol combustion and oxidation in laminar premixed flames and in jet-stirred reactor'
referenceDOI = r'10.1016/j.combustflame.2010.12.008'
location = r'Main article'
table=r''
figure = r'Fig. 9, C3H6 not taken'
# apparatus
kind = r''
#commonProperties
name=r'initial composition'
sourcetype=r'reported'
#speciesLink
preferredKey=['C2H5OH', 'O2', 'N2']
CAS=['NA' ,'NA' ,'NA']
units=['mole fraction','mole fraction','mole fraction']
amount=[0.002,0.024,0.974]
#Datagroup
x=[]
for i in range(Rowsn):
    x.append('x'+str(i+1))
label=next(csv.reader(open(csvF)))
Dname=[]
Dunits=[]
#ifshorter than this!!!!!
# Parent Element
xmld.write('<experiment>' + "\n")
xmld.write('<fileAuthor>' + fileAuthor + '</fileAuthor>' + "\n")
if len(timeshift)>1:
    xmld.write('<timeshift>' + timeshift + '</timeshift>' + "\n")
if len(comment)>0:
    xmld.write('<comment>' + comment + '</comment>' + "\n")
if len(target)>0:
    xmld.write('<ignitionType>' + "\n" +
           '<target>' + target +'</target>'+ "\n" +
           '<type>' + type +'</type>'+ "\n" +
           '</ignitionType>' + "\n")
if len(fileDOI)>0:
    xmld.write('<fileDOI>' + fileDOI + '</fileDOI>' + "\n")
if len(major)>0:
    xmld.write('<fileVersion>' + "\n" +
           '<major>' + major +'</major>'+ "\n" +
           '<minor>' + minor +'</minor>'+ "\n" +
           '</fileVersion>' + "\n")
if len(Rmajor)>0:
    xmld.write('<ReSpecThVersion>' + "\n" +
           '<major>' + Rmajor +'</major>'+ "\n" +
           '<minor>' + Rminor +'</minor>'+ "\n" +
           '</ReSpecThVersion>' + "\n")
xmld.write('<experimentType>' + experimentType + '</experimentType>' + "\n")
xmld.write('<bibliographyLink>' + "\n" +
           '<description>' + description +'</description>'+ "\n" +
           '<referenceDOI>' + referenceDOI +'</referenceDOI>'+ "\n" +
           '<location>' + location +'</location>'+ "\n" +
           '<table>' +table+'</table>'+ "\n" +
           '<figure>' + figure +'</figure>'+ "\n" +
           '</bibliographyLink>' + "\n")
if len(kind)>0:
    xmld.write('<apparatus>' + "\n" +
           '<kind>' + kind +'</kind>'+ "\n" +
           '</apparatus>' + "\n")

xmld.write('<commonProperties>' + "\n")
xmld.write('<property' + " name=" + '"'+name +'"'+
                        " sourcetype=" + '"'+sourcetype +'"'+'>')
for i in range(len(preferredKey)):
    xmld.write('<component><speciesLink' + " preferredKey=" + '"'+preferredKey[i] +'"'+'/>')
    xmld.write('<amount'+ ' units=' +'"'+ str(units[i])+'"'+'>'+ str(amount[i])+'</amount>'+'</component>')
xmld.write('</property></commonProperties>' + "\n")

xmld.write('<dataGroup id="1">' + "\n")

for i in range(len(x)):
    xmld.write('<property id=' + '"'+x[i] +'"'+
                         'label=''"'+rows[i] +'"'+
                         'name=''"' + rows[i] + '"' +
                         'sourcetype=''"' + sourcetype + '"' +
                         'units=''"' + rows[i] + '"' +
               '/>'+ "\n")
    # xmld.write('<amount'+ ' units=' +'"'+ str(units[i])+'"'+'>'+ str(amount[i])+'</amount>'+'</component>')


# Append properties as data points for each column
rowNum = 0

for row in Data:
    # if row zero, create tags.
    if rowNum == 0:
        # Create tag names
        tags = x
        # Remove spaces form tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    # Otherwise append data to datapoints tags
    else:
        xmld.write('<datapoint>' + "\n")
        for i in range(len(tags)):
            xmld.write('    ' + '<' + tags[i] + '>' \
                       + row[i] + '</' + tags[i] + '>' + "\n")
        xmld.write('</datapoint>' + "\n")
    # iterate
    rowNum += 1
# Close main element and file
xmld.write('</dataGroup>' + "\n")
xmld.write('</experiment>' + "\n")

xmld.close()
