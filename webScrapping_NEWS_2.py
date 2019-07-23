from bs4 import BeautifulSoup
import requests


print()

x = input("Enter News to Search: ").split()   #Inputs news topics to be searched
x = ("%20".join(x))

site_Google = "https://news.google.com/search?q=" + str(x) + "&hl=en-IN&gl=IN&ceid=IN%3Aen"   #Creates urls to be parsed
site_IndiaToday = "https://www.indiatoday.in/topic/" + str(x)
site_NDTV = "https://www.ndtv.com/topic/" + str(x)
site_TOI = "https://timesofindia.indiatimes.com/topic/" + str(x) + "/"



# GOOGLE NEWS

print()
print ("GOOGLE NEWS :")

response = requests.get(site_Google)
soup = BeautifulSoup(response.text, 'html.parser')   #passes 


posts = soup.find_all('h3', class_ = "ipQwMb ekueJc RD0gLb")    #finds all tags having given CSS class



for i in range (1,6):           #prints top5 news articles 
   print(str(i) + ". " + posts[i-1].get_text())




# INDIA TODAY

print()
print ("INDIA TODAY NEWS :")

response = requests.get(site_IndiaToday)
soup = BeautifulSoup(response.text, 'html.parser')


posts = soup.find_all('div', class_ = "views-field views-field-php-2")    #finds all tags having given CSS class

for i in range (1,6):           #prints top5 news articles 
   print(str(i) + ". " + posts[i-1].get_text())




# TIMES OF INDIA

print()
print ("TIMES OF INDIA NEWS :")

response = requests.get(site_TOI)
soup = BeautifulSoup(response.text, 'html.parser')


posts = soup.find_all('div', class_ = "content")     #finds all tags having given CSS class

for i in range (1,6):           #prints top5 news articles 
   print(str(i) + ". " + posts[i-1].get_text()[1::])

print()



# NDTV

print()
print ("NDTV NEWS :")

response = requests.get(site_NDTV)
soup = BeautifulSoup(response.text, 'html.parser')    #finds all tags having given CSS class


posts = soup.find_all('p', class_ = "intro")

for i in range (1,6):           #prints top5 news articles 
   print(str(i) + ". " + posts[i-1].get_text()[25::])










