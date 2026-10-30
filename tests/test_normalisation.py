
from asr_error_toolkit.normalisation import normalise_text

def test_case_normalisation():
    assert normalise_text("MOLO") == "molo"

def test_punctuation():
    assert normalise_text("Molo, unjani?") == "molo unjani"

def test_whitespace():
    assert normalise_text("  molo   unjani  ") == "molo unjani"

def test_empty_transcript():
    assert normalise_text("") == ""

def test_non_string_input():
    import pytest

    with pytest.raises(TypeError):
        normalise_text(None)