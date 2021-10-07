from cards import Cards

class Koloda:
    def __init__(self):  # взяли колоду карт

        self.curr_card = 0
        self.c = Cards()
        #print( '============',  type(self.c))
        self.cards = self.c.get_cards()
        self.k = self.cards  # [ [рейтинг, достоинство(название), код символа, масть ],... ]
        self.trump = None

    def card_out(self, trump=False):
        card = self.k.pop(0)  # вытащить карту из колоды
        if trump:  # перемещение карты-козыря в конец колоды
            self.k.append( card )
            self.trump = card

        return card

    def get_card(self,i):
        return self.k[i]

    def set_card(self,i,v ):
        self.k[i] = v

    def get_koloda(self):
        return self.k

    def get_count(self):
        return len(self.k)



if __name__  == '__main__':
    from cards import Cards
    cards = Cards()
    k = Koloda()
    lst = k.card_out()
    print( len(k.get_koloda()) )
    for v in k:
        print( v )