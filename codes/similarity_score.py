from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd

# If augmentation has 50% similarity, it will fail in the filter.
SIM_CUTOFF = 0.5

"""Compute similarity between the augmenations and their original sentence.

Returns:
    Pandas dataframe: Contains augmentations and their similarities with original.
"""
def get_sim_score(df):
    # Counting words, bigrams and trigrams
    vectorizer = CountVectorizer(ngram_range=(1,3)) # TfIdf Vectorizer can be used as well
    aug_vec = vectorizer.fit_transform(df['aug_cleaned'])
    orig_vec = vectorizer.transform(df.iloc[:1]['orig_cleaned']) # We only need one original sentence
    df['sim_scores'] = cosine_similarity(orig_vec, aug_vec).flatten() # Flatten to fit in a column

    return df

"""Add similarity score between augmentations and original sentences.

Returns:
    Pandas dataframe: Contains augmentations and their similarities with original.
"""
def add_sim_score(df):
    # List of original sentence ids
    oid_list = df['oid'].unique()
    # Dataframe to contain similarity for all (augmentated, original) sentence pairs
    final_df = pd.DataFrame()
    # Vertically tack similarity score for the pairs for each original sentence
    try:
        for oid in oid_list:
            final_df = pd.concat([final_df, 
                                get_sim_score(df[df['oid'] == oid])], 
                                axis=0)
    except Exception as e:
        final_df['sim_scores'] = 0
        print('Error in computing similarity.')
        print(str(e))
        
    final_df['sim_cutoff'] = similarity_cutoff()

    return final_df

"""If augmentations have greater similarity with 
originals than this cutoff, then they failed in this filter.

Returns:
    float: Similarity filter cutoff
"""
def similarity_cutoff():
    return SIM_CUTOFF