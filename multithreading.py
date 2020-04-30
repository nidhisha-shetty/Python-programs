#Creating threads for each class, so to execute both classes in parallel(multi-threading)

from threading import *
from time import sleep

class Thread1(Thread):
	def run(self):
		for i in range(5):
			print("t1")
			sleep(1) 	

class Thread2(Thread):
	def run(self):
		for i in range(5):
			print("t2")
			sleep(1)	

t1=Thread1()
t2=Thread2()

t1.start()		
sleep(0.2)	
t2.start()

t1.join()  

t2.join()

print("Main tread execution")
