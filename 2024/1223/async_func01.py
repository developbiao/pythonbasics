import asyncio

# Define a async function
async def say_hello():
    print("Hello")
    await asyncio.sleep(1) # Moock network  request
    print("World")

# Run async funtion
asyncio.run(say_hello())
