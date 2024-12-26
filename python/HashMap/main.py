from hash_table import HashTable

def main():
    phone_book = HashTable(10)
    phone_book.insert('Bob', '508-123-2345')
    phone_book.insert('Jack', '617-555-0283')
    phone_book.insert('Empty', None)
    phone_book.remove('Jack')
    print(phone_book)

if __name__ == '__main__':
    main()
