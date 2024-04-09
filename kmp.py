from typing import List


class KnuthMorrisPratt:
    counter: int = 0

    def calculate_prefix_function(self, sample: str) -> List[int]:
        sample_size = len(sample)
        prefix_f_values = [0] * sample_size
        last_f_value: int = 0

        for i in range(1, sample_size):
            if sample[i] == sample[last_f_value]:
                self.counter += 1
                last_f_value += 1
                prefix_f_values[i] = last_f_value
                i += 1
            else:
                if last_f_value != 0:
                    last_f_value = prefix_f_values[last_f_value - 1]
                else:
                    prefix_f_values[i] = 0
                    i += 1

        return prefix_f_values

    def find(self, text: str, sample: str) -> List[int]:
        self.counter = 0
        prefix_f_values = self.calculate_prefix_function(sample)
        text_size = len(text)
        sample_size = len(sample)

        curr_index_sample: int = 0
        curr_index_text: int = 0

        found_indices = []

        while text_size - curr_index_text >= sample_size - curr_index_sample:
            if sample[curr_index_sample] == text[curr_index_text]:
                self.counter += 1
                curr_index_sample += 1
                curr_index_text += 1

            if curr_index_sample == sample_size:
                found_indices.append(curr_index_text - curr_index_sample)
                curr_index_sample = prefix_f_values[curr_index_sample - 1]
            elif curr_index_text < text_size and sample[curr_index_sample] != text[curr_index_text]:
                self.counter += 1
                if curr_index_sample != 0:
                    curr_index_sample = prefix_f_values[curr_index_sample - 1]
                else:
                    curr_index_text += 1

        return found_indices

    def get_operations_count(self):
        return self.counter


if __name__ == "__main__":
    kmp = KnuthMorrisPratt()
    text: str = 'abcdabcabcdabcdab'
    sample: str = 'abc'
    print(kmp.find(text, sample))
    print(kmp.get_operations_count())
