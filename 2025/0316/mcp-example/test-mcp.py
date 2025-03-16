from mcp.server.fastmcp import FastMCP

# Create an MCP server with a specific name
mcp = FastMCP("my-mcp-server")

@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate BMI given weight in kg and height in meters

    Args:
        weight_kg (float): Weight in kilograms
        height_m (float): Height in meters

    Returns:
        float: Body Mass Index (BMI) value
    """
    return weight_kg / (height_m ** 2)

if __name__ == "__main__":
    # Start the MCP server
    mcp.run()

