## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

class TestCard(unittest.TestCase):
    def setUp(self):
        ## create sample cards and expected values  
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
                self.expected_values.append([Card.suit_names[suit], Card.faces[face_rank], face_rank])

            for other_rank in self.sample_other_ranks:
                self.sample_cards.append(Card(suit, other_rank))
                self.expected_values.append([Card.suit_names[suit], other_rank, other_rank])

    def test_class_var(self):
        self.assertEqual(type(Card.suit_names), type([]))
        self.assertEqual(len(Card.suit_names), 4)
        self.assertEqual(type(Card.rank_levels), type([]))
        self.assertEqual(len(Card.rank_levels), 13)
        self.assertEqual(type(Card.faces), type({}))
        self.assertEqual(len(Card.faces.keys()), 4)

    def test_init(self):
        for i in range(len(self.sample_cards)):
            self.assertEqual(self.sample_cards[i].suit, self.expected_values[i][0])
            self.assertEqual(str(self.sample_cards[i].rank), str(self.expected_values[i][1]))
            self.assertEqual(self.sample_cards[i].rank_num, self.expected_values[i][2])

    def test_print(self):
        for i in range(len(self.sample_cards)):
            self.assertEqual(str(self.sample_cards[i]), str(self.expected_values[i][1]) + " of " + self.expected_values[i][0])


    def tearDown(self):
        pass

class TestDeck(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)

