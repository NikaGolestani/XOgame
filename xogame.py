table = [
    [1 ,2 , 3],
    [4 ,5 , 6],
    [7 ,8 , 9]
]
i=0
def check(y):
    global i
    place=int (input(f"type the best place for {y}:"))
    if  place<1:
        print("invalid value")
        i-=1
    elif place<4:
        if table[0][place-1] != "X" and table[0][place-1]!="O" :
            table[0][place-1] = y
        else:
            print("Selected Place is Full!")
            i-=1
    elif place<7:
        if table[1][place-4] != "X" and table[1][place-4]!="O" :
            table[1][place-4] = y
        else:
            print("Selected Place is Full!")
            i -=1
    elif place<10:
        if table[2][place-7] != "X" and table[2][place-7]!="O":
            table[2][place-7] = y
        else:
            print("Selected Place is Full!")
            i -=1
    else:
        print("invalid value")
        i-=1


def checkwinner(value):
    for i in table:
        if i == [value , value , value]:
            return True
    if table[0][0] == table[1][0] == table[2][0] == value:
        return True
    elif table[0][1] == table[1][1] == table[2][1] == value:
        return True
    elif table[0][2] == table[1][2] == table[2][2] == value:
        return True
    elif table[0][0] == table[1][1] == table[2][2] == value:
        return True
    elif table[0][2] == table[1][1] == table[2][0] == value:
        return True
def printtable():
    print (f"{table[0][0]}|{table[0][1]}|{table[0][2]}")
    print("-----")
    print (f"{table[1][0]}|{table[1][1]}|{table[1][2]}")
    print("-----")
    print (f"{table[2][0]}|{table[2][1]}|{table[2][2]}")
printtable()
while i<9:
    if i%2==0:
        y = "X"
    else:
        y="O"
    x=i%2
    check(y)
    printtable()
    if checkwinner(y)==True:
        print(f"{y} is the WINNER")
        break
    elif i==8:
        print(f"DRAW")
    i+=1
