from typing import Any
from mcp.server.fastmcp import FastMCP
from opensearchpy import OpenSearch
import os
from dotenv import load_dotenv
load_dotenv()
mcp = FastMCP("product-search")
client = OpenSearch(
    hosts=[{'host': os.getenv("OPENSEARCH_HOST"), 'port': 443}],
    http_auth=(os.getenv("OPENSEARCH_USER"), os.getenv("OPENSEARCH_PASS")),
    use_ssl=True,
    verify_certs=True
)
@mcp.tool()
async def search_product(query: str) -> str:
    """
    Search for products from OpenSearch based on natural language query.

    Args:
        query (str): A natural language query like "affordable monitor" or "silver bracelet under $50"
    Returns:
        str: Formatted top 5 results or message if nothing found
    """
    try:
        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title^3", "description", "category", "type"],
                    "fuzziness": "AUTO"
                }
            },
            "size": 5
        }
        response = client.search(index="products", body=search_body)
        hits = response.get("hits", {}).get("hits", [])

        if not hits:
            return " No matching products found."
        results = []
        for hit in hits:
            p = hit["_source"]
            result = f"""
                **Product**: {p.get('title', 'N/A')}
                **Price**: ${p.get('price', 'N/A')}
                **Description**: {p.get('description', 'No description')}
                **Image**: {p.get('image', '')}
                """
            results.append(result.strip())
        return "\n---\n".join(results)
    except Exception as e:
        return f"⚠️ Error querying products: {str(e)}"
if __name__ == "__main__":
    mcp.run(transport="stdio")