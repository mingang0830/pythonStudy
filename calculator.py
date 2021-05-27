print("=======계산기=======")

ERROR_MESSAGE = "잘못된 입력입니다."


def is_digit_with_input(message):
    character = input("{} 수 입력 : ".format(message))
    return character, character.isdigit()


def validate_digit(is_digit):
    if is_digit:
        return True

    print(ERROR_MESSAGE)
    return False


while True:
    first_digit, is_digit = is_digit_with_input("첫번째")
    if not validate_digit(is_digit):
        continue

    operator = input("연산 입력 : ")
    if operator not in ["+", "-", "*", "/"]:
        print(ERROR_MESSAGE)
        continue

    second_digit, is_digit = is_digit_with_input("두번째")
    if not validate_digit(is_digit):
        continue

    result = None
    if operator == "+":
        result = float(first_digit) + float(second_digit)
    elif operator == "-":
        result = float(first_digit) - float(second_digit)
    elif operator == "*":
        result = float(first_digit) * float(second_digit)
    elif operator == "/":
        result = float(first_digit) / float(second_digit)

    print(result)
