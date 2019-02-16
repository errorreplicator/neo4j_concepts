from neo4j_pkg import inject_cypher as ic
from neo4j_pkg import wn_cypher as wc
from wordnet_pkg import extract_wn as ew




# inject_cypher.nodes_outof_wordnet(session,'dog')

# tmp = ew.get_hypernyms('dog')
# print(tmp)


# tmp = ew.get_hypo_tree('dog')

# ic.delete_all()
wc.nodes_outof_wordnet('dog',relation=True)

