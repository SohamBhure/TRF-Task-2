import requests
from bs4 import BeautifulSoup

print()

search = input("Enter Word to Search: ").split()

site = "https://www.dictionary.com/browse/"
for x in search:
    site += str(x)

response = requests.get(site)
soup = BeautifulSoup(response.text,'html.parser')

print()

if (soup.find_all(class_="css-1o58fj8 e1hk9ate4")):

    counter = 1
    posts = soup.find_all(class_="css-1o58fj8 e1hk9ate4")
    for post in posts:

        print(str(counter) + ". " + post.get_text())
        counter += 1

else:
    print("Enter Valid Word")

