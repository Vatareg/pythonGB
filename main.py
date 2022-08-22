def method_HW01_Task01():
    print("Введите координату Х")
    x = int(input())
    print("Введите координату У")
    y = int(input())
    rezult = None
    if (x > 0 and y > 0):
        rezult = 1
    elif (x > 0 and y < 0):
        rezult = 4
    elif (x < 0 and y > 0):
        rezult = 2
    elif (x < 0 and y < 0):
        rezult = 3
    elif (x == 0 or y == 0):
        print("Точка лежит на оси")
    print(f"Точка с координатами Х = {x} и У =  {y}, находится в {rezult} четверть")
def method_HW01_Task02():
    print("Укажите номер четверти:")
    dot = int(input())
    if (dot == 1):
        print("X > 0 и Y > 0")
    elif (dot == 2):
        print("X < 0 и Y > 0")
    elif (dot == 3):
        print("X < 0 и Y < 0")
    elif (dot == 4):
        print("X > 0 и Y > 0")

#method_HW01_Task01()
#method_HW01_Task02()





