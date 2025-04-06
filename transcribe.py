import whisper
import sys
import re
from spellchecker import SpellChecker

def correct_transcription(text):
    """Corrects common transcription errors."""

    # Remove filler words
    text = re.sub(r'\b(um|uh|like|you know)\b', '', text, flags=re.IGNORECASE)

    # Correct punctuation (basic)
    text = re.sub(r'\s+([.,?!])', r'\1', text)
    text = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', text)

    # Spell checking
    spell = SpellChecker()
    words = text.split()
    corrected_words = []
    for word in words:
        corrected_word = spell.correction(word)
        if corrected_word:
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)

    text = " ".join(corrected_words)

    # basic capitalization correction.
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    capitalized_sentences = [sentence.capitalize() for sentence in sentences]
    text = ' '.join(capitalized_sentences)

    return text

model = whisper.load_model("base")  # or "small", "medium", "large"

audio_file = sys.argv[1]

result = model.transcribe(audio_file)

corrected_text = correct_transcription(result["text"])

with open("/output/transcription.txt", "w") as f:
    f.write(corrected_text)