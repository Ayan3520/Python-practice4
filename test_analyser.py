"""
============================================================
ФАЙЛ: main.py
ЗАДАЧА: Главный файл программы — оркестратор.

Practice 7 (Advanced OOP) + Practice 8 (Modules, Packages, Tests)
Вариант D: TopStudentsAnalyser — Топ-10 студентов по баллу за экзамен.

ПРАВИЛО main.py (по заданию Practice 8):
  main.py НЕ содержит определений классов — только импорты и вызовы.
  Все классы находятся в пакете analytics/.

СТРУКТУРА ПРОЕКТА:
  project/
  ├── main.py                  ← вы здесь
  ├── students.csv             ← ваш датасет
  ├── output/
  │   └── result.json          ← результат анализа
  ├── analytics/               ← пакет (Package)
  │   ├── __init__.py
  │   ├── file_manager.py      ← class FileManager
  │   ├── data_loader.py       ← class DataLoader
  │   ├── analyser.py          ← class DataAnalyser, TopStudentsAnalyser, CountryAnalyser
  │   ├── result_saver.py      ← class ResultSaver
  │   └── report.py            ← class Report
  └── tests/
      ├── __init__.py
      └── test_analyser.py     ← 4 unit tests
============================================================
"""

# ── ИМПОРТЫ ИЗ ПАКЕТА ──────────────────────────────────────
# from analytics import ... → Python ищет analytics/__init__.py
# и берёт оттуда уже импортированные классы.
# Это удобно: один источник истины для всех импортов пакета.
from analytics import FileManager, DataLoader, ResultSaver, Report

# Дочерний класс Варианта D импортируем явно из модуля analyser
# (так показано в задании Practice 8)
from analytics.analyser import TopStudentsAnalyser, CountryAnalyser


def main():
    """
    Главная функция — оркестрирует весь процесс.
    
    Разбита на логические шаги, которые соответствуют задачам:
    - Шаг 1: FileManager  (Practice 6 / 7)
    - Шаг 2: DataLoader   (Practice 6 / 7)
    - Шаг 3: Полиморфизм  (Task 5, Practice 7)
    - Шаг 4: Report       (Task 4, Practice 7)
    """

    # ── Имя вашего CSV-файла (замените на своё) ────────────
    input_file  = 'global_university_students_performance_habits_10000 (3).csv'
    output_file = 'output/result.json'

    # ══════════════════════════════════════════════════════
    # ШАГ 1: ФАЙЛОВАЯ СИСТЕМА (FileManager)
    # ══════════════════════════════════════════════════════
    print("\n" + "="*55)
    print("  STEP 1: File System Check")
    print("="*55)

    fm = FileManager(input_file)
    if not fm.check_file():
        # Если файл не найден — прерываем программу.
        # return в main() эквивалентен выходу из программы.
        print("Program stopped: input file not found.")
        return
    fm.create_output_folder()

    # ══════════════════════════════════════════════════════
    # ШАГ 2: ЗАГРУЗКА ДАННЫХ (DataLoader)
    # ══════════════════════════════════════════════════════
    print("\n" + "="*55)
    print("  STEP 2: Loading Data")
    print("="*55)

    dl = DataLoader(input_file)
    data = dl.load()
    if not data:
        print("No data to process. Program stopped.")
        return
    dl.preview()

    # ══════════════════════════════════════════════════════
    # ШАГ 3: ПОЛИМОРФИЗМ (Task 5, Practice 7)
    # Создаём список из двух разных анализаторов.
    # Один цикл — одинаковые вызовы — разное поведение.
    # ══════════════════════════════════════════════════════
    print("\n" + "="*55)
    print("  STEP 3: Polymorphism Demonstration")
    print("="*55)

    # Создаём объекты двух разных дочерних классов
    main_analyser    = TopStudentsAnalyser(data)          # Вариант D
    country_analyser = CountryAnalyser(data[:100])        # Вариант B (на 100 строках для краткости)

    # Помещаем их в общий список — это и есть полиморфизм
    analysers = [main_analyser, country_analyser]

    print("\n" + "-" * 55)
    print("  Running all analysers:")
    print("-" * 55)

    for a in analysers:
        # __str__: print(a) вызывает a.__str__() — разный текст для каждого класса
        print(f"\n→ {a}")
        # analyse() и print_results() — одинаковые имена, разная реализация
        # Цикл НЕ знает, какой класс перед ним — это и есть полиморфизм
        a.analyse()
        a.print_results()

    # ══════════════════════════════════════════════════════
    # ШАГ 4: REPORT — Ассоциация (Task 4, Practice 7)
    # Report USES-A TopStudentsAnalyser + USES-A ResultSaver
    # ══════════════════════════════════════════════════════
    print("\n" + "="*55)
    print("  STEP 4: Report (Association / USES-A)")
    print("="*55)

    # ResultSaver принимает данные и путь к файлу
    saver = ResultSaver(main_analyser.result, output_file)

    # Report не наследует — он использует (ассоциация)
    report = Report(main_analyser, saver)
    report.generate()

    print("\n✓ Program finished successfully.")


# ── ТОЧКА ВХОДА ────────────────────────────────────────────
# if __name__ == "__main__": гарантирует, что main() вызывается
# ТОЛЬКО при прямом запуске файла (python main.py),
# но НЕ при импорте этого файла другим модулем.
if __name__ == "__main__":
    main()
