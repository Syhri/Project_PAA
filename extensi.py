# Syahril Fitrawan Abadi_F55123054
import random
import time
import matplotlib.pyplot as plt

def generate_array(size, max_value=160, seed=42):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(size)]

def is_unique(array):
    return len(array) == len(set(array))

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time

def main():
    sizes = [100, 150, 200, 250, 300, 350, 400, 500]
    max_value = 160
    seed = 42

    worst_case_durations = []
    average_case_durations = []

    for size in sizes:
        array = generate_array(size, max_value, seed)
        worst_case_array = [1] * size

        worst_case_durations.append(measure_time(is_unique, worst_case_array))
        average_case_durations.append(measure_time(is_unique, array))

        print(f"Size = {size}, Worst: {worst_case_durations[-1]:.10f} s, Avg: {average_case_durations[-1]:.10f} s")

    plt.plot(sizes, worst_case_durations, 'ro-', label='Worst Case')
    plt.plot(sizes, average_case_durations, 'bs-', label='Average Case')
    plt.title('Performance: Worst vs Average Case')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
