#operator 연산자
#할당 연산자
a = 1
a += 1 #재할당
a -= 1
a *= 1
a /= 1

# 수리 연산자
b  = 10 / 3 #몫
b2 = 10% 3 #나머지
print(b)
print(type(b))
print(b2)

#비교 연산자
# x = 1
# y = 2
# print(x == y)
# print(x < y)
# print(x != y)
# print(x > y)

#논리 연산자 [and ,or, not, ()]
bitcoin = 100
doge = 20
print(bitcoin > 0 and bitcoin < 200)
print((bitcoin > 0 and bitcoin < 200) or doge > 100)
print(not(bitcoin > 0))
#in 연산자 [리스트]
x = ['mega', 'study', 'shinchon']
print('study' in x)
