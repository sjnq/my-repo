import matplotlib.pyplot as plt

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

plt.bar(x_years, y_data)



#막대 문양 채우기
plt.bar(x_years, y_data, color="C1", edgecolor="black", hatch="/")


plt.show()