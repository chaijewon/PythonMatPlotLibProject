import re

txt="Field. Friend fr!end"
#단어
n=re.findall(r'ie',txt)
print(n)

txt="""
     지난 경기에서 안타와 타점을 추가한 이정후(27, 샌프란시스코 자이언츠)가 한국 프로야구 시절 매우 강했던 메릴 켈리(37)를 상대로 첫 4번 타순에 배치됐다.
    샌프란시스코는 13일(이하 한국시각) 미국 캘리포니아주 샌프란시스코에 위치한 오라클 파크에서 애리조나 다이아몬드백스 와 홈경기를 가진다.
    이날 샌프란시스코는 기존과 조금 다른 타순을 들고 나왔다. 이번 시즌 줄곧 3번 타순에 배치된 이정후가 4번으로 자리를 이동한 것.
    이에 이정후는 메이저리그 데뷔 후 처음으로 4번 타자 자리에서 선발 출전한다. 이정후는 지난해 1번, 이번 시즌 3번으로 나섰다.
    """
# [가-힣] => Konlp
n=re.findall(r'[가-힣]+',txt)
print(n)
print(len(n))
#re.findall(r'\d+',txt)
n=re.findall(r'[0-9]+',txt)
print(n)
text="123456 23456"
print(re.findall(r'234',text))
txt1="white         space"
txt2="white space"
print(re.findall(r"e\ss",txt1))
print(re.findall(r"e\ss",txt2))
# a2f aaa a5f   => a\df
# ^ , $
txt="this this this this"
print(re.findall(r"^this",txt))
print(re.sub(r"^this","Begin",txt))
print(re.findall(r"this$",txt))
print(re.sub(r"this$","End",txt))
# 중괄호
txt="Teth Teeth Teeeth TeeeeTh TeeeeeeeeeTh"
print(re.findall(r"Te{1,4}Th",txt))
# Te => e자가 1개~3개 사이에 있는 문자
print(re.findall(r"Te{0,1}th",txt))
# Teth Teeth
print(re.findall(r"Te{2,}Th",txt))
# *(0이상) , +(1이상)
txt="Tth Teth Teeth Teeeta Taskfsfsfsfdsfth"
print(re.findall(r"Te*th",txt))
# Te*th => T시작 문자는 e가 0이상 th로 종료
# Youtube 동영상 키
print(re.findall(r"Te+th",txt))
print(re.findall(r"T[^e]*th",txt))
# e를 제외한 문자가 여러개 0개 존재
txt="""
    211.238.142.101 127.0.0.1 123,123,123,123 196.168.1.101
    """
n=re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",txt)
print(n)
n=re.findall(r"\d+",txt)
print(n)

txt='"abcd" <abcd>'
n=re.findall(r"<[^>]*>|\"[^\"]*\"",txt)
# < => >제외 => 문자여러개 >
# " => 제외 => 문자여러개 "
# 인용부호 => 사람이름 , Actor
print(n)

# () => 그룹
"""
  (([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3}))\.([0-9]{1,3})
  ------------------------------------------  ------------
                   회사 번호                                고유번호
  
"""
txt="My Phone number is 010-1111-1111"
match=re.search(r"(\d{3})-(\d{4})-(\d{4})",txt)
if match:
    print("번호 전체:",match.group(0))
    print("Area :", match.group(1))
    print("Prifix :", match.group(2))
    print("Line :", match.group(3))
    print(match.groups())
# search => 없는 경우 : none
# 문자 대체 => sub
# 찾기 => findall
# 단어 => 긍정 / 부정 => 데이터사전 => 가중치
# 트위터 / 페이스북 => 대선
# 정규식은 문자열의 형태를 만들어서 찾는다
# ----- 오라클 / MySQL  regexp_like()
# split(정규식) replaceAll(정규식)
