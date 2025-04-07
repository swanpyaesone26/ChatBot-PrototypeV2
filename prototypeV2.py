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
    "How do I join a student club?": "Visit the student affairs office. They’ll provide you a list of clubs and how to register.", # Location & Access
    "Where is the library located?": "The main library is in the Learning Commons Building, Room 200. There’s also a satellite branch in the Science Wing.",
    "Is the library wheelchair accessible?": "Yes, all floors have elevators, ramps, and accessible restrooms.",
    "Are there parking spaces near the library?": "Yes, Lot B (next to the Learning Commons) has reserved spots for library visitors.",
    "Can the public access the university library?": "Community members can enter with a guest pass, but borrowing requires a paid membership.",
    "Where’s the after-hours book return?": "There’s a drop box at the library’s west entrance for returns when closed.",

    # Hours & Availability
    "What are the library’s opening hours?": "Open Mon-Fri 8AM–10PM, Sat 9AM–8PM, and Sun 12PM–6PM during semesters.",
    "Is the library open during holidays?": "Hours are reduced; check the website for holiday schedules.",
    "Does the library close for breaks?": "It operates on reduced hours during spring/winter breaks but remains open.",
    "When is the library least crowded?": "Mornings (8–10AM) and late evenings (after 8PM) are usually quieter.",
    "Is 24/7 access available for students?": "Yes, the 2nd-floor study zone has swipe-card access for students after hours.",

    # Borrowing & Returns
    "How do I check out a book?": "Bring items to the self-check kiosks or circulation desk with your student ID.",
    "Can I borrow textbooks?": "Yes, but course reserves have shorter loan periods (usually 3 hours).",
    "How many books can I borrow at once?": "Undergraduates: 15 items; Graduates: 25 items; Faculty: 50 items.",
    "What’s the loan period for books?": "28 days for general books, 7 days for DVDs, and 3 hours for course reserves.",
    "Can I renew books online?": "Yes, log into your library account or call the circulation desk. Max 2 renewals if no holds.",

    # Fines & Fees
    "What’s the late fee for overdue books?": "$0.50/day per book (max $15). Course reserves: $2/hour (max $25).",
    "Do fines apply on weekends/holidays?": "Yes, fines accumulate every day the library is closed.",
    "How do I pay library fines?": "Online via the student portal or at the finance desk in the library.",
    "Are there fine waivers for first-time offenders?": "Yes, one-time courtesy waivers for minor delays—ask at the desk.",
    "What if I lose a borrowed item?": "You’ll pay the replacement cost + a $10 processing fee.",

    # Technology & Resources
    "Does the library lend laptops/tablets?": "Yes, 4-hour loans (renewable if available) at the Tech Desk. Late fee: $20/hour.",
    "Is printing/scanning available?": "Black-and-white prints: $0.10/page; scanning is free. Use your student credit.",
    "How do I connect to library Wi-Fi?": "Network: ‘Campus_Lib’; log in with your student ID and password.",
    "Can I access e-books from off-campus?": "Yes, use the VPN or log in via the library website with your credentials.",
    "Where are the charging stations?": "Near study carrels on all floors; some have wireless charging pads.",

    # Study Spaces
    "Are there group study rooms?": "Yes, book online (max 3 hours/day). Rooms have whiteboards and monitors.",
    "Is there a silent study area?": "Floor 4 is a no-talk zone; Floor 1 allows quiet conversation.",
    "Can I eat in the library?": "Only in the café area (Floor 1). Covered drinks allowed elsewhere.",
    "Are there lockers for storage?": "Day-use lockers are near the entrance; bring your own lock.",
    "Does the library have standing desks?": "Yes, adjustable desks are in the Health & Wellness Zone (Floor 3).",

    # Research Help
    "How do I cite sources in APA/MLA?": "Use the citation guides on the library website or ask a librarian.",
    "Can librarians proofread my paper?": "They can help with research and citations but not grammar checks.",
    "Where are the academic journals?": "Access them digitally via the ‘Databases’ tab on the library website.",
    "How do I request a research consultation?": "Schedule a 1-on-1 appointment online or at the Reference Desk.",
    "What’s Interlibrary Loan (ILL)?": "A service to borrow books/articles from other libraries (3–10 business days).",

    # Special Collections
    "Does the library have rare books?": "Yes, the Archives Room (by appointment) houses rare manuscripts and local history.",
    "Can I donate books to the library?": "Contact the Collections Office—gifts must meet curriculum needs.",
    "Where are the thesis/dissertation copies?": "Digital copies are in the university repository; print versions are in Archives.",
    "Are there children’s books for student parents?": "Yes, a small family section is near the café (Floor 1).",
    "Does the library host author talks?": "Yes, check the ‘Events’ calendar for upcoming lectures and book signings.",

    # Miscellaneous
    "Is there a lost and found?": "Items are held at the Security Desk for 30 days.",
    "Can I volunteer at the library?": "Apply via the Student Work Program; positions open each semester.",
    "Are therapy dogs allowed in the library?": "Only during scheduled ‘De-Stress Week’ events.",
    "Where’s the closest bathroom?": "Restrooms are on every floor near the elevators.",
    "How do I report noisy patrons?": "Notify staff at the Help Desk or text the library’s noise complaint line.",

    # Events & Workshops
    "Does the library offer tech workshops?": "Yes, weekly sessions on Zotero, LaTeX, and data visualization.",
    "Are there book clubs?": "Faculty-led clubs meet monthly; sign up at the Events Board.",
    "Can I reserve the library for an event?": "Only university-affiliated groups; submit a request 30 days in advance.",
    "Where are movie screenings held?": "In the Media Room (Floor 2) every Friday at 6PM.",
    "How do I access past workshop recordings?": "They’re uploaded to the library’s YouTube channel.",

    # Policies
    "What’s the policy on cell phone use?": "Silent mode only; take calls in the lobby or stairwells.",
    "Can I bring my pet to the library?": "Only service animals are permitted.",
    "Is smoking allowed outside the library?": "Designated smoking areas are 50 feet from all entrances.",
    "What’s the dress code?": "No shirt, no shoes, no service—otherwise, casual attire is fine.",
    "Are political posters allowed on bulletin boards?": "Only university-approved flyers in designated areas."
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