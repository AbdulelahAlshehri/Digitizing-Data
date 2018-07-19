
import csv
__author__ = "Abdulelah Alshehri"
__email__ = "asaalshehr@gmail.com"

#TODO: Change label tags to attributes
#TODO: Include all elements and attributes
#Define CSV file
csvF = r"C:\Users\shehrias\Desktop\DDT\cf.csv"
#Read CSV file
Data= csv.reader(open(csvF))


#Name XML file to be created
xmlFile = r'C:\Users\shehrias\Desktop\DDT\expData.xml'
# XML file to be created
xmld = open(xmlFile, 'w')
#XML Declaration
xmld.write('<?xml version="1.0"?>' + "\n")


#Parent Element
xmld.write('<property>' + "\n")

#Append properties as data points for each column
rowNum = 0

for row in Data:
#if row zero, create tags.
    if rowNum == 0:
#Create tag names
        tags = row
        # Remove spaces form tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    #Otherwise append data to datapoints tags
    else:
        xmld.write('<datapoint>' + "\n")
        for i in range(len(tags)):
            xmld.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmld.write('</datapoint>' + "\n")
    #iterate
    rowNum += 1
#Close main element and file
xmld.write('</property>' + "\n")
xmld.close()