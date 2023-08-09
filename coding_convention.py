import json


class StudentRecordManager:
    """This is a class to manage student records."""

    def __init__(self, filename='studentRecords.json'):
        """
        Initialize the StudentRecordManager.
        Parameters:
        - filename (str): The name of the JSON file to store the records.
        """
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        """
        Load student records from the JSON file.
        Returns:
        - list: List of student records.
        """
        try:
            with open(self.filename, 'r') as file:
                records = json.load(file)
                return records
        except FileNotFoundError:
            return []

    def save_records(self):
        """
        Save student records to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.records, file, indent=4)

    def add_student(self, student_id, name, age, grade):
        """
        Add a new student record.
        Parameters:
        - student_id (int): Student ID.
        - name (str): Student name.
        - age (int): Student age.
        - grade (str): Student grade.
        """
        new_student = {'student_id': student_id, 'name': name, 'age': age, 'grade': grade}
        self.records.append(new_student)
        self.save_records()

    def search_student(self, key, value):
        """
        Search for a student record by student_id or name.
        Parameters:
        - key (str): 'student_id' or 'name'.
        - value (int or str): Value to search for.
        Returns:
        - dict: Student record containing 'age' and 'grade'.
        """
        for student in self.records:
            if student[key] == value:
                return {'age': student['age'], 'grade': student['grade']}
        return None

    def update_student(self, key, value, field, new_value):
        """
        Update a student's information by student_id or name.
        Parameters:
        - key (str): 'student_id' or 'name'.
        - value (int or str): Value to search for.
        - field (str): Field to update ('age' or 'grade').
        - new_value (int or str): New value for the field.
        """
        for student in self.records:
            if student[key] == value:
                student[field] = new_value
                self.save_records()
                return
        print("Student not found.")


if __name__ == "__main__":
    manager = StudentRecordManager()
    while True:
        print("\n1. Add Student\n2. Search Student\n3. Update Student\n4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            manager.add_student(student_id, name, age, grade)
            print("Student added.")

        elif choice == '2':
            search_key = input("What do you want to search by? 'student_id' or 'name': ")
            search_value = input("Enter value to search: ")
            result = manager.search_student(search_key, search_value)
            if result:
                print(f"Age: {result['age']}, Grade: {result['grade']}")
            else:
                print("Student not found.")

        elif choice == '3':
            update_key = input("What do you want to update by? 'student_id' or 'name': ")
            update_value = input("Enter value: ")
            field = input("Enter field to update (age or grade): ")
            new_value = input("Enter new value: ")
            manager.update_student(update_key, update_value, field, new_value)

        elif choice == '4':
            print("Exiting...")
            break
