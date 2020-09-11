from embeddings import *

def context_sim(tokens, i, candidate, window_size):
    """Calculates context similarity for word."""
    left_contexts, right_contexts = [], []
    half_window = int(window_size / 2)
    # Find left contexts if any.
    if i > 0:
        left_contexts = tokens[:i]
        if len(left_contexts) > half_window:
            left_contexts = tokens[i-half_window:i]
    # Find right contexts if any.
    if i < len(tokens) - 1:
        right_contexts = tokens[i+1:]
        if len(right_contexts) > half_window:
            right_contexts = tokens[i+1:i+half_window+1]
    # Calculate context similarity from contexts.
    all_contexts = left_contexts + right_contexts
    context_similarity = sum([wv_model.similarity(candidate, c) for c in all_contexts])
    #print(candidate + " " + str(context_similarity))
    return context_similarity

def language_model():
    """Calculates language model score for word."""
    pass
