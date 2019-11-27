users=[]
posts=[]
comments=[]

username='noa'
password='123'

random=0

while random==0:
	try_username=input('what is your username?')
	try_password=input('what is your password')

	if try_username==username and try_password==password:
		random=1
		print('welcome!!!')

	else:
		print('try again please')	

class User(object):
	def __init__ (self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		self.friends_list =[] 
		self.posts= []
		self.new_messages=[]
		users.append(self)

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

	def  send_d(self):
		reciver=input('Direct Messages with...?')
		message_text=input('enter a message')
		for i in users:
			if reciver in self.name:
				reciver.append(message_text)		

class post:	
	def __init__(self, post_text,date):
		self.post_text=post_text
		self.date = date

		def post(self):
			posts.append(post_text)

		def post_date(self):
			print('posted on' +self.date)


	class Comment(Post):
		def __init__ (self,comment_text):
			self.comment_text=comment_text

		def create_comment(self):
			comments.append(self.comment_text)
			print('your comment is '+ self.comment_text )

		def remove_comment(self, comment_text):
			comments.remove(comment_text)
			print("you removed your comment" + comment_text)

		def edit_comment(self, comment_text):
			self.comment_text=new_comment
			print("your comment has been changed")

class Messages(user):
	def __init__(self,message_text):
		self.message_text=message_text

user1 = User('Eyal','eyal@meet.mit.edu', '123')	
user2 = User("Ariel","ariel@meet.mit.edu", "123")
user2.add_friend("eyal@meet.mit.edu")
user1.add_post('Hello')
user1.get_userInfo()
user2.get_userInfo()
user2.remove_friend("eyal@meet.mit.edu")
