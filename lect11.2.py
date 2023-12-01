#변환
"""
import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/apt.csv", encoding="utf8")

print(df.head())
"""
import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col=0)
print(df.head())
print("\n-----------------------------------------------------\n")

#컬럼명 바꾸기
df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)
#print(df.dtypes)
#print("\n-----------------------------------------------------\n")

df = df["분양가"] = df["분양가"].convert_dtypes()
#print(df.dtypes)

arr = df.to_numpy()
# print(arr)
# print(len(arr))

# print(df.describe())

print(df.transpose())
print(df.T.head())


#정컬


res = df.sort_values(by="지역영")[:5]
print(res)

#res = df.sort_values(by="지역영")
#res = df.sort_values("지역영")
#res = df.sort_values(by="지역영", ascending=True)
res = df.sort_values(by="지역영", ascending=False)
#print(res.head(10))
#print(res.head())

#res = df.sort_values(by="연도")
#res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[10:20]
#print(res)
print(res.head())

#컵컬이름 출력
#res = df["지역명"][:5]
#res = df[["지역명", "연도"]]
#res = df[["지역명", "연도", "분양가"]]
res = df[["지역명", "연도", "분양가"]][:7]
#res = df[["지역명", "연도"]][:5]
print(res)

#print("\n-----------------------------------------------------\n")
#res = df.loc[:, ["지역명", "연도", "분양가"]][:5]
#res =df.loc[:][:5]
#res =df.loc[:][:]
#res =df.iloc[1]
#print(res)


#res = df.loc[:6,["지역명", "연도"]]
#res = df.loc[:6,["지역명", "연도"]][3:]
##res = df.loc[:6,["지역명", "연도"]][:3]
#res = df.loc[6:,["지역명", "연도"]][:7]
##print(res)


#res = df.loc[df["지역명"]=="강원"]
#res = df.loc[df["연도"] > 2020]
#res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
#res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
##res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:]
##print(res)


##df0 = df.copy()
##print(df0)
#print("\n-----------------------------------------------------\n")
#res = df.iloc[2]
##res = df.iloc[2][2]
#print(res)

##res = df[df.index > 3500]
##print(res)

#res = df[df.연도 == 2023]
res = df[df.월 == 3]
print(res)

res = df[(df.연도 == 2023 & df.지역명 =="서울")]
res = df[(df.연도 == 2023 & df.지역명 =="서울")]
res = df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
print(res)

columns = list(df.columns)
print(columns + "컬렁")

df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
print(df)
print("\n-----------------------------------------------------\n")
print(res)


df1.loc[:4, "extra"] = False
print(df1)
df1.loc[:4, "extra"] = "0"
print("\n-----------------------------------------------------\n")
df2 = df1.copy()

res = df2.dropna(how="any")
res = df2.dropna(how="any", inplace=True)
print(df2)
print("\n-----------------------------------------------------\n")

res = df1.fillna(value="1234")
print(res)
print("\n-----------------------------------------------------\n")

res = df.dropna(how="any", inplace=True)
print(res)
print(df2)

res = pd.isna(df1)
print(res)

res = df["연도"].value_counts()
print(res)
print("\n-----------------------------------------------------\n")

res = df.groupby(["지역명", "연도", "월"]).sum()
print(res)
print("\n----------------------\n")
res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)
print("\n-----------------------------------------------------\n")

#

tr = pd.read_csv("C:\\Users\\Catholic\\python\\happy\\data\\train.csv", index_col=0, encoding='cp949')
res = tr.isnull().sum()
print(res)
print("\n-----------------------------------------------------\n")
print("\n----------------------\n")
res = pd.crosstab(tr["Embarked"], tr["Survived"])
print(res)
print("\n-----------------------------------------------------\n")
# 
res = res.columns.map({0:"Dead", 1:"Alive"})
print(res)
print("\n-----------------------------------------------------\n")

