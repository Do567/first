import time


def say_hello():
    i = 0
    while i < 10:
        print("Hello, world!")
        time.sleep(1)
        i += 1

if __name__ == "__main__":
    say_hello()

