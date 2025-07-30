from template import TemplateMethod

class CSVProcessor(TemplateMethod):
    def insert_value_in_doc(self, formatted_data_with_id):
        # Implementation for inserting data into a CSV document
        print(f"Inserting data into CSV: {formatted_data_with_id}")


data1 = ["Alice", "Johnson", "New York"]

csv_processor = CSVProcessor()
csv_processor.insert_data(data1)