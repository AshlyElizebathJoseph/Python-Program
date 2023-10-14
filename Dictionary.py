books={'Wings of Fire':175, 'HomeGoing':104, 'Unfinished':58, 'The Lord of the Rings':150}
print("Dictionary: ",books)
books.update(Unfinshed=78)
print("Updated Dictionary: ",books)
dict=books.pop('HomeGoing')
print('Dictionary= ',books)
print('deleted element=', dict)
books.update({'LOVE':74})
print("Dictionary:",books)
