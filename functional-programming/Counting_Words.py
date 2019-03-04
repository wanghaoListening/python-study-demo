import re


def count_words(filename):
    """
    Count the number of times every word in the file `filename`
    is contained in this file.

    Args:
        filename (str): the filename to count the words in

    Returns:
        dict: a mapping of word to count
    """

    all_words = {}

    with open(filename) as f:
        for line in f:
            words = line.split()

            for word in words:
                #lowercase the word and remove all
                #characters that are not [a-z] or hyphen
                word = word.lower()
                match = re.search(r"([a-z\-]+)", word)

                if match:
                    word = match.groups()[0]

                    if word in all_words:
                        all_words[word] += 1
                    else:
                        all_words[word] = 1

    return all_words




def reduce_dicts(dict1, dict2):
    """
    Combine (reduce) the passed two dictionaries to return
    a dictionary that contains the keys of both, where the
    values are equal to the sum of values for each key
    """

    # explicitly copy the dictionary, as otherwise
    # we risk modifying 'dict1'
    combined = {}

    for key in dict1:
        combined[key] = dict1[key]

    for key in dict2:
        if key in combined:
            combined[key] += dict2[key]
        else:
            combined[key] = dict2[key]

    return combined






if __name__ == '__main__':
    count = count_words('/Users/admin/test.txt')
    print(count)