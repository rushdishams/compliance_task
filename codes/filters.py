import numpy as np

"""Similarity/Grammar scores are checked to see if augmentations pass or fail.

Returns:
    Two pandas dataframes. One with augmentations
    that passed and the other that failed.
"""
def apply_filter(final_df):
    # If similarity/grammar scores are above cutoff, they fail. Otherwise, they pass.
    final_df['sim_filter'] = np.where(final_df['sim_scores'] >= final_df['sim_cutoff'], 
                                      True, 
                                      False)
    final_df['grammar_filter'] = np.where(final_df['grammar_mistakes'] >= final_df['grammar_cutoff'], 
                                          True, 
                                          False)
    
    # Messages about how the augmenations performed
    final_df['checks'] = final_df.apply(create_check_msg , axis=1)

    passed_df, failed_df = filter_decisions(final_df)

    return passed_df, failed_df

"""Generate messages to understand the reason of pass/fail easy.

Returns:
    string: The reason for pass/fail for augmentations
"""
# Generate messages to understand the reason of pass/fail easy
def create_check_msg(row):
    msg = (str(round(row['sim_scores'] * 100, 1)) + '% similarity with ' +  
           str(round(row['grammar_mistakes'], 3)) + ' grammar mistake(s)')
    
    return msg

"""Decide if augmentations pass the filters.
   
Returns:
    Two pandas dataframes. One with augmentations
    that passed and the other that failed.
"""
def filter_decisions(final_df):
    # If an augmenation passes all filters, then it passed.
    # If it fails in any, then it failed.
    passed_df = final_df[(final_df['sim_filter'] == False) & 
                    (final_df['grammar_filter'] == False)]
    failed_df = final_df[(final_df['sim_filter'] == True) | 
                    (final_df['grammar_filter'] == True)]
    
    return passed_df, failed_df