"""
Name          :Rafailia
Surname       :Ioannou
Programm Title: Opap KINO check results for user.
Date          :30/09/16
Description   : First install the requests module.
"""
import requests
import time
import sys
#OPAP KINO web service
url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/";
print "Input your numbers from 1 to 80. Give 12 numbers separate by comma and \" at begin and the end. Sample \"1,2,3,4,5,6,7,8,9,10,11,12\"";
#Read the input numbers
try:
	user_numbers=str(input());
except Exception:
		print("Oops! Something went wrong. Try again...");
		sys.exit();
numbersArray = [int(0)]*12;
numbers = user_numbers.split(",");
position=0;
for num in numbers:
	numbersArray[int(position)] = num;
	position+=1;
current_day = time.strftime("%d");
current_month = time.strftime("%m");
current_year = time.strftime("%Y");

for num in range(1,int(current_day)):
	day = num;
	if(int(num) < 10):
		day = "0" + str(num);
	#Add in the url the date
	urlDate = url + str(day) + "-" + current_month + "-" + current_year + ".json";
	response = requests.get(urlDate);
	if(response.ok):
		#Get response from KINO web service
		data = response.json();
		draws = data["draws"];
		draw = draws["draw"];
		for d in draw:
			drawTime = d["drawTime"];
			drawNo = d["drawNo"];
			results = d["results"];
			winNumbers = 0;
			for result in results:
				for selectedNumber in numbers:
					if(int(result) == int(selectedNumber)):
						winNumbers+=1;
			if(winNumbers>0):
				print(str(drawTime) + "/" + str(drawNo) + " " + "wins:" + str(winNumbers) + " out of " + str(len(numbers)));
