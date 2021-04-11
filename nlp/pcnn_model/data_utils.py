import numpy as np
import os
import re


# shared global variables to be imported from model also
UNK = "<UNK>"
BLANK = "<BLANK>"
NONE = "NA"



# special error message
class MyIOError(Exception):
    def __init__(self, filename):
        # custom error message
        message = """
ERROR: Unable to locate file {}.
FIX: Have you tried running python build_data.py first?
This will build vocab file from your train, test and dev sets and
trimm your word vectors.
""".format(filename)
        super(MyIOError, self).__init__(message)



class getDataset(object):
    """Class that iterates over Dataset
    __iter__ method yields a tuple (words, tags)
        words: list of raw words
        tags: list of raw tags
    If processing_word and processing_tag are not None,
    optional preprocessing is appplied
    """
    def __init__(self, filename, processing_word=None, processing_relation=None, max_iter=None):
        """
        Args:
            filename: path to the file
            processing_words: (optional) function that takes a word as input, process the word and return word idx
            processing_relation: (optional) function that takes a relation as input and return relation idx
            max_iter: (optional) max number of sentences to yield
        """
        self.filename = filename
        self.processing_word     = processing_word
        self.processing_relation = processing_relation
        self.max_iter = max_iter
        self.length = None

    def __iter__(self):
        niter = 0
        with open(self.filename) as f:
            for line in f:
                niter += 1
                if self.max_iter is not None and niter > self.max_iter:
                    break
                word_idx, pos1, pos2 = [], [], []
                line = re.sub('###END###', '</s>', line)
                line = line.strip()
                content = line.split()
                ent1     = content[2]
                ent2     = content[3]
                relation = content[4]
                if self.processing_relation is not None:
                    relation = self.processing_relation(relation)
                sentence = line[5:]
                ent1pos  = sentence.index(ent1)
                ent2pos  = sentence.index(ent2)
                for idx, word in enumerate(sentence):
                    position1 = pos_constrain(idx - ent1pos)
                    position2 = pos_constrain(idx - ent2pos)
                    if self.processing_word is not None:
                        word = self.processing_word(word)
                    word_idx.append(word)
                    pos1.append(position1)
                    pos2.append(position2)
                yield word_idx, pos1, pos2, (ent1pos, ent2pos), relation


    def __len__(self):
        """Iterates once over the corpus to set and store length"""
        if self.length is None:
            self.length = 0
            for _ in self:
                self.length += 1

        return self.length


def shuffle_data(filename):
    """Shuffle large dataset
    Args:
        filename: path to file to be shuffled
    Returns:
        None
    """
    from sys import platform
    import subprocess
    import os.path

    if not os.path.exists(filename):
        raise MyIOError(filename)

    # Linux OS
    if platform == "linux" or platform == "linux2":
        try:
            subprocess.run(["shuf", "-o", filename, filename])
            print("Shuffle {} successfully".format(filename))
        except:
            print("Failed to shuffle datasets.")
    # Mac OS
    elif platform == "darwin":
        try:
            subprocess.run(["gshuf", "-o", filename, filename])
            print("Shuffle {} successfully".format(filename))
        except:
            print("gshuf is uninstalled. run \nbrew install coreutils\n")
    else:
        print("Shuffle is still unsupported on Windows")


def process_wordvectors(filename_wordvectors, filename_words, filename_embeddings, dim=50):
    """Process pre trained word vectors file. Store words and vectors respectively.
    Args:
        filename_wordvectors: path to word vector file
        filename_words: path to store words
        filename_embeddings: path to store vectors
        dim: (int) dimension of embeddings
    """
    try:
        vec = []
        words = []
        dim = dim
        words.append("<BLANK>")
        vec.append(np.zeros(shape=dim))
        words.append("<UNK>")
        vec.append(np.random.normal(size=dim, loc=0, scale=0.05))
        with open(filename_wordvectors, 'r') as f:
            f.readline()
            for line in f:
                line = line.strip()
                content = line.split()
                words.append(content[0])
                vector = list(map(lambda x: float(x), content[1:]))
                vec.append(vector)
        write_vocab(words, filename_words)
        vec = np.array(vec, dtype=np.float32)
        np.savez(filename_embeddings, vec=vec)

    except IOError:
        raise MyIOError(filename_wordvectors)


def process_relation2id(filename_relation_origin, filename_relation):
    """process relation id pairs
    Args:
        filename_relation_origin: (string) the format of the file must be one relation and one index per line.
        filename_relation: (string) path to store relation
    """
    try:
        d = []
        with open(filename_relation_origin) as f:
            for line in f:
                line = line.strip()
                rel, idx = line.split()
                d.append(rel)
        write_vocab(d, filename_relation)

    except IOError:
        raise MyIOError(filename_relation_origin)


def get_processing_word(vocab_words=None, allow_unk=True, UNK = "<UNK>"):
    """Return lambda function that transform a word (string) into list,
    or tuple of (list, id) of int corresponding to the ids of the word.
    Args:
        vocab: dict[word] = idx
    Returns:
        f("hello") = (12345)
                 = (word id)
    """
    def f(word):
        # get id of word
        if vocab_words is not None:
            if word in vocab_words.keys():
                word = vocab_words[word]
            else:
                if allow_unk:
                    word = vocab_words[UNK]
                else:
                    raise Exception("Unknow key is not allowed. Check that "\
                                    "your vocab (tags?) is correct")
        return word

    return f


def pos_constrain(val, max_val=498, min_val=0):
    """Constrain values from 0 to 498
    Args:
        val: value to be constrained
    Returns:
        val: value after map and constrain
    """
    val = val + 60
    return min(max_val, max(min_val, val))


def check_entity_in_sentence(filename_origin, filename_output, filename_failparse):
    """Divide dataset into two group according to whether multi-words entities is parsed correctly.
    Args:
        filename_origin: path to original dataset file.
        filename_output: path to store correct dataset.
        filename_failparse: path to store wrong dataset.
    """
    with open(filename_origin, 'r') as f:
        for line in f:
            content = line.strip().split()
            ent1 = content[2]
            ent2 = content[3]
            sentence = content[5:-1]
            if ent1 in sentence and ent2 in sentence:
                with open(filename_output, 'a') as file:
                    file.write(line)
            if ent1 not in sentence or ent2 not in sentence:
                with open(filename_failparse, 'a') as file:
                    file.write(line)


def get_vocabs(datasets):
    """Build vocabulary from an iteration of dataset objects
    Args:
        dataset: a list of dataset objects
    Returns:
        two sets of all the words and tags respectively in the dataset
    """
    print("Building vocabulary...")
    vocab_words = set()
    vocab_tags  = set()
    for dataset in datasets:
        for words, tags in dataset:
            vocab_words.update(words)
            vocab_tags.update(tags)
    print("- done. {} tokens".format(len(vocab_words)))
    return vocab_words, vocab_tags



def write_vocab(vocab, filename):
    """Writes a vocab to a file
    Writes one word per line.
    Args:
        vocab: iterable that yields word
        filename: path to vocab file
    Returns:
        write a word per line
    """
    print("Writing vocab...")
    with open(filename, "w") as f:
        for i, word in enumerate(vocab):
            if i != len(vocab) - 1:
                f.write("{}\n".format(word))
            else:
                f.write(word)
    print("- done. {} tokens".format(len(vocab)))


def load_vocab(filename):
    """Loads vocab from a file
    Args:
        filename: (string) the format of the file must be one word per line.
    Returns:
        d: dict[word] = index
    """
    try:
        d = dict()
        with open(filename) as f:
            for idx, word in enumerate(f):
                word = word.strip()
                d[word] = idx

    except IOError:
        raise MyIOError(filename)
    return d


def minibatches(data, minibatch_size):
    """
    Args:
        data: generator of (word_idx, pos1, pos2, relation) tuples
        minibatch_size: (int)
    Yields:
        list of tuples
    """
    word_batch, pos1_batch, pos2_batch, entpos_batch, y_batch = [], [], [], [], []
    for (word, pos1, pos2, entpos, y) in data:
        if len(y_batch) == minibatch_size:
            sequence_lengths = get_sequences_length(word_batch)
            assert len(entpos_batch) == len(sequence_lengths)
            pos_batch = list()
            for idx, i in enumerate(entpos_batch):
                a, b = i
                pos_batch.append([a, b, sequence_lengths[idx]])

            yield word_batch, pos1_batch, pos2_batch, pos_batch, y_batch
            word_batch, pos1_batch, pos2_batch, entpos_batch, y_batch = [], [], [], [], []

        word_batch   += [word]
        pos1_batch   += [pos1]
        pos2_batch   += [pos2]
        entpos_batch += [entpos]
        y_batch      += [y]

    if len(y_batch) != 0:
        sequence_lengths = get_sequences_length(word_batch)
        assert len(entpos_batch) == len(sequence_lengths)
        pos_batch = list()
        for idx, i in enumerate(entpos_batch):
            a, b = i
            pos_batch.append([a, b, sequence_lengths[idx]])
        yield word_batch, pos1_batch, pos2_batch, pos_batch, y_batch


def to_piece(data, pos, width=2):
    """Split each sentence in batch into three piece
    accodring to entity1, entity2 position and sentence length.
    Args:
        data: batch of list of ids, representing batch of sentences.
        pos: list of positions, containing entity1, entity2 position and
                sentence length of corresponding sentence in data.
        width: int
    Return:
        left: batch of list of ids, left part of sentences.
        mid: batch of list of ids, middle part of sentences.
        right: batch of list of ids, right part of sentences.
    """
    assert len(data) == len(pos)
    assert np.asarray(pos, dtype=np.int32).shape[1] == 3
    num = len(data)
    left  = []
    mid   = []
    right = []
    for i in range(num):
        left.append(data[i][0:(pos[i][0]+width)])
        mid.append(data[i][max(0, (pos[i][0]-width)) : min((pos[i][1]+width), (pos[i][2]-1))])
        right.append(data[i][(pos[i][1]-width):(pos[i][2]-1)])

    return left, mid, right


def get_sequences_length(sequences):
    """
    Args:
        sequences: a generator of list or tuple
    Returns:
        a list record original length of sequences
    """
    sequence_length = []

    for seq in sequences:
        seq = list(seq)
        sequence_length += [len(seq)]

    return sequence_length


def pad_sequences(sequences, pad_tok=0):
    """
    Args:
        sequences: a generator of list or tuple
        pad_tok: the char to pad with
    Returns:
        a list of list where each sublist has same length
        a list record original length of sequences
    """
    _sequence_padded = []
    max_length = max(map(lambda x : len(x), sequences))

    for seq in sequences:
        seq = list(seq)
        seq_ = seq[:max_length] + [pad_tok]*max(max_length - len(seq), 0)
        _sequence_padded +=  [seq_]

    sequence_padded = np.asarray(_sequence_padded)
    return sequence_padded


def to_bags(data):
    """Split minibatch into bags according to their relations. Corresponding to Eq (9) in paper.
    Args:
        data: one minibatch of batch size
    Return:
        data: a list of bags, each bag contains the instances shared the same relation.
    """
    word_batch, pos1_batch, pos2_batch, pos_batch, y_batch = data
    relations = set(y_batch)
    num_bags = len(list(relations))
    word_bags = [[] for i in range(num_bags)]
    pos1_bags = [[] for i in range(num_bags)]
    pos2_bags = [[] for i in range(num_bags)]
    pos_bags  = [[] for i in range(num_bags)]
    y_bags    = [[] for i in range(num_bags)]
    for idx, i in enumerate(relations):
        for idy, j in enumerate(y_batch):
            if i == j:
                word_bags[idx].append(word_batch[idy])
                pos1_bags[idx].append(pos1_batch[idy])
                pos2_bags[idx].append(pos2_batch[idy])
                pos_bags[idx].append(pos_batch[idy])
                y_bags[idx].append(y_batch[idy])

    print("This batch contains {} bags.".format(num_bags))
    return word_bags, pos1_bags, pos2_bags, pos_bags, y_bags, num_bags