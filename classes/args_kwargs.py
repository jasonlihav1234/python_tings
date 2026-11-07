# Standard positional arguments must come first, followed by *args, then keyword-only parameters, the finally **kwargs
def example_function(*args, **kwargs):
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

example_function(1, 2, 3, a="Value", b=True)

# *operands = *args -> allows function to accept any number of positional inputs
def apply_operator(operator, *operands):
    # Applies operator to a variable number of operands, supports adds and mul
    if operator == "add":
        result = sum(operands)
    elif operator == "mul":
        result = 1
        for n in operands:
            result *= n
    else:
        raise ValueError(f"Unknown operator {operator}. Supported values are 'add' and 'mul'")

    return result

print(apply_operator("add", 1, 2, 3, 4))
print(apply_operator("mul", 1, 2, 3, 4))

# **kwargs = gather extra named parameters in a dictionary
def set_options(**settings):
    print(f"Recieved dictionary: {settings}")
    for key, value in settings.items():
        print(f"\t{key} = {value}")

set_options(timeout=30, user="admin", retries=5)


## unpacking positional arguments
def connect(host, port, timeout):
    print("Here")

params = ["db.internal", 5432, 10]
connect(*params)


## unpacking keyword arguments
def configure_service(name, version, replicas=1):
    print("here2")
    
config = {
    "name": "auth-service",
    "version": "2.1.0",
    "replicas": 3
}

configure_service(**config)
    
