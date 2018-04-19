def greeting(name: str) -> None: ...


# Method hello_world accepts the argument type as str
# Here I put the argument type as int to trigger an error
def hello_world(name: int) -> str: ...

# Method return_two actually returns an int.
# Here I put the return value as str to trigger an error
def return_two() -> str: ...