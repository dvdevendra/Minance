# Reading an excel file using Python 
import xlrd,datetime
  
# Give the location of the file 
loc = input("Enter the path and name of excel file: ") 
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
rows=sheet.nrows
columns=sheet.ncols
sum=0
records={}
#Get all the unique records
for i in range(1,rows):
	lis=sheet.row_values(i)
	date_val = str(datetime.datetime(*xlrd.xldate_as_tuple(lis[1], wb.datemode)))
	date_column_value=date_val.split(" ")
	string=lis[0]+" "+date_column_value[0]+" "+lis[2]
	if string not in records:
		records[string]=1
		sum+=1
	else:
		value=records[string]
		records[string]=value+1

for x in records:
	print(x,"Count ="+str(records[x]))
print("Unique values= "+str(sum))
