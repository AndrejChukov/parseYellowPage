from bs4 import BeautifulSoup
import requests


class parseCategories:
    output_links = set()


    def startParsing(self):
        response = requests.get("https://www.yp.ru/")

        self.soup = BeautifulSoup(response.text, 'html.parser')

        input_links = self.soup.find_all('div', class_='rb__l animate hidden')

        for div in input_links:
            links = div.find_all('a')
            for link in links:
                self.output_links.add("https://www.yp.ru" + str(link.get('href')))

    def returnResult(self):
        return self.output_links
