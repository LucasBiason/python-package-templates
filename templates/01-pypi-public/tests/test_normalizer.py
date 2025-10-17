"""Tests for text_normalizer package."""

import pytest
from text_normalizer import normalize_text, remove_accents, remove_extra_whitespace


def test_remove_accents():
    assert remove_accents("café") == "cafe"
    assert remove_accents("Müller") == "Muller"
    assert remove_accents("São Paulo") == "Sao Paulo"


def test_remove_accents_type_error():
    with pytest.raises(TypeError):
        remove_accents(123)


def test_remove_extra_whitespace():
    assert remove_extra_whitespace("  hello   world  ") == "hello world"
    assert remove_extra_whitespace("test") == "test"


def test_normalize_text():
    assert normalize_text("  Café   Münich  ") == "cafe munich"
    assert normalize_text("  Café   Münich  ", lowercase=False) == "Cafe Munich"


def test_normalize_text_type_error():
    with pytest.raises(TypeError):
        normalize_text(None)
