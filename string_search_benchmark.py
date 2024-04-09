import time

from kmp import KnuthMorrisPratt


class StringSearchBenchmark:
    def __init__(self, algorithms, num_runs_per_test=100):
        self.algorithms = algorithms
        self.num_runs_per_test = num_runs_per_test

    def benchmark(self, text, pattern):
        results = {}

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

            avg_time = sum(algorithm_times) / len(algorithm_times)
            results[type(algorithm).__name__] = {
                "avg_time": avg_time,
                "operations_count": sum(operations_counts) / len(operations_counts) if operations_counts else None
            }

        return results


if __name__ == "__main__":
    naive = Naive()
    kmp = KnuthMorrisPratt()
    rabin_karp = RabinKarp()

    algorithms = [naive, kmp, rabin_karp]

    ssb = StringSearchBenchmark(algorithms)

    text = "This is a test string for benchmarking."
    pattern = "test"

    results = ssb.benchmark(text, pattern)

    for algorithm, time_taken, op_counts in results.items():
        print(f"{algorithm}: {time_taken} seconds, {op_counts} comparisons")
