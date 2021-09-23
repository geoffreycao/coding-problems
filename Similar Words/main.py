from collections import defaultdict



'''
Given a list of words, group words that are similar into a group, return the groups of words.
Similar is defined as each letter in word1 maps one-to-one to a letter in word2.

If two words have a different length, then they are not similar
'''



# Compares two words to determine if they're similar
def compare(word1, word2):
    m1 = [-1] * 26
    m2 = [-1] * 26

    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        c1 = ord(word1[i]) - ord('a')
        c2 = ord(word2[i]) - ord('a')

        if (m1[c1] != -1 and m1[c1] != c2) or (m2[c2] != -1 and m2[c2] != c1):
            return False
        else:
            m1[c1] = c2
            m2[c2] = c1
    return m1



# Uses compare() to compare all words in a pairwise fashion, O(n^2)
def similar(words):

    d = defaultdict(list)

    # 'seen' hashset keeps track of which words we have already visited
    seen = set()

    for i in range(len(words)):
        word1 = words[i]

        # starting at i, and not i + 1, as we still need to add each word to its own entry (a list) in the dictionary
        for j in range(i, len(words)):
            word2 = words[j]
            if word2 in seen:
                continue
            if compare(word1, word2):
                d[word1].append(word2)
                seen.add(word2)

        seen.add(word1)
    ret = []
    for values in d.values():
        ret.append(values)

    return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["cat", "dog", "man", "aabbcc", "aabbxxyy", "tat", "dad"]
    similar(words)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
