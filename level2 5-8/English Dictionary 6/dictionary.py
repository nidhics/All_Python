import json
from difflib import get_close_matches
  
# Loading data from json file
# in python dictionary
data = json.load(open(r"D:/programming with python/level2 5-8/English Dictionary 6/dictionary.json"))
# print(data)  
def translate(w):
    # converts to lower case
    w = w.lower()
  
    if w in data:
        return data[w]
    # # for getting close matches of word
    # elif len(get_close_matches(w, data.keys())) > 0: 
    #     print(get_close_matches(w, data.keys()))            
    #     # yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])

    #     yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes, or N if no: " )
    #     yn = yn.lower()
    #     if yn == "y":
    #         return data[get_close_matches(w, data.keys())[0]]
    #     elif yn == "n":
    #         return "The word doesn't exist. Please double check it."
    #     else:
    #         return "We didn't understand your entry."
    # else:
    #     return "The word doesn't exist. Please double check it."
  
# Driver code
word = input("Enter word: ")
output = translate(word)
print(output)  

if(output==None):
    print("could not find ")
# if type(output) == list:
#     for item in output:
#         print(item)
# else:
#     print(output)
input('Press ENTER to exit')