import threading
import time
import queue

my_lock = threading.Lock()  #вводим блокировку потоков для красивого выводо в консоль заменяя f"\n"

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.tables = tables
        self.queue = queue.Queue()

    def customer_arrival(self):
        for i in range(1, 21):  # 20 посетителей
            print(f"Посетитель номер {i} прибыл")
            customer = Customer(i, self)
            customer.start()
            time.sleep(1)

        # Добавляем метку для завершения работы всех потоков посетителей
        for _ in range(len(self.tables)):
            self.queue.put(None)

    def serve_customer(self, customer):
        while True:
            for table in self.tables:
                if not table.is_busy:
                    table.is_busy = True
                    with my_lock:
                        print(f"Посетитель номер {customer.customer_number} сел за стол {table.number}. (начало обслуживания)")
                        time.sleep(5)
                        print(f"Посетитель номер {customer.customer_number} покушал и ушёл. (конец обслуживания)")
                        table.is_busy = False
                        return
            with my_lock:
                print(f"Посетитель номер {customer.customer_number} ожидает свободный стол. (помещение в очередь)")
                self.queue.put(customer)
                time.sleep(1)

class Customer(threading.Thread):
    def __init__(self, customer_number, cafe):
        super().__init__()
        self.customer_number = customer_number
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)

if __name__ == "__main__":
    # Создаем столики в кафе
    table1 = Table(1)
    table2 = Table(2)
    table3 = Table(3)
    tables = [table1, table2, table3]

    # Инициализируем кафе
    cafe = Cafe(tables)

    # Запускаем поток для прибытия посетителей
    customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
    customer_arrival_thread.start()

    # Ожидаем завершения работы прибытия посетителей
    customer_arrival_thread.join()