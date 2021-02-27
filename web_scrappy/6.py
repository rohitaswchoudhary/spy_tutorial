import requests
import bs4
import pandas as pd


HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'})
offer=[]
def tracker(url,TrackingPrice):
    res = requests.get(url,headers=HEADERS)
    soup = bs4.BeautifulSoup(res.content, features='lxml')
    
    # to prevent script from crashing when there isn't a price for the product
    try:
        title = soup.find(id="productTitle").get_text().strip()
        amount = float(soup.find(id='priceblock_ourprice').get_text().replace("₹","").replace("$","").strip())
        if amount<=TrackingPrice:
            offer.append("You got a offer on the {0} for {1}. Check out the product {2}".format(title,amount,url))
            
            
    except:
        offer.append("Couldn't get details about product")


df=pd.read_csv("AmazonPriceTrackerSheet1.csv")
for i in range(0,len(df["URL"])):
    tracker(df["URL"][i],df["TrackingPrice"][i])
# print(f"message: {offer}")
print("message",offer)