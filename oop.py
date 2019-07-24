from bs4 import BeautifulSoup
import requests


x = input("Enter News to Search: ").split()   #Inputs news topics to be searched
x = ("%20".join(x))


class Google:
    def __init__(self, site):
        self.site  = "https://news.google.com/search?q=" + str(site) + "&hl=en-IN&gl=IN&ceid=IN%3Aen"   #Creates urls to be parsed

    def create_soup(self, site):
        response = requests.get(self.site)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def print_news(self, soup):
        posts = soup.find_all('h3', class_="ipQwMb ekueJc RD0gLb")  # finds all tags having given CSS class
        print()
        print("GOOGLE NEWS")
        for i in range(1, 6):  # prints top5 news articles
            print(str(i) + ". " + posts[i - 1].get_text())

class IndiaToday:
    def __init__(self, site):
        self.site  = site_IndiaToday = "https://www.indiatoday.in/topic/" + str(x)

    def create_soup(self, site):
        response = requests.get(self.site)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def print_news(self, soup):
        posts = soup.find_all('div', class_="views-field views-field-php-2")  # finds all tags having given CSS class
        print()
        print("INDIA TODAY NEWS")
        for i in range(1, 6):  # prints top5 news articles
            print(str(i) + ". " + posts[i - 1].get_text())


class TOI:
    def __init__(self, site):
        self.site = site_TOI = "https://timesofindia.indiatimes.com/topic/" + str(x) + "/"   #Creates urls to be parsed

    def create_soup(self, site):
        response = requests.get(self.site)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def print_news(self, soup):
        posts = soup.find_all('span', class_="w_tle")  # finds all tags having given CSS class
        print()
        print("TIMES OF INDIA  NEWS")
        for i in range(1, 6):  # prints top5 news articles
            print(str(i) + ". " + posts[i - 1].get_text()[1::])

class NDTV:
    def __init__(self, site):
        self.site = site_NDTV = "https://www.ndtv.com/topic/" + str(x)   #Creates urls to be parsed

    def create_soup(self, site):
        response = requests.get(self.site)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def print_news(self, soup):
        posts = soup.find_all('p', class_="intro")
        print()
        print("NDTV NEWS")
        for i in range(1, 6):  # prints top5 news articles
            print(str(i) + ". " + posts[i - 1].get_text()[25::])


def main():
    G_news = Google(x)
    G_soup = G_news.create_soup(G_news)
    G_news.print_news(G_soup)

    IT_news = IndiaToday(x)
    IT_soup = IT_news.create_soup(IT_news)
    IT_news.print_news(IT_soup)

    TOI_news = TOI(x)
    TOI_soup = TOI_news.create_soup(TOI_news)
    TOI_news.print_news(TOI_soup)

    NDTV_news = NDTV(x)
    NDTV_soup = NDTV_news.create_soup(NDTV_news)
    NDTV_news.print_news(NDTV_soup)

if __name__ == '__main__':
    main()


