# Do not change import statements.
import unittest
from SI507F17_project1_cards import *

# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code
# description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
# If more than 3 tests fail, it should be because multiple of the test
# methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try
# to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########


class TestCard(unittest.TestCase):
    def setUp(self):
        # create sample cards and expected values
        self.sample_suits = [0, 1, 2, 3]
        self.sample_face_ranks = [1, 11, 12, 13]
        self.sample_other_ranks = [2, 5, 10]

        self.sample_cards = []
        self.expected_values = []

        self.sample_cards.append(Card())
        self.expected_values.append([Card.suit_names[0], 2, 2])
        for suit in self.sample_suits:
            for face_rank in self.sample_face_ranks:
                self.sample_cards.append(Card(suit, face_rank))
                self.expected_values.append([Card.suit_names[suit],
                                            Card.faces[face_rank], face_rank])

            for other_rank in self.sample_other_ranks:
                self.sample_cards.append(Card(suit, other_rank))
                self.expected_values.append([Card.suit_names[suit],
                                            other_rank, other_rank])

    def test_class_var(self):
        self.assertEqual(type(Card.suit_names), type([]))
        self.assertEqual(len(Card.suit_names), 4)
        self.assertEqual(type(Card.rank_levels), type([]))
        self.assertEqual(len(Card.rank_levels), 13)
        self.assertEqual(type(Card.faces), type({}))
        self.assertEqual(len(Card.faces.keys()), 4)

    def test_init(self):
        for i in range(len(self.sample_cards)):
            self.assertEqual(self.sample_cards[i].suit,
                             self.expected_values[i][0])
            self.assertEqual(str(self.sample_cards[i].rank),
                             str(self.expected_values[i][1]))
            self.assertEqual(self.sample_cards[i].rank_num,
                             self.expected_values[i][2])

    def test_print(self):
        for i in range(len(self.sample_cards)):
            exp_result = str(self.expected_values[i][1]) \
                             + " of " + self.expected_values[i][0]
            self.assertEqual(str(self.sample_cards[i]), exp_result)

    def tearDown(self):
        pass


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertIsInstance(self.deck.cards[0], Card)
        self.assertEqual(len(self.deck.cards), 52)

    def test_pop_up(self):
        exp_suit = self.deck.cards[-1].suit
        exp_rank_num = self.deck.cards[-1].rank_num
        popped_card = self.deck.pop_card()
        self.assertEqual(popped_card.suit, exp_suit)
        self.assertEqual(popped_card.rank_num, exp_rank_num)
        self.assertEqual(len(self.deck.cards), 51)

        exp_suit = self.deck.cards[10].suit
        exp_rank_num = self.deck.cards[10].rank_num
        popped_card = self.deck.pop_card(10)
        self.assertEqual(popped_card.suit, exp_suit)
        self.assertEqual(popped_card.rank_num, exp_rank_num)
        self.assertEqual(len(self.deck.cards), 50)

    def test_shuffle(self):
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards), 52)

    def test_replace(self):
        # test exisiting card
        card_to_rep = self.deck.cards[-1]
        self.deck.replace_card(card_to_rep)
        count = self.deck.cards.count(card_to_rep)
        self.assertTrue(count == 1)

        # test not existing card
        card_to_rep = self.deck.pop_card()
        self.deck.replace_card(card_to_rep)
        self.assertTrue(card_to_rep in self.deck.cards)

    def test_deal_hand(self):
        deck_len = len(self.deck.cards)
        act_cards = self.deck.deal_hand(deck_len)
        self.assertTrue(len(self.deck.cards) == 0)
        self.assertEqual(len(act_cards), deck_len)

    def tearDown(self):
        pass


class TestGame(unittest.TestCase):
    def setUp(self):
        pass

    def test_output1(self):
        exp_result = ["Player1", "Player2", "Tie"]
        act_result = play_war_game(True)
        # test output types
        self.assertEqual(len(act_result), 3)
        self.assertEqual(type(act_result), tuple)
        self.assertTrue(act_result[0] in exp_result)
        self.assertEqual(type(act_result[1]), int)
        self.assertEqual(type(act_result[2]), int)

    def test_ouput2(self):
        # test scores
        act_result = play_war_game(True)
        if act_result[0] == "Player1":
            self.assertTrue(act_result[1] > act_result[2])
        elif act_result[0] == "Player2":
            self.assertTrue(act_result[1] < act_result[2])
        else:
            self.assertTrue(act_result[1] == act_result[2])

    def tearDown(self):
        pass


class TestSong(unittest.TestCase):
    def testUp(self):
        pass

    def test_default(self):
        song = show_song()
        self.assertTrue("Winner" in str(song))

    def test_search(self):
        exp_search = "september"
        song = show_song(exp_search)
        self.assertTrue(exp_search in str(song))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
