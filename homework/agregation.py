class Guitar:
    def __init__(self, strings):
        self.strings = strings

    def play_every_string(self):
        for sound in self.strings.string_sounds:
            print(sound)


class Strings:
    def __init__(self):
        self.string_sounds = ["Mi", "La", "Re", "Sol", "Si", "Mi"]


if __name__ == '__main__':
    strings = Strings()
    guitar = Guitar(strings)
    guitar.play_every_string()