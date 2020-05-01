	#Reading a file
file=open("filehandling.txt", 'r')	#opens a file and reads content
print(file.readline(4))


	#Writing a file
file=open("file",'w')			#opens a file and writes content (creates file if file doesnot exists)
file.write("first line")		#adds this line


	#Copying content from one file to another
filehandling=open("filehandling.txt",'r')		#opens a file and reads content
filehandlingcopy=open("filehandlingcopy",'w')		#opens a file and writes content (creates file if file doesnot exists)

for data in filehandling:				#using for-loop to copy content from 'filehandling' file to 'filehandlingcopy' file file
	filehandlingcopy.write(data)
