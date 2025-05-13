"""
   데이터 연산처리 : numpy
   데이터를 제어 : 통계 => 데이터 변경 = pandas
   데이터 시각화 : matplotlib , seaborn
   => 데이터가 필요
      dataset => 지원하는 것
   => 그래프 종류 , 색상
      seaborn : 색상 , 백그라운드 처리
   pip install numpy
   pip install pandas
   pip install matplotlib
   pip install seaborn

"""
import matplotlib.pyplot as plt
import numpy as np
# 글꼴 변경 => 한글 처리
"""
   막대 그래프 : bar 
   선 그래프 : line 
   가로 막대 그래프 : barh bar
   개수 그래프 : count 
   산점 그래프 : scatter
   히스토그램 : hist
   상자 그래프 : box plot 
"""
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
y=[2,3,1]
x=np.arange(len(y))
print(x)
#
xlabel=['홍길동','이순신','심청이']
plt.title("점수")
plt.bar(x,y)
#
plt.xticks(x,xlabel)
plt.yticks(sorted(y))
plt.show()