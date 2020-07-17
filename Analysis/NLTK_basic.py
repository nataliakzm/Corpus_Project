#Sources:
#1. https://www.linkedin.com/pulse/corpus-analysis-iii-python-juan-martín-fernández-rowda/
#2. https://www.nltk.org/book/ch02.html#ref-lowercase-startswith
#3. https://github.com/dcavar/python-tutorial-notebooks/blob/master/notebooks/Python%20NLTK%20-%20Texts%20and%20Frequencies.ipynb
#4. https://notebooks.azure.com/FriendlyFryer/projects/text-mining/html/02-Text%20Analytics%20Fundamentals.ipynb

import nltk
#_____________________________________________
#Importing Corpus Dataset
'''
 If you want to use your own files, you'll have to tell Python where they are,
 so it can read them. Activate these steps instead if you want to work with one file:
'''
#f = open(r'C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\BBC_Bl_59.txt','rU') #change this to your path
#raw = f.read()
#tokens = nltk.word_tokenize(raw)
#text = nltk.Text(tokens)

'''
What if you have more than one file? You can use the Plain Text Corpus Reader
to deal with several plaintext documents. Note that, if you follow the example below,
you'll need to replace the green sections with the relevant information, 
like your path, your file extension, etc...
'''

from nltk.corpus import PlaintextCorpusReader
files = ".*\.txt"
corpus0 = PlaintextCorpusReader(r"C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\Corpus\Before", files) #change this to your path
corpus  = nltk.Text(corpus0.words())

#print('Сontents', corpus0.fileids()) #Print contents of your corpus
print('Analyzed:', len(corpus0.fileids())) #Print amounts of files that are analyzed

'''
You can test if your data was correctly read just by typing the name of the variable containing it:
    #print(corpus)
    #print(text)
    NB: Recall text variable in all cases below instead of corpus
    in case you go with the analysis of a certain (i.e. one) .txt file. 
'''

#_____________________________________________
#Analyzing 

#1) Word- and token- count
'''
We can get a wordcount using the "len" function. 
What we'll obtain is a count of all words and symbols, repeated words included.
'''
print('Words:', len(corpus)) 

'''
If we wanted to count unique tokens, excluding repeated elements:
'''
print('Tokens:', len(set(corpus))) 

'''
With the "set" function, we can get a list of all the words used in our corpus, i.e., a vocabulary:
    NB: Python will put capitalized words at the beginning of your list.
'''
#print('List of all words:', set(corpus)) #- without the order
#print('List of all words:', sorted(set(corpus))) #- alphabetically sorted


#2) Lexical Richness
'''
We can check how many times a word is used on average, what we call lexical richness.
This indicator can be obtained by dividing the total number of words by the number of unique words:
'''
#print('Lexical richness:', len(corpus)/len(set(corpus)))


#3) Word frequency
'''
If you need to find out how many times a word occurs in your corpus, 
you can try the following (notice this is case-sensitive):
'''
#print('Word frequency:', corpus.count("Russia")) 
#don't forget to change "Russia" to a word that you're looking for

'''
#Frequency distribution and BiGrams are in a separate document
#Stemming and Lemmatization are in a separate document too
'''
#________________________
#Extracting Named Entities

from nltk import pos_tag, ne_chunk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download('maxent_ne_chunker')
nltk.download('words')

print("\nNamed entity chunks:")
people = []
places = []
organizations = []
for corpus in corpus:
    # Find NE chunks
    for chunk in ne_chunk(pos_tag(nltk.word_tokenize(corpus))):
        # Check for a label
        if hasattr(chunk, 'label'):
            #print(chunk)
            # Which tyupe of named entity was found?
            if chunk.label() == 'PERSON':
                people.append(' '.join(c[0] for c in chunk))
            elif chunk.label() == 'GPE':
                places.append(' '.join(c[0] for c in chunk))
            elif chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk))
                
# Print out the consolidated results
print("\nPeople:")
for person in sorted(set(people)):
    print("\t", person)
#print("Places:")
#for place in sorted(set(places)):
#    print("\t", place)
#print("Organizations:")
#for organization in sorted(set(organizations)):
#    print("\t", organization)