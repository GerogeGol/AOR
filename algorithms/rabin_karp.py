class RabinKarp:
    def __init__(self, alphabet_size: int, mod: int):
        self.alphabet_size = alphabet_size
        self.mod = mod
        self.counter = 0

    def hash(self, string: str):
        alphabet_size = self.alphabet_size
        mod = self.mod

        val = 0
        for s in string[:-1]:
            val = ((val + ord(s)) % mod) * alphabet_size

        val = (val + ord(string[-1])) % mod
        return val

    def find(self, text: str, pattern: str) -> int:
        self.counter = 0
        found_indicies = []

        alphabet_size = self.alphabet_size
        mod = self.mod

        pattern_hash = self.hash(pattern)
        pattern_size = len(pattern)

        text_hash = self.hash(text[:pattern_size])

        self.counter += 1
        if pattern_hash == text_hash and pattern == text[:pattern_size]:
            found_indicies.append(0)

        for i in range(1, len(text) - pattern_size + 1):
            sub_symbol = ord(text[i - 1])
            add_symbol = ord(text[i + pattern_size - 1])

            text_hash -= (sub_symbol * alphabet_size ** (pattern_size - 1)) % mod
            text_hash *= alphabet_size
            text_hash += add_symbol
            text_hash %= mod

            self.counter += 1
            if text_hash == pattern_hash and pattern == text[i : i + pattern_size]:
                found_indicies.append(i)

        return found_indicies

    def get_operations_count(self) -> int:
        return self.counter


if __name__ == "__main__":
    rk = RobinKarp(256, 9973)
    print(rk.find("babcabc", "abc"))
    print(rk.find("абобабава", "абоб"))
