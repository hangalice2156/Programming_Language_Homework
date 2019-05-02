# HW2 - Regular Expression with Python

## Environment

- Operation System: Windows 10 1803

- Develop and execute with python 3.7.2-rc1

----

## Homework reports

- For this homework, please execute `Crawler.py` with `Python .\Crawler.py` or `Python3 ./Crawler.py` if you are using Linux.

- In runtime, type author name in command line, for example: Ian Goodfellow (seperate with spacebar)

### Getting url and request

First of all, I tried to figure out rule for the url

Query the example given by TAs, the url is 

https://arxiv.org/search/?query=Ian+Goodfellow&searchtype=all&abstracts=show&order=-announced_date_first&size=50

and then click on to the 2nd page, also changed some query settings, get url like this

https://arxiv.org/search/?query=Ian+Goodfellow&searchtype=all&abstracts=show&order=-submitted_date&size=25&start=50

We can analysis the url and split them into these parts(orders may change while quarying, but it doesn't matter)

- query=[the person we want to find]

- searchtype=[what field we want to search]

- abstracts=[if shows the abstracts of the article]

- order=[the query order of the articles]

- size=[the articles shows per page]

- start=[show the result from which article] (we may use this to flip through the pages)

setting up all of these, we can start sending request to the site and parse the result we want.

### Parsing the html result

- use `content.read()` to turn the response into string, then use `re.findall()` to get what we want.

- we should use RegEx in this assignment, but... it seems that `[\s\S]*?` is needed.

- The regex `[\s\S]*?` means accept all characters unlimited times, but as few as possible. 

Note that in python code, it should be `[\\s\\S]*?` or the pylint will regard it as `Anomalous backslash in string python`

[explanation here](https://stackoverflow.com/questions/19030952/pep8-warning-on-regex-string-in-python-eclipse)

- Then split the result until only the announced year is reserved, then use dictionary to store the result.

- finally, use matplotlib to show the result.

### As for going thorugh pages

While searching, we can find `Showing 51–63 of 63 results for all: Ian Goodfellow` on the page, we can find total results here

Just similar to how we parse the content, using `re.findall(<pattern>)` can do the job

Note that in `Showing 51–63 of`, the `–` is not `-` which is the normal dash we think.

And also, in my system, `–` is regarded as `&ndash;`. So I just use `[\\s\\S]*?` instead of `[0-9|–|,]`

### Getting author for each article

- Just the same as above, parseing the author and split them from html.

In this program, 
I just show the result because there might be another person 
that sign different name in article but the same person.

- For another example: "Stephen Hawking" and "Stephen W. Hawking" and "Stephen William Hawking" 
is the same but my program shows every of them separately