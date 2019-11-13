class User(object):
	def __init__ (self, name, email, password)
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

	def post(self, text):
		self.post.append(text)
		print(self.name + "has posted " + post)

	def "get_userInfo"(self):
		print ("Name:["+self.name+"]"+"email: ["+self.email+"]"+"password: ["+self.password+"]+friends: ["+str.friends_list+"]+'posts: ["+self.posts+"]")

class Post(object):
	def __init__(self, ):
		super(Post, self).__init__()
		self.arg = arg
		

user1 = User("Eyal","eyal@meet.mit.edu", "123")	
user2 = User("Ariel","ariel@meet.mit.edu", "123")
user2.add_friend("eyal@meet.mit.edu")
user1.post('Hello')
user1.get_userInfo()
user2.get_userInfo()
user2.remove_friend("eyal@meet.mit.edu")




