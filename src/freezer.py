class Freezer:
    def __init__(self, volume):
        self.volume = volume
        self.products = [1, 2, 3]

    def __len__(self):
        return len(self.products) #<- ma zwracac ile lodowki jest zajetej


# freezer = Freezer(250)
# print(len(freezer))

# dwie klasy frez i cool, mozemy zrobic freezer dziedziczy po cooler???, maja byc iterable, i mamy zrobic iterator ktory zwraca
#obiekty ktorym koncza sie daty waznosci za x czasu
