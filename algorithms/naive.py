from typing import List


class Naive:
    def __init__(self):
        self.counter = 0

    def find(self, text: str, pattern: str) -> List[int]:
        self.counter = 0
        pattern_size = len(pattern)
        found_indicies = []

        for index in range(len(text) - pattern_size + 1):
            if pattern == text[index : index + pattern_size]:
                found_indicies.append(index)

        return found_indicies

    def get_operations_count(self) -> int:
        return self.counter


if __name__ == "__main__":
    naive = NaiveClass()
    naive.find()
