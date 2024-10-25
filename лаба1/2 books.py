disk_size = 1.44
pages = 100
lines_in_page = 50
chars_in_line = 25
bytes_char = 4

book_size_bytes = pages * lines_in_page * chars_in_line * bytes_char

disk_size_bytes = disk_size * 1024 * 1024

num_books = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:",int(num_books) )
