print("=======계산기=======")
while True:
    a = input("첫번째 수 입력 : ")
    if a.isdigit():
        b = input("연산 입력 : ")
        if b == "+":
            c = input("두번째 수 입력 : ")
            if c.isdigit():
                print(float(a)+float(c))
                break
            else:
                print("잘못된 입력입니다.")
                continue
        elif b == "-":
            c = input("두번째 수 입력 : ")
            if c.isdigit():
                print(float(a)-float(c))
                break
            else:
                print("잘못된 입력입니다.")
                continue
        elif b == "*":
            c = input("두번째 수 입력 : ")
            if c.isdigit():
                print(float(a)*float(c))
                break
            else:
                print("잘못된 입력입니다.")
                continue
        elif b == "/":
            c = input("두번째 수 입력 : ")
            if c.isdigit():
                print(float(a)/float(c))
                break
            else:
                print("잘못된 입력입니다.")
                continue
        else:
            print("잘못된 입력입니다.")
            continue
    else:
        print("잘못된 입력입니다.")