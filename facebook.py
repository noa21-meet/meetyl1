class User(object):
	def __init__ (self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list =[] 
		self.posts= []

	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name + "has added " + email + "as a friend.")

	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name + "has removed " + email + "as a friend.")

	def add_post(self, post_text, date):
		post1 =post(date. text)
		self.date = date
		self.text = post_text
		author = self.name
		self.posts.append(text)
		print(self.name + "has posted " +text)

	def get_userInfo(self):
		print ("Name:["+self.name+"]"+"email: ["+self.email+"]"+"password: ["+self.password+"]+friends: ["+str(self.friends_list)+"]+'posts: ["+str(self.posts)+"]")

class Post(User):
	def __init__(self, post_text,date):
		self.post_text=post_text
		self.comment = []
		self.date = date

			def create_comment(self, comment_text):
				self.comments.append(comment_text)
				print("your comment" + self.comment_text)

			def remove_comment(self, comment_text):
				self.comments.remove(comment_text)
				print("you removed your comment" + comment_text)

			def edit_comment(self, comment_text):
				self.comment_text=new_comment
				print("your comment has been changed")

			def post_date(self):
				print("posted on" + self.post_date)	

user1 = User('Eyal','eyal@meet.mit.edu', '123')	
user2 = User("Ariel","ariel@meet.mit.edu", "123")
user2.add_friend("eyal@meet.mit.edu")
user1.add_post('Hello')
user1.get_userInfo()
user2.get_userInfo()
user2.remove_friend("eyal@meet.mit.edu")

