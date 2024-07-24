import pytest
from string_utils import StringUtils

utils = StringUtils

# Capitilize
def test_capitilize():
    # Позитив
    assert utils.capitilize("volgograd") == "Volgograd"
    assert utils.capitilize("hello") == "Hello"
    assert utils.capitilize("москва") == "Москва"
    # Негатив
    assert utils.capitilize("") == ""
    assert utils.capitilize("   ") == "    "
    assert utils.capitilize("12345LOL") == "12345LOL"

# Trim
def test_trim():
    # Позитив
    assert utils.trim(" Volgograd") == "Volgograd"
    assert utils.trim(" Hello   ") == "Hello    "
    assert utils.trim(" Москва  ") == "Москва   "
    # Негатив
    assert utils.trim("") == ""

@pytest.mark.xfail()
def test_trim_numbers():
    assert utils.trim("55555") == "55555"

@pytest.mark.xfail()
def test_trim_srt_non():
    assert utils.trim(" LOL ") == " LOL "

# To_list
@pytest.mark.parametrize("string, delimeter, result", [
    # Positive
    ("один,два,три,четыре", ",", ["один", "два", "три", "четыре"]),
    ("1@2@3@4@5", "@", ["1", "2", "3", "4", "5"]),
    ("123,456,789,101112", ",", ["123", "456", "789", "101112"]),
    # Negative
    ("", None, []),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
        assert res == result

# Contains
@pytest.mark.parametrize("string, simbol, result", [
("Love", "v", True),
("Love", "L", True),
("Homwork", "k", True),
("Волгоград", "г", True),
("Автомобиль", "А", True),
("ИЫШРСИШаывААЫ", "Ы", True),
("Love", "Z", False),
("Kids", "J", False),
("sgsIrgoserpo", "Ы", False),
])
def test_contains(string, simbol, result):
    res = utils.contains(string, simbol)
    assert res == result

# Delete_symbol
@pytest.mark.parametrize("string, simbol, result", [
("Love", "v", "Loe"),
("Love", "L", "ove"),
("Homwork", "k", "Homwor"),
("Волгоград", "г", "Волорад"),
("Автомобиль", "А", "втомобиль"),
("ИЫШРСИШаывААЫ", "Ы", "ИШРСИШаывАА"),
("Love", "Z", "Love"),
("Kids", "J", "Kids"),
("sgsIrgoserpo", "Ы", "sgsIrgoserpo"),
])
def test_delete_symbol(string, simbol, result):
    res = utils.delete_symbol(string, simbol)
    assert res == result

# Starts_with
@pytest.mark.parametrize("string, simbol, result", [
("Love", "L", True),
("Love", "L", True),
("Homwork", "H", True),
("Волгоград", "В", True),
("Автомобиль", "А", True),
("ИЫШРСИШаывААЫ", "И", True),
("Love", "Z", False),
("Kids", "J", False),
("sgsIrgoserpo", "Ы", False),
])
def test_starts_with(string, simbol, result):
    res = utils.starts_with(string, simbol)
    assert res == result

# End_with
@pytest.mark.parametrize("string, simbol, result", [
("Love", "e", True),
("Love", "L", False),
("Homwork", "k", True),
("Волгоград", "д", True),
("Автомобиль", "ь", True),
("ИЫШРСИШаывААЫ", "Ы", True),
("Love", "Z", False),
("Kids", "J", False),
("sgsIrgoserpo", "Ы", False),
])
def test_end_with(string, simbol, result):
    res = utils.end_with(string, simbol)
    assert res == result

# Is_empty
@pytest.mark.parametrize("string, result", [
("",  True),
("Love", False),
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result


# List_to_string
@pytest.mark.parametrize("lst, joiner, result", [
    # Positive
    (["один", "два", "три", "четыре"], ",", "один,два,три,четыре" ),
    (["1", "2", "3", "4", "5"], "1@2@3@4@5",  "@")
])
def test_list_to_string(lst, joiner, result):
    if joiner is None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result