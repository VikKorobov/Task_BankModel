class Bank:

    def __init__(self, name: str):

        self._name: str = name.strip().lower()

    def get_name(self) -> str:

        return self._name.capitalize()
