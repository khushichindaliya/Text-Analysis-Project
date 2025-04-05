import pickle

# Save data to a file (will be part of your data fetching script)

with open('dickens_texts.pkl','w') as f:
    pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
with open('dickens_texts.pkl','r') as f:
    reloaded_copy_of_texts = pickle.load(f)