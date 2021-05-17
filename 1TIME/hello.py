# 입력을 담당하는 기능.
def ret_input():
# 값이 들어 왔을 때 해당하는 내용으로 출력 하는 기능
# 입력을 받아서 그 입력값을 넣으면 
# 만약 1번이면 해피엔딩

# 들여쓰기 주의!
    inp = int(input("입력 : "))
    return inp
# 들여쓰기 주의!
# 함수값에 inp를 받아옴. 15번줄 소스 코드 밑에 return inp를 사용하지 않으면 오류가 발생함.
def if_show(inp):
    #잘못된 예시 inp = 0,1,2 사용시 잘못된 결과값이 나옴.
    if inp == 1:
        print("해피엔딩")
    # 2번이면 새드엔딩
    elif inp == 2:
        print("새드엔딩")
    # 그외의 값은 게임오버
    else:
        print("게임오버")

# 돈을 입력하는 기능
money =  int (input("돈을 입력하세요. : "))