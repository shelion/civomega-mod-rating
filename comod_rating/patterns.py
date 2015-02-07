"""
contains `PATTERNS`, defining strings that this module may respond to

Wrap "blanks" in {braces}

The content inside the braces dictate the type of object being entered.  This content should be lowercase, underscore_separated.

e.g. 
PATTERNS = frozenset([
    "is {person} a {thing}?",
    "is {person} a {thing} in {place}?",
])


"""

VOTE_PATTERNS = frozenset([
    "which votes are about {topic}?",
    "what votes are about {topic}?"
    "How did {person} vote on {bill}?"
    ])

PATTERNS = VOTE_PATTERNS