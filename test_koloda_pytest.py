#import pytest
import koloda
from koloda import Koloda
from cards import Cards

class Test_koloda:
    def setup(self):
        self.koloda = Koloda()

    def teardown(self):
        pass

    def test_get_count(self):
        assert self.koloda.get_count() == 36

    def test_init(self):
        assert self.koloda.curr_card == 0
        assert isinstance( self.koloda.c, Cards )
        c = Cards()
        assert len(c.get_cards()) == 36
        assert len(c.get_cards()[0]) == 4  # [ [рейтинг, достоинство(название), код символа, масть ],... ]
        assert self.koloda.trump == None

    def test_card_out(self):
        self.koloda.card_out(trump=True)
        assert len(self.koloda.k) == 36
        self.koloda.card_out()
        assert len(self.koloda.k) == 35

    def test_set_get_card(self):
        self.koloda.set_card( 0,[1,2,3,4])
        assert self.koloda.get_card( 0 ) == [1,2,3,4]
