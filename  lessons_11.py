# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
# w = QWidget()
# w.resize(600,600)
# w.setWindowTitle('Timur')
# w.show()
# sys.exit(app.exec_())

# import numpy  as np
# nums = np.array([100,200,300,400])
# nums2 =nums*1.16
# print(nums2)

# # https://matplotlib.org/stable/users/installing/index.html
# https://habr.com/ru/articles/468295/

import matplotlib.pyplot as plt
# x=[1,2,3,4,5,6]
# y=[3,4,5,6,8,9]

# plt.bar(x,y)
# plt.title( "Заголовок")
# plt.xlabel( "X")
# plt.ylabel( "Y")
# plt.show()

# plt.plot(x,y)
# plt.title( "Заголовок")
# plt.xlabel( "X")
# plt.ylabel( "Y")
# plt.show()

# данные для графика
# x = ['Apple', 'Samsung', 'Xiaomi', 'One plus', 'Nokia']
# y = [50,20,10,15,5]

# # создание графика
# #линейный график
# # plt.plot(x,y)
# # точеченый
# # plt.scatter(x,y)
# # столбчатая
# plt.bar(x,y)
# plt.title('Это заголовок')
# plt.xlabel('Это Х')
# plt.ylabel('Это Y')
# plt.show()


import matplotlib.pyplot as plt

# данные для графика
labels = ['Apple', 'Xiaomi', 'OnePlus', 'Nokia']
sizes = [40, 30, 20,10]
colors = ['red','blue', 'green', 'yellow']
explode = (0.1, 0,0,0)
# создаем диаграму
plt.pie(sizes, explode=explode, labels = labels, colors = colors,
autopct = '%1.1f%%', shadow= True, startangle = 140)
plt.show()