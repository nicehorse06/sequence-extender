import unittest
from sequence import Sequence


class SequenceTestCase(unittest.TestCase):

    def test_raw_str_to_list(self):
        this_seq = Sequence(raw_str='1 2 3 4 5')
        self.assertEqual(this_seq.raw_str_to_list('2 4 6 8'), [2, 4, 6, 8])

    def test_return_answer_str(self):
        this_seq = Sequence(raw_str='1 2 3 4 5')
        this_seq.output_list = ['3', '33', '50', '100']
        self.assertEqual(this_seq.return_answer_str(), '3 33 50 100')

    def test_seq_length(self):
        this_seq = Sequence(raw_str='1 2 3 4 5')
        self.assertEqual(this_seq.seq_length(), 5)

    def test_last_item(self):
        this_seq = Sequence(raw_str='1 2 3 4 7')
        self.assertEqual(this_seq.last_item(), 7)

    def test_last_of_last_item(self):
        this_seq = Sequence(raw_str='1 2 3 4 7 11')
        self.assertEqual(this_seq.last_of_last_item(), 7)

    def test_common_difference(self):
        this_seq = Sequence(raw_str='2 4 6 8')
        self.assertEqual(this_seq.common_difference(), 2)

    def test_common_ratio(self):
        this_seq = Sequence(raw_str='2 6 18')
        self.assertEqual(this_seq.common_ratio(), 3)

    def test_is_empty_list(self):
        this_seq = Sequence(raw_str='2 6 18')
        this_empty_seq = Sequence(raw_str='')

        self.assertTrue(this_empty_seq.is_empty_list())
        self.assertFalse(this_seq.is_empty_list())

    def test_empty_seq(self):
        this_seq = Sequence(raw_str='2 6 18')
        self.assertEqual(this_seq.empty_seq(), '')

    def test_is_only_one_item(self):
        this_seq = Sequence(raw_str='2 6 18')
        this_only_one_seq = Sequence(raw_str='1')

        self.assertTrue(this_only_one_seq.is_only_one_item())
        self.assertFalse(this_seq.is_only_one_item())

    def test_only_one_item_seq(self):
        this_seq = Sequence(raw_str='1')
        forged_seq = '1 1 1 1 1 1 1 1 1 1'
        self.assertEqual(this_seq.only_one_item_seq(), forged_seq)

    def test_is_arithmetic(self):
        arithmetic_list = [
            '2 4 6 8 10',
            '1 3 5 7 9',
            '5 10',
        ]
        not_arithmetic_list = [
            '2 4 8 16',
            '1 1 2 3 5 8',
        ] 
        for this_str in arithmetic_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertTrue(this_seq.is_arithmetic())

        for this_str in not_arithmetic_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertFalse(this_seq.is_arithmetic())

    def test_forge_arithmetic(self):
        this_seq = Sequence(raw_str='2 4 6 8')
        forged_seq = '10 12 14 16 18 20 22 24 26 28'
        self.assertEqual(this_seq.forge_arithmetic(), forged_seq)

    def test_is_geometric(self):
        geometric_list = [
            '2 4 8 16',
            '4 12 36',
        ]
        not_geometric_list = [
            '2 4 6 8 10',
            '1 3 5 7 9',
            '1 1 2 3 5 8',
        ] 
        for this_str in geometric_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertTrue(this_seq.is_geometric())

        for this_str in not_geometric_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertFalse(this_seq.is_geometric())

    def test_forge_geometric(self):
        this_seq = Sequence(raw_str='2 6 18 54')
        forged_seq = '162 486 1458 4374 13122 39366 118098 354294 1062882 3188646'
        self.assertEqual(this_seq.forge_geometric(), forged_seq)

    def test_is_fibonacci(self):
        fibonacci_list = [
            '1 1 2 3 5 8',
        ]
        not_fibonacci_list = [
            '2 4 6 8 10',
            '1 3 5 7 9',
            '1 4 10 15',
        ] 
        for this_str in fibonacci_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertTrue(this_seq.is_fibonacci())

        for this_str in not_fibonacci_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertFalse(this_seq.is_fibonacci())

    def test_forge_fibonacci(self):
        this_seq = Sequence(raw_str='1 1 2 3 5 8')
        forged_seq = '13 21 34 55 89 144 233 377 610 987'
        self.assertEqual(this_seq.forge_fibonacci(), forged_seq)

    def test_is_square_seq(self):
        square_list = [
            '1 4 9 16',
            '1 9 25'
        ]
        not_square_list = [
            '2 4 6 8 10',
            '1 3 5 7 9',
            '1 4 10 15',
        ] 
        for this_str in square_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertTrue(this_seq.is_square_seq())

        for this_str in not_square_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertFalse(this_seq.is_square_seq())

    def test_forg_square_seq(self):
        this_seq = Sequence(raw_str='1 4 9 16')
        forged_seq = '25 36 49 64 81 100 121 144 169 196'
        self.assertEqual(this_seq.forg_square_seq(), forged_seq)

    def test_is_high_order_arithmetic(self):
        high_order_arithmetic_list = [
            '1 2 4 7',
            '3 4 6 9',
            '1 3 5 7 9',
            '1 2 3 4 5',
        ]

        high_order_arithmetic_with_ratio_list = [
            '4 14 34 74 154',
            '1 3 7 15',
        ]

        not_high_order_arithmetic_list = [
            '1 4 10 15',
            '1 1 2 3 5 8'
        ] 
        for this_str in high_order_arithmetic_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertTrue(this_seq.is_high_order_arithmetic(with_ratio=False))

        for this_str in high_order_arithmetic_with_ratio_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertTrue(this_seq.is_high_order_arithmetic(with_ratio=True))

        for this_str in not_high_order_arithmetic_list:
            this_seq = Sequence(raw_str=this_str)
            self.assertFalse(this_seq.is_high_order_arithmetic(with_ratio=False))
            self.assertFalse(this_seq.is_high_order_arithmetic(with_ratio=True))

    def test_forge_high_order_arithmetic(self):
        this_high_order_arithmetic_seq_not_with_datio = Sequence(raw_str='1 2 4 7')
        this_high_order_arithmetic_seq_with_ratio = Sequence(raw_str='4 14 34 74')
        forged_seq = '11 16 22 29 37 46 56 67 79 92'
        forged_seq_with_ratio = '154 314 634 1274 2554 5114 10234 20474 40954 81914'
        self.assertEqual(this_high_order_arithmetic_seq_not_with_datio.forge_high_order_arithmetic(
            with_ratio=False), forged_seq)
        self.assertEqual(this_high_order_arithmetic_seq_with_ratio.forge_high_order_arithmetic(
            with_ratio=True), forged_seq_with_ratio)

if __name__ == '__main__':
    unittest.main()
