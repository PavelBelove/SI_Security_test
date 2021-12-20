"""Test of task2"""
import pytest
from scripts.task2 import calculate


@pytest.mark.parametrize('days, levels, bonus_list, max_bonus', [
    (3, 0, [6, 2, 1], 12),
    (3, 0, [2, 4, 8], 14),
    (3, 3, [6, 2, 1], 12),
    (3, 3, [2, 4, 8], 14),
    (3, 1, [2, 4, 8], 6),
    (5, 0, [2, 6, 3], 19),
    (4, 0, [2, 6, 5], 15),
    (1, 0, [10, 2, 3], 10),
    (10, 0, [1], 10),
])
def test_calculate_good(days, levels, bonus_list, max_bonus):
    """test_calculate_good"""
    assert calculate(days, levels, bonus_list) == max_bonus


@pytest.mark.parametrize('days, levels, bonus_list, max_bonus', [
    (3, 4, [6, 2, 1], 12),
])
def test_calculate_index_error(days, levels, bonus_list, max_bonus):
    """test_calculate_index_error"""
    with pytest.raises(IndexError):
        assert calculate(days, levels, bonus_list) == max_bonus


def test_calculate_value_error():
    """test_calculate_value_error"""
    with pytest.raises(TypeError):
        assert calculate(4, 3, [2, '6', 5])
        assert calculate('4', 3, [2, 5, 5])
        assert calculate(4, '3', [2, 5, 5])
