# ============================================================
# ФАЙЛ: analytics/__init__.py
# ЗАДАЧА: Превращает папку analytics/ в Python-пакет (Package).
#         Task 2, Practice 8.
# ============================================================
#
# Что такое __init__.py?
# Когда Python видит папку с __init__.py внутри, он считает её ПАКЕТОМ.
# Это позволяет делать импорт вида: from analytics import FileManager
#
# Относительные импорты (с точкой):
# from .file_manager import FileManager
#        ↑ точка означает "из текущего пакета" (analytics/)
# Это нужно, чтобы модули внутри пакета находили друг друга корректно.
#
# После этих импортов в __init__.py, пользователь пакета может писать:
#   from analytics import FileManager
# вместо более длинного:
#   from analytics.file_manager import FileManager
# ============================================================

from .file_manager import FileManager
from .data_loader import DataLoader
from .analyser import DataAnalyser, TopStudentsAnalyser, CountryAnalyser
from .result_saver import ResultSaver
from .report import Report
