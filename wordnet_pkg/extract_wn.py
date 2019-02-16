from nltk.corpus import wordnet as wn
import re

def check_synset(synset_word):
    pattern = r'^(\S*?)\.'
    word = re.search(pattern, synset_word)
    print(synset_word)
    print('Checking:', word.group())

    synset_check = wn.synset(synset_word)

    hyp = lambda s:s.hypernyms()
    print(synset_check.tree(hyp))

    print(40 * '*')
    types = synset_check.hypernyms()
    for x in types:
        for lemma in x.lemmas():
            print(lemma.name())

def get_synsets(word):
    synsets = []
    words = wn.synsets(word)
    for x in words:
        synsets.append(x.name())
    return synsets

def get_1st_synsets(word):
    words = wn.synsets(word)
    for x in words:
        return(x.name()) #will run only once

def get_hypernyms(synset_word):
    obj = wn.synset(synset_word)
    obj_list = obj.hypernyms()
    if len(obj_list)>0:
        return obj_list[0].name()
    else:
        return # in case word doesn have hypernyms (e.g. top level)

tree_table = []
def get_hypo_tree_recursion(synset_word):
    word = get_hypernyms(synset_word)
    if word:
        tree_table.append(word)
        get_hypo_tree_recursion(word)
    else:
        return

def get_hypo_tree(word):
    hypo_table = []
    flag_go = True
    obj = get_1st_synsets(word)
    hypo_table.append(obj)
    while flag_go:
        tmp = get_hypernyms(obj)
        if tmp:
            hypo_table.append(tmp)
            obj=tmp
        else:
            flag_go = False
    return (hypo_table,'hypernym_of')



