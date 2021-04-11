import os
import numpy as np


class Config():
    def __init__(self):
        pass

    # embeddings
    dim_word = 50
    dim_pos = 5
    dim = dim_word + 2 * dim_pos

    add_unk_and_blank = True

    max_len = 120
