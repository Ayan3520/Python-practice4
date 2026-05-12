# ============================================================
# МОДУЛЬ: report.py
# КЛАСС:  Report
# ЗАДАЧА: Демонстрация Ассоциации (USES-A relationship).
#         Task 4, Practice 7.
# ============================================================

class Report:
    """
    Класс Report демонстрирует АССОЦИАЦИЮ (Association / USES-A).
    
    Что такое ассоциация?
    Report НЕ НАСЛЕДУЕТ от DataAnalyser или ResultSaver.
    Вместо этого он ИСПОЛЬЗУЕТ их объекты через атрибуты.
    
    Отличие от наследования:
    - Наследование (IS-A):  TopStudentsAnalyser IS-A DataAnalyser
    - Ассоциация  (USES-A): Report USES-A DataAnalyser + USES-A ResultSaver
    
    Report — "оркестратор": он знает о существовании analyser и saver,
    делегирует им работу, но не берёт их функциональность "в себя".
    """

    def __init__(self, analyser, saver):
        """
        Конструктор принимает готовые объекты analyser и saver.
        Это называется Dependency Injection — зависимости передаются снаружи,
        а не создаются внутри класса. Это делает код гибким и тестируемым.
        """
        # self.analyser USES-A DataAnalyser (или любой его дочерний класс)
        self.analyser = analyser
        # self.saver USES-A ResultSaver
        self.saver = saver

    def generate(self):
        """
        Метод-оркестратор: последовательно вызывает все этапы.
        
        Report сам ничего не вычисляет — он только координирует:
        1. Запускает анализ через analyser
        2. Выводит результаты через analyser
        3. Сохраняет файл через saver
        
        Благодаря полиморфизму, generate() работает с ЛЮБЫМ дочерним
        классом DataAnalyser — он вызывает analyse() и print_results(),
        не зная, какой именно класс ему передан.
        """
        print("Generating report...")
        self.analyser.analyse()
        self.analyser.print_results()

        # Обновляем данные в saver перед сохранением —
        # analyse() мог изменить self.analyser.result
        self.saver.result_data = self.analyser.result
        self.saver.save_json()

        print("Report complete.")
