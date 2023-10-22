class item_category():
    def __init__(self, name: str, depr_threshold: int):
        self.name = name
        self.depr_threshold = depr_threshold

regular: item_category = item_category("regular", 95)
dairy: item_category = item_category("dairy", 80)
