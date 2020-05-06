# 과제 1 사용자에게 이름과 전화번호를 입력받아 출력하라. 단, 출력 예와 같이 이름과 전화번호는 줄바꿈 해야한다.
# 입력 예 : 손창하
# 입력 예 : 01067662333
'''출력 예 : 제 이름은 손창하입니다.
제 전화번호는 01067662333입니다.
'''
name_string = input()
num_string = input()
print("제 이름은", name_string, "입니다.\n" "제 전화번호는", num_string, "입니다.")

# 과제 2 아래 2- 1,2,3번 과제를 수행하여 a를 출력 예와 같게 바꾸어라.
# 과제 2-1 공백2개를 1개로 바꾸고 :는 ,로 바꾼다. 단, 모든 함수는 1번만 사용가능
a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
b = a.replace(":", ",")
c = ' '.join(b.split())

# 과제 2-2 naMe를 소문자로 바꾸고 뒤에 있는 my를 My로 바꿔라.
d = c.replace("naMe", "name")
e = d.replace("my", "My")

# 과제 2-3 주민번호를 뒷자리 1자리만 남기고 지워라
f = e.replace("!!!!!!", "")
print(f)
# 다른 방법이 있을 것 같은데...잘 모르겠네요ㅠㅠ

# 출력 예: My name is Son Chang Ha, My pin is 000125-3.