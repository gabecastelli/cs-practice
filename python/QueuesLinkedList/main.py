from queue import Queue

def main():
    q = Queue('first data')
    q.enqueue('second in line')

    q.enqueue(3)
    print(q)
    print('dequeuing...')
    q.dequeue()
    print(q)
    print(q.empty())
    q.dequeue()
    q.dequeue()
    print(q.empty())

if __name__ == '__main__':
    main()