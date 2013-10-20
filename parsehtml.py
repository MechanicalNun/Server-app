#! /usr/bin/python

from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import nltk

BASE_URL = "http://www.chicagoreader.com"

def get_category_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html,'lxml')
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
    return category_links

def get_sins(section_url):
    sinhtml = urlopen(section_url).read()
    sinsoup = BeautifulSoup(sinhtml,'lxml')
    sincat = sinsoup.findAll('font')
    sins = [re.findall(r'[A-Z]+', str(sincat[l])) for l in range(0, len(sincat))]
    
    # clean up sins:
    # Remove single letters:
    for linecnt, line in enumerate(sins):
        while False in [bool(len(l) > 1) for l in line]:
            [line.pop(cnt) for cnt, item in enumerate(line) if len(item) == 1]

    [line.pop(cnt) for cnt, item in enumerate(line) if len(item) == 1]
    [line.pop(cnt) for cnt, item in enumerate(line) if len(item) == 1]
    [line.pop(cnt) for cnt, item in enumerate(line) if len(item) == 1]
    [line.pop(cnt) for cnt, item in enumerate(line) if len(item) == 1]        


    # zerocnt = 0

    # for line in sins:
    #     if len(line) == 0:
    #         zerocnt+=1    
    # print "zerocount is:%s"%zerocnt        


    # while zerocnt != 0:
    #     print "zerocount is:%s"%zerocnt
    #     [sins.pop(cnt) for cnt, line in enumerate(sins) if len(line) == 0]
    #     for line in sins:
    #         if len(line) == 0:
    #             zerocnt+=1   
    #         else:
    #             break

    # turn caps letters into sentences:
    for line in sins:
        ' '.join([a.lower() for a in line]) 

    return sins

def all_word_distribution(sins):
    # join all words into one text
    out = []
    [out.extend(line) for line in sins]
    stop_words = ['not', 'to', 'the', 'of', 'in', 'is', 'niv', 'that', 'for', 'and', 
                  'but', 'with', 'with', 'you', 'be', 'by', 'on', 'an', 'his', 'has', 
                  'are', 'will', 'being', 'which', 'man', 'all', 'or', 'as'] 
    out = [a.lower() for a in out if a not in stop_words]

    [line.pop(cnt) for cnt, item in enumerate(line) if len(item) == 1]



    
    return out

def main():
    sins = get_sins("http://www.wogim.org/sinlist.htm")
    return sins


if __name__ == '__main__': main()


# TF-IDF

# word in a single document over the same word in all documents: 
# [w for w in words]
# [d for d in documents]
# (number of words/ all words in doc) / num of docs that the word appears in)





