from typing import List
from algorithms.utils import compare_builtin


class Naive:
    def __init__(self, comparator=compare_builtin):
        self.counter = 0
        self.comparator = comparator

    def preprocessing(self, pattern: str):
        return

    def find(self, text: str, pattern: str) -> List[int]:
        self.counter = 0
        pattern_size = len(pattern)
        found_indicies = []

        for index in range(len(text) - pattern_size + 1):
            equal, count = self.comparator(pattern, text[index : index + pattern_size])
            self.counter += count
            self.counter += 1
            if equal:
                found_indicies.append(index)

        return found_indicies

    def get_operations_count(self) -> int:
        return self.counter


if __name__ == "__main__":
    naive = NaiveClass()
    naive.find()
