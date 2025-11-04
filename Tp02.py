import random
import time
import matplotlib.pyplot as plt

# ---------- Array Generation ----------
def create_array(n, mode):
    if mode == 'A':
        return list(range(n))
    elif mode == 'D':
        return list(range(n, 0, -1))
    return [random.randint(0, n) for _ in range(n)]

# ---------- Sorting Algorithms ----------
def selection_sort(T):
    n = len(T)
    cmp = swp = 0
    for i in range(n - 1):
        min_i = i
        for j in range(i + 1, n):
            cmp += 1
            if T[j] < T[min_i]:
                min_i = j
        if min_i != i:
            T[i], T[min_i] = T[min_i], T[i]
            swp += 1
    return cmp, swp

def bubble_sort(T):
    n = len(T)
    cmp = swp = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            cmp += 1
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                swp += 1
    return cmp, swp

def insertion_sort(T):
    cmp = swp = 0
    for i in range(1, len(T)):
        key = T[i]
        j = i - 1
        while j >= 0 and T[j] > key:
            cmp += 1
            T[j + 1] = T[j]
            swp += 1
            j -= 1
        if j >= 0:
            cmp += 1
        T[j + 1] = key
    return cmp, swp

def exchange_sort(T):
    n = len(T)
    cmp = swp = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            cmp += 1
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
                swp += 1
    return cmp, swp

# ---------- Performance Measurement ----------
def average(algo, n, mode, runs=30):
    total_cmp = total_swp = total_t = 0
    for _ in range(runs):
        T = create_array(n, mode)
        start = time.process_time_ns()
        c, s = algo(T[:])
        end = time.process_time_ns()
        total_cmp += c
        total_swp += s
        total_t += (end - start)
    return total_cmp / runs, total_swp / runs, total_t / runs

# ---------- Configuration ----------
algos = {
    "Selection": selection_sort,
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Exchange": exchange_sort
}

modes = {'A': 'Ascending', 'D': 'Descending', 'R': 'Random'}
sizes = [10, 100, 1000]

# ---------- Run Experiments ----------
results = {}

for m, m_name in modes.items():
    results[m_name] = {}
    for name, algo in algos.items():
        results[m_name][name] = []
        for n in sizes:
            c, s, t = average(algo, n, m)
            results[m_name][name].append((c, s, t))

# ---------- Print Results ----------
for n in sizes:
    print(f"\n--- Array size: {n} ---")
    for m_name in modes.values():
        print(f"\nCase: {m_name}")
        for algo_name in algos:
            idx = sizes.index(n)
            c, s, t = results[m_name][algo_name][idx]
            print(f"{algo_name:10s} | Comparisons: {c:.1f} | Swaps: {s:.1f} | Time: {t/1e9:.6f}s")

# ---------- Plot Results ----------
plt.figure(figsize=(10, 6))
for m_name, algo_data in results.items():
    for algo_name, metrics in algo_data.items():
        times = [t for (_, _, t) in metrics]
        plt.plot(sizes, times, marker='o', label=f"{algo_name} - {m_name}")

plt.title("Execution Time Comparison (All Modes)")
plt.xlabel("Array Size")
plt.ylabel("Average Time (ns)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

