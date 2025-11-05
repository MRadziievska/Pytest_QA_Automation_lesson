

def test_1():   # pytest -v Lesson_3.py
    assert True

def test_2():
     assert True

def test_3():
    assert True

def test_4():
    assert True

def test_5():   # pytest -q Lesson_3.py
    assert True

def test_6():
    assert True

def test_7():   # pytest -qq Lesson_3.py
    assert False

def test_8():
    assert True

def test_qa_2():  # pytest -k "qa" -v Lesson_3.py
    assert True

def test_qa_3():   # pytest --ff Lesson_3.py
    assert False

# pytest --junitxml=report.xml Lesson_3.py

def test_qa_4():  # pytest --maxfail=2 Lesson_3.py
    assert False

def test_qa_6():
    time.sleep(1)  # pytest --durations=2 -vv Lesson_3.py
    assert True