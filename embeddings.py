from gensim.models import KeyedVectors

# Load embeddings for simplifier.
wv_path = "resources/embeddings/vectors.kv"
wv_model = KeyedVectors.load(wv_path, mmap='r')
