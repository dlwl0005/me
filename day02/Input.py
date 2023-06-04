#표준입력장치(키보드 통해서 넣는거)
# gender = input("성별:")
# print(f"{gender}성전환(트랜스젠더) {gender}으로는 최초로 국내 종합체육대회에 출전한 나화린(37·철원군)씨가 사이클 종목에서 2관왕에 올라 전국체육대회 출전권을 획득했다. 지난 4월 7일 법원으로부터 성별 정정허가를 받은 나씨는 국내 첫 성전환 출전 선수로 관심을 모았다.")
#
# a =input("숫자:")
# b =input("숫자2:")
# c = int(a)
# d = int(b)
# print(c+d)
# print(c*d)
# print(c/d)
# print(c-d)
# print(c % d)
# print(c>d)
# name = input("이름:")
# mbti = input("mbti:")
# food = input("음식:")
# list1 = input("어플1:")
# list2 = input("어플2:")
# list3 = input("어플3:")
# list4 = str([list1, list2, list3])
# print(f"당신의 이름은 {name}이고,mbti는  {mbti} 이고,최애음식은  {food} 입니다.자주사용하는 어플은  {list4}  입니다.")
mbti1 = input("외향인가요 내향인가요")
mbti2 = input("직관적인가요 감각적인가요")
mbti3 = input("이성적인가요 감성적인가요")
mbti4 = input("즉흥적인가요 계획적인가요")
mbti = {'e':'외향','i': '내향', 'n':'직관', 's': '감각', 't': '이성', 'f':'감성', 'p':'즉흥', 'j':'계획'}
print(f"당신은 mbti 성향을 봤을 때, {mbti[mbti1]}이시고, {mbti[mbti2]}이시고,{mbti[mbti3]}이시고,{mbti[mbti4]}입니다.")




