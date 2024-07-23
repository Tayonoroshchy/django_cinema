from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    id: int
    name: str


@dataclass
class ElasticSearchObject:
    id: int
    imdb_rating: float
    genre: str
    title: str
    description: str
    director: str = None
    actors_names: str = None
    writers_names: str = None
    actors: List[Person] = None
    writers: List[Person] = None
