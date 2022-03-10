# from difflib import get_close_matches
  
# def closeMatches(word, wrds):
#      print(get_close_matches(word, wrds))
  
# word = 'apple'
# allWords = ['ape', 'apple', 'peach', 'puppy']
# closeMatches(word, allWords)


# f=open("nidhi.txt")
# by default file is in reading mode
f=open("nidhi.txt","r+")
# print(f.readline())#read single line
# print(f.read())#read whole file, if pointer reader is at 0 index, else jahan se choota hai
f.write(" this is a write able file in file.")
f.close()


# fw=open("writenidhi.txt","w")
# fw.write(" this is a write able file.")#write in the file but delete everything which is already written
# fw.close()



fw_app=open("writenidhi.txt","a")
fw_app.write("\n this is a write able file in file. ")#write in the file but delete everything which is already written
fw_app.close()