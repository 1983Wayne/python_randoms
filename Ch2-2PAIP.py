### Sentence = Noun-Phrase + Verb-Phrase
### Noun-Phrase = Article + Noun
### Verb-Phrase = Verb + Noun-Phrase
### Article = The, A
### Noun = Man, ball, woman, table
### Verb = hit, took, saw, liked

# Supposedly called the 'Context-free phrase structure' with generative syntax

import random

def sentence():
    return noun_phrase() + verb_phrase()

def verb_phrase():
    return verb() + noun_phrase()

def verb():
    return one_of('hit took saw liked'.split())
    
def article():
    return one_of('the a'.split())
    
def noun():
    return one_of('man ball woman table'.split())

def noun_phrase():
    return article() + adj_maybe() + noun() + PP_star()

def one_of(l):
    return [random.choice(l)]

def adj_maybe():
    if random.randint(0, 1) == 0:
        return adj() + adj_maybe()
    return []

def PP_star():
    if random.randint(0, 1) == 0:
        return PP() + PP_star()
    return []

def PP():
    return prep() + noun_phrase()

def prep():
    return one_of('to in by with on'.split())
    
def adj():
    return one_of('big little blue green adiabatic'.split())
