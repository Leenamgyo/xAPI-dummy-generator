
def only_input_choice_number():
    while True:    
        input_ = input("1 ~ 4 사이의 숫자를 입력하세요:")
        if input_ in ["1", "2", "3", "4"]:
            return input_
        