from bs4 import BeautifulSoup
import requests


print()

x = input("Enter News to Search: ").split()

x = ("%20".join(x))

site_Google = "https://news.google.com/search?q=" + str(x) + "&hl=en-IN&gl=IN&ceid=IN%3Aen"
site_IndiaToday = "https://www.indiatoday.in/topic/" + str(x)
site_NDTV = "https://www.ndtv.com/topic/" + str(x)
site_TOI = "https://timesofindia.indiatimes.com/topic/" + str(x) + "/"



# GOOGLE NEWS

print()
print ("GOOGLE NEWS :")

response = requests.get(site_Google)
soup = BeautifulSoup(response.text, 'html.parser')

counter = 1
posts = soup.find_all('h3', class_ = "ipQwMb ekueJc RD0gLb")



for i in range (1,6):
   print(str(i) + ". " + posts[i-1].get_text())




# INDIA TODAY

print()
print ("INDIA TODAY NEWS :")

response = requests.get(site_IndiaToday)
soup = BeautifulSoup(response.text, 'html.parser')

counter = 1
posts = soup.find_all('div', class_ = "views-field views-field-php-2")

for i in range (1,6):
   print(str(i) + ". " + posts[i-1].get_text())




# TIMES OF INDIA

print()
print ("TIMES OF INDIA NEWS :")

response = requests.get(site_TOI)
soup = BeautifulSoup(response.text, 'html.parser')

counter = 1
posts = soup.find_all('div', class_ = "content")

for i in range (1,6):
   print(str(i) + ". " + posts[i-1].get_text()[1::])

print()



# NDTV

print()
print ("NDTV NEWS :")

response = requests.get(site_NDTV)
soup = BeautifulSoup(response.text, 'html.parser')

counter = 1
posts = soup.find_all('p', class_ = "intro")

for i in range (1,6):
   print(str(i) + ". " + posts[i-1].get_text()[25::])










