# 입력암호화
"""
import getpass

pw = input("Pass :")
pw = getpass.getpass("Pass : ")
print(pw)
"""

# 해시함수(sha256)
"""
import hashlib

hl = hashlib.sha256()
#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "1234567890"
target = "to be or not to be, That is aa question"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
"""

# keccak256
"""
import Crypto.Hash.keccak as kek
#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "1234567890"
target = "to be or not to be, That is aa question"

kksh = kek.new(digest_bits = 256)
kksh.update(target.encode("utf-8"))


print(kksh.digset())
print(kksh.hexdigest())
"""

#입력기 
"""
import getpass
import hashlib

pw = getpass.getpass("Pass : ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())

"""
#암호화 파일 저장
"""
import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
    else:
        return True
    
if pwInsert():
    pw = input('new pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
else:
    print("not allow password")
"""


#시스템정보 확인
"""
import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)

print(pf)
"""

#웹페이지 읽기
"""
import urllib.request as ur

url = 'https://www.google.com'
#url = 'https://daum.net'
#url = 'https://xkcd.com/'

#res = urllib.request.urlopen(url)
res = ur.urlopen(url)

web = res.read()

with open("ul.htal", "wb") as fp:
    fp.write(web)
    
#print(web.decode("utf-8"))
print(web)
"""

#웹페이지 읽기2
"""
import http.client as hc

url = "www.daum.net"
#url = "www.google.com"
#url = "www.v.daum.net"

#conn = http.client.HTTPSConnection(url)
corn = hc.HTTPSConnection(url)
#corn.request("GET", "/")
corn.request("GET", "/v/20231103063908539")

r = corn.getresponse()

with open("ulcl.html", 'wb') as fp:
    fp.write(r.read())
    
corn.close()

print(r)
"""
#멀티스레드
"""
import time 

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

start = time.time()
for i in range(3):
    counter(f"num{i}")
    print(i)
end = time.time()

#print("single end")
print("sinle end", end - start)

"""
###

"""import threading as td
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")

thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

start = time.time()
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
end = time.time

print("multi end", end - start)
"""

#(다음 수업)
"""
import multiprocessing 
import time
def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
process1 = mp.Process(target=counter, args=("1num",))
#process2 = mp.Process(target=counter, args=("2num",))
#process3 = mp.Process(target=counter, args=("3num",))

start = time.time()

process1.start()
#process2.start()
#process3.start()

process1.join()
#process2.join()
#process3.join()
end = time.time

process3("proc-end", end-start)"""
"""
#main 실행
def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    main()
    #main()
    

import asyncio
import random as rd
import time
async def tester(name):
    snum = rd.randint(10, 20)
    print(f"{name} - {snum}")
    for i in range(snum):
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
    
    print(f"end of {name}")
    
async def main():
    task1 = asyncio.create_task(tester("1test"))
    
    task2 = asyncio.create_task(tester("2test"))
    
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end", end-start)
    
if __name__ == '__main__':
    asyncio.run(main())
    


import asyncio
import time

async def worker1():
    for i in range(1, 6):
        print(f"Task 1: Step {i}")
        await asyncio.sleep(1)
async def worker2():
    for i in range(1, 4):
        print(f"Task 2: Step {i}")
        await asyncio.sleep(2)
        
async def main():
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())
    
    print("start task")
    start = time.time()
    await task_1
    await task_2
    end = time.time()
    print("end-", end-start)
    print("end task")
    
if __name__ == 'main__':
    asyncio.run(main())  
    
    
    
#스케출 처리
import time
import sched

start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
    
    print(f"end of {name}")

def run():
    s = sched.scheduler()
    s.enter(5, 1, tester, ('1num',))
    s.enter(5, 1, tester, ('4num',))
    s.enter(3, 1, tester, ('2num',))
    s.enter(7, 1, tester, ('3num',))
    s.run()


if __name__ == "__main__":
    run()
    main()
    print("end")"""
    
# 문자열 비교
"""
import diff_match_patch.diff_match_patch as dm

origin = "To be or not to be, That is a question!"
copyed = "To be and not to be, That is a question!"


dmp = dm()
diff = dmp.diff_main(origin, copyed)
print(diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d)"""
# 테스트용 데이터 생성
"""
from faker import Faker as fk

#temp = fk()
temp = fk("ko-KR")
print(temp.name())


#temp = fk("ko-KR")
print(temp.name() + "," + 
	temp.address() + "," + 
	temp.postcode() + "," + 
	temp.company() + "," + 
	temp.job() + "," + 
	temp.phone_number() + "," + 
	temp.email() + "," + 
	temp.user_name() + "," + 
	temp.ipv4_private() + "," + 
	temp.ipv4_public() + "," + 
	temp.catch_phrase() + "," + 
	temp.color_name() + "\n")

# Faker
from faker import Faker as fk

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

#with open("fktemp.csv", "w", newline='') as f:
with open("fktemp.txt", "w", newline='') as f:
    
    for i in range(30):
        f.write(temp.name() + "," + 
	        temp.address() + "," + 
	        temp.postcode() + "," + 
	        temp.company() + "," + 
	        temp.job() + "," + 
	        temp.phone_number() + "," + 
	        temp.email() + "," + 
	        temp.user_name() + "," + 
	        temp.ipv4_private() + "," + 
	        temp.ipv4_public() + "," + 
	        temp.catch_phrase() + "," + 
	        temp.color_name() + "\n")
        
        """
#시스템명령어 사용
"""
import subprocess as sp
import pprint

# res = sp.run(["cmd", "/c", "dir"], capture_output=True)
# res = sp.run(["cmd", "/c", "dir"], capture_output=False)
res = sp.run(["cmd", "/c", "ipconfig", "all"], capture_output=False)
#res = sp.run(["cmd", "/c", "ipconfig", "all"], capture_output=True)
print(res)
#pprint.pprint(res)

try :
	"구현 코드"
except :
	"구현 코드중 에러 발생시 실행할 코드"
"""
#에러처리
"""
import traceback as tb

def tester():
    #return 1/0
    return 1

def caller():
    tester()
    
def main():
    try :
        caller()
            
    #except ZeroDivisionError:
       # print("zde error")
    	# 0을 나누어 에러 발생시 처리
     
     
    except ValueError :
        print("ve error")
	    # 유효하지 않는 정수를 입력했을시 처리
 
 
    except Exception as ex :
        print("ex error", ex)
        # 모든 예외를 처리할때 처리
        
    else :
        print("ok")
	    # 에러가 없으면

    finally :
        print("end")
	    # 해당 함수가 에러가 있든 없든, 완료될때 처리



"""

#9.1

#import bs4.BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests as rq


url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

#pres = res_html.find("h1")
pres = res_html.find("h2")
print(pres)
print("\n1---------------------------------------\n")
print(pres.get_text().strip())
print("\n2---------------------------------------\n")
print(pres.next_element.get_text().strip())
print("\n6---------------------------------------\n")
print(pres.get_text())

tres = res_html.find("title")
print(tres)
print("\n3---------------------------------------\n")
print(tres.next_element)
print(tres.get_text().strip())
print("\n4---------------------------------------\n")



fares = res_html.findAll("a")
for i in fares:
    print(i,get_text())

#print(fares)
print("\n5---------------------------------------\n")

clres = res_html.findAll(class_ = "doc-title")
print(clres)
print("\n6---------------------------------------\n")
clrs = res_html.find(class_ = "head_top")
pres(clrs)
print(cllrs.get_text())


item = res_html.select_one()


############


from bs4 import BeautifulSoup as bs
import requests as rq
url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.coutainer-do")
print(item)
print(item.get_text())
print("\n6---------------------------------------\n")
