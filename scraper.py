from bs4 import BeautifulSoup
import requests
import json

def scrape(q):
    web_page = requests.get('https://codeforces.com/problemset/problem/'+q.split('-')[0]+'/'+q.split('-')[1]).text.encode("utf-8")
    soup = BeautifulSoup(web_page, 'lxml')
    head = soup.find('div', class_ ="header").text  
    tail = soup.find('div', class_ = "input-specification").text + soup.find('div', class_ = "output-specification").text + soup.find('div', class_ = "sample-tests").text
    content = soup.find('div', class_ = "problem-statement").text.replace(head,'')
    content = content.replace(tail,'').replace("$$$","$$")

    data = {
        "title": soup.find('div',class_ = "title").text,
        "time_limit": soup.find('div', class_ = "time-limit").text.replace('time limit per test',''),
        "memory_limit": soup.find('div',class_ = "memory-limit").text.replace('memory limit per test',''),
        "input_file": soup.find('div', class_ = "input-file").text.replace('input',''),
        "output_file": soup.find('div', class_ = "output-file").text.replace('output',''),
        "content": content,
        "input_specs": soup.find('div', class_ = "input-specification").text.replace('Input','').replace("$$$","$$"),
        "output_specs": soup.find('div', class_ = "output-specification").text.replace('Output','').replace("$$$","$$"),
        "sample_tests": soup.find('div', class_ = "sample-tests").text.replace('Examples', '').replace('Example',''),
    }
    return data