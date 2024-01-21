import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def move_file(source_path, destination_folder):
    """
    Переміщення файлу з вказаного джерела до вказаної папки при використанні shutil.move.
    """
    try:
        shutil.move(str(source_path), str(destination_folder))
        print(f"Moved: {source_path} to {destination_folder}")
    except Exception as e:
        print(f"Error moving {source_path}: {e}")

def process_folder(root_folder, destination_root, num_threads):
    """
    Опрацювання папки та сортування файлів за розширенням з використанням багатьох потоків.

    Args:
        root_folder (str): Шлях до вихідної папки.
        destination_root (str): Шлях до кореневої папки для сортування файлів за розширенням.
        num_threads (int): Кількість потоків для паралельної обробки файлів.

    """
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Перетворення шляху в Path об'єкт для роботи з pathlib
        root_path = Path(root_folder)

        # Рекурсивне сканування всіх файлів та папок у вихідній папці
        for source_path in root_path.rglob("*"):
            if source_path.is_file():
                # Визначення розширення файлу та папки призначення для розміщення
                file_extension = source_path.suffix.lower()
                destination_folder = Path(destination_root) / file_extension[1:]
                
                # Створення папки призначення, якщо вона ще не існує
                destination_folder.mkdir(parents=True, exist_ok=True)

                # Виклик функції move_file в окремому потоці для паралельного переміщення файлів
                executor.submit(move_file, source_path, destination_folder)

if __name__ == "__main__":
    # Запитати користувача про шлях до папки
    source_folder = input("Введіть шлях до папки, яку ви хочете сортувати: ")

    # Перевірка, чи існує введений шлях
    if not Path(source_folder).exists():
        print(f"Папка {source_folder} не існує.")
    else:
        # Шлях до кореневої папки для сортування файлів за розширенням
        destination_root_folder = "Сортовані файли"
        num_threads = 4

        Path(destination_root_folder).mkdir(parents=True, exist_ok=True)

        process_folder(source_folder, destination_root_folder, num_threads)