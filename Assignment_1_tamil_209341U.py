#!/usr/bin/env python
# coding: utf-8

# In[29]:


import re

file_name="tamil.txt"

file = open(file_name, "rt", encoding="utf8")
data = file.read()
words = data.split()
print('Number of words in text file :', len(words))


# In[30]:


# Declare a dictionary 
dictionary = {} 
   
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def isSpecialChar(char):
    special_punctuation_chars = "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~" #add all the punctuation, special marks.
    return char in special_punctuation_chars

# count method to store frequency of each word   
def count(word): 
        
    if not(hasNumbers(word) or isSpecialChar(word) or ''==word or None==word):
           
        # check if each word has special char at its last and ignore
        if isSpecialChar(word[-1]): 
            word = word[0:len(word) - 1] 

        # check if each word has special char at the beggning and ignore
        if isSpecialChar(word[0]): 
            word = word[1:len(word)-1] 
            
        # increment key if exists. 
        if word in dictionary: 
            dictionary[word] += 1

        # add new key "word" and set 1 as value. 
        else: 
            dictionary.update({word: 1}) 
        return 1
    else:
         #print('Not a word, skipped: '+ word)
        return 0
         

      


# In[31]:



# take each word from words list (populated from the text file) and pass it to the count method. 
wordsAfterFiltering=0
for word in words: 
    if(count(word)>0):
        wordsAfterFiltering+=1
print("Words after filtering: "+str(wordsAfterFiltering))
   
# print the keys and its corresponding values. 
#for key in dictionary: 
 #   print ("Frequency of " + key + " : " + str(dictionary[key]) ) 
    
print('Number of unique, valid words: '+ str(len(dictionary.items())))


# In[32]:


#sort dictionary in reverse order
sorted_tuples=sorted(dictionary.items(), reverse=True, key = 
             lambda kv:(kv[1], kv[0]))   

print(sorted_tuples)


# In[33]:


count=0
rank_list=[]
frequency_list=[]
for pair in sorted_tuples:
    count+=1
    rank_list.append(count)
    frequency_list.append(pair[1]) 


# In[34]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#plot the Gaussian curve
ax.plot(rank_list, frequency_list, label = "Rank vs Frequency")

ax.set(xlabel='Rank', ylabel='Frequency',
       title='Tamil.txt - Rank vs Frequecy Plot')
ax.grid()
plt.legend()
plt.show()


# In[35]:


#frequency of frequencies
fof={}
for pair in sorted_tuples:
        # increment key if exists. 
        if pair[1] in fof: 
            fof[pair[1]] += 1

        # add new key "the frequency" and set 1 as value. 
        else: 
            fof.update({pair[1]: 1}) 

#sort dictionary in reverse order
sorted_fof=sorted(fof.items(), reverse=True, key = 
             lambda kv:(kv[1], kv[0]))   

print(sorted_fof)

