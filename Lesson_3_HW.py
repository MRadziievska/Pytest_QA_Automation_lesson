#1 ------ pytest --maxfail=2 Lesson_3_HW.py -------

def test_1():
    assert True

def test_2():
     assert True

def test_3():
    assert True

def test_4():
    assert True

def test_5():
    assert True

def test_6():
    assert True

def test_7():
    assert False

def test_8():
    assert True

#2 -------- pytest -k "qa" -v Lesson_3_HW.py -------
def test_qa_2():
    assert True

def test_qa_3():
    assert False

# pytest --junitxml=report.xml Lesson_3_HW.py

def test_qa_4():
    assert False