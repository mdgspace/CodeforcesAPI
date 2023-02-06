from bs4 import BeautifulSoup
import requests

print("Type the code forces question number (format: 1729A should be given as 1729-A) :")
q = input()

web_page = requests.get('https://codeforces.com/problemset/problem/'+q.split('-')[0]+'/'+q.split('-')[1]).text.encode("utf-8")

soup = BeautifulSoup(web_page, 'lxml')

head = soup.find('div', class_ ="header").text
tail = soup.find('div', class_ = "input-specification").text + soup.find('div', class_ = "output-specification").text + soup.find('div', class_ = "sample-tests").text

content = soup.find('div', class_ = "problem-statement").text.replace(head,'')
content = content.replace(tail,'')


title = soup.find('div',class_ = "title").text
time_limit = soup.find('div', class_ = "time-limit").text.replace('time limit per test','')
memory_limit = soup.find('div',class_ = "memory-limit").text.replace('memory limit per test','')
input_file = soup.find('div', class_ = "input-file").text.replace('input','')
output_file = soup.find('div', class_ = "output-file").text.replace('output','')
input_specs = soup.find('div', class_ = "input-specification").text.replace('Input','')
output_specs = soup.find('div', class_ = "output-specification").text.replace('Output','')
sample_tests = soup.find('div', class_ = "sample-tests").text.replace('Examples', '').replace('Example','')

print("\n\nTITLE: "+title)
print("TIME LIMIT: "+ time_limit)
print("MEMORY LIMIT: "+ memory_limit)
print("INPUT: "+input_file+" input")
print("OUPUT: "+output_file+" output")
print("\nCONTENT:\n"+content+"\n")
print("INPUT SPECIFICATIONS:\n"+input_specs)
print("OUTPUT SPECIFICATIONS:\n"+output_specs+"\n")
print("SAMPLE TESTS: \n"+ sample_tests)