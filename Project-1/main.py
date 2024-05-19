import copy

from classes import Student, BTree, Queue, SortedQueue
import csv
import time

students = []
with open('./data/stud_record.csv', 'r', encoding='utf-8-sig') as rf:
    reader = csv.DictReader(rf, delimiter=',')
    for row in reader:
        students.append(
            Student(num_id=row['number'], name=row['name'], age=row['age'], gender=row['gender'], city=row['city']))

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        return result, end_time - start_time
    return wrapper

@measure_time
def enqueue_student(queue, student):
    queue.enqueue(student)

@measure_time
def search_student(queue, num_id):
    return queue.search(num_id)

@measure_time
def delete_student(queue, num_id):
    return queue.delete(num_id)

def logger(name, data_structure, avg_count=1000):
    student_to_insert = Student(301, "Beltran", 22.18, "M", "Kolsi")
    student_to_search = Student(12, "Reid", 28.54, "M", "Pacoima")
    student_to_delete = Student(12, "Reid", 28.54, "M", "Pacoima")

    insert = []
    search = []
    delete = []
    for i in range(avg_count):
        copy_of_ds = copy.deepcopy(data_structure)
        _, insert_time_unsorted = enqueue_student(copy_of_ds, student_to_insert)
        _, search_time_unsorted = search_student(copy_of_ds, student_to_search.num_id)
        _, delete_time_unsorted = delete_student(copy_of_ds, student_to_delete.num_id)
        insert.append(insert_time_unsorted)
        search.append(search_time_unsorted)
        delete.append(delete_time_unsorted)

    print(f"Initial {name} size:", data_structure.size())
    print(f"Time to insert in {name}: {sum(insert)/avg_count}")
    print(f"Time to search in {name}: {sum(search)/avg_count}")
    print(f"Time to delete in {name}: {sum(delete)/avg_count}")

def analys_queues():
    # Test Unsorted Queue
    print("Testing Unsorted Queue")
    unsorted_queue = Queue()
    for student in students:
        unsorted_queue.enqueue(student)
    logger("Unsorted Queue", unsorted_queue)

    # Test Sorted Queue
    print("\nTesting Sorted Queue")
    sorted_queue = SortedQueue()
    for student in students:
        sorted_queue.enqueue(student)
    logger("Sorted Queue", sorted_queue)

    """    
    b_tree = BTree(order=5)
    expected_len = 0
    for student in students:
        b_tree.insert(student)
        expected_len += 1"""

analys_queues()


def test_queues():

    # Test Unsorted Queue
    print("Testing Unsorted Queue")
    unsorted_queue = Queue()
    for student in students:
        unsorted_queue.enqueue(student)

    print("Initial Unsorted Queue:", unsorted_queue)

    print("Dequeue from Unsorted Queue:", unsorted_queue.dequeue())
    print("After Dequeue:", unsorted_queue)

    print("Search for numid 2 in Unsorted Queue:", unsorted_queue.search(2))
    print("Delete numid 1 in Unsorted Queue:", unsorted_queue.delete(1))
    print("After Delete:", unsorted_queue)

    # Test Sorted Queue
    print("\nTesting Sorted Queue")
    sorted_queue = SortedQueue()
    for student in students:
        sorted_queue.enqueue(student)

    print("Initial Sorted Queue:", sorted_queue)

    print("Dequeue from Sorted Queue:", sorted_queue.dequeue())
    print("After Dequeue:", sorted_queue)

    print("Search for numid 2 in Sorted Queue:", sorted_queue.search(2))
    print("Delete numid 1 in Sorted Queue:", sorted_queue.delete(1))
    print("After Delete:", sorted_queue)

#test_queues()

"""    
b_tree = BTree(order=5)
expected_len = 0
for student in students:
    b_tree.insert(student)
    expected_len += 1"""
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
print('-------------')
#delete test
print(f'Tree before deletions: \n{b_tree}')
print('As list', b_tree.get_as_list(), len(b_tree.get_as_list()))
print('--------------')
delete_students = students
expected_len = len(students)
for student in delete_students:
    print(f'Deleting {student}')
    b_tree.delete(student.get_id())
    expected_len -= 1
    print(f'Tree after delete:')
    print(b_tree)
    print('As list', b_tree.get_as_list())
    print('Is list correct?', b_tree.get_as_list() == sorted(b_tree.get_as_list()))
    print('Is correct length?', len(b_tree.get_as_list()) == expected_len)
    print('------------')
"""