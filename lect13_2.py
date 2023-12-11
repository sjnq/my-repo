import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
"""
#다중 그래프 출력

# 사용데이터
x1 = [2,3,6,7,10]
x2 = [1,4,5,8,9]

y1 = [1,4,5,8,9]
y2 = [2,4,6,8,10]


#pip.style.use("bmh")
plt.subplot(2, 1, 1)    # 1set
#plt.subplot(1, 2, 1)    # 2set
#plt.subplot(3, 1, 1)    # 3set
#plt.subplot(2, 2, 1)    # 4set
plt.plot(x1, y1, "o-")

plt.title("x2 Graph")
plt.xlabel("x2 data")
plt.ylabel("y2 data")

plt.style.use("bmh")
################################
plt.subplot(2, 2, 2)
plt.plot(x2,y2,".-")

plt.title("X2 Graph")
plt.xlabel("x2-data")
plt.ylabel("y2-data")

plt.style.use("ggplot")



plt.subplot(2, 2, 3)
plt.plot(x1,y1,".-")
plt.plot(x2,y2,".-")

plt.title("X3 Graph")
plt.xlabel("x3-data")
plt.ylabel("y3-data")

plt.style.use("classic")



plt.subplot(2, 2, 4)
plt.plot(x1,y2,".-")
plt.plot(x2,y1,".-")

plt.title("X4 Graph")
plt.xlabel("x4-data")
plt.ylabel("y4-data")

plt.style.use("Solarize_Light2")

plt.tight_layout()

plt.savefig("data/imggg.jpg")
plt.savefig("data/imggg.png")

plt.show() """

################################################
#다중 객체를 이용한 막대 그래프 출력
"""
x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.bar(x_years, y_data)
ax2.bar(x_years, y_data)
ax3.bar(x_years, y_data)
ax4.bar(x_years, y_data)

ax1.bar(x_years, y_data, color = "aquamarine", edgecolor = "black", hatch="/")
ax2.bar(x_years, y_data, color = "salmon", edgecolor = "black", hatch="\\")
ax3.bar(x_years, y_data, color = "navajowhite", edgecolor = "black", hatch="+")
ax4.bar(x_years, y_data, color = "lightskybule", edgecolor = "black", hatch="*")

plt.tight_layout()

plt.show()
"""
################################
"""
#Seaborn 사용
#pip install seaborn
tips = sns.load_dataset("tips")
print(tips)
#상관관계 출력
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()
"""
#### 타이타닉 데이터
"""
tips = sns.load_dataset("tips")
print(tips)

#plt.figimage(figsize = (10, 6))


sns.regplot(x="day", y="tip", data=tips)
sns.regplot(x="day", y="total_bill", data=tips, palette = "")
sns.regplot(x="tip", y="total_bill", data=tips)
sns.regplot(x="sex", y="total_bill", data=tips)
sns.regplot(x="sex", y="tip", data=tips)
sns.regplot(x="smoker", y="total_bill", data=tips)
sns.regplot(x="smoker", y="tip", data=tips)
sns.regplot(x="time", y="total_bill", data=tips)

plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("Average")

plt.show()

"""
#타이타닉 데이터

"""
titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show()


#각 지표별 출력
sns.countplot(x="class", hue="who", data=titanic)
sns.countplot(x="class", hue="alive", data=titanic)
sns.countplot(x="sex", hue="alive", data=titanic)
sns.countplot(x="alone", hue="who", data=titanic)

#sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)
#sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show()

"""
#주식

df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

#df0["Open "].plot()
#df0["High"].plot()
#df0["Low"].plot()
df0["Close"].plot()

plt.grid(True)
plt.show()


#다우지수와 코스피 비교
dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

plt.figure(figsize=(7,7))

# 종가 기준
plt.plot(dow.index, dow.Close, "r--", label="Dow")
plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

#최고
plt.plot(dow.index, dow.High, "r--", label="Dow")
plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

#해당 site 1~ 100 페이지 파싱 ########################################
d = (dow.Close / dow.Closr.loc["2012-06-01"]) * 100
k = (kospi.Close / kospi.Closr.loc["2012-06-01"]) * 100
plt.plot(d.index, d, "r--", label="Dow")
plt.plot(k.index, k, "b", label="KOSPI")

plt.grid(True)

plt.legend()
plt.show() 




#국내 개별 종목 분석
# 해당 데이터를 가져오는 URL
# code 는 종목명
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs


headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
url = "https://finance.naver.com/item/sise_day.nhn?code={}"
#url = "https://finance.naver.com/item/sise_day.nhn?code={}"

res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))
print(table)

df_list = []
#페이지 파싱
page = 1
for page in range(1, 100):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break
print(df_list)

#데이터 처리
df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.figure(digsize = (15, 5))
plt.title("Target (close)")

plt.xticks(rotation = 45)
plt.plot(df["날짜"], df["종가"], "co-")
plt.grid(color = "gray", linestyle ="--")
plt.show()

#nasea
import yfinance as yf

ticker = "AAPL"  #예시
ticker = "MSFT"  #MS
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)


#시각
plt.figure(figsize = (12, 6))
plt.plot(data["Close"], label="Close Price")


data["MA_50"] = data["Close"].rolling(window=50).mean()
data["MA_200"] = data["Close"].rolling(window=200).mean()

plt.plot(data["MA_50"], label="50-day Mean Average")
plt.plot(data["MA_200"], label="200-day Mean Average")

plt.title("Stock Price")
plt.xlabel("Date")
plt.ylabel("Price($)")
plt.legend()

plt.show()

######################################
#국가별 인구 데이터 분석
import requests
from datetime import datetime
from matplotlib import dates as mdates
from bs4 import BeautifulSoup as bs

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = bs(response.text, "html.parser")

#국가 
countries=[]
populations=[]

rows=soup.select("#example2 tbody tr")
for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))
    
    countries.append(country)
    populations.append(population)
    
top_countries = countries[:10]
top_populations = populations[:10]

plt.figure(figsize=(12, 6))
# plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.bar(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show()