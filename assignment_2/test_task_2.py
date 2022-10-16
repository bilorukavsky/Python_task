from assignment_2.task_2 import remove_element
from assignment_2.task_2 import remove_element_one


def test_remove_element():
    nums_1 = [0, 1, 2, 2, 3, 0, 4, 2]
    val_1 = 2
    assert remove_element(nums_1, val_1) == 5
    assert nums_1 == [0, 1, 3, 0, 4]

    nums_2 = [3, 2, 2, 3]
    val_2 = 2
    assert remove_element(nums_2, val_2) == 2
    assert nums_2 == [3, 3]


def test_remove_element_one():
    nums_1 = [0, 1, 2, 2, 3, 0, 4, 2]
    val_1 = 2
    assert remove_element_one(nums_1, val_1) == 5

    nums_2 = [3, 2, 2, 3]
    val_2 = 2
    assert remove_element_one(nums_2, val_2) == 2
