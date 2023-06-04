#Data Types
#프로그래밍 언어에서 두가지로 나뉨
#1. 컴파일 언어
# - 데이터 타입이 미리 정함
# -dallor -> int doller = 10 or String doller = "10"
# - 하나라도 틀리면(컴파일 과정) 걸러짐
from builtins import print, type

# 2. 인터프리터 언어 ex) python, javascript
# - 데이터 타입을 그 때 정함
# - 일단 돌림

# 1. str(문자열)
a = "메가스터디"
print(type(a))
#2. int (정수)
b = 123
print(type(b))
#3 . float(실수)
c = 123.123
print(type(c))
#4. list
d= [123, '4566', 12.56, [1,2,3]]
print(type(d))
#5. dict
e= {'name': 'jos', 'age': 21, 'language':['c','java']}
print(type(e))
#6. set 집합
f = {"apple", "banana", "pineapple", "apple"}
print(f)