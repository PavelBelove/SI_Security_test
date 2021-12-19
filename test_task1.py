import pytest
from task1 import analyse

conveyor = [5, 6, 7, 8, 9, 10]
program_1 = [
        ('принять', 46),
        ('выгрузить', 46),
        ('принять', 21),
        ('выгрузить', 21),
        ]
program_2 = [
        ('принять', 1),
        ('принять', 2),
        ('выгрузить', 1),
        ('принять', 3),
        ('принять', 4),
        ('выгрузить', 3),
        ]

use_conveyor_program = [
        ('принять', 1),
        ('принять', 2),
        ('выгрузить', 10),
        ('выгрузить', 1),
        ('принять', 3),
        ('принять', 4),
        ('выгрузить', 3),
]

unloading_the_penultimate_program = [
        ('выгрузить', 9),
]

unloading_the_last = [
        ('выгрузить', 10),
]



good_test_list_filled_conveyor = [
        (program_1, conveyor, 4),
        (program_2, conveyor, 6),
        (use_conveyor_program, conveyor, 9),
        (unloading_the_last, conveyor, 1),
        (unloading_the_penultimate_program, conveyor, 3),
]

good_test_list_empty_conveyor = [
        (program_1, 4),
        (program_2, 6),

]

@pytest.mark.parametrize('program, conveyor,  expected_result', good_test_list_filled_conveyor)
def test_analyse_filled_conveyor(program, conveyor,  expected_result): 
    assert analyse(program, conveyor) == expected_result

@pytest.mark.parametrize('program,  expected_result', good_test_list_empty_conveyor)
def test_analyse_empty_conveyor(program,  expected_result): 
    assert analyse(program) == expected_result

def test_analyse_empty_program(): 
    assert analyse([]) == 0
    assert analyse([], conveyor) == 0

def test_analyse_missing_number(): 
        with pytest.raises(ValueError):
                assert analyse([('выгрузить', 1)], conveyor) 

def test_analyse_wrong_command(): 
        with pytest.raises(AssertionError):
                assert analyse([('', 10)], conveyor) 
