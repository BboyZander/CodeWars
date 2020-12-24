def cakes(recipe, available):
    if len(available) < len(recipe):
        return 0
    else:
        recipe_list = list(recipe.keys())
        return min([available[k] // recipe[k] for k in recipe_list])