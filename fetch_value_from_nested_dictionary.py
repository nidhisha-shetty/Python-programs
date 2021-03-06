#Fetch the value of nested dictionary using recurssion

def get_all_values(nested_dictionary, inp):
    for key, value in nested_dictionary.items():
        if key==inp:
            print(value)
        elif type(value) is dict:
            get_all_values(value, inp)

nested_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key4" : "value4",
        "key5" : "value5",
        "key6" :{
            "key7" : "value7",
            "key8" : "value8"
        }
    }
}
inp=input("Enter a key")
get_all_values(nested_dictionary, inp)

#---------------------------------------------------

#Fetch the value of nested dictionary using for loop

def dictionary_path(res):
  path=dict
  for key in res:
    if key in path:
      path=path[key]
    else:
      return False
dict = {
  'yo': "man",
  'hello': "hey",
  'jinga': {
    'key_one': "value",
    'another': {
      'key_two': "value",
      'ano': {
        'key_three': "value"
      }
    }
  }
}
inp="jinga.another.ano.key_three"
res=inp.split('.')
print(dictionary_path(res))
