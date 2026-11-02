# ASR Error Toolkit
[![codecov](https://codecov.io/gh/nokuthabam/asr-error-toolkit/graph/badge.svg?token=62XFXXU1WE)](https://codecov.io/gh/nokuthabam/asr-error-toolkit)

A lightweight Python toolkit for evaluating Automatic Speech Recognition (ASR) output through transcript normalisation, Word Error Rate (WER), Character Error Rate (CER), and word-level error alignment.

The project aims to make ASR evaluation more transparent by helping developers and researchers understand not only how accurately a model transcribes speech, but also where recognition errors occur.

It is particularly motivated by research into low-resource African languages, although the toolkit is designed for general ASR evaluation.

## Features

The toolkit currently supports:

* **Transcript normalisation:** Unicode NFC normalisation, case folding, punctuation handling, and whitespace standardisation.
* **Word Error Rate (WER):** Calculates word-level transcription error rates.
* **Character Error Rate (CER):** Calculates character-level transcription error rates.
* **Word alignment:** Identifies correct matches, substitutions, deletions, and insertions using JiWER.
* **Automated testing:** Unit tests developed with pytest.
* **Continuous integration:** Automated testing through GitHub Actions.
* **Code coverage:** Coverage reporting using pytest-cov.

Multiword substitution spans are currently represented as grouped entries rather than individual word substitutions.

## Technology Stack

* Python 3.12
* JiWER
* pytest
* pytest-cov
* GitHub Actions

## Project Structure

```text
asr-error-toolkit/
├── .github/
│   └── workflows/
│       └── tests.yml
├── asr_error_toolkit/
│   ├── __init__.py
│   ├── normalisation.py
│   ├── metrics.py
│   └── alignment.py
├── tests/
│   ├── test_normalisation.py
│   ├── test_metrics.py
│   └── test_alignment.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/nokuthabam/asr-error-toolkit.git
cd asr-error-toolkit
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Python 3.12 is the development and testing version.

## Usage

### 1. Transcript Normalisation

Normalise transcripts before evaluation:

```python
from asr_error_toolkit.normalisation import normalise_text

text = "Molo, UNJANI?"

normalised = normalise_text(text)

print(normalised)
```

Output:

```text
molo unjani
```

### 2. Word Error Rate

Calculate WER between a reference transcript and an ASR prediction:

```python
from asr_error_toolkit.metrics import calculate_wer

reference = "molo unjani"
hypothesis = "molo njani"

score = calculate_wer(reference, hypothesis)

print(f"WER: {score:.2%}")
```

Output:

```text
WER: 50.00%
```

WER is calculated as:

$$
WER = \frac{S + D + I}{N}
$$

Where:

* **S:** Substitutions
* **D:** Deletions
* **I:** Insertions
* **N:** Number of words in the reference transcript

### 3. Character Error Rate

Calculate character-level transcription errors:

```python
from asr_error_toolkit.metrics import calculate_cer

reference = "molo"
hypothesis = "mola"

score = calculate_cer(reference, hypothesis)

print(f"CER: {score:.2%}")
```

Output:

```text
CER: 25.00%
```

### 4. Word-Level Error Alignment

Inspect the differences between reference and predicted transcripts:

```python
from asr_error_toolkit.alignment import align_transcripts

reference = "molo unjani namhlanje"
hypothesis = "molo namhlanje"

results = align_transcripts(reference, hypothesis)

for result in results:
    print(result)
```

Output:

```python
{'reference': 'molo', 'hypothesis': 'molo', 'operation': 'equal'}
{'reference': 'unjani', 'hypothesis': '', 'operation': 'delete'}
{'reference': 'namhlanje', 'hypothesis': 'namhlanje', 'operation': 'equal'}
```

The supported alignment operations are:

| Operation    | Description                                      |
| ------------ | ------------------------------------------------ |
| `equal`      | Reference and hypothesis tokens match.           |
| `substitute` | The hypothesis contains different text.          |
| `delete`     | A reference word is missing from the hypothesis. |
| `insert`     | The hypothesis contains an additional word.      |

## Running Tests

Run the complete test suite:

```bash
python -m pytest -v
```

Generate a test coverage report:

```bash
python -m pytest --cov=asr_error_toolkit --cov-report=term-missing
```

The GitHub Actions workflow also runs automated tests when changes are pushed or pull requests are opened.

## Current Limitations

* The toolkit currently evaluates individual reference–hypothesis pairs rather than complete datasets.
* Transcript normalisation follows a fixed policy rather than configurable language-specific rules.
* Multiword substitutions are grouped into alignment spans.
* Empty reference transcripts are rejected.
* CSV input, batch evaluation, and report generation are not yet implemented.

## Planned Improvements

Future development may include:

* CSV-based transcript evaluation.
* Batch WER and CER calculation.
* Detailed error reports and CSV exports.
* Configurable text normalisation.
* Corpus-level evaluation.
* Phonetic error analysis.
* Visualisation of recurring recognition errors.

## Research Motivation

This toolkit is inspired by ongoing research into automatic speech recognition for low-resource African languages, particularly the Nguni language family.

ASR evaluation commonly relies on aggregate metrics such as WER and CER. Although useful, these metrics do not independently explain the linguistic or phonetic patterns underlying recognition errors.

By combining error metrics with transcript alignment and, eventually, phonetic analysis, the project aims to support more detailed investigations into ASR performance.

The toolkit is developed independently of private research repositories and does not contain restricted research datasets or model weights.

## Project Status

**Active development — early version**

Core transcript normalisation, WER/CER evaluation, and basic word alignment have been implemented.

Additional evaluation and reporting capabilities are planned.
