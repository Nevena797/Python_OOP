from project.table.table import Table


class OutsideTable(Table):

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value not in range(51, 100 + 1):
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")

        self.__table_number = value
