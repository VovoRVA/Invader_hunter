from run import InvaderRecognizer
import unittest


class TestStringMethods(unittest.TestCase):
    def test_one(self):
        invader = [['o']]
        radar = [['o', 'o'],
                 ['-', 'o']]
        inv_rec = InvaderRecognizer(1)
        res = inv_rec.get_matches(invader, radar)
        # testing matches are 3
        self.assertEqual(len(res), 3)
        # testing match rate is at least 1
        for _, r in res:
            self.assertGreaterEqual(r, 1)

    def test_two(self):
        invader = [['-', 'o'],
                   ['o', 'o']]
        radar = [['o', 'o', '-'],
                 ['-', 'o', 'o'],
                 ['o', 'o', 'o']]
        inv_rec = InvaderRecognizer(0.7)
        res = inv_rec.get_matches(invader, radar)
        # testing matches are 2
        self.assertEqual(len(res), 2)
        # testing match rate is at least 0.7
        for _, r in res:
            self.assertGreaterEqual(r, 0.7)

    def test_edge_case(self):
        invader = [['o', 'o', 'o'],
                   ['o', 'o', 'o'],
                   ['-', 'o', '-']]
        radar = [['o', 'o', '-', '-', '-'],
                 ['o', 'o', '-', '-', '-'],
                 ['o', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-']]
        inv_rec = InvaderRecognizer(0.65)
        res = inv_rec.get_matches(invader, radar)
        self.assertEqual(len(res), 1)
        self.assertGreaterEqual(res[0][0], [0, -1])
        self.assertGreaterEqual(res[0][1], 0.65)


if __name__ == '__main__':
    unittest.main()