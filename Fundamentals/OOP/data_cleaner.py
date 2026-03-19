class DataCleaner:
    def __init__(self, data : list):
        self.data = data
        self.new_data = []

    def drop_nulls(self):
        for row in self.data:
            if all(value is not None for value in row.values()):
                self.new_data.append(row)

    def drop_empty_strings(self):
        temp_data = []
        for row in self.new_data:
            if all(value != '' for value in row.values()):
                temp_data.append(row)
        self.new_data = temp_data   

    def summary(self):
        removed = len(self.data) - len(self.new_data)
        print(f"Original data: {len(self.data)}")
        print(f"Cleaned data: {len(self.new_data)}")
        print(f'Number of nulls removed: {removed}')


data = [
    {"name": "Sebastian", "age": 23, "salary": None},
    {"name": "", "age": None, "salary": 50000},
    {"name": "Ana", "age": 25, "salary": 60000},
]

cleaner = DataCleaner(data)
cleaner.drop_nulls()         # elimina rows con cualquier None
cleaner.drop_empty_strings() # elimina rows con strings vacíos
cleaner.summary()            # imprime cuántos rows quedaron y cuántos se eliminaron