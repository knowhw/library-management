
from os import system
import platform
from os import system as console
# from platform import system
import sys


class Library:
	
	def __init__(self):

		self.books = open("books.txt", "a+")
		


	def file_closed(self):
		print("file colosed!")
		del self.books
	
	
	
	
	def list_book(self, match=''):
		
		match = match.lower()
		# filtre
		count=0
		# search by word

		self.books.seek(0)
		
		book_lines = self.books.readlines()
		
		
		
		lines = [ line for line in book_lines if not line == "\n" ]
					
					
		if match:
			# key 4 -> match: Search by Word
			
			for line in lines:
				# print title, author
				
				if line.lower().find(match) > -1:
					ID, title, author, published, pages = line.split(",")
					print("#", "'%s'" % title, author)
					
					count+=1
		else:
			# key 1 -> List Books
			
			for line in lines:
				# print title, author
				
				ID, title, author, published, pages = line.split(",")
				print("#%s" % ID, "'%s'" % title, author)
				count+=1
				

		if not count:
			msg='No results found!'
			print(msg)
	
		else:
			if match:
				msg='\n%s results found!' % count
				print(msg)
			
		 

	def __getID(self, lines):
		
		try:
			
			index = int (lines [-1] [0])
			# son eklenen kitap indeksi
			
			return index +1
			# return indeks+1
		except:
			return 1
			# kitap listesi bos ise
			# index = 1
			
			
	def add_book(self, attr, count=10):
		
		# key 2: Add Book 
		# attr: title, author, published, pages
		
		from time import sleep
		title, author, published, pages = attr
		
		
		self.books.seek(0)
	
		with self.books as string:
			
			
			lines = string.readlines()
			
			ID = self.__getID(lines)
			string.write("%s,%s,%s,%s,%s\n" % (ID, title, author, published, pages))
			# yeni kayit ve son satira bir bos satir ekle
			

			
		while count:
			
			sleep(.1)
			print (end=".",  flush=1)
			
			count -=1


		
	def remove_book(self, inputext):
		# main -> input: title
		
		inputext = inputext.lower()
		
		
		
		self.books.seek(0)
		
		book_list = self.books.read()
		
		
		
		arr = [ [ item ] for item in book_list.splitlines() if item ]
		# bos satirlari listeye alma
		for index, line in enumerate(arr):
			
			ID, title, author, published, pages = line [0].split(chr(44)) 
			title = title.lower()
			
			
			if title.startswith(inputext):
				# inputext ile baslayan kitaplari kitap listesinden siliyoruz
				del arr [index] [:]
			

		# solution mode="w"
		with open("books.txt", "w") as book:
			book.writelines([ "%s\n" % line [0] for line in arr if line])
		


	def library_delete(self, key):
		
		if key == 'y':
			
			if "Linux" in platform.system(): 
				console("rm books.txt")
				# kitapligi sil
				
				
		self.list_book()
				
				



if __name__ == '__main__':

	
	
	while 1:
		
		

		menu="""
Main Menu
-------------

 1. List Books
 2. Add Book
 3. Remove Book
 4. Search by Word
 
 5. Delete
 q. Exit
 
"""
		lib = Library()
		

		
		
		# lib.add_book(attr)
		# lib.remove_book(title)
		# lib.list_book(author)
		# lib.file_closed()
		# lib.library_delete(key)
		
		
		case = input("%s\nEnter a choice (1-5):" % menu)
		
		
		
		
		while 2:
					
			
			if case == '1' : 
				
				system('clear')
				
				lib.list_book()
				# terminale kitabin baslik ve yazar niteliklerini yazdiriyoruz
				break
				
				
			elif case == "2" : 
				
				attr = "title: ", "book author: ", "published date: ", "pages: "
				
				attr = ( input( item )  for item in attr )
				
				lib.add_book(attr)
				# kitapliga yeni bir kitap ekliyoruz
				system("clear")
				
				break
				
				
			elif case == '3':
				
				
				title = input('title:')
				
				lib.remove_book(title)
				# kitap basligina gore arama yapma ve silme islemi
				system('clear')
				
				break
				
			elif case == '4': 
				
				
				author = input('word:')
				
				system('clear')
				lib.list_book(author)
				# butun sutunlarda kelimeye gore arama yapma ve listeleme
				
				break
				
			elif "Linux" in platform.system() and case == '5': 
			
				key = input('are you sure you want to delete the library? (y/n):')
						
				
				lib.library_delete(key)
				# kitapligi klasorden siliyoruz
				system('clear')	
					
				break
				
			else:
				
				if case == 'q': 
					lib.file_closed()
					sys.exit(1)

				else:
					system('clear')	
					break
			
