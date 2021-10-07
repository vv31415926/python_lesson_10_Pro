from cards import Cards

class Test_cards:
    def setup(self):
        self.cards = Cards()

    def teardown(self):
        pass

    def test_init(self):
        assert self.cards.cards == []

    def test_get_cards(self):   # [[рейтинг, достоинство(название), код символа, масть ],...]
        assert len(self.cards.get_cards()) == 36
        assert len(self.cards.get_cards()[0]) == 4

    def test_ind(self):
        assert self.cards.ind( ['0','1','2','3']  ) == '12'



