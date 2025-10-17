"""
Text Normalizer - Simple text normalization utilities.

This package provides utilities for normalizing text by removing accents,
extra whitespace, and converting to lowercase.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .normalizer import normalize_text, remove_accents, remove_extra_whitespace

__all__ = [
    "normalize_text",
    "remove_accents",
    "remove_extra_whitespace",
]

