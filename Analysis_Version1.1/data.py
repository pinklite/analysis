from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import json
from pprint import pprint

print('Hello World')
my_list = []
text = " "

filename = "links.csv"
f = open(filename, "w", newline='')

data = json.load(open('batch_one.json'))
pprint(data)
for key, value in data.items():
    print(value)
    x = 'https://www.imdb.com/name/' + value + '/bio?ref_=nm_ov_bio_sm'
    f.write(key + "," + value + ",")
    uClient = uReq(x)
    html_page2 = uClient.read()
    uClient.close()
    page_soup_new = soup(html_page2, "html.parser")
    name_links = page_soup_new.find('h3')
    if name_links.a is not None:
        result = name_links.a.text;
        print(result)
        f.write(result + ",")
    direct_links2 = page_soup_new.find_all('table')
    table_info = page_soup_new.find('table', attrs={"class": "dataTable labelValueTable"})
    flag = 1
    text = " "
    if table_info is not None:
        rows = table_info.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            give_text = cols[0].text
            #print(give_text)
            if give_text == "Birth Name":
                    flag = 0
                    text = cols[1].text
                    print("Birth Name: " + text)

    if flag:
        text = " Not Found "
        print("Birth Name: " + text)

    f.write(text + ",")

    table_info_two = page_soup_new.find('table', attrs={"id": "tableSpouses"})

    flag1 = 1
    text1 = " "
    if table_info_two is not None:
        rows = table_info_two.find_all('tr')
        for row in rows:
            cols = row.find('td')
            find_a = cols.find('a')
            #print(find_a)
            #col_a = cols.find_all('a')
            #give_text = cols[0].text
            #print(cols.text)
            if cols is not None:
                if find_a is not None:
                    flag = 0
                    result = find_a.text.strip()
                    find_href = find_a.get('href')
                    print("Spouse Name : " + result)
                    print("Link: " + find_href)
                    break
                else:
                    result = cols.text.strip()
                    find_href = "Not Found"
                    print("Spouse Name : " + result)
                    print("Link: " + find_href)
                    flag = 0
                    break
            else:
                    flag = 1

    if flag:
        result = " Not Found "
        find_href = "Not Found"
        print("Spouse Name : " + result)
        print("Link: " + find_href)

    f.write(result + ",")
    f.write(find_href + "\n")


f.close()

