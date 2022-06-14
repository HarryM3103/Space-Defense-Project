class ScoreBoard:

    def __init__(self, filename: str):
        self.filename = filename

    def createTextFile(self):
        with open(self.filename, "w") as w:
            w.write("")

    def addItem(self, item):
        with open(self.filename, "a") as a:
            a.write(f"{item}\n")

    def high_score(self) -> list:
        contentsList = []
        with open(self.filename, "r") as h:
            for text in h:
                text = text.rstrip('\r\n')
                contentsList.append(int(text))
        return (sorted(contentsList))[::-1]


print(ScoreBoard("score.txt").high_score())
