from data import load_augmentations, write_decisions
from preprocess import preprocess
from similarity_score import add_sim_score
from grammar_score import add_grammar_score
from filters import apply_filter

# Parse original sentences and their augmentations
data = load_augmentations()
if not data:
    exit()
# Normalize/Preprocess data
df = preprocess(data)
# Add similarity score between original and each of its augmentations
df = add_sim_score(df)
# Add grammar mistakes of augmentations
df = add_grammar_score(df)
# Apply filter
passed_df, failed_df = apply_filter(df)
# Write filter decisions
write_decisions(passed_df, failed_df)