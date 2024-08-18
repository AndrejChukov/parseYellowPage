import ssl
import requests
from bs4 import BeautifulSoup
import certifi
from openpyxl import Workbook


from parse_categories import *


data = []

workbook = Workbook()
sheet = workbook.active
sheet.title = "Data"


parseCategories = parseCategories()

parseCategories.startParsing()

# for url in parseCategories.returnResult():

#     session = requests.Session()
#     session.mount('https://', requests.adapters.HTTPAdapter(max_retries=5))
#     response = session.get(url, timeout=10)
    
#     soup = BeautifulSoup(response.text, 'html.parser')

#     names = soup.find_all("a", class_="testtjlw")
#     sites = soup.find_all("div", class_="mdl-grid company__info detail__address")

#     for site in sites:

#         for name in names: 
#             for item in site.find_all("a"):

#                 if "https://" in item.get("href") or "http://" in item.get("href"):
#                     data[name.get("href")] = item.get("href")

#                 else:
#                     data[name.get("href")] = ''
    
#     print(url + " -- Успешно скопирован")
    

# print("Программа выполнена успешно!")

# sheet.append(['Ссылка на компанию', 'Есть(нет) сайта'])

# for key, value in data.items():
#     sheet.append([key, value])

# workbook.save('output.xlsx')

# print(soup.find("li", class_="ui_next_page").find("a").get('href')) 


for url in parseCategories.returnResult():
    session = requests.Session()
    session.mount('https://', requests.adapters.HTTPAdapter(max_retries=5))
    response = session.get(url, timeout=10)


    soup = BeautifulSoup(response.text, 'html.parser')



    for item in soup.find_all("div", class_="js-company"):
        try:
            data.append((item.find("a", class_="testtjlw").text, "https://www.yp.ru" + item.find("a", class_="testtjlw").get("href"), item.find("p", class_="company__url").find("a").get("href")))
        except:
            data.append((item.find("a", class_="testtjlw").text, "https://www.yp.ru" + item.find("a", class_="testtjlw").get("href"), ""))
    print(url + "  -- Успешно спаршено")

print("Программа выполнена успешно!")


sheet.append(['Имя компании', 'Ссылка на компанию', 'Есть(нет) сайта'])


for item in data:
    sheet.append([item[0], item[1], item[2]])

workbook.save('output.xlsx')