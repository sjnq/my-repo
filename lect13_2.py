#import FinaceDataReader as fdr
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

##########
plt.style.use("Solarize_Light2")
plt.tight_layout()

####이미지
plt.savefig("data/img.jpg")
#plt.savefig("data/img.png")

plt.subplot(2, 3, 4)

plt.plot(x2, y2, ".-")

plt.show()"""
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


