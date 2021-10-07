import unittest
from cards import Cards

class TestCards( unittest.TestCase ):
    def setUp(self):
        self.cards = Cards()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertListEqual( self.cards.cards, [] )

    def test_get_cards(self):   # [[рейтинг, достоинство(название), код символа, масть ],...]
        self.assertEqual( len(self.cards.get_cards()),  36 )
        self.assertEqual( len(self.cards.get_cards()[0]), 4 )

    def test_ind(self):
        self.assertEqual( self.cards.ind( ['0','1','2','3']  ), '12' )






