import unittest
from koloda import Koloda
from cards import Cards

class testKoloda( unittest.TestCase ):
    def setUp(self):
        self.koloda = Koloda()

    def tearDown(self):
        pass

    def test_get_count(self):
        self.assertEqual( self.koloda.get_count(), 36 )

    def test_init(self):
        self.assertEqual(  self.koloda.curr_card,  0 )
        self.assertTrue(  isinstance(self.koloda.c, Cards)  )
        c = Cards()
        self.assertEqual(  len(c.get_cards()),  36 )
        self.assertEqual(  len(c.get_cards()[0]) , 4  )# [ [рейтинг, достоинство(название), код символа, масть ],... ]
        self.assertEqual(  self.koloda.trump, None )

    def test_card_out(self):
        self.koloda.card_out(trump=True)
        self.assertEqual( len(self.koloda.k), 36 )
        self.koloda.card_out()
        self.assertEqual( len(self.koloda.k), 35 )

    def test_set_get_card(self):
        self.koloda.set_card( 0,[1,2,3,4])
        self.assertListEqual( self.koloda.get_card( 0 ) , [1,2,3,4] )