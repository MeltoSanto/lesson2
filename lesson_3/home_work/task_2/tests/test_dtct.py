import pytest
from lesson_3.home_work.task_2.func import dtct

def test_dtct():
    assert  type(dtct(txt='Привет, как тебя зовут?')) == str
    with pytest.raises(Exception):
        dtct(112314141)