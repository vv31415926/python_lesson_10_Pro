import unittest
from gamer import Gamer

class TestGamer( unittest.TestCase ):
    def setUp(self):
        self.gamer = Gamer('Valery')

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual( self.gamer.name, 'Valery' )
        self.assertListEqual( self.gamer.cards, [] )

    def test_get_name(self):
        self.assertEqual( self.gamer.get_name(), 'Valery' )

    def test_(self):
        self.gamer.accept_cards( [1,2,3,4])
        self.assertListEqual( self.gamer.cards, [[1,2,3,4]] )
        self.gamer.accept_cards([5, 6, 7, 8],[9,10,11,12])
        self.assertListEqual( self.gamer.cards, [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]] )

    def test_del_card(self):
        self.gamer.accept_cards([1, 2, 3, 4])
        self.assertListEqual( self.gamer.cards, [[1, 2, 3, 4]] )
        self.gamer.del_card(0)
        self.assertListEqual( self.gamer.cards, [] )

    def test_set_tramp(self):
        self.gamer.accept_cards([1, 2, 3, 'red'])
        self.assertListEqual( self.gamer.cards, [[1, 2, 3, 'red']] )
        self.gamer.set_tramp( 'red',100 )
        self.assertListEqual( self.gamer.cards, [[101, 2, 3, 'red']] )