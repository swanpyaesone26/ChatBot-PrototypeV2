import re

# Tokenizer function (tokenizes only the key)
def tokenize(text):
    """Tokenizes and cleans text by removing punctuation and converting to lowercase."""
    return tuple(re.sub(r'[^\w\s]', '', text.lower()).split())

# Function to count matches for the query in a document
def count_matches(doc_tokens, query_tokens):
    """Counts the number of query words present in a document."""
    matches = 0
    document_set = set(doc_tokens)
    for token in query_tokens:
        if token in document_set:
            matches += 1
    return matches

# Function to count matches for each document
def count_matches_per_document(documents, query_tokens):
    """Counts matches for each document."""
    match_counts = []
    for index, doc_tokens in enumerate(documents):  
        matches = count_matches(doc_tokens, query_tokens)
        match_counts.append((index, matches))
    return match_counts

# Function to rank documents based on match counts
def rank_documents(match_counts, documents):
    """Ranks documents based on match counts."""
    # Sort the documents by match count (descending) and original index (ascending)
    sorted_count = sorted(match_counts, key=lambda x: (-x[1], x[0]))
    
    # Return the top 1 document (first in the sorted list)
    return documents[sorted_count[0][0]] if sorted_count else None