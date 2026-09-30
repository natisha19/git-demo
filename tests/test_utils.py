"""Tests for the utility functions."""

from datetime import date

import pytest

from src.utils import (
    add,
    calculate_age,
    format_date,
    greet,
    multiply,
    subtract,
)

INVALID_NAME_MESSAGE = "Name must be a non-empty string"


class TestGreet:
    """Tests for greet()."""

    def test_returns_greeting_message_with_name(self):
        assert greet("Alice") == "Hello, Alice! Welcome to the Git workshop!"

    def test_raises_for_empty_name(self):
        with pytest.raises(ValueError, match=INVALID_NAME_MESSAGE):
            greet("")

    def test_raises_for_non_string_input(self):
        with pytest.raises(TypeError, match=INVALID_NAME_MESSAGE):
            greet(123)


class TestCalculateAge:
    """Tests for calculate_age()."""

    def test_calculates_age_correctly(self):
        assert calculate_age(date.today().year - 25) == 25

    def test_raises_for_future_birth_year(self):
        with pytest.raises(ValueError, match="Birth year cannot be in the future"):
            calculate_age(date.today().year + 1)

    def test_raises_for_non_number_input(self):
        with pytest.raises(TypeError, match="Birth year must be a number"):
            calculate_age("1990")

    def test_raises_for_boolean_input(self):
        with pytest.raises(TypeError, match="Birth year must be a number"):
            calculate_age(True)

    def test_raises_for_non_positive_birth_year(self):
        with pytest.raises(ValueError, match="Birth year must be a positive number"):
            calculate_age(0)


class TestFormatDate:
    """Tests for format_date()."""

    def test_formats_date_correctly(self):
        assert format_date(date(2024, 1, 15)) == "January 15, 2024"

    def test_formats_date_without_ambiguous_suffix(self):
        assert format_date(date(2024, 3, 1)) == "March 1, 2024"

    def test_raises_for_non_date_input(self):
        with pytest.raises(TypeError, match="Input must be a date object"):
            format_date("2024-01-15")


class TestAdd:
    """Tests for add()."""

    def test_adds_two_numbers_correctly(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0


class TestSubtract:
    """Tests for subtract()."""

    def test_subtracts_two_numbers_correctly(self):
        assert subtract(5, 3) == 2
        assert subtract(1, 1) == 0
        assert subtract(0, 5) == -5


class TestMultiply:
    """Tests for multiply()."""

    def test_multiplies_two_numbers_correctly(self):
        assert multiply(2, 3) == 6
        assert multiply(-2, 4) == -8
        assert multiply(0, 5) == 0

    def test_multiplies_floats(self):
        assert multiply(1.5, 2) == 3.0

    def test_raises_for_non_number_input(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("2", 3)

    def test_raises_for_second_argument_non_number(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(2, None)
