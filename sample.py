from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "neo4jneo4j"))

def print_movies_for_actor(tx, name):
    for record in tx.run("MATCH (a:Person)-[:ACTED_IN]->(f) "
                         "WHERE a.name = {name} "
                         "RETURN f.title", name=name):
        print(record["f.title"])
        #print(record)

with driver.session() as session:
    session.read_transaction(print_movies_for_actor, "Al Pacino")

