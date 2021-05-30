# 모듈 내용 선언하기

from CakeShopInfo import Cakeshop 
from CakeCustomerInfo import Cakecustomer

# 케이크와 고객 연동 class 생성
class cake_customer:

    def cake_data():
        cake_d = []
        with open('cakeshop.csv', 'r', encoding='utf-8') as f1:
            data = f1.readlines()
            # print(data) -> ['Cheese Cake, 25000\n', 'Chocolate Cake, 26000\n', 'Icecream Cake, 27000\n', 'Customizing Cake, 35000']
            for cake in data:
                ec = cake.split(',')
                # print(ec) # -> ['Cheese Cake', ' 25000\n'] ['Chocolate Cake', ' 26000\n'] ['Icecream Cake', ' 27000\n'] ['Customizing Cake', ' 35000']
                cake_d.append(Cakeshop(ec[0], ec[1]))
            return cake_d
            # print(type(cake_d)) -> list

    def all_print(a):
        for c in a:
            print(c)
            # print(type(c)) # -> <class 'CakeShopInfo.Cakeshop'>

   
    def cust_data():
        cust_d = []
        with open('cakecustomer.csv', 'r', encoding='utf-8') as f2:
            data2 = f2.readlines()
            for cust in data2:
                ec = cust.split(',')
                cust_d.append(Cakecustomer(ec[0], ec[1], ec[2]))
            return cust_d

    def cake_cust_match():
        all_cake = []
        all_cust = []

        with open('cakeshop.csv', 'r', encoding='utf-8') as f1:
            data = f1.readlines()
            for cake in data: 
                all_cake.append(cake.split(','))

        with open('cakecustomer.csv', 'r', encoding='utf-8') as f2:
            data2 = f2.readlines()
            for cust in data2:
                all_cust.append(cust.strip('\n').split(','))
        
        all_match = []
        for a in all_cake:
            # print(a)
            for b in all_cust:
                # print(b)
                if a[0] == b[2]:
                    all_match.append(b[0] + '가 주문한 케이크 ' + a[0] + '가 준비되면 ' + b[1] + ' 으로 연락하세요.')
        return all_match

    if __name__ == ('__main__'):
        # print(cake_data()) #-> 주소값이 나옴
        # all_cake(cake_data()) # ->  TypeError : __str__ returned non-string (type tuple) -> __str__ 에 , 가아닌 + 사용하면 error 해결가능
        # cake_cust_match() # -> None : 잘못된 부분 찾기
        print(cake_cust_match())



