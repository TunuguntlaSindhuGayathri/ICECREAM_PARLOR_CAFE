class SeasonalFlavorOffering:
    def __init__(self, id, name, is_seasonal):
        self.id = id
        self.name = name
        self.is_seasonal = is_seasonal

class IngredientInventory:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class CustomerFlavorSuggestion:
    def __init__(self, id, flavor_id, suggestion):
        self.id = id
        self.flavor_id = flavor_id
        self.suggestion = suggestion

class AllergyConcern:
    def __init__(self, id, concern):
        self.id = id
        self.concern = concern
