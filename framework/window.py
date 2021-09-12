class Window:
    def __init__(self, width: int, height: int, title: str):
        self.width = width
        self.height = height
        self.title = title

    def get_size(self) -> tuple[int, int]:
        return self.width, self.height
