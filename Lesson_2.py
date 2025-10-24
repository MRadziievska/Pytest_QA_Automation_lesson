# запускаем тесты через терминал: pytest -v Lesson_2.py

import pytest

@pytest.mark.smoke
def test_1():
    print("hello")
    assert True

@pytest.mark.regression #pytest -m "smoke or regression" -v Lesson_2.py
def test_2():
    assert True

@pytest.mark.regression
def test_3():
    assert True

@pytest.mark.smoke
@pytest.mark.regression   # pytest -m "smoke and regression" -v Lesson_2.py
def test_4():
    assert True

def test_5():  # pytest -m "not regression" -v Lesson_2.py
    assert True

@pytest.mark.regression
def test_6():
    assert True

def test_7():
    assert True

def test_8():
    assert True

@pytest.mark.smoke  # pytest -m "not regression" -v Lesson_2.py
def test_9():
    assert True

def test_10():
    assert True

