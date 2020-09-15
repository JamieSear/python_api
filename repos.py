class Repos():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._description = data['description']
        self._url = data['url']
        # print(self._url)
        self._save()

    def _save(self):
        self.all.append(self)
        # print(self.all.name)

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_url(self):
        return self._url

    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]
