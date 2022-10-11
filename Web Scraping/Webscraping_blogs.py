from turtle import title
from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://webscraper.io/blog"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='blogno')

with open('Blogs.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Name', 'Date', 'Category']
    thewriter.writerow(header)

    for list in lists:
        name = list.find('a', class_="titleblog").text
        date = list.find('p', class_="date").text
        category = list.find('p', class_="category").text

        info = [name,date,category]
        print(info)
        thewriter.writerow(info)