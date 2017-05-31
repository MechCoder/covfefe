import random

def covfefe(x, n=1, random_state=None):
    """
    Covfefe my strings.

    Parameters
    ----------
    x: string
        String with spaces in-between.

    n: int
        Number of words to replace by covfefe.

    random_state: None, int
        Set random state for reproducible covfefes.
    """
    random.seed(random_state)
    x = x.split(" ")
    if n > len(x):
        raise ValueError(
            "Sorry, you don't have enough power to "
            "replace more than %d words by covfefes." % len(x))
    for s in random.sample(range(0, len(x)), n):
        x[s] = "covfefe"
    return " ".join(x)
