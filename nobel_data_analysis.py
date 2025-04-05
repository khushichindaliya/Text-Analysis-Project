from mediawiki import MediaWiki


def clean_text(text):
    """
    Convert text to lowercase and remove punctuation by keeping only alphanumeric characters and whitespace.
    """
    text = text.lower()
    cleaned = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned += char
    return cleaned


def word_frequencies(text):
    """
    Uses the cleaned text into split words and counts the frequency of each word.
    """
    cleaned = clean_text(text)
    words = cleaned.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def remove_stop_words(freq, stop_words):
    """
    Removes stop words from the frequency dictionary.
    """
    filtered_freq = {}
    for word in freq:
        if word not in stop_words:
            filtered_freq[word] = freq[word]
    return filtered_freq


def top_n_words(dictionary, n):
    """
    Finds the top n words by frequency from a dictionary.
    """
    sorted_words = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]


def main():
    wikipedia = MediaWiki()
    nobel = wikipedia.page("Nobel Prize")

    # Compute word frequencies.
    frequency = word_frequencies(nobel.content)
    print("Total unique words:", len(frequency))

    stop_words = {
        "the",
        "and",
        "a",
        "an",
        "in",
        "of",
        "to",
        "is",
        "it",
        "for",
        "on",
        "that",
        "this",
        "with",
        "as",
        "by",
        "at",
        "be",
        "are",
        "was",
        "were",
        "but",
        "or",
        "if",
        "so",
        "not",
        "too",
    }

    filtered_frequency = remove_stop_words(frequency, stop_words)

    top_words = top_n_words(filtered_frequency, 10)
    print("Top 10 words are:")
    for word, count in top_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
