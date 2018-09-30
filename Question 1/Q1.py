import datetime
# Check for the leap year
def leap_year(year):
	count_pos=0
	count_neg=0
	year_pos=year
	year_neg=year
	for i in range(1,3):
		if (( year_pos%400 == 0) or (( year_pos%4 == 0 ) and ( year_pos%100 != 0))):
			break
		else:
			year_pos=year_pos+1
			count_pos+=1
	if count_pos==2:
		for i in range(3,1,-1):
			if (( year_neg%400 == 0) or (( year_neg%4 == 0 ) and ( year_neg%100 != 0))):
				break
			else:
				year_neg=year_neg-1
				count_neg+=1
	else:
		return year_pos,0
	if count_neg<count_pos:
		return 0,year_neg
	return year_pos,year_neg
	#Get the year input from the user
num = int(input("Please Enter the Year : "))
	#Check if the input year is a leap year or not
if (( num%400 == 0) or (( num%4 == 0 ) and ( num%100 != 0))):
		dat = datetime.date(num,2,29)
		print(dat.strftime("%A"))
else: 
	print("This is not a leap year")
	year_fw,year_bk=leap_year(num)		#Check for the closest leap year
	if year_fw==0:
		dat = datetime.date(year_bk,2,29)
		print("Closest leap year :",(year_bk))
		print(dat.strftime("%A"))
	elif year_bk==0:
		dat = datetime.date(year_fw,2,29)
		print("Closest leap year :",(year_fw))
		print(dat.strftime("%A"))
	else:
		dat1 = datetime.date(year_fw,2,29)
		dat2 = datetime.date(year_bk,2,29)
		print("Closest leap years :")
		print(year_bk,dat2.strftime("%A"))
		print(year_fw,dat1.strftime("%A"))
