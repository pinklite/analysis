from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv
import json
from pprint import pprint

print('Hello World')
my_list = []
text = " "

data = json.load(open('batch_four.json'))
pprint(data)
for values in data.values():
    print(values)
    my_url_info = 'https://www.imdb.com/name/' + values + '/bio?ref_=nm_ov_bio_sm'
    print(my_url_info)
    my_list.append(my_url_info)

''' old code 

filename = "links.csv"
f = open(filename, "w", newline='')

print("\n Extract list from CSV: \n")

for x in my_list:
    print(x)
    uClient = uReq(x)
    html_page2 = uClient.read()
    uClient.close()
    page_soup_new = soup(html_page2, "html.parser")
    direct_links2 = page_soup_new.find_all('table')
    # print(page_soup_new)
    name_links = page_soup_new.find_all('h3')
    for links in name_links:
        if links.a != None:
            result = links.a.text;
            f.write(result + ",")
    table_info = page_soup_new.find('table', attrs={"class": "dataTable labelValueTable"})
    if table_info != None:
        rows = table_info.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            give_text = cols[0].text
            # print(give_text)
            if give_text == "Birth Name":
                text = cols[1].text
                print("Birth Name: " + text)
                f.write("," + text + "\n")

f.close()

old code finish '''

filename = "links.csv"
f = open(filename, "w", newline='')

for x in my_list:

    print(x)
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

    f.write(text + "\n")


f.close()
