from jiwer import wer, cer
from .normalisation import normalise_text


def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculate the Word Error Rate (WER)
    between a reference and hypothesis transcript.
    """
    reference = normalise_text(reference)
    hypothesis = normalise_text(hypothesis)

    if not reference:
        raise ValueError("Reference cannot be empty when calculating WER.")
    
    return wer(reference, hypothesis)


def calculate_cer(reference: str, hypothesis: str) -> float:
    """
    Calculate the Character Error Rate (CER)
    between a reference and hypothesis transcript.
    """
    reference = normalise_text(reference)
    hypothesis = normalise_text(hypothesis)

    if not reference:
        raise ValueError("Reference cannot be empty when calculating CER.")
    
    return cer(reference, hypothesis)