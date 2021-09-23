# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from collections import defaultdict


# compares two words to determine if they're similar
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




def similar(words):

    d = defaultdict(list)
    seen = set()

    for i in range(len(words)):
        word1 = words[i]

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
