"""
대화형 프로그래밍 과제 05 - vending machine
이름: 허버트
학번: 2020110876
"""

# vending machine's initial coin count and product quantity
machine_coin = 10000  # 100 coins each worth 100 won
water = 1000  # ml
coffee = 500  # g
prim = 500  # g
sugar = 500  # g
paper_cup = 30

coin_input = int(input("Insert your coin: "))  # prompt user to input his/her coins
balance = coin_input  # amount of money owed to the customer
while True:

    if balance < 300:
        print("돈이 부족합니다", balance, "원:")
        print('''
        ---------------------------
        커피 자판기 동작을 종료합니다
        ---------------------------
        ''')
        break
    else:
        print(
            '''
            -----------------------------------
                    커피 자판기 (300원)
            1. 블랙 커피
            2. 프림 커피
            3. 설탕 프림 커피
            4. 재고 현황
            5. 종료

            '''
        )
        choice = int(input("메뉴를 선택하세요:"))

        if choice == 5:
            break

        if coffee < 30 or prim < 15 or sugar < 10 or water < 100 or machine_coin < 100:  # checking the inventory
            print("Sorry,there isn't enough ingredients to make your coffee")
            break
        else:
            if choice == 1:
                coffee -= 30  # 30g of coffee is used
                water -= 100  # 100ml of water is used
                paper_cup -= 1  # 1 paper cup is used
                balance -= 300
                machine_coin += 300
                print("블랙 커피를 선택하셨습니다." + " 잔돈:", balance)
            elif choice == 2:
                coffee -= 15  # 15g of coffee is used
                water -= 100  # 100ml of water is used
                prim -= 15  # 15g of prim is used
                paper_cup -= 1  # 1 paper cup is used
                balance -= 300
                machine_coin += 300
                print("프림커피를 선택하셨습니다." + " 잔돈:", balance)
            elif choice == 3:
                coffee -= 10  # 10g of coffee is used
                water -= 100  # 100ml of water is used
                prim -= 10  # 10g of prim is used
                sugar -= 10  # 10g of sugar is used
                paper_cup -= 1
                balance -= 300
                machine_coin += 300
                print("설탕커피를 선택하셨습니다." + " 잔돈:", balance)
            elif choice == 4:
                print("재고 현황:")
                print("coffee: ", coffee, "g,", " prim: ", prim, "g,", " sugar: ", sugar, "g")
                print("water: ", water, "ml,", " paper cups: ", paper_cup, "개")
                print("자판기 남은 돈: ", machine_coin, "원,", "잔돈 현황: ", balance, "원")
