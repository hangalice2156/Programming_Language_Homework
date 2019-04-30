import urllib.request
import re
import matplotlib.pyplot

#author = input("Search Author: ")
author = 'Ian Goodfellow'
author = author.replace(' ', '+') #The request should be [string]+[string] or we will get "bad request"
searchtype = "all"
abstracts = "show"
order = "-announced_date_first"
size = "50"
start = "0"
url = "https://arxiv.org/search/?query=" + author + "&searchtype=" + searchtype + "&abstracts=" + abstracts + "&order=" + order + "&size=" + size +  "&start=" + start
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = 'originally announced[\\s\\S]*?</p>' #The announced date is right after this section and end with </p>
result = re.findall(pattern, html_str)

date = {}

years = []
count_in_years = []

print("[ Author: " + author + " ]")

for r in result:
    time_announced = r.split("originally announced</span>")[1].split("</p>")[0].split(" ")[2].split(".")[0].strip()
    #using dictionary in python for counting atricles in each year. format: '<years>' : <count>
    if time_announced not in date:
        date.setdefault(time_announced, 1)
    else:
        date[time_announced] += 1

for i in date.keys():
    #print(i + ": ")
    #print(date.get(i))
    years.append(i)
    count_in_years.append(date.get(i))

matplotlib.pyplot.bar(years, count_in_years)
matplotlib.pyplot.show()