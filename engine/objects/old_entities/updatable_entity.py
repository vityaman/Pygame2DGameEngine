from abc import abstractmethod


class UpdatableEntity:
    UpdatableEntities = []

    def __init__(self):
        self.UpdatableEntities.append(self)

    @abstractmethod
    def update(self):
        pass

    def __del__(self):
        self.UpdatableEntities.remove(self)
