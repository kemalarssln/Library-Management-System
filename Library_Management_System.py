class Library:
    def addBooks():
        with open('Books.txt', 'a+', encoding='utf-8') as file:
            BookName = input('Enter the Book Name: ')
            AuthorName = input('Enter the Author Name: ')
            FirstPublicationDate = input('Enter the First Publication Date: ')
            PageNumber = input('Enter the Page Number: ')
            if FirstPublicationDate.isnumeric() and PageNumber.isnumeric():
                file.write(f"{BookName},{AuthorName},{FirstPublicationDate},{PageNumber}\n")
                print('Book has been created.')
            else:
                print("Data Error: Book creation failed. Please enter only numerical values for page number and first publication date.")
    def ListBooks():
        z = 0             
        with open('Books.txt', 'r', encoding='utf-8') as file:
            for line in file.read().splitlines():
                z = z+1
                info = line.strip().split(',')
                book_name, author_name = info[0], info[1]
                print(f"Book Name: {book_name}, Author: {author_name}")
        print(f'There are a total of {z} books available in the library.')
    def RemoveBook():
        delete_book = input('Please enter the book to be deleted: ').strip().lower()
        with open('Books.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        book_deleted = False
        with open('Books.txt', 'w', encoding='utf-8') as file:
            for line in lines:
                book_info = line.strip().split(',')
                if delete_book != book_info[0].lower():  #in kullanmamamın sebebi girilen değerin tüm verilerini silmesi startswith kullanmamamın sebebi ise örneğin vera ve veranda gibi
                    file.write(line)                       #iki kitap olursa vera girildiğinde verandayıda sileceği için tercih etmedim kontrol mekanızmaları kurup kodu uzatmak yerine
                elif not book_deleted:                     #böyle bir kontrol sistemi kurdum.
                    book_deleted = True
                    print(f'{book_info} book has been deleted.')

        if not book_deleted:
            print(f'{delete_book} book not found.')

    def SearchBook():
        choice = input('Please select the operation you want to perform\n1- Search by Book Title\n2- Search by Author Name\n3- Search by Publication Date\n4- Search by Page Count\n')
        if choice == '1':
            searchBookByname = input('Enter the Book Title: ').strip().lower()
            x = -1
            found = False
            with open('Books.txt', 'r', encoding='utf-8') as file:
                for line in file.read().splitlines():
                    x = x + 1
                    info = line.strip().split(',')
                    if searchBookByname == info[0].lower():
                        print(f'The book {searchBookByname} is found at line {x}.')
                        found = True 
            if not found:
                print('Book not found.')
        elif choice == '2':
            author = input('Enter the Author Name: ').strip().lower()
            x = -1
            z = 0
            found = False
            with open('Books.txt', 'r', encoding='utf-8') as file:
                for line in file.read().splitlines():
                    x = x + 1
                    info = line.strip().split(',')
                    if author == info[1].lower():
                        print(f'The book "{info[0]}" by the author "{info[1]}" is found at line {x}.')
                        found = True
                        z = z+1
            print(f'The author "{author}" has {z} books available in the library.')
            if not found:
                print('Author not found.')
        elif choice == '3':
            publication_date_start,publication_date_end = input('Enter the Publication Date Start: '),input('Enter the Publication Date End: ')
            x = -1
            z = 0
            found = False
            with open('Books.txt', 'r', encoding='utf-8') as file:
                for line in file.read().splitlines():
                    x = x + 1
                    info = line.strip().split(',')
                    if int(publication_date_start) <= int(info[2]) <= int(publication_date_end) or int(publication_date_start) >= int(info[3]) >= int(publication_date_end):
                        print(f'The book "{info[0]}" with {info[2]} dates is located between {publication_date_start} and {publication_date_end} dates at line {x}.')
                        found = True
                        z = z+1
            print(f'There are {z} books published on {publication_date_start},{publication_date_end} in the library.')
            if not found:
                print(f'No books published on were found in the library.')
        elif choice == '4':
            page_range_start,page_range_end = input('Enter the starting page number: '),input('Enter the ending page number: ')
            x = -1
            z = 0
            found = False
            with open('Books.txt', 'r', encoding='utf-8') as file:
                for line in file.read().splitlines():
                    x = x + 1
                    info = line.strip().split(',')
                    if int(page_range_start) < int(info[3]) < int(page_range_end) or int(page_range_start) > int(info[3]) > int(page_range_end):
                        print(f'The book "{info[0]}" with {info[3]} pages is located between {page_range_start} and {page_range_end} pages at line {x}.')
                        found = True
                        z = z+1
            print(f'There are {z} books within the specified page range in the library.')
            if not found:
                print(f'No books were found within the specified page range in the library.')


    while True:
        print('***MENU***')
        process = input('1- List Books\n2- Add Book\n3- Remove Book\n4- Search Book\n5- Exit\n')

        if process =='1':
            ListBooks()
        elif process =='2':
            addBooks()
        elif process =='3':
            RemoveBook()
        elif process =='4':
            SearchBook()
        else:
            break