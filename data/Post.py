from uuid import uuid4


class Post:
    def __init__(self, title):
        self.title = title
        self.id = str(uuid4())


posts = [
    Post('Post 1'),
    Post('Post 2')
]
