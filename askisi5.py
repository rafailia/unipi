"""
Name          :Rafailia
Surname       :Ioannou
Programm Title: Beers Name by Type
Date          :30/09/16
Description   : First install the requests module.
"""
import requests
import json
import sys
api_key="b4877dc6e478a789262b2c7fc3f60842";
url_categories = "http://api.brewerydb.com/v2/categories/?key=";
url_styles = "http://api.brewerydb.com/v2/styles/?key=";
response_categories = requests.get(url_categories+api_key);
if(response_categories.ok):
	jData_categories = json.loads(response_categories.content);
	data_categories = jData_categories["data"];
	print("Choose type number:");
	for items_category in data_categories:
		category_type = items_category["id"];
		category_name = items_category["name"];
		print(str(category_type) + ":" + category_name);
	try:
		choice=str(input());
	except Exception:
		print("Oops!  That was no valid number.  Try again...");
		sys.exit();
	response_styles = requests.get(url_styles+api_key);
	if(response_styles.ok):
		jData_styles = json.loads(response_styles.content);
		data_styles = jData_styles["data"];
		beers_found = False;
		count=1;
		for items in data_styles:
			categoryId = items["categoryId"];
			beerType = items["id"];
			beerName = items["name"];
			if(int(choice) == int(categoryId)):
				beers_found = True;
				print(str(count) + ":" + beerName);
				count+=1;
		if(not beers_found):
			print("No Beers Found.");
	else:
		print("Error Retrieving beers.");
else:
	print("Error Retrieving Data.");
