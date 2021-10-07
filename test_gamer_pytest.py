from gamer import Gamer

class Test_gamer:
    def setup(self):
        self.gamer = Gamer('Valery')

    def teardown(self):
        pass

    def test_init(self):
        assert self.gamer.name == 'Valery'
        assert self.gamer.cards == []

    def test_get_name(self):
        assert self.gamer.get_name() == 'Valery'

    def test_(self):
        self.gamer.accept_cards( [1,2,3,4])
        assert self.gamer.cards == [[1,2,3,4]]
        self.gamer.accept_cards([5, 6, 7, 8],[9,10,11,12])
        assert self.gamer.cards == [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]

    def test_del_card(self):
        self.gamer.accept_cards([1, 2, 3, 4])
        assert self.gamer.cards == [[1, 2, 3, 4]]
        self.gamer.del_card(0)
        assert self.gamer.cards == []

    def test_set_tramp(self):
        self.gamer.accept_cards([1, 2, 3, 'red'])
        assert self.gamer.cards == [[1, 2, 3, 'red']]
        self.gamer.set_tramp( 'red',100 )
        assert self.gamer.cards == [[101, 2, 3, 'red']]