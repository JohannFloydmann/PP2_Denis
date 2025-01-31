from dict import movies

def listGood(lt):
    out = list()
    for el in lt:
        if el["imdb"] > 5.5:
            out.append(el["name"])
    return out

print(listGood(movies))