"""
  6~7  => 10중순 => 3
  사용기술

  BackEnd : Java , Python , JSP ,
            ThymeLeaf , Numpy , Pandas , Matplotlib
            MyBatis JPA
  FrontEnd : HTML5,JavaScript(ES6)
            Jquery , Ajax , VueJs , Vuex , Pinia
            React , React-Query , Redux , Next
            NodeJS

  Framework : Spring , Spring-Boot , Django
  database : oracle21c / mysql3 / sqlite3
  AWS , Docker , CI/CD

  => Spring-Boot : MySql , JPA
     => React , 타임리프 (CI/CD)
                ---------------
  => 희망부서
     SI/SM => Java웹개발
     -----------------
     솔루션
     프레임워크 : AI
     ----------------- SW개발
     Java웹개발/SW개발
     이력서용 / PPT
"""
import os
import sys
import urllib.request
import json
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import  WordCloud
"""
  Python 문법 
   변수 / 연산자 / 제어문 / 함수 / 집합데이터형(list,set,tuple,dict)
  Numpy : 배열 / 연산처리 
  Pandas 
  Matplotlib / seaborn 
  ---------------------
  JSON / XML / BS4 (크롤링) => 셀레니움 
  -----------------------------------
"""
client_id = "OtKU74j2Bx_QN_K5YPck"
client_secret = "eyn6LY7L0j"
fd=input("검색어 입력:")
encText = urllib.parse.quote(fd)
url = "https://openapi.naver.com/v1/search/news.json?display=100&query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

json_data=json.loads(response_body)
print(json_data)
total_str=""
for news in json_data['items']:
     total_str+=news['description']
"""
=> 형태소 분석 : korean_text / 꼬꼬마 
okt=Okt()
noun=okt.nouns(total_str)
print(noun)
list=pd.DataFrame(noun)
"""
font_path="c:/pydata/NanumGothic.ttf"
wc=WordCloud(max_font_size=200,
             background_color="white",
             width=800,height=800,
             font_path=font_path)
wc.generate(total_str)
plt.figure(figsize=(10,8))
plt.imshow(wc)
plt.axis('off')
plt.show()
"""
=> bar chart 
count=Counter(noun)
noun_list=count.most_common(100)
#최빈값 : 횟수가 가장 많은 것
# {1,3,6,6,6,7,7,10,10} => 6
n=[]
for v in noun_list:
    if len(v[0])>1 and v[1]>9:
      #print(v)
      n.append(list(v))
#print(n)
column=["단어","횟수"]
list=pd.DataFrame(n,columns=column)
list_top=list.sort_values(by="횟수",ascending=False).head(10)
print(list)
plt.figure(figsize=(20,10))
plt.rc('font',family="Malgun Gothic")
plt.bar(list_top['단어'],list_top['횟수'])
plt.title('오늘의 뉴스')
plt.show()
"""


