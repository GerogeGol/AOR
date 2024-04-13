from typing import List


class KnuthMorrisPratt:
    counter: int = 0

    def calculate_prefix_function(self, sample: str) -> List[int]:
        sample_size = len(sample)
        prefix_f_values = [0] * sample_size

        k = 0
        for i in range(1, sample_size):
            while k > 0 and sample[i] != sample[k]:
                k = prefix_f_values[k - 1]
            if sample[i] == sample[k]:
                k += 1

            prefix_f_values[i] = k

        return prefix_f_values

    def preprocessing(self, sample: str):
        self.prefix_f_values = self.calculate_prefix_function(sample)
        self.sample_size = len(sample)

    def find(self, text: str, sample: str) -> List[int]:
        self.counter = 0
        self.in_loop = 0
        prefix_f_values = self.prefix_f_values
        sample_size = self.sample_size

        found_indices = []

        k = 0
        for i in range(len(text)):
            self.counter += 1
            self.in_loop += 1
            while k > 0 and sample[k] != text[i]:
                self.counter += 1
                k = prefix_f_values[k - 1]

            self.counter += 1
            if sample[k] == text[i]:
                k += 1

            self.counter += 1
            if k == sample_size:
                index = i - sample_size + 1
                found_indices.append(index)
                k = 0

        return found_indices

    def get_operations_count(self):
        return self.counter - self.in_loop


if __name__ == "__main__":
    kmp = KnuthMorrisPratt()
    text: str = "abcdabcabcdabcdab"
    sample: str = "abc"
    print(kmp.find(text, sample))
    print(kmp.get_operations_count())

    text: str = "abcdabcabcdabcdab"
    sample: str = "abc"
    print(kmp.find(text, sample))
    print(kmp.get_operations_count())
