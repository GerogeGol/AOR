class NaiveClass:
    def __init__(self):
        self.counter = 0

    def find(self, text: str, pattern: str):
        self.counter = 0
        for index in range(len(text)):
            i = 0
            for letter in pattern:
                if letter != text[index + i]:
                    break
                i += 1
            self.counter += 1
            if i == len(pattern):
                return index
        return -1

    def get_operations_count(self) -> int:
        return self.counter


if __name__ == '__main__':
    naive = NaiveClass()
    naive.find()
