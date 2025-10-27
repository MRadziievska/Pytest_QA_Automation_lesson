import pytest

@pytest.mark.smoke # Additional Arguments - -m "retest or smoke" -v
def test_1():
    print("hello")
    assert True

@pytest.mark.regression  # pytest -m "regression" -v Lesson_2_HW.py
def test_2():
    assert True

@pytest.mark.regression
def test_3():
    assert True

@pytest.mark.smoke
@pytest.mark.regression
def test_4():
    assert True

def test_5():
    assert True

@pytest.mark.regression
def test_6():
    assert True
@pytest.mark.retest
def test_7():
    assert True

@pytest.mark.retest
def test_8():
    assert True

@pytest.mark.retest
@pytest.mark.smoke
def test_9():
    assert True

def test_10():
    assert True