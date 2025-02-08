def possible(my_tiles, table_sets):
    for tile in my_tiles:
        pass
def can_add(tile,tile_set):
    pass
def type_of_set(tile_set) -> "same colors" | "same numbers":
    color = None
    for tile in tile_set:
        if color is None:
            color = tile[0]
        else:
            if color != tile[0]:
                return "same numbers"
    return "same colors"

