import jiwer
from .normalisation import normalise_text

def align_transcripts(reference: str, hypothesis: str) -> list[dict]:
    """
    Align reference and hypothesis transcripts.

    Returns a list of dictionaries containing reference tokens,
    hypothesis tokens, and their corresponding edit operations.
    Multiword substitutions are grouped into a single entry.
"""
    output = []
    reference = normalise_text(reference)

    if not reference:
        raise ValueError("Reference cannot be empty when aligning transcripts.")
    if not hypothesis:
        raise ValueError("Hypothesis cannot be empty when aligning transcripts.")
    result = jiwer.process_words(reference, hypothesis)
    reference_words = result.references[0]
    hypothesis_words = result.hypotheses[0]
    for chunk in result.alignments[0]:
        operation = chunk.type
        ref_tokens = reference_words[chunk.ref_start_idx: chunk.ref_end_idx]
        hype_tokens = hypothesis_words[chunk.hyp_start_idx: chunk.hyp_end_idx]
        if operation == 'equal':
            for ref, hyp in zip(ref_tokens, hype_tokens):
                info = {
                    "reference": ref,
                    "hypothesis": hyp,
                    "operation": operation
                }
                output.append(info)

        elif operation == 'delete':
            for ref in ref_tokens:
                info = {
                        "reference": ref,
                        "hypothesis": "",
                        "operation": operation
                    }
                output.append(info)
        elif operation == 'insert':
            for hyp in hype_tokens:
                info = {
                    "reference": "",
                    "hypothesis": hyp,
                    "operation": operation
                }
                output.append(info)
        else:
            info = {
                "reference": " ".join(ref_tokens),
                "hypothesis": " ".join(hype_tokens),
                "operation": operation
            }
            output.append(info)
        
    return output


if __name__ == "__main__":
    reference = "molo unjani namhlanje"
    hypothesis = "molo namhlanje"

    print(align_transcripts(reference, hypothesis))