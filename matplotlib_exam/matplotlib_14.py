import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns
import csv
"""
f=open('c:/pydata/202101_gender.csv')
data=csv.reader(f)
m=[]
f=[]
name=input("동네를 입력하세요:")
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i])) #남자
            f.append(int(row[i+103])) #여자
        break
plt.plot(m,label="Man")
plt.plot(f,label="Woman")
plt.legend()
plt.show()
"""
"""
plt.style.use('ggplot')
plt.scatter([1,2,3,4],[10,30,20,40],s=[30,60,90,120],
            c=range(4),cmap='jet')
plt.colorbar()
plt.show()
"""
f=open('c:/pydata/202101_gender.csv')
data=csv.reader(f)
m=[]
f=[]
size=[]
name='청담동'
for row in data:
    if name in row[0]:
        for i in range(3,104):
            m.append(int(row[i])) #남자
            f.append(int(row[i+103])) #여자
            size.append(math.sqrt(int(row[i])+int(row[i+103])))
        break
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.figure(figsize=(10,5),dpi=300)
plt.title('지역 성별 인구 그래프')
plt.scatter(m,f,s=size,c=range(101),alpha=0.5,cmap='jet')
plt.colorbar()
plt.plot(range(max(m)),range(max(m)),'g')
plt.xlabel("남성")
plt.ylabel("여성")
plt.show()
