import pytest
import time
from datetime import datetime
from main import solution_slow, solution_fast


def start_measure():
    return datetime.now()


def stop_measure(start_time) -> float:
    total_time = datetime.now() - start_time
    return total_time.total_seconds()


def test_measure():
    start_time = start_measure()
    time.sleep(10)
    cyccle_time = stop_measure(start_time)

    assert round(cyccle_time, 1) == 10.00


class TestSlowSolution:
    """
    Test cases for solution.py base on email from Jana Derichova's:

    Například, pro pole A = [1, 3, 6, 4, 1, 2] by funkce měla vrátit 5.

    Pro pole A = [1, 2, 3] by měla funkce vrátit 4.

    Pro pole A = [-1, -3] by měla funkce vrátit 1.


    """

    def test_pos_nums_within_range(self):
        list_positive_nums = [1, 3, 6, 4, 1, 2]

        start_time = start_measure()
        actual = solution_slow(list_positive_nums)
        stop_time = stop_measure(start_time)
        expected = 5
        assert actual == expected

    def test_pos_nums_outside_initial_list(self):
        list_positive_nums = [1, 2, 3]
        actual = solution_slow(list_positive_nums)
        expected = 4

        assert actual == expected

    def test_neg_nums(self):
        nums = [-1, -3]
        actual = solution_slow(nums)
        expected = 1

        assert actual == expected

    def test_neg_inside_range(self):
        nums = [-100_000, -99_000, -100_00, -100_00, -100_00, 1]
        actual = solution_slow(nums)

        assert actual == 2

    def test_neg_ouside_range(self):
        nums = [-100_001, -99_000, -100_00, -100_00, -100_00, 1]
        with pytest.raises(Exception) as e:
            actual = solution_slow(nums)

        assert str(e.value) == "Input number is lower than the -100 000"

    def test_pos_ouside_range(self):
        nums = [100_001, 99_000, 100_00, 100_00, 100_00, 1]
        with pytest.raises(Exception) as e:
            actual = solution_slow(nums)

        assert str(e.value) == "Input number is higher than the 100 000"

    def test_large_dataset(self):
        nums = [i for i in range(100_000)]
        expected = nums.pop(-2)
        start_time = start_measure()
        actual = solution_slow(nums)
        stop_time = stop_measure(start_time)
        print(f"\nSlow Solution time: {stop_time}")
        assert actual == expected


class TestFastSolution:

    def test_pos_nums_within_range(self):
        list_positive_nums = [1, 3, 6, 4, 1, 2]

        start_time = start_measure()
        actual = solution_fast(list_positive_nums)
        stop_time = stop_measure(start_time)
        expected = 5
        assert actual == expected

    def test_pos_nums_outside_initial_list(self):
        list_positive_nums = [1, 2, 3]
        actual = solution_fast(list_positive_nums)
        expected = 4

        assert actual == expected

    def test_neg_nums(self):
        nums = [-1, -3]
        actual = solution_fast(nums)
        expected = 1

        assert actual == expected

    def test_neg_inside_range(self):
        nums = [-100_000, -99_000, -100_00, -100_00, -100_00, 1]
        actual = solution_fast(nums)

        assert actual == 2

    def test_neg_ouside_range(self):
        nums = [-100_001, -99_000, -100_00, -100_00, -100_00, 1]
        with pytest.raises(Exception) as e:
            actual = solution_fast(nums)

        assert str(e.value) == "Input number is lower than the -100 000"

    def test_pos_ouside_range(self):
        nums = [100_001, 99_000, 100_00, 100_00, 100_00, 1]
        with pytest.raises(Exception) as e:
            actual = solution_fast(nums)

        assert str(e.value) == "Input number is higher than the 100 000"

    def test_large_dataset_fastest(self):
        nums = [i for i in range(-100_000, 100_000)]
        expected = nums.pop(-2)
        start_time = start_measure()
        actual = solution_fast(nums)
        stop_time = stop_measure(start_time)
        print(f"\nFast Solution time: {stop_time}")
        assert actual == expected
