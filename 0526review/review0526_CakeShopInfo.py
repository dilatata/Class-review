# 클래스 생성

class Cakeshop:
    def __init__(self, c_name, c_price):
        self.cake_name = c_name
        self.cake_price = c_price

    def getC_name(self):
        return self.cake_name

    def getC_price(self):
        return self.cake_price

    def __str__(self):
        return '케익의 이름은' + self.cake_name + ' 케익의 가격은 ' + self.cake_price


    

    
