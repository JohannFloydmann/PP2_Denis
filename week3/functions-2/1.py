from dict import movies

def isGood(dict):
    return dict["imdb"] > 5.5

print(isGood(movies[0]))