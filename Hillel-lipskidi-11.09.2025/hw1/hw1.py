def string_length(s: str) -> int:
    return len(s)

def concatenate(a: str, b: str) -> str:
    return a + b
print("strings is ok")


def square(x: int | float) -> int | float:
    return x * x

def add(a: int | float, b: int | float) -> int | float:
    return a + b

def div_and_mod(a: int, b: int) -> tuple[int, int]:
    return divmod(a, b)
print("int n float is ok")


from typing import List, Union

def average(numbers: List[Union[int, float]]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def common_elements(list1: List[Union[int, float, str]], list2: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result
print("lists is ok")


def print_keys(d: dict) -> None:
    for key in d.keys():
        print(key)

def merge_dicts(d1: dict, d2: dict) -> dict:
    merged = d1.copy()
    merged.update(d2)
    return merged
print("dict is ok")


def union_sets(a: set, b: set) -> set:
    return a.union(b)
def is_subset(a: set, b: set) -> bool:
    return a.issubset(b)
print("sets is ok")


def even_or_odd(n: int) -> str:
    if n % 2 == 0:
        return "Paired"
    else:
        return "Unpaired"
def filter_even(numbers: list[int]) -> list[int]:
    return [x for x in numbers if x % 2 == 0]
print("cycle is ok")