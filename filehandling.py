	#Reading a file
# file=open("filehandling.txt", 'r')
# print(file.readline(4))


	#Writing a file
# file=open("file",'w')		#creates file
# file.write("first line")	#adds this line


	#Copying content from one file to another
filehandling=open("filehandling.txt",'r')
filehandlingcopy=open("filehandlingcopy",'w')

for data in filehandling:
	filehandlingcopy.write(data)



