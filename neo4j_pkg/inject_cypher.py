from neo4j import GraphDatabase, basic_auth
from wordnet_pkg import extract_wn

driver = GraphDatabase.driver("bolt://localhost:7687",auth=basic_auth("neo4j",r'cbdh22,.'))

def delete_all(ses):
    query = "match (n) detach delete n"
    ses.run(query)
    print('All nodes deleted')

def delete_node_byid(ses,n_id):
    query = f"match (n) where id(n)={n_id} detach delete n"
    ses.run(query)

def delete_relation(ses,label,node_name1,node_name2,relation):
    query = f"match (:{label}{{name:'{node_name1}'}})-[r:{relation}]->(:{label}{{name:'{node_name2}'}}) delete r"
    ses.run(query)

def add_relation(ses,label,no1_name,no2_name,relation_name):
    query=f"merge (a:{label}{{name:'{no1_name}'}}) " \
          f"merge (b:{label}{{name:'{no2_name}'}})" \
          f"create (a)-[:{relation_name}]->(b)"
    ses.run(query)

def create_node(ses,label,name,number):
    query = f"create (n:{label} {{name:'{name}',number:'{number}'}})"
    ses.run(query)

def create_node_relation(ses,label,name,wn_name,relation):
    #code goes here

def nodes_outof_wordnet(ses,word):#take it to wn_cypher..
    hypernyms,relation = extract_wn.get_hypo_tree(word)
    for hype_name in hypernyms:
        create_node(ses,'animal',hype_name,1)





