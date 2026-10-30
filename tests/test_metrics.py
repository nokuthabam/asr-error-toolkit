import pytest

from asr_error_toolkit.metrics import calculate_wer, calculate_cer


def test_perfect_prediction():
    assert calculate_wer("molo unjani", "molo unjani") == 0.0


def test_word_substitution():
    assert calculate_wer("molo unjani", "molo enkosi") == 0.5


def test_character_error():
    assert calculate_cer("molo", "mola") == 0.25


def test_normalisation():
    assert calculate_wer("MOLO, UNJANI?", "molo unjani") == 0.0


def test_empty_reference():
    with pytest.raises(ValueError):
        calculate_wer("", "molo")


def test_empty_hypothesis():
    assert calculate_wer("molo", "") == 1.0

