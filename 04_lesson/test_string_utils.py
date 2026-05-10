import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Dekstop", "Dekstop"),
    ("  Twitch", "Twitch"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Dekstop", "Dekstop"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Dekstop", "D", True),
    ("Twitch", "o", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Dekstop", "l", True),
    ("Twitch", "i", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Dekstop", "D", "ekstop"),
    ("Twitch", "i", "Twtch"),
])
def test_delete_positiv(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Dekstop", "D", "dekstop"),
    ("Twitch", "i", "Twitch"),
])
def test_delete_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
