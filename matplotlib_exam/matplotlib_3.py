import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
"""
emp_df=pd.read_csv('c:/pydata/EMP.csv')
#print(emp_df)
x=emp_df['ENAME']
y=emp_df['SAL']
plt.xticks(rotation=150)
plt.bar(x,y)
plt.show()
"""
"""
plt.plot([1,2,3],[4,4,4],'-',color="r",label="Solid")
plt.plot([1,2,3],[3,3,3],'--',color="g",label="Dashed")
plt.plot([1,2,3],[2,2,2],':',color="b",label="Dotted")
plt.plot([1,2,3],[1,1,1],'-.',color="m",label="DashDot")
plt.xlim([0,5])
plt.ylim([0,5])
plt.legend()
plt.show()
"""
"""
  color 'b' , 'g' , 'r' 
  라인선 : '-' '--' ':' '-.'
"""
"""
plt.plot([1,2,3],[5,6,9],'m*--')
plt.show()
"""
"""
x=np.arange(3)
years=['2023','2024','2025']
values=[100,500,900]
plt.bar(x,values)
plt.xticks(x,years)
plt.show()
# 하이차트 , d3 ...
"""
"""
x=np.arange(3)
years=['2023','2024','2025']
values=[100,500,900]
plt.barh(x,values)
plt.xticks(x,years)
plt.show()
"""
"""
np.random.seed(0)
n=50
x=np.random.rand(n)
y=np.random.rand(n)
area=(30*np.random.rand(n))**2
colors=np.random.rand(n)
plt.scatter(x,y,s=area,c=colors,alpha=0.5,cmap="Spectral")
plt.colorbar()
plt.show()
# 산점 분포도
"""
"""
  자바 , spring , oracle|mysql , Ajax , Vue|React
  python , docker , AWS , GIT 
"""
"""
names=['홍길동','이순신','심청이','강감찬','김두한']
values=[34,32,16,18,50]
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
plt.pie(values,labels=names,autopct="%.1f%%")
plt.show()
"""
arr=np.random.standard_normal((30,40))
plt.matshow(arr)
plt.colorbar()
plt.show()
"""
 bar / pie / scatter / line 
"""


