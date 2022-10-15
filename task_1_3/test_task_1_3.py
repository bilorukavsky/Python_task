from task_1_3 import single_number

def test_single_number():
    nums_1 = [1]
    assert single_number(nums_1) == 1

    nums_2 = [2, 2, 3]
    assert single_number(nums_2) == 3

    nums_3 = [4, 1, 2, 1, 2]
    assert single_number(nums_3) == 4
    
