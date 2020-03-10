#Count the numberof active employees in a company

import sys

class emplstatus:
  count=0
	emplist={"4":"active","5":"active"}

	def __init__(self, eid, empstatus):
		self.eid=eid
		self.empstatus=empstatus

	def changestatus(self, eid, newstatus):
		self.eid=eid
		self.newstatus=newstatus

e=emplstatus(input("Enter new employee's id: "), input ("Enter new employee's status: "))

if e.empstatus!="active":
	print("The default status has to be active")
	sys.exit()

emplstatus.emplist[e.eid]=""+e.empstatus
print(emplstatus.emplist)

e.changestatus(input("Enter the employee's id for status change: "), input ("Enter the updated status: "))

if e.eid in emplstatus.emplist:
	emplstatus.emplist[e.eid]=""+e.newstatus
else:
	print("Invalid ID")

print(emplstatus.emplist)

emplstatus.count=emplstatus.count+sum(values == "active" for values in emplstatus.emplist.values())

print("Total active employees are: "+str(emplstatus.count))


