from nltk.corpus import wordnet as wn
import re

def check_synset(synset):
    pattern = r'^(\S*?)\.'
    word = re.search(pattern,synset)
    print(synset)
    print('Checking:', word.group())

    synset_check = wn.synset(synset)

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
        return(x.name())

def get_hypernyms(synset_word):

    obj = wn.synset(synset_word)
    obj_list = obj.hypernyms()
    if len(obj_list)>0:
        return obj_list[0].name()
    else:
        return
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
    goon = True
    obj = get_1st_synsets(word)
    hypo_table.append(obj)
    while goon:
        tmp = get_hypernyms(obj)
        if tmp:
            hypo_table.append(tmp)
            obj=tmp
        else:
            goon = False
    return (hypo_table,'hypernym')

# get_hypo_tree(obj[0])
# print(tree_table)
# print(obj)
# last = get_hypernyms(obj[0])

# if last:
#     print(last)
# else:
#     print('last object')
# check_synset(obj[0])
# get_hypernyms(obj[0])

# for word in obj:
#     for x in word.lemmas():
#         print(x.name())
# all_synsets = list(wn.all_synsets())
# print(len(all_synsets))

# for synset in list(wn.all_synsets('n'))[:10]:
#     print(synset)