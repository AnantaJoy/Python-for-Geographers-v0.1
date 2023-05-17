import json
from pathlib import Path

movies = [
    {"id":1, "title":"Batman","year":2022},
    {"id":2, "title":"Superman","year":2017},    
]

data = json.dumps(movies)

# write data to json
Path("movies.json").write_text(data)

# Read data from json
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0])