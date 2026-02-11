import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def summarize(text, ratio=0.3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    freq = defaultdict(int)
    for w in words:
        if w.isalnum() and w not in stop_words:
            freq[w] += 1

    sentences = sent_tokenize(text)
    sentence_scores = {}

    for sent in sentences:
        for w in word_tokenize(sent.lower()):
            if w in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[w]

    summary_len = max(1, int(len(sentences) * ratio))
    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:summary_len]

    return " ".join(summary)


if __name__ == "__main__":
    text = """
    Artificial intelligence is transforming many industries.
    It enables machines to learn from data and make decisions.
    Natural language processing is a branch of AI focused on text.
    Summarization helps extract key information from large documents.
    """

    print("\n--- Summary ---\n")
    print(summarize(text))

