from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
ps = PorterStemmer()
import timeit
import random

with open('SportsList.txt','r') as di:  # UNIX 250k unique word list 
    all_words_set={line.strip() for line in di}
#all_words_list=list(all_words_set) 
sport_list=set(all_words_set)
#set_f

#for w in all_words_set:

#	print w
#stop words that are useless for the tokenizing 
example_text = "I am watching batman in Florida."
stop_words = set(stopwords.words("english"))
#print stop_words
words = word_tokenize(example_text)
filtered_sentence = []
for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)


for w in filtered_sentence:
	print ps.stem(w)
print nltk.pos_tag(words)
count = 0
for word in filtered_sentence:
	if word in sport_list:
	        count+=1
print count

#print filtered_sentence


# Tag	Meaning	Examples
# ADJ	adjective	new, good, high, special, big, local
# ADV	adverb	really, already, still, early, now
# CNJ	conjunction	and, or, but, if, while, although
# DET	determiner	the, a, some, most, every, no
# EX	existential	there, there's
# FW	foreign word	dolce, ersatz, esprit, quo, maitre
# MOD	modal verb	will, can, would, may, must, should
# N	noun	year, home, costs, time, education
# NP	proper noun	Alison, Africa, April, Washington
# NUM	number	twenty-four, fourth, 1991, 14:24
# PRO	pronoun	he, their, her, its, my, I, us
# P	preposition	on, of, at, with, by, into, under
# TO	the word to	to
# UH	interjection	ah, bang, ha, whee, hmpf, oops
# V	verb	is, has, get, do, make, see, run
# VD	past tense	said, took, told, made, asked
# VG	present participle	making, going, playing, working
# VN	past participle	given, taken, begun, sung
# WH	wh determiner	who, which, when, what, where, how
tagged = nltk.pos_tag(filtered_sentence)
chunk_gram = r"""Chunk: {<VBG.?><NNP.?>*} """
chunk_parser = nltk.RegexpParser(chunk_gram) 
chunked = chunk_parser.parse(tagged)
#print chunked
for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
	a = subtree
	print subtree.leaves()
	#print a.key(1)
	list1,list2 =zip(*subtree) 
	print list1
	sport=list1[1].lower()
	print sport
	if sport=='cricket':
		print 'yes' 
	else:
		print 'no'

# for i in filtered_sentence:
# 	tagged = nltk.pos_tag(words)
# 	named_entity = nltk.ne_chunk(tagged)
