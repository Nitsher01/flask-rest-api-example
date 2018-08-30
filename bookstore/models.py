from bookstore import db

class Book(db.Model):
 	"""docstring for Book"""
 	__tablename__ = 'books'
 	
 	id = db.Column(db.Integer, primary_key = True)
 	book_name = db.Column(db.String(100), nullable = False)
 	book_price = db.Column(db.Float, nullable = False)
 	book_num = db.Column(db.BigInteger, nullable = False)

 	def __repr__(self):
 		return f"""book_name: {self.book_name},
 		book_price: {self.book_price},
 		book_num: {self.book_num}
 		"""
