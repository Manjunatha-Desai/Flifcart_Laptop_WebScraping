from bs4 import BeautifulSoup
import requests

url= requests.get('https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=155ea509-1834-4e62-b07b-743f08f404aa').text
#print(url)

soup =  BeautifulSoup(url,'lxml')
#print(soup)

laptops=soup.find_all('div', class_='_2kHMtA')
#print(mobiles)

for laptop in laptops:
     mBrand = laptop.find('div', class_='_4rR01T').text
     mPrice = laptop.find('div', class_='_30jeq3 _1_WHN1').text.replace("₹","")
     mstars = laptop.find('li', class_='rgWa7D').text
     print(f'''"Laptop Brand Name:"{mBrand.strip()}'''),
     print(f'''"Price of the Laptop is :"{mPrice.strip()}'''),
     print(f'''"Ratings:"{mstars.strip()}''')
     print()
     #writer.writerow(mBrand,mPrice)
     #print(laptop)
