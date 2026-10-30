import re
import unicodedata


def normalise_text(text: str) -> str:
    """Normalise a transcript for ASR evaluation."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    text = unicodedata.normalize("NFKC", text)  # Normalize unicode characters
    text = text.casefold()  # Convert to lowercase

    # Remove punctuation while preserving word characters
    text = "".join(
        " " if unicodedata.category(char).startswith("P") else char
        for char in text
    )

    # Remove repeated whitespace
    return re.sub(r"\s+", " ", text).strip()

