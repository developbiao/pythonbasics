from agno.memory.v2 import Memory, UserMemory
from rich.pretty import pprint

memory = Memory()

# Add a memory for the default user
memory.add_user_memory(
    memory=UserMemory(
        memory="The user's name is Sun jaing meng", topics=["name"]
    )
)

print("Memories:")
pprint(memory.memories)

# Add memories for Jane Doe
jane_doe_id = "jane_doe@example.com"
memory_id_1 = memory.add_user_memory(
    memory=UserMemory(memory="This user's name is Jane Doe", topics=["name"]),
    user_id=jane_doe_id,
)

memory_id_2 = memory.add_user_memory(
    memory=UserMemory(memory="She likes to play tennies", topics=["hobbies"]),
    user_id=jane_doe_id,
)

memories = memory.get_user_memories(user_id=jane_doe_id)

print("Memories:")
pprint(memories)


# Delete a memory
print("\nDeleting memory")
memory.delete_user_memory(user_id=jane_doe_id, memory_id=memory_id_2)
print("Memory deleted\n")
memories = memory.get_user_memories(user_id=jane_doe_id)
print("Memories:")
pprint(memories)

# Repalce a memmory
print("\nReplacing memory")
memory.replace_user_memory(
    memory_id=memory_id_1,
    memory=UserMemory(memory="This user's name is Jane Doe", topics=["name"]),
    user_id=jane_doe_id,
)
print("Memory replaced\n")
memories = memory.get_user_memories(user_id=jane_doe_id)



