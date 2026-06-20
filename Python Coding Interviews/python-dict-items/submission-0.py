from typing import Dict, List, Tuple


def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    in_tuple = []
    for k, v in age_dict.items():
        in_tuple.append((k,v))
    return in_tuple

# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
