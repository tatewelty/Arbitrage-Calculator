

#def arbitrage(odds1, odds2, Investment):




odds1=input("Input odds 1")


def odds_converter(odds):
    if odds.startswith("+"):
        odds.probability = float(odds1[1:])
        odds.probability = (100 / (odds.probability + 100)) * 100
        print("Positive")
        print(odds.probability)







if odds1.startswith("+"):
    probability1=float(odds1[1:])
    probability1=(100/(probability1+100))*100
    print("Positive")
    print(probability1)

elif odds1.startswith("-"):
        probability1=float(odds1[1:])
        probability1=(probability1/(probability1+100))*100
        print("Negative")
        print(probability1)

else:
    probability1=float(odds1)
    probability1=1/probability1*100
    print("Decimal")
    print(probability1)



odds_converter(odds1)


