# This file has some test cases for LRU.py
import LRU

input_1 = [("lru", 2), ('put',(1, 1)), ('get', 1), ('put', (2, 3)), ('put', (3, 5)), ('get', 1), ('get', 3)]
output_1 = [None, None, 1, None, None, -1, 5]

input_2 = [("lru",1), ('put',(1, 1)), ('get', 1), ('put', (2, 3)), ('put', (3, 5)), ('get', 2), ('get', 3)]
output_2 = [None, None, 1, None, None, -1, 5]

input_list = [input_1, input_2]
output_list = [output_1, output_2]

def verify() -> bool:

    lru = None
    
    for i in range(len(input_list)):
        inputs, outputs = input_list[i], output_list[i]
        for input, output in zip(inputs, outputs):
            if input[0] == 'lru':
                lru = LRU.LRUCache(input[1])
            elif input[0] == 'put':
                ret_val = lru.put(*input[1])
                if ret_val != output:
                    return False
                
            elif input[0] == 'get':
                ret_val = lru.get(input[1])
                if ret_val != output:
                    return False
        print(f"passed test {i + 1}")
    return True

print(verify())