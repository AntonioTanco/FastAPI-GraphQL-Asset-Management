import typer
import requests
import json

app = typer.Typer()

@app.command()

def get_all_assets():


    # Defines GraphQL query for Assets
    
    query = """
    {
        assets {
            id
            hostname
            serialNumber
            description
        }
    }
    """

    # Make the request to your GraphQL API
    response = requests.post('http://localhost:8000/graphql', json={'query': query})

    # Print the response
    print(json.dumps(response.json(), indent=4))
