#Lemmatization and Stemming

#Source: https://notebooks.azure.com/FriendlyFryer/projects/text-mining/html/02-Text%20Analytics%20Fundamentals.ipynb
#path = C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\Corpus\Before
#training file - C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\BBC_Bl_59.txt 

import nltk
import pandas as pd
import matplotlib.pyplot as plt
#_____________________________________________
#Importing Corpus Dataset

from nltk.corpus import PlaintextCorpusReader
files = ".*\.txt"
corpus0 = PlaintextCorpusReader(r"C:\Users\Lenovo\Desktop\UNISI\Corpus Approaches\Project\Analysis\Corpus\After", files)
corpus  = nltk.Text(corpus0.words())

#print('Сontents', corpus0.fileids()) #Print contents of your corpus
print('Analyzed:', len(corpus0.fileids())) #Print amounts of files that are analyzed
print('Words:', len(corpus)) 
#print('Word frequency:', corpus.count("Russia")) 

'''
#Stemming (Snowball stemmer vs. PorterStemmer)
'''
#from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

# Get the word stems
#ps = PorterStemmer()
ss = SnowballStemmer("english")
#stems = [ps.stem(word) for word in corpus]
stems = [ss.stem(word) for word in corpus]

# Get Frequency distribution
fdistcorpus = nltk.FreqDist(stems)
for x in ":,.-–[]();!'\"\t\n/ ’?1234567890": #exclude punctuations and numbers(last is optional)
    del fdistcorpus[x]


stopwords = """
The
mr
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
i
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
befor
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
Mr
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
wouldn't
one
two
say
also
like
last
first
make
told
go
work
call
even
mani
becaus
veri
said
sald
use
onli
back
take
ani
show
live
want
made
includ
look
citi
still
sinc
dure
come
get
much
think
around
may
well
move
ad
#
"""

for x in stopwords.split():
    del fdistcorpus[x]

#print('60 most common tokens:', fdistcorpus.most_common(60))
print(fdistcorpus['sochi'])


#count_frame = pd.DataFrame(fdistcorpus, index =[0]).T
#count_frame.columns = ['Count']


# Plot frequency
#counts = count_frame.sort_values('Count', ascending = False)
#fig = plt.figure(figsize=(16, 9))
#ax = fig.gca()    
#counts['Count'][:30].plot(kind = 'bar', ax = ax)
#ax.set_title('Frequency of the most common stems')
#ax.set_ylabel('Frequency of stem')
#ax.set_xlabel('Stem')
#plt.show()


'''
#Lemmatization
'''

#from nltk import WordNetLemmatizer
#nltk.download("wordnet")

# Get the word stems
#lem = WordNetLemmatizer()
#lemmas = [lem.lemmatize(word) for word in corpus]

# Get Frequency distribution
#fdistcorpus = nltk.FreqDist(lemmas)
#for x in ":,.-–[]();!'\"\t\n/ ’?1234567890": #exclude punctuations and numbers(last is optional)
#    del fdistcorpus[x]
'''
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
Mr
#
"""
'''
#for x in stopwords.split():
#    del fdistcorpus[x]

#count_frame = pd.DataFrame(fdistcorpus, index =[0]).T
#count_frame.columns = ['Count']

# Plot frequency
#counts = count_frame.sort_values('Count', ascending = False)
#fig = plt.figure(figsize=(16, 9))
#ax = fig.gca()    
#counts['Count'][:60].plot(kind = 'bar', ax = ax)
#ax.set_title('Frequency of the most common lemmas')
#ax.set_ylabel('Frequency of lemma')
#ax.set_xlabel('Lemma')
#plt.show()