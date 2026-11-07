square = lambda x: x * x
print(square(5))

## Sorting collections with lambda

services = [("web-app", 3), ("database", 1)]
print(f"Default sort: {sorted(services)}")

def get_replica_count(svc_tuple):
    return svc_tuple[1]

print(f"Sorting by replica count - standard function: {sorted(services, key=get_replica_count)}")
print(f"Sorting by replica count - lambda function: {sorted(services, key=lambda svc: svc[1])}")



## Transforming collections with lambda
my_numbers = [1, 2, 3, 4]
print(list(map(lambda num: num * 2, my_numbers)))

ports = [80, 443, 8080, 22]
port_description = list(map(lambda port: f"Port {port} is open", ports))
print(port_description)

## Filtering collections with lambda
ports = [80, 443, 8080, 22, 5432]
privileged_ports = list(filter(lambda port: port < 1024, ports))
print(privileged_ports)
