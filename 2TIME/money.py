# import a 와 똑같은 기능을 할수 있는것
# from hello import input_money, money_pung 으로도 사용가능하다. (flask 실습때와 똑같음.)
from a import input_money, money_pung

# 돈을 입력하는 기능		
m = input_money()		
# 넣은 돈 출력		
print("당신의 돈은 {}원".format(m))		
# 그 돈을 넣으면 3배로 뻥튀기 해주는 기능		
input("수리 수리 마수리~~ 얍!!(엔터)")		
# 뻥튀기 된 돈을 출력		
print("당신의 돈은 {}원".format(money_pung(m)))		