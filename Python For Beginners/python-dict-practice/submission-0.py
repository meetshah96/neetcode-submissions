from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count_char = {}
    for k in word:
        count_char[k] = count_char.get(k,0) + 1
    return count_char




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
