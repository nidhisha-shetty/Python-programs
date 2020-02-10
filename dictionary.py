#dictionary is used to store data in 'key:value' form, 'keys' in dictionary are unique 

#storring data in dictionary in 'key:value' form
data={1:'nidhihsa',2:'shetty'}

#retrieving value of key '2'
data[2]

#retrieving value of key '2' using 'get' function
data.get(2)

#retrieving value of key '3' which is not present in the dictionary
data.get(3, 'key is missing in the dictionary')

#creating dictionary using list
keys=['Maharashtra','Karnataka']    #list of states
values=['Mumbai','Bangalore']       #list of capitals
data=dict(zip(keys,values))         #creating dictionary by combining keys and values list
print(data)                         #print the dictionary having states as keys and citiies as values


#adding a data to dictionary
data['Rajasthan']='Jaipur'

#deleting data from dictionary
del data['Maharashtra']

#using list and dictionary as values in a dictionary
prog_lang={'JS':'Atom', 'CS':'VS', 'Python':['Sublime', 'Pycharm'], 'Java':{'JSE': 'Eclipse', 'JEE':'Netbeans'}
prog_lang['JS']                    #retrieving value of JS
print(prog_lang['Python'][1])      #retrieving value from a list
print(prog_lang['Java']['JSE'])    #retrieving value from a dictionary

