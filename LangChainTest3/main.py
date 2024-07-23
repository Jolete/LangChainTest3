from modules.environment.environment_utilities import (
    load_environment_variables,
    verify_environment_variables,
)
from modules.neo4j.credentials import neo4j_credentials
from langchain_community.graphs import neo4j_graph

# Main program
try:
    
    #region Load environtment

    # Load environment variables using the utility
    env_vars = load_environment_variables()
    
    # Verify the environment variables
    if not verify_environment_variables(env_vars):
        raise ValueError("Some environment variables are missing!")

    #endregion
    
    #region neo4j db
    
    graph = neo4j_graph.Neo4jGraph(
        url=env_vars["NEO4J_URI"],
        username=env_vars["NEO4J_USERNAME"],
        password=env_vars["NEO4J_PASSWORD"]
    )

    result = graph.query("""
        MATCH (m:Movie{title: 'Toy Story'}) 
        RETURN m.title, m.plot, m.poster
        """)

    print("Pintem el resultat de la consulta \n")
    print(result)
    print("\n")
    print("Pintem l'esquema de la BD de Neo4j \n")
    print(graph.schema + "\n")
    #endregion

except Exception as e:
    print(f"An unexpected error occurred: {e}")