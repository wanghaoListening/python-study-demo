import tensorflow as tf
import numpy as np
from .model.config import Config


class Embedding(object):
    def __init__(self, word_vec_mat, word, pos1, pos2):
        """
        A function to initial the class.
        :param word_vec_mat: pre_trained word embedding matrix, shape=(vocab_size, dim_word)
        :param word: the index of the word
        :param pos1:
        :param pos2:
        """
        self.word_embedding = tf.get_variable("word_embedding", initializer=word_vec_mat, dtype=tf.float32)
        if Config.add_unk_and_blank:
            self.word_embedding = tf.concat([self.word_embedding,
                                             tf.get_variable('unk_word_embedding', [1, Config.dim_word],
                                                             dtype=tf.float32,
                                                             initializer=tf.contrib.layers.xavier_initializer()),
                                             tf.constant(np.zeros((1, Config.dim_word), dtype=np.float32))], 0)
        self.word = word
        self.pos1 = pos1
        self.pos2 = pos2

    def get_word_embedding(self):
        with tf.variable_scope("word_embedding", reuse=tf.AUTO_REUSE):
            x = tf.nn.embedding_lookup(self.word_embedding, self.word)
        return x

    def get_pos_embedding(self):
        with tf.variable_scope("pos_embedding", reuse=tf.AUTO_REUSE):
            pos_tol = Config.max_len * 2
            pos1_embedding = tf.get_variable("pos1_embedding", [pos_tol, Config.dim_pos], dtype=tf.float32, \
                                             initializer=tf.contrib.layers.xavier_initializer())
            pos2_embedding = tf.get_variable("pos2_embedding", [pos_tol, Config.dim_pos], dtype=tf.float32, \
                                             initializer=tf.contrib.layers.xavier_initializer())
            input_pos1 = tf.nn.embedding_lookup(pos1_embedding, self.pos1)
            input_pos2 = tf.nn.embedding_lookup(pos2_embedding, self.pos2)
            x = tf.concat([input_pos1, input_pos2], -1)
            return x

    def get_word_position_embedding(self):
        w_embedding = self.get_word_embedding()
        p_embedding = self.get_pos_embedding()
        return tf.concat([w_embedding, p_embedding], -1)



class PieceWiseCNN(object):

    def __init__(self, word_vec_mat, word, pos1, pos2):
        """
        A function to initial the class.
        :param word_vec_mat: pre_trained word embedding matrix, shape=(vocab_size, dim_word)
        :param word: the index of the word
        :param pos1:
        :param pos2:
        """

    def pcnn(self, left_emb, mid_emb, right_emb, feature_map, n_class):
        left = tf.keras.layers.Conv1D(filters=feature_map, kernel_size=3)(
            left_emb)  # [batch_size,maxlen,word_emb_size+2*pos_emb_size(10)]
        left = tf.keras.layers.GlobalMaxPool1D()(left)  # [batch_size,feature_map]
        mid = tf.keras.layers.Conv1D(filters=feature_map, kernel_size=3)(
            mid_emb)  # [batch_size,maxlen,word_emb_size+2*pos_emb_size(10)]
        mid = tf.keras.layers.GlobalMaxPool1D()(mid)  # [batch_size,feature_map]
        right = tf.keras.layers.Conv1D(filters=feature_map, kernel_size=3)(
            right_emb)  # [batch_size,maxlen,word_emb_size+2*pos_emb_size(10)]
        right = tf.keras.layers.GlobalMaxPool1D()(right)  # [batch_size,feature_map]
        final_feature = tf.concat([left, mid, right], 1)  # [batch_size,3*feature_map]
        out = tf.keras.layers.Dense(n_class, activation="softmax")(final_feature)  # [batch_size,n_class]
        return out
