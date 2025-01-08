from kigsley import get_kigsley_info
def print_hello(name: str) -> str:
    return f"Hello, {name}!"

response = print_hello("kingsley")
print(response)

def add(a:int, b:int) -> int:
    return a + b

print(add(1, 2))    

print(get_kigsley_info())