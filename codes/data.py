import json, os

INPUT_PATH = os.getcwd() + '/data/augmentations.json'
OUTPUT_PATH = os.getcwd() + '/out/augmentations_filtered.json'

"""Load augmentations in json format
Returns: 
    json: Original sentences and their augmentations
"""
def load_augmentations():
    # Read augmentations
    data = None
    try:
        with open(INPUT_PATH) as data_file:    
            data = json.load(data_file)
    except Exception as e:
        print('Error reading augmentations')
        print(str(e))
    finally:
        return data

"""Creating the json payload (output)
"""
def write_decisions(passed_df, failed_df):
    payload = dict()
    # Dict key passed contains augmentations that passed the filters
    # Dict key failed contains augmentations that failed
    payload['passed'] = passed_df[['aug', 'checks']].\
                        rename(columns={'aug':'augmentation'}).\
                        to_dict(orient='records')
    payload['failed'] = failed_df[['aug', 'checks']].\
                        rename(columns={'aug':'augmentation'}).\
                        to_dict(orient='records')

    try:
        # Write the filter outcomes to json
        with open(OUTPUT_PATH, 'w+') as file:
            json.dump(payload, file)
    except Exception as e:
        print('Error writing output')
        print(str(e))