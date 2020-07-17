#Frequency distributions & Bigrams
#path = C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\Corpus\Before
#training file - C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\BBC_Bl_59.txt 

#Source: https://www.linkedin.com/pulse/corpus-analysis-iii-python-juan-martín-fernández-rowda/
#Also: https://www.nltk.org/book/ch02.html#ref-lowercase-startswith
#and: https://github.com/dcavar/python-tutorial-notebooks/blob/master/notebooks/Python%20NLTK%20-%20Texts%20and%20Frequencies.ipynb

import nltk
import pandas as pd
import matplotlib.pyplot as plt

#_____________________________________________
#Importing Corpus Dataset

from nltk.corpus import PlaintextCorpusReader
files = ".*\.txt"
corpus0 = PlaintextCorpusReader(r"C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\Corpus\Before", files)
corpus  = nltk.Text(corpus0.words())

#print('Сontents', corpus0.fileids()) #Print contents of your corpus
print('Analyzed:', len(corpus0.fileids())) #Print amounts of files that are analyzed
print('Words:', len(corpus)) 
#print('Word frequency:', corpus.count("Russia")) 

#_____________________________________________
#Frequency distributions
'''
One key piece of information you probably want to get is the number of occurrences
of each token or vocabulary item. One way to do this is using frequency distributions.
You can also use this method to find how many times a certain word occurs.
'''
fdistcorpus = nltk.FreqDist(corpus) #activate this if you refer to 'fdistcorpus'
for x in ":,.-–[]();!'\"\t\n/ ’?1234567890": #exclude punctuations and numbers(last is optional)
    del fdistcorpus[x]

stopwords = """
The
."
.”
,"
,”
“
”
".
.“
000
A
I
me
my
myself
we
We
our
ours
ourselves
you
you're
you've
you'll
you'd
your
yours
yourself
yourselves
he
He
him
his
himself
she
she's
her
hers
herself
it
It
it's
its
itself
they
They
them
their
theirs
themselves
what
which
who
whom
this
that
that'll
these
those
am
is
are
was
were
be
been
being
have
has
had
having
do
does
did
doing
a
an
the
and
but
if
or
because
as
until
while
of
at
by
for
with
about
against
between
into
through
during
before
after
above
below
to
from
up
down
in
out
on
off
over
under
again
further
then
once
here
there
when
where
why
how
all
any
both
each
few
more
most
other
some
such
no
nor
not
only
own
same
so
than
too
very
s
t
can
will
just
don
don't
should
should've
now
d
ll
m
o
re
ve
y
ain
aren
aren't
could
couldn
couldn't
didn
didn't
doesn
doesn't
hadn
hadn't
hasn
hasn't
haven
haven't
isn
isn't
mightn't
mustn
mustn't
needn
needn't
shan
shan't
shouldn
shouldn't
wasn
wasn't
weren
weren't
won
won't
would
wouldn
twitter
image
photo
wouldn't
said
one
two
But
In
also
years
like
last
first
told
says
make
since
around
And
much
still
This
even
back
many

"""

for x in stopwords.split():
    del fdistcorpus[x]

#print(list(fdistcorpus.most_common())) #print a list of all words
#print('Frequency distributions:', fdistcorpus)
 
#or a similar way to do this is using the vocab function:
#print('Frequency distributions:', corpus.vocab())

'''
Conversely, if you wanted to see the words that only appear one time:
'''
#print(fdistcorpus.hapaxes())

'''
If you only want to see, for example, the 10 most common tokens from your corpus,
there's a function for that:
'''
#print('10 most common tokens:', fdistcorpus.most_common(10))

'''
It's possible also to represent frequency of a given word
'''
#print(fdistcorpus.freq('Russia'))
#print(fdistcorpus['Russia']) #count of the number of times a given word occurred

'''
We can have the frequency distributions results presented in many ways
'''
#for sample in fdistcorpus: 
#    print(sample) #Represents everything in one column

#print(fdistcorpus.tabulate(10)) #a table for 10 words

#or you can represent tthe frequency distributions in chart:
#print(fdistcorpus.plot(40)) #you can mention the number of words in brackets that you want to visualize

#or cumulative plot of the frequency distribution - print(fdistcorpus.plot(10, cumulative=True))

#_____________________________________________
#Visualization

'''
#1) Visualization for Frequency distribution of words
'''
#------------
#count_frame = pd.DataFrame(fdistcorpus, index =[0]).T
#count_frame.columns = ['Count']

# Plot frequency
#counts = count_frame.sort_values('Count', ascending = False)
#fig = plt.figure(figsize=(16, 9))
#ax = fig.gca()    
#counts['Count'][:60].plot(kind = 'bar', ax = ax)
#ax.set_title('Frequency of the most common words')
#ax.set_ylabel('Frequency of word')
#ax.set_xlabel('Word')
#plt.show() 
#-----------
'''
2)Visualization for Frequency distribution of BiGrams
'''
#-----------
#from nltk import ngrams

#n = 2
#nGramsInDoc = []
#nGrams = ngrams(corpus, n)
#for grams in nGrams:
#    nWords = ' '.join(g for g in grams)
#    nGramsInDoc.append(nWords)

# Count the frequency of each n-gram
#fdistcorpus = nltk.FreqDist(nGramsInDoc)  
#count_frame = pd.DataFrame(fdistcorpus, index =[0]).T
#count_frame.columns = ['Count']

# Plot the frequency of the top 60 n-grams
#counts = count_frame.sort_values('Count', ascending = False)
#fig = plt.figure(figsize=(16, 9))
#ax = fig.gca()    
#counts['Count'][:60].plot(kind = 'bar', ax = ax)
#ax.set_title('Frequency of the most common n-grams')
#ax.set_ylabel('Frequency of n-gram')
#ax.set_xlabel('n-gram')
#plt.show()
#-----------
