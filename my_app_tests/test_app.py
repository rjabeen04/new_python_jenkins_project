from my_app.app import add

def test_add():
    # two simple assertions
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
