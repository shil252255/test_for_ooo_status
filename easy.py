class TreeStore:
    """
    Тут уже данные не зависят первоисточника. И за это приходиться платить более долгим созданием экземпляра.
    """

    def __init__(self, items: list[dict]):
        """
        Тут все данные дублируются в новые переменные
        """
        self._items_dict = {item['id']: {**item} for item in items}
        self._items_list = list(self._items_dict.values())  # если просто сделать item.copy то,
                                                            # сами элементы dict останутся прежними
        self._items_by_parents = {key: [] for key in self._items_dict.keys()}
        # Хотя тут можно было использовать defaultdict, но решил обойтись чем по проще
        for item in self._items_list[1:]:  # полагаюсь на то что первый элемент всегда наследуется от root и только он
            self._items_by_parents[item['parent']].append(item)

    def getAll(self) -> list[dict]:
        """
        Tут уж мы сами вольны выбирать где именно тратить на это время.
        Но логично, что методы вызываются чаще, чем создаются экземпляры.
        """
        return self._items_list

    def getItem(self, item_id: int) -> dict:
        """Тут без изменений"""
        return self._items_dict[item_id]

    def getChildren(self, item_id: int) -> list[dict]:
        """Упростил и перенес вычисления в __init__"""
        return self._items_by_parents[item_id]

    def _getParent(self, item: dict) -> dict:
        """Заменил рекурсию на генератор (впервые в Python использовал ':=' )"""
        while item['parent'] != 'root':
            yield (item := self._items_dict[item['parent']])

    def getAllParents(self, item_id: int) -> list[dict]:
        return list(self._getParent(self._items_dict[item_id]))
