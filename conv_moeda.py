moeda = str(input("qual é a moeda que queres converter?: "))
mone = float(input("quanto dinheiro tens?: "))
if moeda == "dollar":
    print(mone * 1.8, "$")
elif moeda == "yen":
    print(mone *165.74, "¥")
elif moeda == "Bolivar VN":
    print(mone * 46.3151, "Bs")
else:
    print("isso não é valido!!")