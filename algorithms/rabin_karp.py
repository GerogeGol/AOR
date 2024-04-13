from algorithms.utils import compare_builtin


class RabinKarp:
    def __init__(self, alphabet_size: int, mod: int, comparator=compare_builtin):
        self.alphabet_size = alphabet_size
        self.mod = mod
        self.counter = 0
        self.preprocessing_time = 0
        self.comparator = comparator

    def hash(self, string: str):
        alphabet_size = self.alphabet_size
        mod = self.mod

        val = 0
        for s in string[:-1]:
            val = ((val + ord(s)) % mod) * alphabet_size

        val = (val + ord(string[-1])) % mod
        return val

    def preprocessing(self, pattern: str):
        self.pattern_hash = self.hash(pattern)
        self.pattern_size = len(pattern)
        self.last_multiplier = pow(self.alphabet_size, self.pattern_size - 1, self.mod)

    def find(self, text: str, pattern: str) -> int:
        self.counter = 0

        alphabet_size = self.alphabet_size
        mod = self.mod

        pattern_hash = self.pattern_hash
        pattern_size = self.pattern_size
        compare = self.comparator

        text_hash = self.hash(text[:pattern_size])

        found_indicies = []
        self.counter += 1
        if pattern_hash == text_hash:
            equal, count = compare(pattern, text[:pattern_size])
            self.counter += count
            self.counter += 1
            if equal:
                found_indicies.append(0)

        for i in range(1, len(text) - pattern_size + 1):
            sub_symbol = ord(text[i - 1])
            add_symbol = ord(text[i + pattern_size - 1])

            text_hash = (
                (text_hash - (sub_symbol * self.last_multiplier) % mod) * alphabet_size
                + add_symbol
            ) % mod

            self.counter += 1
            if text_hash == pattern_hash:
                equal, count = compare(pattern, text[i : i + pattern_size])
                self.counter += count
                self.counter += 1
                if equal:
                    found_indicies.append(i)

        return found_indicies

    def get_operations_count(self) -> int:
        return self.counter


if __name__ == "__main__":
    rk = RabinKarp(256, 9973)
    print(rk.find("babcabc", "abc"))
    print(rk.find("абобабава", "абоб"))
