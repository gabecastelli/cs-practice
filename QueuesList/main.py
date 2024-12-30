from queue import Queue

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    print(q)

if __name__ == '__main__':
    main()