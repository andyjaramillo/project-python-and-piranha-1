import requests

r =requests.get('')
print(r.text[0:500])

class Post:
    def __init__(self, subtitle, description) -> None:
        self.subtitle = subtitle
        self.description = description
    