class rectangle:
	def __init__(self, s1, s2):
		self.s1=s1
		self.s2=s2
	def area_calc(self):
		self.area=self.s1*self.s2
		return self.area

r1=rectangle(5,10)
r2=rectangle(3,9)

r1.area_calc()
r2.area_calc()

print(r1.area)
print(r2.area)