# Q.10
# Word Frequency
# Write a Python program to take a sentence from the user and store each word and its frequency in a 
# dictionary. Display the resulting dictionary.


word={}
sentence=input("enter sentence")

words=sentence.split()

for i in range(len(words)):
    if words[i] in word:
        word[words[i]]=word[words[i]]+1
    else:
        word[words[i]]=1
        
print("word frequence")
for key ,value in word.items():
    print(key , ":" , value)