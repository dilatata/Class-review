# 클래스 생성

class Cakecustomer:
    def __init__(self, name, number, choice):
        self.customer_name = name
        self.customer_number = number
        self.customer_choice = choice

    def getName(self):
        return self.customer_name

    def getNumber(self):
        return self.customer_number
    
    def getChoice(self):
        return self.customer_choice
    
    def __str__(self):
        return '고개의 이름은' + self.customer_name + '고객의 전화번호는 ' + self.customer_number + '주문 케익은' + self.customer_choice


    

    
