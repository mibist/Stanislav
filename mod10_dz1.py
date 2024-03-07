import threading
import time

def print_numbers():
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def print_letters():
    for char in 'abcdefghij':
        print(char)
        time.sleep(1)

if __name__ == "__main__":
    thread_numbers = threading.Thread(target=print_numbers)
    thread_letters = threading.Thread(target=print_letters)

    thread_numbers.start()
    thread_letters.start()

    thread_numbers.join()
    thread_letters.join()