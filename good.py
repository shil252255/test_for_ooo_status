from collections import defaultdict


class TreeStore:
    _items_dict: dict[int: dict]
    _items_by_parents: dict[int: dict]
    _items_list: list[dict]

    def __init__(self, items: list[dict]):
        self._items_dict = {}
        self._items_list = []
        self._items_by_parents = defaultdict(list)
        for item in items:
            new_item = item.copy()
            self._items_by_parents[item['parent']].append(new_item)
            self._items_dict[item['id']] = new_item
            self._items_list.append(new_item)

    def getAll(self) -> list[dict]:
        return self._items_list

    def getItem(self, item_id: int) -> dict:
        return self._items_dict[item_id]

    def getChildren(self, item_id: int) -> list[dict]:
        return self._items_by_parents[item_id]

    def _getParent(self, item: dict) -> dict:
        while item['parent'] != 'root':
            yield (item := self._items_dict[item['parent']])

    def getAllParents(self, item_id: int) -> list[dict]:
        return list(self._getParent(self._items_dict[item_id]))
