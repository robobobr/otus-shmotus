"""Module docstring: tests shmests"""

LIST_ONE = [1, 2, 3, 4, 5]
TUPLE_ONE = ("ow", 3, "ned")
STRING_ONE = "wtf"
STRING_TWO = "bbq"
SET_ONE = set('So far so good')

DICT_ONE = {
    "key1":1,
    "key2":"two"
}

def multipulti(int1, int2):
    """multiplication in a custom function, spiffy!"""
    return int(int1) * int(int2)

##################################

##################################

def test_1(run_at_startup):
    """
    Testing the length of predetermined list and running some starting procedures
    """
    assert len(LIST_ONE) == 5
    print(run_at_startup)

def test_2():
    """
    Testing string concatenation
    """
    assert STRING_ONE + STRING_TWO == "wtfbbq"

def test_3():
    """
    Testing a value in a dictionary
    """
    assert DICT_ONE["key1"] > 0

def test_4():
    """
    Testing a value in a dictionary
    """
    assert "two" in DICT_ONE.values()

def test_5():
    """
    Testing a key in a dictionary
    """
    assert "key1" in DICT_ONE.keys()

def test_6():
    """
    Testing a function
    """
    assert multipulti(2, 2) == 4

def test_7():
    """
    Testing tuple's length
    """
    assert len(TUPLE_ONE) == 3

def test_8():
    """
    Testing tuple's content
    """
    assert "lol" not in TUPLE_ONE

def test_9():
    """
    Testing set's content
    """
    assert 'g' in SET_ONE

def test_10():
    """
    Testing set's length
    """
    assert len(SET_ONE) == 9
