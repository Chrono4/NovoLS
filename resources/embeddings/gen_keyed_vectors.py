import sys
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

if len(sys.argv) > 1:
    # Convert GloVe vectors to Word2Vec for gensim.
    print("Converting GloVe embeddings to Word2Vec...")
    glove_file = sys.argv[1]
    tmp_file = "word2vec_from_glove.txt"
    _ = glove2word2vec(glove_file, tmp_file)
    # Load model as KeyVectors and then save.
    print("Saving embeddings as KeyedVectors...")
    model = KeyedVectors.load_word2vec_format(tmp_file)
    model.save("vectors.kv")
    print("Done!")
else:
    print("Please enter the location of the GloVe word embeddings.")
    
