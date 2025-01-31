from dict import movies

def categoryAvg(category):
    lt = [x["imdb"] for x in movies if x["category"] == category]
    return sum(lt)/len(lt)

print(categoryAvg("Romance"))
print(categoryAvg("Action"))