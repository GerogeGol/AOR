import time
from pathlib import Path

from algorithms.kmp import KnuthMorrisPratt
from algorithms.rabin_karp import RabinKarp
from algorithms.naive import Naive

PATH_TO_BENCHMARKS = Path("./benchmarks")


class StringSearchBenchmark:
    def __init__(self, algorithms, num_runs_per_test=100):
        self.algorithms = algorithms
        self.num_runs_per_test = num_runs_per_test

    def benchmark(self, text, pattern):
        results = {}
        answers = []
        for algorithm in self.algorithms:
            algorithm_times = []
            operations_counts = []

            for _ in range(self.num_runs_per_test):
                start_time = time.time()
                result = algorithm.find(text, pattern)
                end_time = time.time()
                algorithm_times.append(end_time - start_time)

                if hasattr(algorithm, "get_operations_count"):
                    operations_counts.append(algorithm.get_operations_count())

            answers.append(result)
            if len(answers) != 1:
                for i, el1 in enumerate(answers):
                    for j, el2 in enumerate(answers):
                        if el1 != el2:
                            raise Exception(f"{i} {el1 = } != {j} {el2 = }")

            avg_time = sum(algorithm_times) / len(algorithm_times)
            results[type(algorithm).__name__] = {
                "avg_time": avg_time,
                "operations_count": sum(operations_counts) / len(operations_counts)
                if operations_counts
                else None,
            }

        return results


if __name__ == "__main__":
    naive = Naive()
    kmp = KnuthMorrisPratt()
    rabin_karp = RabinKarp(1000, 9973)

    algorithms = [naive, kmp, rabin_karp]

    ssb = StringSearchBenchmark(algorithms)

    for begin in ("bad", "good"):
        for i in range(1, 5):
            t_name = f"{begin}_t_{i}.txt"
            w_name = f"{begin}_w_{i}.txt"

            t_ind = PATH_TO_BENCHMARKS / t_name
            w_ind = PATH_TO_BENCHMARKS / w_name
            with open(t_ind, "r", encoding="utf-8") as f_file, open(
                w_ind, "r", encoding="utf-8"
            ) as s_file:
                text = f_file.read()
                pattern = s_file.read()

            results = ssb.benchmark(text, pattern)
            print(f"Benchmark file: {t_name}")
            print(f"Length of text: {len(text)}")
            print(f"Length of pattern: {len(pattern)}")
            print()
            for algorithm, values in results.items():
                print(
                    f"{algorithm:16}:\t{values['avg_time']} ms,\t{values['operations_count']} comparisons"
                )
            print()
