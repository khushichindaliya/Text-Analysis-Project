import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from mediawiki import MediaWiki

# Import functions from nobel_data_analysis.py
from nobel_data_analysis import (
    clean_text,
    word_frequencies,
    remove_stop_words,
    top_n_words,
)


def fetch_pages(titles):
    """
    Fetch a list of MediaWiki pages for the given list of titles and return a list of page objects fetched from Wikipedia.
    """
    wikipedia = MediaWiki()
    pages = []
    for title in titles:
        try:
            page = wikipedia.page(title)
            pages.append(page)
        except Exception as error:
            print(f"Error fetching page '{title}': {error}")
    return pages


def cosine_similarity(dict1, dict2):
    """
    Compute the cosine similarity between two word frequency dictionaries.
    """
    dot = 0
    for word in dict1:
        if word in dict2:
            dot += dict1[word] * dict2[word]
    norm1 = sum(value * value for value in dict1.values()) ** 0.5
    norm2 = sum(value * value for value in dict2.values()) ** 0.5
    if norm1 == 0 or norm2 == 0:
        return 0
    return dot / (norm1 * norm2)


def compute_similarity_matrix(pages, stop_words):
    """
    Compute a cosine similarity matrix for a list of pages using word frequencies. Each page's content is processed to compute word frequencies (with stop words removed).
    """
    freq_list = []
    for page in pages:
        freq = word_frequencies(page.content)
        filtered_freq = remove_stop_words(freq, stop_words)
        freq_list.append(filtered_freq)

    n = len(freq_list)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i, j] = cosine_similarity(freq_list[i], freq_list[j])
    return matrix


def plot_mds(titles, dissimilarity_matrix):
    """
    Compute a 2D embedding using MDS from the dissimilarity matrix and plot the results.
    """
    mds = MDS(dissimilarity="precomputed", random_state=42)
    coords = mds.fit_transform(dissimilarity_matrix)
    # MDS (Multidimensional Scaling) is a technique used to reduce the dimensions of data while preserving the distance (or dissimilarity) between points. dissimilarity='precomputed' tells MDS that you are providing a matrix of dissimilarities (not similarities). The transformation converts the dissimilarity matrix into 2D coordinates (coords), where each row represents a page's position in the 2D space.

    plt.figure()
    plt.scatter(
        coords[:, 0], coords[:, 1]
    )  # The x and y coordinates from coords are used to create a scatter plot, where each point corresponds to a page.
    for i, title in enumerate(titles):
        plt.annotate(
            title, (coords[i, 0], coords[i, 1])
        )  # Each point in the scatter plot is annotated with the corresponding page title.
    plt.title("Clustering of Nobel-related Wikipedia Pages")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.show()


def main():
    titles = [
        "Nobel Prize",
        "Nobel Prize in Physics",
        "Nobel Prize in Chemistry",
        "Nobel Peace Prize",
    ]

    pages = fetch_pages(titles)

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

    similarity_matrix = compute_similarity_matrix(pages, stop_words)

    # Convert similarity to dissimilarity for MDS (dissimilarity = 1 - similarity)
    dissimilarity_matrix = 1 - similarity_matrix

    plot_mds(titles, dissimilarity_matrix)


if __name__ == "__main__":
    main()
