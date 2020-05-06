import sys
from sequence import Sequence

def extend_seq(input_str):
    this_sequence = Sequence(raw_str=input_str)

    if this_sequence.is_empty_list():
        return this_sequence.empty_seq()

    if this_sequence.is_only_one_item():
        return this_sequence.only_one_item_seq()

    if this_sequence.is_arithmetic():
        return this_sequence.forge_arithmetic()

    if this_sequence.is_geometric():
        return this_sequence.forge_geometric()

    if this_sequence.is_fibonacci():
        return this_sequence.forge_fibonacci()

    if this_sequence.is_square_seq():
        return this_sequence.forg_square_seq()

    if this_sequence.is_high_order_arithmetic():
        return this_sequence.forge_high_order_arithmetic()

    if this_sequence.is_high_order_arithmetic(with_ratio=True):
        return this_sequence.forge_high_order_arithmetic(with_ratio=True)

    return 'unknown sequence'

if __name__ == '__main__':
    print('Please input from keyboard in the form of integers separated by spaces. (e.g. 2 4 6):')
    input_list = sys.stdin.readline().split('\n')
    print(extend_seq(input_list[0]))
