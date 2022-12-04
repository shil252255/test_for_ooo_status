class TreeStore:
    """
    Быстро и НЕПРАВИЛЬНО!*

    *первое, что пришло в голов до того как начал думать.
    """

    def __init__(self, items: list[dict]):
        """Самый быстрый метод вариант 'создания' класса так как по сути ничего не создает
          и использует ссылки на объекты items что в итоге может привести(приведет) к ошибкам."""
        self.items_list = items  # Понадобиться только для getAll()
        self.items = {item['id']: item for item in items}

    def getAll(self) -> list:
        """ Вообще можно было бы использовать list(self.items.values()), но это медленнее. (1,14/0,0014)"""
        return self.items_list

    def getItem(self, item_id: int) -> dict:
        """Ну вот тут прям таки даже не знаю как еще быстрее."""
        return self.items[item_id]

    def getChildren(self, item_id: int) -> list:
        """Самый медленный метод, так как при первом взгляде не придумал как сделать это все без перебора"""
        return [item for item in self.items.values() if item['parent'] == item_id]

    def __getAllParents_by_item(self, item: dict) -> list:
        """
        Довольно быстрый метод, но рекурсия накладывает ограничение на длину цепочки
        можно конечно двигать sys.setrecursionlimit(15000) но... такое себе.
        метод сделал внутренним так-как его нет в ТЗ.
        """
        if item['parent'] != 'root':
            return [item] + self.__getAllParents_by_item(self.items[item['parent']])
        return [item]

    def getAllParents(self, item_id: int) -> list:
        """внешняя обертка для __getAllParents_by_item()"""
        return self.__getAllParents_by_item(self.items[item_id])[1:]
