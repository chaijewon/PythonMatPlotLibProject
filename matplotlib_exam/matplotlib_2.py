import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=sns.load_dataset("tips")
#data=sns.get_dataset_names()
print(df)
"""
['anagrams',
 'anscombe', 
 'attention', 
 'brain_networks', 
 'car_crashes', 
 'diamonds', 
 'dots', 
 'dowjones', 
 'exercise', 
 'flights', 
 'fmri', 
 'geyser', 
 'glue', '
 healthexp', 
 ***'iris', 
 
 'mpg', 
 'penguins', 
 'planets', 
 'seaice', 
 'taxis', 
 *** 'tips', 
 *** 'titanic']
"""
"""
url="https://sports.news.naver.com/kbaseball/record/index?category=kbo&year=2024"
kbo=pd.read_html(url)
print(kbo)
# 반드시 <table>
"""

# 1. hist plot
p=sns.color_palette('winter',2)
#sns.histplot(x=df['total_bill'],palette=p)
#sns.histplot(x=df['total_bill'],y=df['tip'],palette=p)
#sns.kdeplot(x=df['total_bill'],y=df['tip'],palette=p)
# 일반 그래프
#sns.barplot(x=df['sex'],y=df['tip'],palette=p)
#예매율 , 히트수
#sns.countplot(x=df['sex'],palette=p)
#sns.boxplot(x=df['total_bill'],palette=p)
#sns.boxplot(y=df['total_bill'],x=df['smoker'],palette=p)
sns.lmplot(x='tip',y='total_bill',data=df,hue='sex',palette=p)
plt.show()