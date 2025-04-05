from mediawiki import MediaWiki
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nobel_data_analysis import clean_text  

def fetch_documents():
    """
    Fetch the Nobel Prize Wikipedia page.
    """
    wikipedia = MediaWiki()
    nobel = wikipedia.page("Nobel Prize")
    content = nobel.content
    documents = content.split('\n\n')
    return documents

def perform_topic_modeling(documents, num_topics=3, num_top_words=5):
    """
    Perform topic modeling on the provided documents using scikit-learn's LDA.
    """
    vectorizer = CountVectorizer(preprocessor=clean_text, stop_words='english')
    dtm = vectorizer.fit_transform(documents)  # Create a document-term matrix

    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda_model.fit(dtm)

    feature_names = vectorizer.get_feature_names_out()

    for topic_id, topic in enumerate(lda_model.components_):
        top_indices = topic.argsort()[-num_top_words:][::-1]
        top_words = [feature_names[i] for i in top_indices]
        print(f"Topic {topic_id}:")
        print(" ".join(top_words))
        print()

def main():
    documents = fetch_documents()
    perform_topic_modeling(documents)

if __name__ == '__main__':
    main()
