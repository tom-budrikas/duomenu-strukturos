import copy
import sys
import time
from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from JumpSearch import jump_search
from LinearSearch import linear_search
from LinkedList import LinkedList
import os

from SelectionSort import selection_sort
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import timeit
import tests

data_100_file = open("data_100.txt", "r")
data_100 = data_100_file.read().split("\n")
data_100 = list(map(int, data_100))
data_10000_file = open("data_10000.txt", "r")
data_10000 = data_10000_file.read().split("\n")
data_10000 = list(map(int, data_10000))
data_1000000_file = open("data_1000000.txt", "r")
data_1000000 = data_1000000_file.read().split("\n")
data_1000000 = list(map(int, data_1000000))

data_100_file.close()
data_10000_file.close()
data_1000000_file.close()

result_file = open("result.txt", "w")
result = ""

insert_start_100_time = timeit.timeit(lambda: tests.test_insert_start(data_100), number=10)
insert_end_100_time = timeit.timeit(lambda: tests.test_insert_end(data_100), number=10)

result += "=== LINKED LISTS ===\n\n"

result += f"Average time to populate 100 elements into linked list inserting at the start: {insert_start_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to populate 100 elements into linked list inserting at the end: {insert_end_100_time / 10 * 1000:.4f} ms\n"

insert_start_10000_time = timeit.timeit(lambda: tests.test_insert_start(data_10000), number=10)
insert_end_10000_time = timeit.timeit(lambda: tests.test_insert_end(data_10000), number=10)

result += f"\nAverage time to populate 10000 elements into linked list inserting at the start: {insert_start_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to populate 10000 elements into linked list inserting at the end: {insert_end_10000_time / 10 * 1000:.4f} ms\n"

insert_start_1000000_time = timeit.timeit(lambda: tests.test_insert_start(data_1000000), number=10)
insert_end_1000000_time = timeit.timeit(lambda: tests.test_insert_end(data_1000000), number=10)

result += f"\nAverage time to populate 1000000 elements into linked list inserting at the start: {insert_start_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to populate 1000000 elements into linked list inserting at the end: {insert_end_1000000_time / 10 * 1000:.4f} ms\n"

print_100_time = timeit.timeit(lambda: tests.test_print_nodes(LinkedList(data_100)), number=10)
print_10000_time = timeit.timeit(lambda: tests.test_print_nodes(LinkedList(data_10000)), number=10)

result += f"\nAverage time to print 100 element linked list as string: {print_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to print 10000 element linked list as string: {print_10000_time / 10 * 1000:.4f} ms\n"

list_100 = LinkedList(data_100)
find_start_node_100_time = timeit.timeit(lambda: tests.test_find_node(list_100, 0), number=10)
find_middle_node_100_time = timeit.timeit(lambda: tests.test_find_node(list_100, 49), number=10)
find_end_node_100_time = timeit.timeit(lambda: tests.test_find_node(list_100, 99), number=10)

result += f"\nAverage time to find first node in 100 element linked list: {find_start_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find middle node in 100 element linked list: {find_middle_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find last node in 100 element linked list: {find_end_node_100_time / 10 * 1000:.4f} ms\n"

list_10000 = LinkedList(data_10000)
find_start_node_10000_time = timeit.timeit(lambda: tests.test_find_node(list_10000, 0), number=10)
find_middle_node_10000_time = timeit.timeit(lambda: tests.test_find_node(list_10000, 4999), number=10)
find_end_node_10000_time = timeit.timeit(lambda: tests.test_find_node(list_10000, 9999), number=10)

result += f"\nAverage time to find first node in 10000 element linked list: {find_start_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find middle node in 10000 element linked list: {find_middle_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find last node in 10000 element linked list: {find_end_node_10000_time / 10 * 1000:.4f} ms\n"

list_1000000 = LinkedList(data_1000000)
find_start_node_1000000_time = timeit.timeit(lambda: tests.test_find_node(list_1000000, 0), number=10)
find_middle_node_1000000_time = timeit.timeit(lambda: tests.test_find_node(list_1000000, 499999), number=10)
find_end_node_1000000_time = timeit.timeit(lambda: tests.test_find_node(list_1000000, 999999), number=10)

result += f"\nAverage time to find first node in 1000000 element linked list: {find_start_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find middle node in 1000000 element linked list: {find_middle_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find last node in 1000000 element linked list: {find_end_node_1000000_time / 10 * 1000:.4f} ms\n"

delete_start_node_100_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_100), 0), number=10)
delete_middle_node_100_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_100), 49), number=10)
delete_end_node_100_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_100), 99), number=10)

result += f"\nAverage time to delete first node in 100 element linked list: {delete_start_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to delete middle node in 100 element linked list: {delete_middle_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to delete last node in 100 element linked list: {delete_end_node_100_time / 10 * 1000:.4f} ms\n"

delete_start_node_10000_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_10000), 0), number=10)
delete_middle_node_10000_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_10000), 4999), number=10)
delete_end_node_10000_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_10000), 9999), number=10)

result += f"\nAverage time to delete first node in 10000 element linked list: {delete_start_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to delete middle node in 10000 element linked list: {delete_middle_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to delete last node in 10000 element linked list: {delete_end_node_10000_time / 10 * 1000:.4f} ms\n"

delete_start_node_1000000_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_1000000), 0), number=10)
delete_middle_node_1000000_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_1000000), 499999), number=10)
delete_end_node_1000000_time = timeit.timeit(lambda: tests.test_delete_node(LinkedList(data_1000000), 999999), number=10)

result += f"\nAverage time to delete first node in 1000000 element linked list: {delete_start_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to delete middle node in 1000000 element linked list: {delete_middle_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to delete last node in 1000000 element linked list: {delete_end_node_1000000_time / 10 * 1000:.4f} ms\n"

list_100 = LinkedList(data_100)
find_start_node_100_time = timeit.timeit(lambda: tests.test_find_node(list_100, 0), number=10)
find_middle_node_100_time = timeit.timeit(lambda: tests.test_find_node(list_100, 49), number=10)
find_end_node_100_time = timeit.timeit(lambda: tests.test_find_node(list_100, 99), number=10)

result += f"\nAverage time to find first node in 100 element linked list: {find_start_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find middle node in 100 element linked list: {find_middle_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find last node in 100 element linked list: {find_end_node_100_time / 10 * 1000:.4f} ms\n"

list_10000 = LinkedList(data_10000)
find_start_node_10000_time = timeit.timeit(lambda: tests.test_find_node(list_10000, 0), number=10)
find_middle_node_10000_time = timeit.timeit(lambda: tests.test_find_node(list_10000, 4999), number=10)
find_end_node_10000_time = timeit.timeit(lambda: tests.test_find_node(list_10000, 9999), number=10)

result += f"\nAverage time to find first node in 10000 element linked list: {find_start_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find middle node in 10000 element linked list: {find_middle_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find last node in 10000 element linked list: {find_end_node_10000_time / 10 * 1000:.4f} ms\n"

list_1000000 = LinkedList(data_1000000)
find_start_node_1000000_time = timeit.timeit(lambda: tests.test_find_node(list_1000000, 0), number=10)
find_middle_node_1000000_time = timeit.timeit(lambda: tests.test_find_node(list_1000000, 499999), number=10)
find_end_node_1000000_time = timeit.timeit(lambda: tests.test_find_node(list_1000000, 999999), number=10)

result += f"\nAverage time to find first node in 1000000 element linked list: {find_start_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find middle node in 1000000 element linked list: {find_middle_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to find last node in 1000000 element linked list: {find_end_node_1000000_time / 10 * 1000:.4f} ms\n"

insert_start_node_100_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_100), 0), number=10)
insert_middle_node_100_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_100), 49), number=10)
insert_end_node_100_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_100), 99), number=10)

result += f"\nAverage time to insert first node in 100 element linked list: {insert_start_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to insert middle node in 100 element linked list: {insert_middle_node_100_time / 10 * 1000:.4f} ms\n"
result += f"Average time to insert last node in 100 element linked list: {insert_end_node_100_time / 10 * 1000:.4f} ms\n"

insert_start_node_10000_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_10000), 0), number=10)
insert_middle_node_10000_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_10000), 4999), number=10)
insert_end_node_10000_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_10000), 9999), number=10)

result += f"\nAverage time to insert first node in 10000 element linked list: {insert_start_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to insert middle node in 10000 element linked list: {insert_middle_node_10000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to insert last node in 10000 element linked list: {insert_end_node_10000_time / 10 * 1000:.4f} ms\n"

insert_start_node_1000000_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_1000000), 0), number=10)
insert_middle_node_1000000_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_1000000), 499999), number=10)
insert_end_node_1000000_time = timeit.timeit(lambda: tests.test_insert_node(LinkedList(data_1000000), 999999), number=10)

result += f"\nAverage time to insert first node in 1000000 element linked list: {insert_start_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to insert middle node in 1000000 element linked list: {insert_middle_node_1000000_time / 10 * 1000:.4f} ms\n"
result += f"Average time to insert last node in 1000000 element linked list: {insert_end_node_1000000_time / 10 * 1000:.4f} ms\n"

result += "\n\n=== SORTS ===\n\n"

bubble_sort_100_time = timeit.timeit(lambda: bubble_sort(copy.deepcopy(data_100)), number=1)
selection_sort_100_time = timeit.timeit(lambda: selection_sort(copy.deepcopy(data_100)), number=1)
insertion_sort_100_time = timeit.timeit(lambda: insertion_sort(copy.deepcopy(data_100)), number=1)

result += f"Average time to bubble sort 100 element array: {bubble_sort_100_time * 1000:.4f} ms\n"
result += f"Average time to selection sort 100 element array: {selection_sort_100_time * 1000:.4f} ms\n"
result += f"Average time to insertion sort 100 element array: {insertion_sort_100_time * 1000:.4f} ms\n"

bubble_sort_10000_time = timeit.timeit(lambda: bubble_sort(copy.deepcopy(data_10000)), number=1)
selection_sort_10000_time = timeit.timeit(lambda: selection_sort(copy.deepcopy(data_10000)), number=1)
insertion_sort_10000_time = timeit.timeit(lambda: insertion_sort(copy.deepcopy(data_10000)), number=1)

result += f"\nAverage time to bubble sort 10000 element array: {bubble_sort_10000_time * 1000:.4f} ms\n"
result += f"Average time to selection sort 10000 element array: {selection_sort_10000_time * 1000:.4f} ms\n"
result += f"Average time to insertion sort 10000 element array: {insertion_sort_10000_time * 1000:.4f} ms\n"

result += "\n\n=== SEARCHES ===\n\n"

sorted_100 = copy.deepcopy(data_100)
selection_sort(sorted_100)
sorted_10000 = copy.deepcopy(data_10000)
selection_sort(sorted_10000)

linear_search_100_time = timeit.timeit(lambda: linear_search(sorted_100, 1532), number=1)
jump_search_100_time = timeit.timeit(lambda: jump_search(sorted_100, 1532), number=1)
binary_search_100_time = timeit.timeit(lambda: linear_search(sorted_100, 1532), number=1)

result += f"Average time to search for an element (1532) in 100 element array with linear search: {linear_search_100_time * 1000:.4f} ms\n"
result += f"Average time to search for an element (1532) in 100 element array with jump search: {jump_search_100_time * 1000:.4f} ms\n"
result += f"Average time to search for an element (1532) in 100 element array with binary search: {binary_search_100_time * 1000:.4f} ms\n"

linear_search_10000_time = timeit.timeit(lambda: linear_search(sorted_10000, 1532), number=1)
jump_search_10000_time = timeit.timeit(lambda: jump_search(sorted_10000, 1532), number=1)
binary_search_10000_time = timeit.timeit(lambda: linear_search(sorted_10000, 1532), number=1)

result += f"\nAverage time to search for an element (1532) in 10000 element array with linear search: {linear_search_10000_time * 1000:.4f} ms\n"
result += f"Average time to search for an element (1532) in 10000 element array with jump search: {jump_search_10000_time * 1000:.4f} ms\n"
result += f"Average time to search for an element (1532) in 10000 element array with binary search: {binary_search_10000_time * 1000:.4f} ms"

result_file.write(result)
print("Output results successfully to: result.txt")
result_file.close()