import pandas as pd


def read_file(file_path):
    """Reads a text file and returns a list of lines."""
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    return lines


def preprocess_data(static_words_path, static_tags_path, static_candidates_path,
                    formal_words_path, formal_tags_path, formal_candidates_path, formal_labels_path):
    # Read data from files
    static_words = read_file(static_words_path)
    static_tags = read_file(static_tags_path)
    static_candidates = read_file(static_candidates_path)

    formal_words = read_file(formal_words_path)
    formal_tags = read_file(formal_tags_path)
    formal_candidates = read_file(formal_candidates_path)
    formal_labels = read_file(formal_labels_path)

    # Process static idioms - assign label 1 for all instances
    static_data = [{'words': words.lower().split(), 'tags': tags.split(),
                    'candidate': candidate, 'label': 1}
                   for words, tags, candidate in zip(static_words, static_tags, static_candidates)]

    # Process formal idioms
    formal_data = [{'words': words.lower().split(), 'tags': tags.split(),
                    'candidate': candidate, 'label': int(label)}
                   for words, tags, candidate, label in zip(formal_words, formal_tags, formal_candidates, formal_labels)]

    # Convert to DataFrames for ease of use
    static_df = pd.DataFrame(static_data)
    formal_df = pd.DataFrame(formal_data)

    return static_df, formal_df


def fetch_preprocessed_data():
    # File paths for static idioms
    static_base_path = 'EPIE_Corpus/Static_Idioms_Corpus/'
    static_words_path = static_base_path + 'Static_Idioms_Words.txt'
    static_tags_path = static_base_path + 'Static_Idioms_Tags.txt'
    static_candidates_path = static_base_path + 'Static_Idioms_Candidates.txt'

    # File paths for formal idioms
    formal_base_path = 'EPIE_Corpus/Formal_Idioms_Corpus/'
    formal_words_path = formal_base_path + 'Formal_Idioms_Words.txt'
    formal_tags_path = formal_base_path + 'Formal_Idioms_Tags.txt'
    formal_candidates_path = formal_base_path + 'Formal_Idioms_Candidates.txt'
    formal_labels_path = formal_base_path + 'Formal_Idioms_Labels.txt'

    # Preprocess the data
    return preprocess_data(static_words_path,
                           static_tags_path,
                           static_candidates_path,
                           formal_words_path,
                           formal_tags_path,
                           formal_candidates_path,
                           formal_labels_path)
