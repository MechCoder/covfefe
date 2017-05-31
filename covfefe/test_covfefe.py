"""
Test my covfefes beacuse coverage is important.
"""

from covfefe import covfefe

def test_covfefe():
    x = "Despite the constant negative press ??"
    for n_words in range(1, 6):
        for rand_state in range(100):
            assert(covfefe(x, n_words, rand_state).split(" ").count("covfefe") == n_words)
