from stika.json import JSONEncoder, JSONDecoder
import json
from dataclasses import dataclass
import typing

if __name__ == "__main__":
    pass


@dataclass
class Child:
    name: str
    age: int


@dataclass
class Parent:
    name: str
    age: int
    child: typing.Union[Child, int, None]


c = Child("Bob", 2)
p = Parent("Alice", 25, c)

d = json.dumps(p, cls=JSONEncoder, indent=4)
print(d)
l = json.loads(d, cls=JSONDecoder, data_cls=dict)
print(l)

l = json.loads(d, cls=JSONDecoder, data_cls=Parent)
print(l)