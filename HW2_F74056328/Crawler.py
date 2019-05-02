import urllib.request
import re
import matplotlib.pyplot
import math #for counting page size, need to use ceil()

author = input("Search Author: ")
#author = 'Ian Goodfellow'
author = author.replace(' ', '+') #The request should be [string]+[string] or we will get "bad request"
searchtype = "all"
abstracts = "show"
order = "-announced_date_first"
size = 50
url = "https://arxiv.org/search/?query=" + author + "&searchtype=" + searchtype + "&abstracts=" + abstracts + "&order=" + order + "&size=" + str(size)
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = 'originally announced[\\s\\S]*?</p>' #The announced date is right after this section and end with </p>
pattern_count = 'Showing[\\s\\S]*?results'
pattern_authors = 'Authors:</span>[\\s\\S]*?</p>'

## getting total result number in search result to find out how much pages.
result_count = re.findall(pattern_count, html_str)
result_count = result_count[0].split('of')[1].split(' ')[1].strip()
page_count = math.ceil((int(result_count)) / size)

date = {}
co_authors = {}

years = []
count_in_years = []

print("[ Author: " + author + " ]")

for p in range(0, page_count):
    ## request html for each pages using &start=<number> in url
    url = "https://arxiv.org/search/?query=" + author + "&searchtype=" + searchtype + "&abstracts=" + abstracts + "&order=" + order + "&size=" + str(size) +  "&start=" + str(size * p)
    content = urllib.request.urlopen(url)
    html_str = content.read().decode('utf-8')
    result = re.findall(pattern, html_str)
    result_author = re.findall(pattern_authors, html_str)

    ## finding announced date
    for r in result:
        time_announced = r.split("originally announced</span>")[1].split("</p>")[0].split(" ")[2].split(".")[0].strip()
        #using dictionary in python for counting atricles in each year. format: '<years>' : <count>
        if time_announced not in date:
            date.setdefault(time_announced, 1)
        else:
            date[time_announced] += 1

    ## finding authors for each article
    for rr in result_author:
        author_temp = re.findall("<a[\\s\\S]*?</a>", rr)
        #print(author_temp)
        for tmp in author_temp:
            splitted_author = tmp.split("</a>")[0].split(">")[1].strip()
            #print(splitted_author)
            if splitted_author not in co_authors:
                co_authors.setdefault(splitted_author, 1) # '<author>' : <count>
            else:
                co_authors[splitted_author] += 1


for i in date.keys():
    #print(i + ": ")
    #print(date.get(i))
    years.append(i)
    count_in_years.append(date.get(i))

#sort_author = [(k, co_authors[k]) for k in sorted(co_authors, key = co_authors.get, reverse = True)] #sort the result by it's key
sorted_author = [(k, co_authors[k]) for k in sorted(co_authors.keys())]

for j, k in sorted_author:
    print("[" + j + "]: " + str(k) + " Times")

matplotlib.pyplot.bar(years, count_in_years)
matplotlib.pyplot.show()