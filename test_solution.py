from main import solution

class TestSolution:
    """
    Test cases for solution.py base on email from Jana Derichova's:

    Například, pro pole A = [1, 3, 6, 4, 1, 2] by funkce měla vrátit 5.

    Pro pole A = [1, 2, 3] by měla funkce vrátit 4.

    Pro pole A = [-1, -3] by měla funkce vrátit 1.


    """
    def test_pos_nums_within_range(self):
        list_positive_nums = [1,3,6,4,1,2]

        actual = solution(list_positive_nums)
        expected = 5

        assert actual == expected

    def test_pos_nums_outside_range(self):
        list_positive_nums = [1, 2, 3]
        actual = solution(list_positive_nums)
        expected = 4

        assert actual == expected

    def test_neg_nums(self):
        nums = [-1, -3]
        actual = solution(nums)
        expected = 1

        assert actual == expected
