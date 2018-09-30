from datetime import date, timedelta
import requests,datetime,os

def download_file(day,month,year):
	print("Downloading for",day,month,year)
	file_url = "https://nseindia.com/content/historical/EQUITIES/"+str(year)+"/"+month+"/cm"+str(day)+month+str(year)+"bhav.csv.zip"
	r = requests.get(file_url, stream = True) 
	with open("cm"+str(day)+month+str(year)+"bhav.csv.zip","wb") as zip: 
		for chunk in r.iter_content(chunk_size=1024):  
			if chunk:
				zip.write(chunk)
	
	file_info = os.stat("cm"+str(day)+month+str(year)+"bhav.csv.zip")
	size=file_info.st_size/1024
	if size<1:	#Files for holiday days are less than 1KB. So delete them
		os.remove("cm"+str(day)+month+str(year)+"bhav.csv.zip")
	else:	# Save the file at given location
		os.rename(os.getcwd()+"\\cm"+str(day)+month+str(year)+"bhav.csv.zip", loc+"\\cm"+str(day)+month+str(year)+"bhav.csv.zip")
	
if __name__=='__main__':
	loc=input("Enter the location where file needs to be downloaded :")
	now = datetime.datetime.now()
	prev = now - timedelta(days=365)
	start_date = date(prev.year, prev.month, prev.day)  # start date
	end_date = date(now.year, now.month, now.day)  # end date
	delta = end_date - start_date         # timedelta
	for i in range(delta.days + 1):
		dat=start_date + timedelta(i)
		day=dat.strftime("%d")
		month=dat.strftime("%b").upper()
		year=dat.strftime("%Y")
		weekday=dat.strftime("%a")
		if weekday=='Sat' or weekday=='Sun':	#Saturday and Sunday is holiday. So, no need to download the files for these days.
			continue
		download_file(day,month,year)
	
	print("Completed")
