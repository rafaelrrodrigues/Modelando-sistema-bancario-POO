from client import Client

class NaturalPerson(Client):
    def __init__(self, id, name, birthdate, address) -> None:
        super().__init__(address)
        self._id = str(id)
        self._name = str(name)
        self._birthdate = birthdate
