"""import calc as cm
#print(cm.Calc.add(1, 2))
cl = cm.Calc()

print(cl.add(1, 2))
"""

#줄임말 처리
"""
import textwrap as tw
targeText = "To be or not to be, That is a question"
#target = "동해물과 백부산이 마르고"
res = tw.shorten(targeText, width=10)

print(res)
"""

#줄 바꿈 처리
"""
import textwrap as tw

target = "To be or not to be, That is a question"
longTarget = target * 10000


print(longTarget)
print("\n=======================\n")

res = tw.wrap(longTarget, width= 50)
print(res)

#join() 함수 추가, 출력
print("\n=======================\n")

print('\n'.join(res))

#fill() 함수로 처리
print("\n=======================\n")
rs = tw.fill(longTarget, width=50)
print(rs)
"""

#문자열 치환
"""
line = "홍길동의 주민번호는 012345-1234567 입니다"
word_result = []
for word in line.split(" "):
    if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
        word = word[:6] + "-" + "*******"
    word_result.append(word)
print(" ".join(word_result))

#정규표현식
import re

line = "홍길동의 주민번호는 012345-1234567 입니다"
res = re.compile("()d{6})[-]\d{7}")
print(res.sub("\g<1>-*******", line))
"""

#날짜 출력
"""
import datetime as dt

day1 = dt.date(2023, 10, 23)
print(day1)

day2 = dt.date(2023, 7, 8)
print(day2)

#날짜 계산
diff = day1 - day2
print(diff)

#날짜 객체1
import datetime as dt

res = dt.datetime(2023, 11, 1, 12, 35, 40)
tHour = res.hour
tMin = res.minute
tSec = res.second

print(res, tHour, "  ", tMin, "  ", tSec)

#날짜 객체2
import datetime as dt


day = dt.date(2023, 11, 1)
time = dt.time(12, 30, 40)

res = dt.datetime.combine(day, time)
print(res, tHour, tMin)
"""

#요일 판별
"""
import datetime as dt

day = dt.date(2023, 11, 1)
print(day.weekday())

yesterday = dt.date(2023, 10, 31)
print(yesterday.weekday())
"""
#날짜 세기
"""
import datetime as dt

today = dt.date.today()
print(today)

#difday = dt.timedelta(day = 20)
#difday = dt.timedelta(hours = 200)
difday = dt.timedelta(minutes = 2000)


print(difday)
print(today + difday)
"""

#단어 세기
"""
import collections as cl
import re
"""
poem = """
내가 그의 이름을 불러 주기 전에는
그는 다만
하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러 주었을 때
그는 나에게로 와서
꽃이 되었다.
내가 그의 이름을 불러 준 것처럼
나의 이 빛깔과 향기에 알맞은
누가 나의 이름을 불러 다오.
그에게로 가서 나도
그의 꽃이 되고 싶다.
우리들은 모두
무엇이 되고 싶다.
너는 나에게 나는 너에게
잊혀지지 않는 하나의 눈짓이 되고 싶다."""
"""
wd = re.findall(r"\w+", poem)
#print(wd)
print(len(wd))


cnt = cl.Counter(wd)
print(cnt.most_common(1))
"""
# 정렬 출력
"""
import pprint 
data = {"month": "9", "num": 642, "link": "", "year": "2009", "news": "", "safe_title": "Creepy", "transcript": "[[Two people are sitting on chairs.]]\nMan: Hey, cute netbook.\nWoman: \nWhat.\n\n\nMan: Your laptop. I just --\nWoman: No, why are you talking to me.\n\nWoman: Who do you think you are? If I were even slightly interested, I'd have shown it.\n\nWoman: Hey everyone, this dude's hitting on me.\nVoice #1: Haha\nVoice #2: Creepy\nVoice #3: Let's get his picture for Facebook to warn others.\n\n((This panel fades into a thought bubble of the actual man.))\n[[The girl is typing on her laptop.]]\nDear blog,\nCute boy on train still ignoring me.\n\n{{Title text: And I even got out my adorable new netbook!}}", "alt": "And I even got out my adorable new netbook!", "img": "https://imgs.xkcd.com/comics/creepy.png", "title": "Creepy", "day": "28"}
print(data)
pprint.pprint(data)

"""

# 최대공약수
"""
import math
res =  math.gcd(60, 100, 80)
print(res)
"""
# 최소공배수
"""
res = math.lcm(15, 25)
print(res)
"""

# 로또 번호 생성
"""import random

res = []
while len(res) < 6:
    num = random.randint(1, 45)
    if num not in res:
        res.append(num)
print(res)
"""
# 평균값 구하기

"""import statistics as st

data = [48,92, 57, 59, 63, 74, 36, 91]
res = st.mean(data)

print(res)

re =st.median(data)
print(re)"""

# 압축하기
"""
import zlib

data = "To be or not to be, That is a question!"
longData = data * 1000

print(len(longData))
print("\n ==================== \n")


cmp = zlib.compress(longData.encode(encoding="utf-8"))
print(cmp)
print("\n ==================== \n")
print(len(cmp))


decmp = zlib.decompress(cmp).decode("utf-8")
print(decmp)

print("\n ==================== \n")
print(len(decmp))
"""

# 파일 압축 저장
"""
import gzip

data = "To be or not to be, That is a question!" * 10000
print(len(data))

with gzip.open('data.txt.gz', 'wb') as fp:
    fp.write(data.encode('utf-8'))
    
with gzip.open('data.txt.gz', 'rd') as fp:
    read_data = fp.read().decode('utf-8')
    print(read_data)
"""
# 압축 2
"""
import bz2
data = "To be or not to be, That is a question!" * 10000

cmp = bz2.compress(data.encode(encoding="utf-8"))
print(cmp)
print("\n ==================== \n")
print(len(cmp))

decmp = bz2.decompress(cmp).decode("utf-8")
print(decmp)
print("\n ==================== \n")
print(len(decmp))
"""

# 파일 압축
"""

import zipfile as zf

data = "To be or not to be, That is a question!" * 10000
fp1 = open("atar.txt", "w")
fp1.write(data)
fp1.close()

fp2 = open("btar.txt", "w")
fp2.write(data)
fp2.close()

fp3 = open("ctar.txt", "w")
fp3.write(data)
fp3.close()


with zf.ZipFile('txt.tar', 'w') as myzip:
    myzip.write('atar.txt')
    myzip.write('btar.txt')
    myzip.write('ctar.txt')


with zf.ZipFile('txt.tar') as myzip:
    myzip.extractall()
"""


import argparse
import functools

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add', type=int, nargs='+', metavar='N', help='더할 숫자')
parser.add_argument('-m', '--mul', type=int, nargs='+', metavar='N', help='곱할 숫자')
parser.add_argument('-m', '--sub', type=int, nargs='+', metavar='N', help='할 숫자')

args = parser.parse_args()

if args.add:
    print("총합 %d입니다." % functools.reduce(lambda x, y: x + y, args.add))
if args.mul:
    print("총곱 %d입니다." % functools.reduce(lambda x, y: x * y, args.mul))