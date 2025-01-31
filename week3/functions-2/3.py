from dict import movies

def categoryList(category):
    return [x["name"] for x in movies if x["category"] == category]

print(categoryList("Romance"))