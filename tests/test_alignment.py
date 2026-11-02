import pytest

from asr_error_toolkit.alignment import align_transcripts

def test_align_transcripts():
    reference = "molo unjani namhlanje"
    hypothesis = "molo njani namhlanje"
    expected_output = [
        {"reference": "molo", "hypothesis": "molo", "operation": "equal"},
        {"reference": "unjani", "hypothesis": "njani", "operation": "substitute"},
        {"reference": "namhlanje", "hypothesis": "namhlanje", "operation": "equal"}
    ]
    assert align_transcripts(reference, hypothesis) == expected_output

def test_delete_operation():
    reference = "molo unjani namhlanje"
    hypothesis = "molo namhlanje"
    expected_output = [
        {"reference": "molo", "hypothesis": "molo", "operation": "equal"},
        {"reference": "unjani", "hypothesis": "", "operation": "delete"},
        {"reference": "namhlanje", "hypothesis": "namhlanje", "operation": "equal"}
    ]
    assert align_transcripts(reference, hypothesis) == expected_output

def test_insert_operation():
    reference = "molo unjani"
    hypothesis = "molo enkosi unjani"

    expected_output = [
        {"reference": "molo", "hypothesis": "molo", "operation": "equal"},
        {"reference": "", "hypothesis": "enkosi", "operation": "insert"},
        {"reference": "unjani", "hypothesis": "unjani", "operation": "equal"}
    ]

    assert align_transcripts(reference, hypothesis) == expected_output

def test_multiple_equal_words():
    reference = "molo unjani namhlanje"
    hypothesis = "molo unjani namhlanje"

    expected_output = [
        {"reference": "molo", "hypothesis": "molo", "operation": "equal"},
        {"reference": "unjani", "hypothesis": "unjani", "operation": "equal"},
        {"reference": "namhlanje", "hypothesis": "namhlanje", "operation": "equal"}
    ]

    assert align_transcripts(reference, hypothesis) == expected_output