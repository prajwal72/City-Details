import requests
from bs4 import BeautifulSoup
city = "Jamshedpur"  #write the name of city in the string
website_url = requests.get('https://en.wikipedia.org/wiki/'+city).text
soup = BeautifulSoup(website_url,'lxml')
flag = 0
s1 = 'Country'
s2 = 'Nation'
print(city + '\n')
for i in range(0, 35):
    try:
        table = soup.find_all('tr',{'class':['mergedtoprow', 'mergedrow']})[i]
        key = table.find('th').text
        try:
            value = table.find('td').text
        except:
            value = ""
        if flag == 0:
            if s1 in key or s2 in key:
                flag = 1
                continue
        if flag == 0:
            continue        
        loop = 1
        while loop == 1:
            loop = 0
            l = len(key)
            for j in range(0,l):
                if key[j] == '[':
                    k = j
                if key[j] == ']':
                    key = key[:k] + key[j+1:]
                    loop = 1
                    break
        loop = 1
        while loop == 1:
            loop = 0
            l = len(value)
            for j in range(0,l):
                if value[j] == '[':
                    k = j
                if value[j] == ']':
                    value = value[:k] + value[j+1:]
                    loop = 1
                    break
        print(key + ": " + value)
    except:
        continue
