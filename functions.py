import re

# Tokenizer function (tokenizes only the key)
def tokenize(text):
    """Tokenizes and cleans text by removing punctuation (including ?,!) and converting to lowercase."""
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


# Function to expand short forms in user queries and this is the updated function in Version 2
def expand_shortforms(query, shortforms_dict):
    """Expands abbreviations in user queries using the shortforms dictionary."""
    words = query.split()
    expanded_words = []
    
    # Check for multi-word abbreviations
    query_lower = query.lower()
    for abbreviation, expansion in shortforms_dict.items():
        # Use regex to replace multi-word abbreviations
        if abbreviation in query_lower:
            query = query.replace(abbreviation, expansion)
    
    words = query.split()
    
    for word in words:
        lower_word = word.lower()
        if lower_word in shortforms_dict:
            # Preserve original capitalization of the first letter if present
            if word[0].isupper():
                expanded = shortforms_dict[lower_word].capitalize()
            else:
                expanded = shortforms_dict[lower_word]
            expanded_words.append(expanded)
        else:
            expanded_words.append(word)
    
    return ' '.join(expanded_words)