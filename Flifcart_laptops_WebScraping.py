from bs4 import BeautifulSoup
# to import the bs4 module
import requests
# import the  requests module for getting data from url

url= requests.get('https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=155ea509-1834-4e62-b07b-743f08f404aa').text
#print(url)

soup =  BeautifulSoup(url,'lxml')
#print(soup)

laptops=soup.find_all('div', class_='_2kHMtA')
#print(laptops)


for laptop in laptops:
     lBrand = laptop.find('div', class_='_4rR01T').text
     lPrice = laptop.find('div', class_='_30jeq3 _1_WHN1').text.replace("₹","")
     lProcessor = laptop.find('li', class_='rgWa7D').text
     #print(f'''Laptop Brand Name:{lBrand.strip()}'''),
     #print(f'''Price of the Laptop is :{lPrice.strip()}'''),
     #print(f'''Processor:{lProcessor.strip()}''')
     #print()
     laptop_dict={
         "laptop Brand":lBrand,
         "laptop Price":lPrice,
         "laptop Processor":lProcessor
         }
  
     print(laptop_dict)
     