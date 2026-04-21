class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter


class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grades(self, index):
        score = self.get_by_index(index)
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        elif score >= 50:
            return "E"
        else:
            return "F"

    def find(self, points):
        indexy_zaku = []
        for i in range(len(self.scores)):  # kredit tonda
            if self.scores[i] == points:
                indexy_zaku.append(i)
        return indexy_zaku

    def get_sorted(self):
        all_scores = self.scores.copy()
        n = len(all_scores)
        for i in range(n):
            for j in range(0, n - i - 1):
                if all_scores[j] > all_scores[j+1]:
                    all_scores[j], all_scores[j +
                                              1] = all_scores[j+1], all_scores[j]
        return all_scores


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    pocet = results.count()
    print(f"Test psalo {pocet} žáků.")

    for i in range(pocet):
        body = results.scores[i]
        znamka = results.get_grades(i)
        print(f"Student {i}: {body} points – {znamka}")

    print("Studenti s plným počtem bodů:")
    plny_pocet = results.find(100)
    print(plny_pocet)

    print("Seřazené výsledky:")
    serazene = results.get_sorted()
    print(serazene)


if __name__ == "__main__":
    main()
