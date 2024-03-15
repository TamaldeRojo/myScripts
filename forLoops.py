import timeit

def main():
    a = 0
    for i in range(1000):
        a += i * i
    print("done")
    return a


if __name__ == "__main__":
    time = timeit.timeit("main()",number=1)
    print(time)