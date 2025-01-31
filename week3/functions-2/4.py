from dict import movies

def avg(mov):
    sum = 0
    for el in mov:
        sum += el["imdb"]
    return sum/len(mov)

print(avg([movies[0], movies[1], movies[7]]))