import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
metro_all=pd.read_csv('c:/pydata/subway.csv')
#print(metro_all)
# dataset => data.go.kr , seoul.data.go.kr
"""
print(metro_all.head()) #상위 5개 head(10)
print(metro_all.tail())
print(metro_all.info) #요약 정보 
"""
"""
1. 데이터 확인 
  head : 사용월  호선명 지하철역  ...  03시-04시 승차인원  03시-04시 하차인원 작업일자
  
  metro_all['호선명'] 
"""
#1. 불필요한 컬럼 제거
#202403
#print(sorted(list(set(metro_all['사용월']))))
metro_recent=metro_all[metro_all['사용월']==202403]
#print(metro_recent)
metro_recent=metro_recent.drop(columns={'작업일자'})
#print(metro_recent)
# 특정 호선 승하차 데이터 = 시각화
line='2호선'
metro_st=metro_recent.groupby(['호선명','지하철역']).mean().reset_index()
#print(metro_st)
metro_st_line2=metro_st[metro_st['호선명']==line]
#print(metro_st_line2)
# 승차인원 확인
metro_get_on=pd.DataFrame()
metro_get_on['지하철역']=metro_st_line2['지하철역']
print(metro_recent.columns)
#print(int(len(metro_recent.columns)-3)/2)
for i in range(int((len(metro_recent.columns)-3)/2)):
    #print(metro_st_line2.column[3+2*i])
    metro_get_on[metro_st_line2.columns[3+2*i]]=metro_st_line2[metro_st_line2.columns[3+2*i]]
metro_get_on=metro_get_on.set_index('지하철역')
#print(metro_get_on)

df=pd.DataFrame(data=metro_st_line2,
                index=metro_st_line2['지하철역'])
#print(df)
df['평균 승차 인원수']=metro_get_on.mean(axis=1).astype(int)
print(df['평균 승차 인원수'])
top10_on=df.sort_values(by="평균 승차 인원수",ascending=False).head(10)
plt.figure(figsize=(20,10))
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.bar(top10_on.index,top10_on['평균 승차 인원수'])
plt.show()

metro_get_off=pd.DataFrame()
metro_get_off['지하철역']=metro_st_line2['지하철역']
for i in range(int((len(metro_recent.columns)-3)/2)):
    #print(metro_st_line2.column[3+2*i])
    metro_get_off[metro_st_line2.columns[4+2*i]]=metro_st_line2[metro_st_line2.columns[4+2*i]]
metro_get_off=metro_get_off.set_index('지하철역')
print(metro_get_off)

df['평균 하차 인원수']=metro_get_off.mean(axis=1).astype(int)
print(df['평균 승차 인원수'])
top10_off=df.sort_values(by="평균 하차 인원수",ascending=False).head(10)
plt.figure(figsize=(20,10))
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.bar(top10_off.index,top10_off['평균 승차 인원수'])
plt.show()



