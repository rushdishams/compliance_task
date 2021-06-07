## Project Overview

Filters to detect useful and unuseful augmentations for given original sentences.

## Project files

### Code Challenge
`compliance_task/notebook` directory contains a jupyter notebook that has justifications for various assumptions and justifications
`compliance_task/codes` directory contains python codes for the filters
`compliance_task/data` directory contains the input json file
`compliance_task/out` directory contains the output json file

To run: 
`python compliance_task/codes/driver.py`

All the required libraries are in `compliance_task/requirements.txt`

### System Design Challenge
`compliance_task/system_design` directory contains slide decks for system design task

## Remarks on Improvements
1. Instead of count vectorizer, we could use tfidf vectorizer for similarity measure.
2. It is merely assumed that an augmentation is duplicate/near-duplicate if it has 50%
similarity with the original sentence. This heuristics can be found by analyzing judgments
of compliance officers statistically.
3. As BoW model is used for similarity measure, context information is lost. Although 
bigrams and trigrams are considered, it is not enough to capture contexts. A deep learning
model with word embedding layer would be much more accurate. The decision of using such model
depends on the accuracy-speed tradeoff. For this task, simplicity is maintained.
4. There are many minor grammar rules that can be ignored. A thorough investigation on the 
grammar rules used in the `language_tool_python` library is recommended.
5. The data preprocessing was kept simple by observing the data samples. There could be 
many diffierent types of noise not reflected in this particular set of data. Getting more
example data could make the preprocessing more sophisticated.
6. The grammar filter cutoff, likewise the similarity filter cutoff, could be made more
sophisticated using statistical analysis of the compliance officer's judgments. 
7. Finally, the fidelity filter is a semantic filter that could be achieved by checking
augmentations against their original sentences using semantic similarity measures using
WordNet or a deep learning model with word embedding layer.



