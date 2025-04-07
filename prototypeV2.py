import re
from prototypeV2 import tokenize, count_matches_per_document, rank_documents

uni_document = {
    "Excuse me, where is the registration office?": "It's on the first floor of the administration building, Room 102.",
    "What are the office hours for student services?": "We’re open from 9 a.m. to 4 p.m., Monday to Friday.",
    "How can I get my student ID card?": "You need to fill out the ID request form and bring a photo to the registrar's office.",
    "When does the semester start?": "The semester starts on August 7th.",
    "Where can I get a copy of my transcript?": "You can request it at the registrar’s office or apply online through the student portal.",
    "Is there a lost and found on campus?": "Yes, it's located at the security office near the main gate.",
    "How do I apply for a dorm room?": "You need to submit a housing application online before the deadline.",
    "Are there scholarships available for international students?": "Yes, we offer several scholarships. You can get the list from the scholarship office or our website.",
    "Where is the library and what are its hours?": "The library is behind the science building. It’s open from 8 a.m. to 8 p.m. on weekdays.",
    "Can I change my course after registration?": "Yes, but only during the add/drop period, which ends in the second week of classes.",
    "Who can I contact if I have IT problems with my student portal": "You should contact the IT support center at Room 305 in the admin building or email support@university.edu.",
    "Where do I pay my tuition fees?": "You can pay online through the portal or at the finance office on the second floor.",
    "How do I join a student club?": "Visit the student affairs office. They’ll provide you a list of clubs and how to register.",
}


# Input question from the user
user_question = input("Please enter your question: ")

# Tokenizing the user's question
user_question_tokens = tokenize(user_question)

# Tokenizing the keys in the uni_document and creating the updated dictionary
uni_document_tokenized = {tokenize(key): value for key, value in uni_document.items()}

# Count matches for each document
document_tokens = list(uni_document_tokenized.keys())  # List of tokenized document keys
match_counts = count_matches_per_document(document_tokens, user_question_tokens)

# Rank the documents based on the match count
best_matching_document = rank_documents(match_counts, list(uni_document.values()))

# Output the best matching answer
print(best_matching_document if best_matching_document else "Sorry, I couldn't find an answer to your question.")