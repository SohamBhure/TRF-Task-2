#Importing necessary libraries
import requests
from bs4 import BeautifulSoup

print()   ####

search = input("Enter Word to Search: ").split()  #Inputs the word to be searched

site = "https://www.dictionary.com/browse/"
for x in search:                    #Creates the url to be parsed
    site += str(x)

response = requests.get(site)
soup = BeautifulSoup(response.text,'html.parser')

print()

if (soup.find_all(class_="css-1o58fj8 e1hk9ate4")):  #for valid word

    counter = 1
    posts = soup.find_all(class_="css-1o58fj8 e1hk9ate4")
    for post in posts:       #prints all definations from the website

        print(str(counter) + ". " + post.get_text())
        counter += 1

else:      #for invalid word
    print("Enter Valid Word")

