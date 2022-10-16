from assignment_2.task_3 import single_number
from assignment_2.task_3 import single_number_one
from assignment_2.task_3 import single_number_two
from assignment_2.task_3 import single_number_three


def test_single_number():
    nums_1 = [1]
    assert single_number(nums_1) == 1

    nums_2 = [2, 2, 3]
    assert single_number(nums_2) == 3

    nums_3 = [4, 1, 2, 1, 2]
    assert single_number(nums_3) == 4


def test_single_number_one():
    nums_1 = [1]
    assert single_number_one(nums_1) == 1

    nums_2 = [2, 2, 3]
    assert single_number_one(nums_2) == 3

    nums_3 = [4, 1, 2, 1, 2]
    assert single_number_one(nums_3) == 4


def test_single_number_two():
    nums_1 = [1]
    assert single_number_two(nums_1) == 1

    nums_2 = [2, 2, 3]
    assert single_number_two(nums_2) == 3

    nums_3 = [4, 1, 2, 1, 2]
    assert single_number_two(nums_3) == 4


def test_single_number_three():
    nums_1 = [1]
    assert single_number_three(nums_1) == 1

    nums_2 = [2, 2, 3]
    assert single_number_three(nums_2) == 3

    nums_3 = [4, 1, 2, 1, 2]
    assert single_number_three(nums_3) == 4
    