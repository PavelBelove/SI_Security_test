"""Test of task1"""
import pytest
from scripts.task1 import analyse, ACTION_ACCEPT, ACTION_UNLOAD


test_conveyor = [5, 6, 7, 8, 9, 10]
program_1 = [
    (ACTION_ACCEPT, 46),
    (ACTION_UNLOAD, 46),
    (ACTION_ACCEPT, 21),
    (ACTION_UNLOAD, 21),
]
program_2 = [
    (ACTION_ACCEPT, 1),
    (ACTION_ACCEPT, 2),
    (ACTION_UNLOAD, 1),
    (ACTION_ACCEPT, 3),
    (ACTION_ACCEPT, 4),
    (ACTION_UNLOAD, 3),
]

use_conveyor_program = [
    (ACTION_ACCEPT, 1),
    (ACTION_ACCEPT, 2),
    (ACTION_UNLOAD, 10),
    (ACTION_UNLOAD, 1),
    (ACTION_ACCEPT, 3),
    (ACTION_ACCEPT, 4),
    (ACTION_UNLOAD, 3),
]

unloading_the_penultimate_program = [
    (ACTION_UNLOAD, 9),
]

unloading_the_last = [
    (ACTION_UNLOAD, 10),
]


good_test_list_filled_conveyor = [
    (program_1, test_conveyor, 4),
    (program_2, test_conveyor, 6),
    (use_conveyor_program, test_conveyor, 9),
    (unloading_the_last, test_conveyor, 1),
    (unloading_the_penultimate_program, test_conveyor, 3),
]

good_test_list_empty_conveyor = [
    (program_1, 4),
    (program_2, 6),
]


@pytest.mark.parametrize('program, conveyor, expected_result', good_test_list_filled_conveyor)
def test_analyse_filled_conveyor(program, conveyor, expected_result):
    """test_analyse_filled_conveyor"""
    assert analyse(program, conveyor) == expected_result


@pytest.mark.parametrize('program, expected_result', good_test_list_empty_conveyor)
def test_analyse_empty_conveyor(program, expected_result):
    """test_analyse_empty_conveyor"""
    assert analyse(program) == expected_result


def test_analyse_empty_program():
    """test_analyse_empty_program"""
    assert analyse([]) == 0
    assert analyse([], test_conveyor) == 0


def test_analyse_missing_number():
    """test_analyse_empty_program"""
    with pytest.raises(ValueError):
        assert analyse([(ACTION_UNLOAD, 1)], test_conveyor)


def test_analyse_wrong_command():
    """test_analyse_empty_program"""
    with pytest.raises(AssertionError):
        assert analyse([('', 10)], test_conveyor)
