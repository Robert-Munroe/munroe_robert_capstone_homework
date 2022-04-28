# I am referencing data class code from these sources:
# "https://docs.python.org/3/library/dataclasses.html"
# "https://realpython.com/python-data-classes/#basic-data-classes"
# this is the first time I've used a dataclass, so I'll list references here
from dataclasses import dataclass


@dataclass
class InventoryItem:
    item_name: str
    item_price: float
    item_type: str

