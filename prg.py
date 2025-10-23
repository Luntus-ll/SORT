
import time
import random

def bubble(arr):
    st = time.time()
    n = len(arr)
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    elapsed_time = time.time() - st
    return arr, comparisons, swaps, elapsed_time

def select(arr):
    st = time.time()
    n = len(arr)
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    elapsed_time = time.time() - st
    return arr, comparisons, swaps, elapsed_time

def insert(arr):
    st = time.time()
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
    elapsed_time = time.time() - st
    return arr, comparisons, swaps, elapsed_time

def generate(size):
    ascending = list(range(1, size + 1))
    descending = list(range(size, 0, -1))
    random_arr = [random.randint(1, 1000) for _ in range(size)]
    return ascending, descending, random_arr

def main():
    size = 10
    ascending, descending, random_array = generate(size)
    test_arr = {
        "По возрастанию": ascending,
        "По убыванию": descending,
        "Случайный": random_array
    }

    print(f"{'Массив':15} | {'Bubble sort':12} | {'Selection sort':14} | {'Insertion sort':14}")
    

    algorithms = [
        ("Bubble Sort", bubble),
        ("Selection Sort", select),
        ("Insertion Sort", insert)
    ]

    for description, array in test_arr.items():
        row = f"{description:15} |"
        for name, func in algorithms:
            array_copy = array.copy()
            sorted_arr, comp, swaps, elapsed_time = func(array_copy)
            row += f" Сравнения:{comp:4} Перестановки:{swaps:4} Время:{elapsed_time:.4f} секунд |"
        print(row)

if __name__ == "__main__":
    main()
