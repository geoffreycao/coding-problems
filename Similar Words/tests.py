import sys
sys.path.insert(0, 'main.py')
import main

input_1 = ["cat", "dog", "man", "aabbcc", "aabbxxyy", "tat", "dad"]
output_1 = \
[
    ["cat", "dog", "man"],
    ["aabbcc"],
    ["aabbxxyy"],
    ["tat", "dad"]
]

input_2 = ["abc", "cde", "def", "aabbcc", "aabbaa"]
output_2 = \
[
    ["abc", "cde", "def"],
    ["aabbcc"],
    ["aabbaa"]
]

input_3 = ["abc", "aba"]
output_3 = [["abc"], ["aba"]]

def verify() -> bool:
    inputs = [input_1, input_2, input_3]
    outputs = [output_1, output_2, output_3]

    for input, output in zip(inputs, outputs):
        result = main.similar(input)
        print(f"result: {result}")
        for i in range(len(result)):
            r_words = result[i]
            if len(r_words) != len(output[i]):
                return False
            for word1, word2 in zip(sorted(r_words), sorted(output[i])):
                if word1 != word2:
                    return False

    return True


print(verify())