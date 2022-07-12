import pytest

from lesson_4.home_work.task_1.func import q_a

def test_qa_pos():
    assert q_a(1, 2, 5) == None

def test_qa_neg():
    with pytest.raises(Exception):
        q_a("a", "b", "c")