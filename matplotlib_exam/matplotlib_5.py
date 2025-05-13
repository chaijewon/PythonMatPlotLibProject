import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import missingno as msno
from wordcloud import  WordCloud,STOPWORDS
# 값이 없는 경우 , 문법배제
set(STOPWORDS)
print(sns.__version__)
df=pd.read_csv("c:/pydata/car_recall.csv")
# 한글처리
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
"""
#print(df)
# 상위 5개
print(df.head())
# 하위 5개
print(df.tail())
# 상위 10개
print(df.head(10))
# 정보요약
print(df.info())
# 한글처리
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus']=False
msno.matrix(df)
plt.show()
# isna() 함수 이용
# print(df.isna().sum())
# print(df)
# 1. 중복값을 제거 
"""
"""
data=[
    ['사과',3000],
    ['배',5000],
    ['딸기',4000],
    ['귤',5000],
    ['사과',3000],
    ['배',5000]
]
f=[x[0] for x in data]
p=[x[1] for x in data]
print(f)
print(p)
df=pd.DataFrame({
    "과일":f,
    "가격":p
})
print(df)
#중복 여부 확인
print(df.duplicated())
#중복 제거
new_df=df.drop_duplicates()
print(new_df)
# 데이터 추가
df['순서']=range(len(f))
print(df.drop_duplicates())
print(df.drop_duplicates(['가격']))
"""
print("Before",len(df))
df=df.drop_duplicates()
print("After",len(df))
# 데이터 column 변경
# print(df['생산기간(부터)'])
# 2021-04-29
def parse_year(s):
    return int(s[:4])
def parse_month(s):
    return int(s[5:7])
def parse_day(s):
    return int(s[8])
# print(df['생산기간(까지)'])
# print(df['리콜개시일'])
# column추가

# alter table car_recall add start_year...
df['start_year']=df['생산기간(부터)'].apply(parse_year)
df['start_month']=df['생산기간(부터)'].apply(parse_month)
df['start_day']=df['생산기간(부터)'].apply(parse_day)

df['end_year']=df['생산기간(까지)'].apply(parse_year)
df['end_month']=df['생산기간(까지)'].apply(parse_month)
df['end_day']=df['생산기간(까지)'].apply(parse_day)

df['recall_year']=df['리콜개시일'].apply(parse_year)
df['recall_month']=df['리콜개시일'].apply(parse_month)
df['recall_day']=df['리콜개시일'].apply(parse_day)

#print(df.head(3))
#print(df['start_year'])
#필요없는 컬럼을 제거
df=(df.drop(columns=['생산기간(부터)','생산기간(까지)','리콜개시일'])
    .rename(columns={"제작자":"makes","차명":"model","리콜사유":"case"})
   )
print(df.head(3))
# 데이터 읽기 => 컬럼(한글) 처리 어렵다 => 영문 변경
"""
  df['column'] df['생산기간(부터)'] df['FROM']
"""
# 데이터 분석
# 특정 부분을 추출 => 분석
# 1) 제조사별 리콜 현황
df=df[df['recall_year']==2022]
print(df.recall_year.min(),df.recall_year.max())
df.groupby('makes').count()['model'].sort_values(ascending=False)
print('================제조사별 리콜 현황=======================')
print(df.groupby('makes').count()['model'].sort_values(ascending=False))
tmp=pd.DataFrame(df.groupby('makes').count()['model'].sort_values(ascending=False)).rename(columns={"model":"count"})
print('================제조사별 리콜 현황 변경후=================')
print(tmp)
# 시각화
plt.figure(figsize=(20,10)) #margin-left=20 margin-top=10
ax=sns.countplot(x='makes',data=df,palette="Set2",order=tmp.index)
plt.xticks(rotation=270)
plt.show()



