from mediawiki import MediaWiki
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment_analysis(snippet):
    """Conducting sentinment analysis on any piece of text"""
    score = SentimentIntensityAnalyzer().polarity_scores(snippet)
    return score


def main():
    wikipedia = MediaWiki()
    nobel = wikipedia.page("Nobel Prize")

    print("\nSentiment scores for the Wikipedia page on nobel prizes is:")
    print(sentiment_analysis(nobel.content))

    # for my understanding:
    # 'neg': indicates that there is no negative sentiment detected.
    # 'neu': 0.614 – About 61.4% of the sentiment is neutral.
    # 'pos': 0.386 – Approximately 38.6% of the sentiment is positive.
    # 'compound': 0.7417 – overall sentiment score that combines the previous three scores into one value. A compound score close to 1 (or, in this case, 0.7417) indicates a strong positive sentiment.


if __name__ == "__main__":
    main()
