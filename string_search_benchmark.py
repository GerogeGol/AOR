import time
from pathlib import Path

from algorithms.kmp import KnuthMorrisPratt
from algorithms.rabin_karp import RabinKarp
from algorithms.naive import Naive
from algorithms.utils import compare, compare_builtin

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

            algorithm.preprocessing(pattern)

            for _ in range(self.num_runs_per_test):
                start_time = time.time()
                result = algorithm.find(text, pattern)
                end_time = time.time()
                algorithm_times.append(end_time - start_time)

                if hasattr(algorithm, "get_operations_count"):
                    operations_counts.append(algorithm.get_operations_count())

            answers.append(result)

            avg_time = sum(algorithm_times) / len(algorithm_times) * 1000
            results[type(algorithm).__name__] = {
                "avg_time": avg_time,
                "operations_count": sum(operations_counts) / len(operations_counts)
                if operations_counts
                else None,
            }

        if not self.check_answers(answers):
            raise Exception()

        return results

    def check_answers(self, answers: list[list[int]]) -> bool:
        for i, el1 in enumerate(answers):
            for j, el2 in enumerate(answers):
                if el1 != el2:
                    return False
        return True


def benchmark(ssb, algorithms, filename):
    with open(filename, "w") as out:
        experiment_files = []
        for begin in ("bad", "good"):
            for i in range(1, 5):
                t_name = f"{begin}_t_{i}.txt"
                w_name = f"{begin}_w_{i}.txt"

                t_ind = PATH_TO_BENCHMARKS / t_name
                w_ind = PATH_TO_BENCHMARKS / w_name

                experiment_files.append((t_ind, w_ind))

        print(
            "File",
            "Text Length",
            "Pattern length",
            "Naive avg_time",
            "KMP avg_time",
            "RabinKarp avg_time",
            "Naive comparisons",
            "KMP comparisons",
            "RabinKarp comparisons",
            sep=",",
            file=out,
        )
        for text_file, word_file in experiment_files:
            with open(text_file, "r", encoding="utf-8") as f_file, open(
                word_file, "r", encoding="utf-8"
            ) as s_file:
                text = f_file.read()
                pattern = s_file.read()

            results = ssb.benchmark(text, pattern)
            naive = results["Naive"]
            kmp = results["KnuthMorrisPratt"]
            rabin_karp = results["RabinKarp"]
            print(
                text_file.name,
                len(text),
                len(pattern),
                naive["avg_time"],
                kmp["avg_time"],
                rabin_karp["avg_time"],
                naive["operations_count"],
                kmp["operations_count"],
                rabin_karp["operations_count"],
                sep=",",
                file=out,
            )


if __name__ == "__main__":
    comparator = compare_builtin
    naive = Naive(comparator=comparator)
    kmp = KnuthMorrisPratt()
    rabin_karp = RabinKarp(100, 6700417, comparator=comparator)

    algorithms = [naive, kmp, rabin_karp]
    ssb = StringSearchBenchmark(algorithms, 1000)

    benchmark(ssb, algorithms, "builtin_comparator.csv")

    print("builtin ended")

    comparator = compare

    naive = Naive(comparator=comparator)
    kmp = KnuthMorrisPratt()
    rabin_karp = RabinKarp(100, 6700417, comparator=comparator)

    algorithms = [naive, kmp, rabin_karp]
    ssb = StringSearchBenchmark(algorithms, 1000)

    benchmark(ssb, algorithms, "for_loop_comparator.csv")
