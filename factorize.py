import time

# Спочатку реалізуємо синхронну версію функції factorize:

def factorize_sync(*numbers):
    start_time = time.time()
    result = []
    for num in numbers:
        factors = [i for i in range(1, num + 1) if num % i == 0]
        result.append(factors)
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")
    return result

#Перевіримо правильність роботи цієї функції:

def test_factorize_sync():
    try:
        start_time = time.time()
        a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
        assert a == [1, 2, 4, 8, 16, 32, 64, 128]
        assert b == [1, 3, 5, 15, 17, 51, 85, 255]
        assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
        assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
        end_time = time.time()
        print(f"All assertions passed successfully. The function is correct. Execution time: {end_time - start_time} seconds")
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == '__main__':
    test_factorize_sync()

#Реалізуємо покращену версію, яка використовує паралельні обчислення з використанням багатьох ядер процесора:

import multiprocessing

def factorize_parallel(*numbers):
    start_time = time.time()
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        result = pool.map(factorize_single, numbers)
    end_time = time.time()
    print(f"Parallel execution time: {end_time - start_time} seconds")
    return result

def factorize_single(num):
    return [i for i in range(1, num + 1) if num % i == 0]

#Перевіримо правильність роботи цієї функції:

def test_factorize_parallel():
    try:
        start_time = time.time()
        a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
        assert a == [1, 2, 4, 8, 16, 32, 64, 128]
        assert b == [1, 3, 5, 15, 17, 51, 85, 255]
        assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
        assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
        end_time = time.time()
        print(f"All assertions passed successfully. The function is correct. Execution time: {end_time - start_time} seconds")
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == '__main__':
    test_factorize_parallel()