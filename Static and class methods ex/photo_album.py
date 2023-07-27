import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__initialize_photo()
        self.current_row_idx = 0

    def __initialize_photo(self):
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self,label):
        if len(self.photos[self.current_row_idx]) == 4:
            self.current_row_idx += 1
        try:
            self.photos[self.current_row_idx].append(label)
            return f"{label} photo added successfully on page {self.current_row_idx + 1} slot {len(self.photos[self.current_row_idx])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        res = "-" * 11 + "\n"
        for page in self.photos:
            res += " ".join(['[]' for photo in page]) + "\n"
            res += "-" * 11 + "\n"

        return res
