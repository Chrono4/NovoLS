from nltk.tokenize import wordpunct_tokenize as tokenize
from gensim.parsing.preprocessing import STOPWORDS
from wordfreq import zipf_frequency as zfreq
from gensim.models import KeyedVectors

from features import context_sim, language_model
from embeddings import *
import sys

# Parameters for simplifier.
LANG = "en"
MIN_COMPLEXITY = 5.20
CANDIDATE_NO = 10
WINDOW_SIZE = 6

def suitable_candidate(tokens, i, c):
    """Checks if candidate is suitable for simplification."""
    # Checks candidate is less complex than original word.
    less_complex = zfreq(c[0], LANG) > zfreq(tokens[i], LANG)
    # Checks candidate is not morphological derivation.
    not_morph = c[0] not in tokens[i] and tokens[i] not in c[0]
    
    return less_complex and not_morph
    
def simplify_token(tokens, i):
    """Simplifies a token given index and all tokens."""
    # Get top 10 similar words and remove those that are not suitable.
    candidates = wv_model.most_similar(tokens[i], topn = CANDIDATE_NO)
    candidates = [c for c in candidates if suitable_candidate(tokens, i, c)]
    # Rank candidates based on features.
    syntactic_ranked = sorted(candidates, key = lambda c: c[1])
    complexity_ranked = sorted(candidates, key = lambda c: zfreq(c[0], LANG))
    context_ranked = sorted(candidates, key = lambda c: context_sim(tokens, i, c[0], WINDOW_SIZE))
    # Calculate overall rank for each candidate.
    overall_ranked = [(c[0], syntactic_ranked.index(c) +
                       complexity_ranked.index(c) +
                       context_ranked.index(c)) for c in candidates]

    return overall_ranked
    
if __name__ == '__main__':
    # If supplied, set text to user input.
    if len(sys.argv) > 1:
        raw_str = sys.argv[1]
    else:
        raw_str = "This is a particularly convoluted sentence requiring simplification."
        
    # Copy of tokens to prevent changes to original.
    tokens = tokenize(sys.argv[1])
    tokens_copy = tokens.copy()
    # For each copied token
    for i in range(len(tokens_copy)):
        # Make current word lowercase.
        tokens_copy[i] = tokens_copy[i].lower()
        # Conditions ensuring only valid and complex words are simplified.
        word_valid = tokens_copy[i] in wv_model.vocab and tokens_copy[i] not in STOPWORDS
        word_complex = zfreq(tokens_copy[i], LANG) < MIN_COMPLEXITY
        # Only simplify tokens in model and not in stopwords.
        if word_valid and word_complex:
            result = simplify_token(tokens_copy, i)
            print(result)
            
        
        

        



