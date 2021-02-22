# def get_all_values(nested_dictionary, inp):
#     for key, value in nested_dictionary.items():
#         if key==inp:
#             print(value)       
#         elif type(value) is dict:
#             get_all_values(value, inp)

# nested_dictionary = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": {
#         "key4" : "value4",
#         "key5" : "value5",
#         "key6" :{
#             "key7" : "value7",
#             "key8" : "value8"
#         }
#     }
# }
# inp=input("Enter a key")
# get_all_values(nested_dictionary, inp)



def get_all_values(nested_dictionary, inp):
    for key, value in nested_dictionary.items():
        if key==inp:
            print(value)       
        elif type(value) is dict:
            for key, value in nested_dictionary.items():
                if key==inp:
                    print(value)

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
