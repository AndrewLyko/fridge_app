class Fridge:
    def __init__(self, cooler_volume, freezer_volume):
        self.cooler = []
        self.freeze = []
        self._cooler_volume = cooler_volume
        self._freezer_volume = freezer_volume

    @property
    def cooler_volume(self):
        return self._cooler_volume

    @cooler_volume.setter
    def cooler_volume(self, new_volume):
        if new_volume > 0:
            self.cooler_volume = new_volume

    @property
    def freezer_volume(self):
        return self._freezer_volume

    @freezer_volume.setter
    def freezer_volume(self, new_volume):
        if new_volume > 0:
            self.freezer_volume = new_volume

    def __str__(self):
        return f"Cooler Volume: {self.cooler_volume}l, freezer volume: {self.freezer_volume}l"
