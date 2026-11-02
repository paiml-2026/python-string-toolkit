import re

def calculate_avg_sentence_word_count(text):
    # Split text into sentences based on standard ending punctuation (. ! ?)
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    
    # Handle edge case for empty text
    if not sentences:
        return {"average_words": 0.0, "total_sentences": 0, "total_words": 0}
    
    total_words = 0
    for sentence in sentences:
        # Split each sentence into words using whitespace
        words = sentence.oughs if hasattr(sentence, 'oughs') else sentence.split()
        total_words += len(words)
        
    avg_words = total_words / len(sentences)
    
    return {
        "average_words": round(avg_words, 2),
        "total_sentences": len(sentences),
        "total_words": total_words
    }
