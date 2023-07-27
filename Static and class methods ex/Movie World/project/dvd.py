import datetime


class DVD:
    id_counter = 1

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        day, month_number_as_str, year = date.split('.')
        monthinteger = int(month_number_as_str)
        month = datetime.date(1900, monthinteger, 1).strftime('%B')

        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        rented_status = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {rented_status}"
