from linked_list import LinkedList

def main():
    list = LinkedList()
    list.append('Some string')
    list.append(58)
    list.prepend('Prepended item')
    list.insert(2, 'inserted data')
    list.insert(2, 'more stuff')
    print(list)
    print(list.find(58))

    list.pop_back()
    print(list)

    list.pop_front()
    print(list)

    list.remove(2)
    print(list)
    list.remove(1)
    print(list)
    list.pop_back()
    print(list)

if __name__ == '__main__':
    main()
