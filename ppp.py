from turtle import Turtle
import turtle
class Ball():
	"""docstring for ClassName"""
	def __init__(self,r,color,dy,dx):
		def __init__(self):
			self.r = r/10
			self.dx=dx
			self.dy=dy
			self.color(color)
			self.penup()
			self.shape('circle')

	def move(self,screen_width,screen_height):
			current_x=self.dx
			self.goto(screen_width,screen_height)
			new_x=current_x+(self.dx-current_x)
			current_y=self.dy
			self.goto(screen_width,screen_height)
			new_y=current_y+(self.dy-current_y)	
			right_side=self.xpos+self.r
			left_side=self.xpos+self.r		
			up_side=self.xpos+self.r
			down_side=self.xpos+self.r		
			self.goto(new_y,new_x)

			ball_size=[right_side,left_side,up_side,down_side]

			if self.pos>Ball_size:
				self.pos=self.xpos-1,self.ypos-1
					




		