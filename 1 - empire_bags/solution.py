class UniqueValue:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash((self.value, type(self.value)))

    def __eq__(self, other):
        if type(self.value) == type(other.value):
            return self.value.__eq__(other.value)
        else:
            return False


def unique_tags(payload: dict) -> list:
    tags = set(map(UniqueValue, payload.get('tags', [])))

    return list(map(lambda t: t.value, tags))



input_data = {
    "title": "Звездные войны 1: Империя приносит баги",
    "description": "Эпичная сага по поиску багов в старом легаси проекте Империи",
    "tags": [
        2,
        "семейное кино",
        "космос",
        "сага",
        "эпик",
        "добро против зла",
        True,
        1.0,
        "челмедведосвин",
        "debug",
        "ipdb",
        "PyCharm",
        "боевик",
        "боевик",
        "эникей",
        "дарт багус",
        5,
        6,
        4,
        "блокбастер",
        "кино 2020",
        7,
        3,
        9,
        12,
        "каникулы в космосе",
        "коварство"
    ],
    "version": 17
}

result = unique_tags(input_data)
print('Результат', result)
