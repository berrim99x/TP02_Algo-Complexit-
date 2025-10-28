import random, time

def create_array(n, mode):
    if mode == 'A':
        return list(range(n))
    elif mode == 'D':
        return list(range(n, 0, -1))
    else:
        return [random.randint(0, n) for _ in range(n)]

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

def average(algo, n, mode):
    total_cmp = total_swp = total_t = 0
    for _ in range(30):
        T = create_array(n, mode)
        start = time.time()
        c, s = algo(T[:])
        end = time.time()
        total_cmp += c
        total_swp += s
        total_t += (end - start)
    return total_cmp / 30, total_swp / 30, total_t / 30

algos = {
    "Selection": selection_sort,
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Exchange": exchange_sort
}

modes = {'A': 'Ascending', 'D': 'Descending', 'R': 'Random'}
sizes = [10, 100, 1000]

for n in sizes:
    print(f"\n--- Array size: {n} ---")
    for m, m_name in modes.items():
        print(f"\nCase: {m_name}")
        for name, f in algos.items():
            c, d, t = average(f, n, m)
            print(f"{name:10s} | Comparisons: {c:.1f} | Swaps: {d:.1f} | Time: {t:.6f}s")
