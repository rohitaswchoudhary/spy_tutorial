# importing modules 
import json 
import requests 
import pandas as pd 
import matplotlib.pyplot as plt 

# storing the url in the form of string 
url = "https://api.covid19india.org/state_district_wise.json"

# function to get data from api 


def casesData(): 
	# getting the json data by calling api 
	data = ((requests.get(url)).json()) 
	states = [] 

	# getting states 
	for key in data.items(): 
		states.append(key[0]) 

	# getting statewise data 
	for state in states: 
		f = (data[state]['districtData']) 
		tc = [] 
		dis = [] 
		act, con, dea, rec = 0, 0, 0, 0

		# getting districtwise data 
		for key in (data[state]['districtData']).items(): 
			district = key[0] 
			dis.append(district) 
			active = data[state]['districtData'][district]['active'] 
			confirmed = data[state]['districtData'][district]['confirmed'] 
			deaths = data[state]['districtData'][district]['deceased'] 
			recovered = data[state]['districtData'][district]['recovered'] 
			if district == 'Unknown': 
				active, confirmed, deaths, recovered = 0, 0, 0, 0
			tc.append([active, confirmed, deaths, recovered]) 
			act = act + active 
			con = con + confirmed 
			dea = dea + deaths 
			rec = rec + recovered 
		tc.append([act, con, dea, rec]) 
		dis.append('Total') 
		parameters = ['Active', 'Confirmed', 'Deaths', 'Recovered'] 

		# creating a dataframe 
		df = pd.DataFrame(tc, dis, parameters) 
		print('COVID - 19', state, 'District Wise Data') 
		print(df) 

		# plotting of data 
		plt.bar(dis, df['Active'], width = 0.5, align = 'center') 
		fig = plt.gcf() 
		fig.set_size_inches(18.5, 10.5) 
        # plt.xlabel('no of people')
		plt.xticks(rotation = 75) 
		plt.show() 
		print('*' * 100) 


# states data available throug API 
# ''' 
# 0 State Unassigned 
# 1 Andaman and Nicobar Islands 
# 2 Andhra Pradesh 
# 3 Arunachal Pradesh 
# 4 Assam 
# 5 Bihar 
# 6 Chandigarh 
# 7 Chhattisgarh 
# 8 Delhi 
# 9 Dadra and Nagar Haveli and Daman and Diu 
# 10 Goa 
# 11 Gujarat 
# 12 Himachal Pradesh 
# 13 Haryana 
# 14 Jharkhand 
# 15 Jammu and Kashmir 
# 16 Karnataka 
# 17 Kerala 
# 18 Ladakh 
# 19 Lakshadweep 
# 20 Maharashtra 
# 21 Meghalaya 
# 22 Manipur 
# 23 Madhya Pradesh 
# 24 Mizoram 
# 25 Nagaland 
# 26 Odisha 
# 27 Punjab 
# 28 Puducherry 
# 29 Rajasthan 
# 30 Sikkim 
# 31 Telangana 
# 32 Tamil Nadu 
# 33 Tripura 
# 34 Uttar Pradesh 
# 35 Uttarakhand 
# 36 West Bengal 
# '''

#Driver Code 
casesData() 
