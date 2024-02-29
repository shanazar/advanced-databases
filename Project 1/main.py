from classes import Student, BTree
import csv

students = []
with open('./data/stud_record.csv', 'r', encoding='utf-8-sig') as rf:
    reader = csv.DictReader(rf, delimiter=',')
    for row in reader:
        students.append(
            Student(num_id=row['number'], name=row['name'], age=row['age'], gender=row['gender'], city=row['city']))

b_tree = BTree(degree=3)
expected_len = 0
for student in students:
    b_tree.insert(student)
    expected_len += 1
"""
# insertion test
    print(f'Insert value: {student}')
    print(b_tree)
    print('As list', b_tree.get_as_list())
    print('Is list correct?', b_tree.get_as_list() == sorted(b_tree.get_as_list()))
    print('Is correct length?', len(b_tree.get_as_list()) == expected_len)
    print('-----------')
# search test
for student in students:
    found_student = b_tree.search(student.get_id())
    print(f'Found key? {found_student.get_id() == student.get_id()}')
    print(f'Fetched student: {student.get_id()} - {student.get_name()}')
"""
