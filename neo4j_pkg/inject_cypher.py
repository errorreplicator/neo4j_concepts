from neo4j import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", r'cbdh22,.'))

def delete_all():
    query = "match (n) detach delete n"
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", r'cbdh22,.'))
    ses = driver.session()
    ses.run(query)
    print('All nodes deleted')

def delete_node_byid(n_id):
    query = f"match (n) where id(n)={n_id} detach delete n"
    ses = driver.session()
    ses.run(query)

def delete_relation(label,node_name1,node_name2,relation):
    query = f"match (:{label}{{name:'{node_name1}'}})-[r:{relation}]->(:{label}{{name:'{node_name2}'}}) delete r"
    ses = driver.session()
    ses.run(query)

def add_relation(label,no1_name,no2_name,relation_name):
    query=f"merge (a:{label}{{name:'{no1_name}'}}) " \
          f"merge (b:{label}{{name:'{no2_name}'}})" \
          f"create (a)-[:{relation_name}]->(b)"
    ses = driver.session()
    ses.run(query)

def create_node(label,name,wn_name):
    query = f"create (n:{label} {{name:'{name}',wn_name:'{wn_name}'}})"
    ses = driver.session()
    ses.run(query)

def create_2node_relation(label,wn_name1,wn_name2,relation):
    query = f"match (a:{label}),(b:{label})" \
            f"where a.wn_name='{wn_name1}' and b.wn_name='{wn_name2}'" \
            f"create (a)-[r:{relation}]->(b)" \
            f"return r"
    ses = driver.session()
    ses.run(query)







