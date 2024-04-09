from typing import List


class Naive:
    def __init__(self):
        self.counter = 0

    def find(self, text: str, pattern: str) -> List[int]:
        self.counter = 0
        found_indicies = []

        for index in range(len(text)):
            i = 0
            for letter in pattern:
                self.counter += 1
                if letter != text[index + i]:
                    break
                i += 1

            self.counter += 1
            if i == len(pattern):
                found_indicies.append(index)

        return found_indicies

    def get_operations_count(self) -> int:
        return self.counter


if __name__ == "__main__":
    naive = NaiveClass()
    naive.find()
