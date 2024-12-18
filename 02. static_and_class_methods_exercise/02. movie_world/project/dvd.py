from calendar import month_name


class DVD:
    def __init__(self, name: str, id_number: int, creation_year: int, creation_month: str,
                 age_restriction: int) -> None:
        self.name = name
        self.id = id_number
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id_number: int, name: str, date: str, age_registration: int):
        day, month, year = [int(x) for x in date.split(".")]  # data dd.mm.year
        return cls(name, id_number, year, month_name[month], age_registration)

    def __repr__(self):
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) "
                f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")
