from assignment_1.task_1 import find_median_sorted_arrays
from assignment_1.task_1 import reverse
from assignment_1.task_1 import max_area
from assignment_1.task_1 import count_digit_one


def test_find_median_sorted_arrays():
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2.00000

    nums3 = [1, 2] 
    nums4 = [3, 4]
    assert find_median_sorted_arrays(nums3, nums4) == 2.50000


def test_reverse():
    test_case_1 = 123
    test_case_2 = -123
    test_case_3 = 120

    assert reverse(test_case_1) == 321
    assert reverse(test_case_2) == -321
    assert reverse(test_case_3) == 21


def test_max_area():
    test_height_1 = [1, 1]
    test_height_2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    assert max_area(test_height_1) == 1
    assert max_area(test_height_2) == 49


def test_count_digit_one():
    test_case_1 = 13
    test_case_2 = 0

    assert count_digit_one(test_case_1) == 6
    assert count_digit_one(test_case_2) == 0
