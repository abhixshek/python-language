class Fibonacci:
    def __init__(self):
        self.num = 0
    def __next__(self):
        self.num += 1
        if self.num == 5:
            raise StopIteration

        return self.num


    def __iter__(self):
        return self

if __name__ == "__main__":
    f = Fibonacci()

    for i in f:
        print(i)

