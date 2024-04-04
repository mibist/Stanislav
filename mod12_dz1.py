import unittest
from main import Student  #Подключаем класс Student из скаченного main.py https://github.com/yanchuki/HumanMoveTest.git.

class TestStudent(unittest.TestCase):
    def test_walk_distance(self):
        student = Student("John")
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 50, f"Дистанции не равны {student.distance} != 50")

    def test_run_distance(self):
        student = Student("Alice")
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 100, f"Дистанции не равны {student.distance} != 100")

    def test_running_vs_walking(self):
        runner = Student("Bob")
        walker = Student("Charlie")
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertGreater(runner.distance, walker.distance, f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}")

if __name__ == "__main__":
    unittest.main()

