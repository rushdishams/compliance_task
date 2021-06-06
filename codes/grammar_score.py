import language_tool_python as lt

# Initializing for grammar checking
tool = lt.LanguageTool('en')

"""Count grammar mistakes in augmentations

Returns:
    int: Total grammar mistakes in an augmentation
"""
def get_grammar_mistakes(s):
    return len(tool.check(s))

"""Add grammar mistakes for augmentations

Returns:
    Pandas dataframe: Contains augmentations and their grammar mistakes
"""
def add_grammar_score(final_df):
    # Get grammar mistakes for each augmentation
    final_df['grammar_mistakes'] = final_df['aug'].apply(lambda x: get_grammar_mistakes(x))
    final_df['grammar_cutoff'] = grammar_cutoff(final_df)

    return final_df

"""Compute cutoff for grammar filter. Augmentations
with grammar mistakes higher than the cutoff will fail.

Returns:
    float: Grammar mistake filter cutoff
"""
def grammar_cutoff(final_df):
    # Get 75th and 25th percentile of grammar mistakes
    q3 = final_df['grammar_mistakes'].quantile(0.75)
    q1 = final_df['grammar_mistakes'].quantile(0.25)
    # Calculate inter-quartile range and then the upper bound
    iqr = q3 - q1
    cutoff = q3 + 1.5 * iqr
    
    return cutoff
