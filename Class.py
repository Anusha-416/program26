import random as r
class Coin:
    def __init__(self):
        self.sideup="Heads"
    def toss(self):
        if r.randint(0,1)==0:
            self.sideup="Heads"
        else:
            self.sideup="tails"
    def get_sideup(self):
        return self.sideup
def main():
    my_coin=Coin()
    print("before tossing a coin",my_coin.get_sideup())
    print("am tossing the coin")
    my_coin.toss()
    print("after tossing the coin",my_coin.get_sideup())
main()
