import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Configure stopword remover and stemmer
stops = stopwords.words('english')
stemmer = PorterStemmer()

# Regex to remove punctuations and to keep alphanumerics only
NOPUNCT_REGEX = re.compile(r'[/(){}\[\]\|@,;\.!]')
ALNUM_REGEX = re.compile(r'[^a-zA-Z0-9  ]')

"""Create dataframe from json data and apply
various preprocess filters.

Returns:
    Pandas dataframe: Each row is a (original sentence, augmentation) pair
"""
def preprocess(data):
    # Generate rows containing (augmentation, original) sentence pairs
    rows = [(oid, orig, aid, aug) 
        for oid, orig in enumerate(data) 
        for aid, aug in enumerate(data[orig])]
    
    # Create dataframe with the pairs
    df = pd.DataFrame(rows, 
                  columns=['oid', 'orig', 'aid', 'aug'])
    
    # Lower case all text
    df = change_case(df)

    # Apply regex filters, remove stops and stem function words
    try:
        df['orig_cleaned'] = df['orig_lower'].apply(clean_text)
        df['aug_cleaned'] = df['aug_lower'].apply(clean_text)
    except Exception as e:
        df['orig_cleaned'] = df['orig_lower']
        df['aug_cleaned'] = df['aug_lower']
        print('Error in text processing.')
        print(str(e))
    
    return df

"""Change cases of the sentences

Returns:
    Pandas dataframe: Sentences lower-cased
"""
# Changing all text to lowercase
def change_case(df):
    for col in ['orig', 'aug']:
        df[col + '_lower'] = df[col].str.lower()
    
    return df

"""Text normalization routines.

Returns:
    string: normalized sentences
"""
def clean_text(text):
    # Remove punctuation, keep alphanumerics
    # Finally, remove stops and stem function words
    text = str(text)
    text = NOPUNCT_REGEX.sub(' ', text)
    text = ALNUM_REGEX.sub('', text)
    text = ' '.join([w for w in text.split() if w not in stops])
    text = ' '.join([stemmer.stem(w) for w in text.split()])

    return text
