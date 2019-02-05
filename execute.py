from neo4j_pkg import inject_cypher
from neo4j import GraphDatabase,basic_auth

driver = GraphDatabase.driver('bolt://localhost:7687',auth=basic_auth("neo4j",'cbdh22,.'))
session = driver.session()
# inject_cypher.delete_all(session)

# inject_cypher.create_node(session,'Friend','Piotr','22')
# inject_cypher.create_node(session,'Friend','Dorota','2')

# inject_cypher.add_relation(session,'Friend','Dorota','Piotr','Wife')
# inject_cypher.delete_relation(session,'Friend','Dorota','Piotr','Wife')


inject_cypher.nodes_outof_wordnet(session,'dog')