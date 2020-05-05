def cakes(recipe, available):
    # Your code here:
    count = []
    for key, value in recipe.items():
        if key not in available.keys():
            return 0
        else:
            count.append(available[key] // value)
    return min(count)
    # This one works too:
    # return min(available.get(k, 0) // recipe[k] for k in recipe)
