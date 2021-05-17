print("게임시작")
print("누구를 만났습니다.")
print("누구를 만났을까요?")
input()
print("과연 누구를 ~~~")
input()
print("1. 만난다. 2. 거절한다.")

# hello.py를 포함시킨다.
import hello
# 입력을 담당하는 기능
a = hello.ret_input()
# 값이 들어 왔을 때 해당하는 내용으로 출력하는 기능
hello.if_show(a)
# 돈을 입력하는 기능
print ("돈 넣어 볼까?")
# 넣은 돈 출력
a = hello.money
# 그 돈을 넣으면 3배로 뻥튀기 해주는 기능
# 뻥튀기 된 돈을 출력