"""
Core text normalization functions.

This module provides the main text normalization functionality including
accent removal, whitespace cleanup, and case conversion.
"""

import re
import unicodedata


def remove_accents(text: str) -> str:
    """
    Remove accents from text.

    Args:
        text: Input text with potential accents

    Returns:
        Text with accents removed

    Example:
        >>> remove_accents("café")
        'cafe'
        >>> remove_accents("Müller")
        'Muller'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    nfd_form = unicodedata.normalize("NFD", text)
    return "".join(char for char in nfd_form if unicodedata.category(char) != "Mn")


def remove_extra_whitespace(text: str) -> str:
    """
    Remove extra whitespace from text.

    This function removes leading/trailing whitespace and reduces multiple
    consecutive spaces to a single space.

    Args:
        text: Input text with potential extra whitespace

    Returns:
        Text with normalized whitespace

    Example:
        >>> remove_extra_whitespace("  hello   world  ")
        'hello world'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    text = text.strip()
    return re.sub(r"\s+", " ", text)


def normalize_text(text: str, lowercase: bool = True) -> str:
    """
    Normalize text by removing accents, extra whitespace, and optionally converting to lowercase.

    This is the main normalization function that combines multiple operations.

    Args:
        text: Input text to normalize
        lowercase: Whether to convert text to lowercase (default: True)

    Returns:
        Normalized text

    Example:
        >>> normalize_text("  Café   Münich  ")
        'cafe munich'
        >>> normalize_text("  Café   Münich  ", lowercase=False)
        'Cafe Munich'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    text = remove_accents(text)
    text = remove_extra_whitespace(text)

    if lowercase:
        text = text.lower()

    return text

