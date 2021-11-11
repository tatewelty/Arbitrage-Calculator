input1 = input("Input Odds 1  ")
input2 = input("Input Odds 2  ")
Investment = float(input("Total Bet  "))


class Odds:
    def __init__(self, odds, probability):
        self.odds = odds
        self.probability = probability

def odds_converter(odds):
    if odds.odds.startswith("+"):
        odds.probability = float(odds.odds[1:])
        odds.probability = (100 / (odds.probability + 100)) * 100
        #print("Positive")
        #print(odds.probability)

    elif odds.odds.startswith("-"):
        odds.probability = float(odds.odds[1:])
        odds.probability = (odds.probability / (odds.probability + 100)) * 100
        #print("Negative")
        #print(odds.probability)

    else:
        odds.probability = float(odds.odds)
        odds.probability = 1 / odds.probability * 100
        #print("Decimal")
        #print(odds.probability)

odds1 = Odds(input1,0)
odds2 = Odds(input2,0)

odds_converter(odds1)
odds_converter(odds2)



Arbitrage=odds1.probability+odds2.probability
if (Arbitrage<100):
    print("Profitable")
elif Arbitrage==100:
    print("Break Even")
else:
    print("NOT Profitable")

Profit=(Investment/(Arbitrage/100))-Investment

bet1=(Investment*odds1.probability)/Arbitrage
bet2=(Investment*odds2.probability)/Arbitrage




print("Bet 1: $",round(bet1,2))
print("Bet 2: $",round(bet2,2))
print("Profit: $", round(Profit,2))

