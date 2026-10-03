# ============================================================
# PYTHON PROGRAMMING TASKS
# All 12 programs in one file
# ============================================================


# ============================================================
# PROGRAM 1: Safecracker - Palindrome and Digit Sum
# ============================================================

def can_crack(n):
    if n < 0:
        return False

    original = n
    digit_sum = 0
    reversed_number = 0

    while n > 0:
        digit = n % 10
        digit_sum += digit
        reversed_number = reversed_number * 10 + digit
        n //= 10

    # 0 is a palindrome, but division by zero is not possible.
    if original == 0:
        return True

    return original == reversed_number and original % digit_sum == 0


print("\nPROGRAM 1: SAFECRACKER")
n = int(input("Enter a number: "))
print("Output:", can_crack(n))


# ============================================================
# PROGRAM 2: Most Frequent Word
# ============================================================

import string

def most_frequent_and_longest_repeated(paragraph):
    words = paragraph.lower().split()

    cleaned_words = []
    for word in words:
        cleaned = word.strip(string.punctuation)
        if cleaned:
            cleaned_words.append(cleaned)

    frequency = {}

    for word in cleaned_words:
        frequency[word] = frequency.get(word, 0) + 1

    most_frequent = max(frequency, key=frequency.get)
    most_count = frequency[most_frequent]

    repeated_words = [
        word for word, count in frequency.items()
        if count > 1
    ]

    longest_repeated = max(repeated_words, key=len) if repeated_words else None

    return most_frequent, most_count, longest_repeated


print("\nPROGRAM 2: MOST FREQUENT WORD")
paragraph = input("Enter a paragraph: ")

word, count, longest = most_frequent_and_longest_repeated(paragraph)

print(f"Most frequent word: '{word}' ({count} times)")

if longest:
    print(f"Longest repeated word: '{longest}'.")
else:
    print("Longest repeated word: None.")


# ============================================================
# PROGRAM 3: Staircase Climbing - Recursion and Memoization
# ============================================================

import time
from functools import lru_cache

def count_ways_recursive(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return (
        count_ways_recursive(n - 1)
        + count_ways_recursive(n - 2)
        + count_ways_recursive(n - 3)
    )


@lru_cache(maxsize=None)
def count_ways_memo(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    return (
        count_ways_memo(n - 1)
        + count_ways_memo(n - 2)
        + count_ways_memo(n - 3)
    )


print("\nPROGRAM 3: STAIRCASE CLIMBING")
n = int(input("Enter number of stairs: "))

print("Ways using recursion:", count_ways_recursive(n))
print("Ways using memoization:", count_ways_memo(n))

# Time comparison for n = 30
test_n = 30

start = time.perf_counter()
recursive_result = count_ways_recursive(test_n)
recursive_time = time.perf_counter() - start

count_ways_memo.cache_clear()

start = time.perf_counter()
memo_result = count_ways_memo(test_n)
memo_time = time.perf_counter() - start

print("\nTime comparison for n = 30:")
print("Recursive result:", recursive_result)
print("Recursive time:", recursive_time, "seconds")
print("Memoized result:", memo_result)
print("Memoized time:", memo_time, "seconds")

print(
    "Observation: Memoization is much faster because previously "
    "calculated results are stored and reused."
)


# ============================================================
# PROGRAM 4: Collatz Conjecture
# ============================================================

from functools import lru_cache

@lru_cache(maxsize=None)
def collatz_steps(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + collatz_steps(n // 2)
    else:
        return 1 + collatz_steps(3 * n + 1)


print("\nPROGRAM 4: COLLATZ CONJECTURE")

n = int(input("Enter a positive integer: "))
print("Steps to reach 1:", collatz_steps(n))

longest_number = 1
longest_chain = 0

for number in range(1, 10001):
    steps = collatz_steps(number)

    if steps > longest_chain:
        longest_chain = steps
        longest_number = number

print(
    f"Between 1 and 10,000, the number producing the longest "
    f"chain is {longest_number}, with {longest_chain} steps."
)


# ============================================================
# PROGRAM 5: Library Management System
# ============================================================

class Item:
    def __init__(self, title):
        self.__title = title
        self.__is_borrowed = False

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def is_borrowed(self):
        return self.__is_borrowed

    def get_title(self):
        return self.__title

    def __str__(self):
        status = "Borrowed" if self.__is_borrowed else "Available"
        return f"Item: '{self.__title}' ({status})"


class Book(Item):
    def __init__(self, title, author, pages):
        super().__init__(title)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book: '{self.get_title()}' by {self.author} ({self.pages} pages)"


class DVD(Item):
    def __init__(self, title, duration_minutes):
        super().__init__(title)
        self.duration_minutes = duration_minutes

    def __str__(self):
        return (
            f"DVD: '{self.get_title()}' "
            f"({self.duration_minutes} minutes)"
        )


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def borrow_item(self, title):
        for item in self.items:
            if item.get_title().lower() == title.lower():
                if item.borrow():
                    print(f"'{title}' has been borrowed.")
                else:
                    print(f"'{title}' is already borrowed.")
                return

        print(f"'{title}' was not found in the library.")

    def show_available(self):
        print("Available Items:")

        found = False

        for item in self.items:
            if not item.is_borrowed():
                print(item)
                found = True

        if not found:
            print("No items are currently available.")


print("\nPROGRAM 5: LIBRARY MANAGEMENT SYSTEM")

lib = Library()

lib.add_item(Book("Atomic Habits", "James Clear", 320))
lib.add_item(DVD("Inception", 148))

lib.borrow_item("Inception")
lib.show_available()


# ============================================================
# PROGRAM 6: Circle Class
# ============================================================

import math

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def Area(self):
        return math.pi * self.r * self.r

    def Perimeter(self):
        return 2 * math.pi * self.r

    def testBelongs(self, x, y):
        distance_squared = (
            (x - self.a) ** 2 +
            (y - self.b) ** 2
        )

        return distance_squared <= self.r ** 2


print("\nPROGRAM 6: CIRCLE CLASS")

a = float(input("Enter center x-coordinate: "))
b = float(input("Enter center y-coordinate: "))
r = float(input("Enter radius: "))

circle = Circle(a, b, r)

print("Area:", circle.Area())
print("Perimeter:", circle.Perimeter())

x = float(input("Enter point x-coordinate: "))
y = float(input("Enter point y-coordinate: "))

if circle.testBelongs(x, y):
    print("The point belongs to the circle.")
else:
    print("The point does not belong to the circle.")


# ============================================================
# PROGRAM 7: Computation Class
# ============================================================

class Computation:
    def __init__(self):
        pass

    def Factorial(self, n):
        if n < 0:
            return None

        result = 1

        for i in range(1, n + 1):
            result *= i

        return result

    def Sum(self, n):
        return n * (n + 1) // 2

    def testPrim(self, n):
        if n < 2:
            return False

        if n == 2:
            return True

        if n % 2 == 0:
            return False

        divisor = 3

        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 2

        return True

    def testPrims(self, n1, n2):
        return self.testPrim(n1) and self.testPrim(n2)


print("\nPROGRAM 7: COMPUTATION CLASS")

comp = Computation()

n = int(input("Enter an integer for factorial: "))
print("Factorial:", comp.Factorial(n))

n = int(input("Enter n to find sum from 1 to n: "))
print("Sum:", comp.Sum(n))

n = int(input("Enter an integer to test for prime: "))

if comp.testPrim(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if comp.testPrims(n1, n2):
    print("Both numbers are prime.")
else:
    print("Both numbers are not prime.")


# ============================================================
# PROGRAM 8: Inheritance
# ============================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayPerson(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, rollNo, course):
        super().__init__(name, age)
        self.rollNo = rollNo
        self.course = course

    def displayStudent(self):
        print("\nStudent Details:")
        self.displayPerson()
        print("Roll No:", self.rollNo)
        print("Course:", self.course)


class Teacher(Person):
    def __init__(self, name, age, employeeId, subject):
        super().__init__(name, age)
        self.employeeId = employeeId
        self.subject = subject

    def displayTeacher(self):
        print("\nTeacher Details:")
        self.displayPerson()
        print("Employee ID:", self.employeeId)
        print("Subject:", self.subject)


print("\nPROGRAM 8: INHERITANCE")

student = Student("Rahul", 19, 101, "Computer Science")
teacher = Teacher("Dr. Sharma", 40, "T001", "Python")

student.displayStudent()
teacher.displayTeacher()


# ============================================================
# PROGRAM 9: Anagram Checker
# ============================================================

def is_anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    return sorted(word1) == sorted(word2)


print("\nPROGRAM 9: ANAGRAM CHECKER")

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if is_anagram(word1, word2):
    print("Yes")
else:
    print("No")


# ============================================================
# PROGRAM 10: Hill Number Check
# ============================================================

def is_hill_number(n):
    digits = [int(digit) for digit in str(n)]

    if len(digits) < 3:
        return False

    i = 1

    # Strictly increasing part
    while i < len(digits) and digits[i] > digits[i - 1]:
        i += 1

    # There must be at least one increase
    if i == 1:
        return False

    # Strictly decreasing part
    decrease_start = i

    while i < len(digits) and digits[i] < digits[i - 1]:
        i += 1

    # There must be at least one decrease
    if decrease_start == len(digits):
        return False

    return i == len(digits)


print("\nPROGRAM 10: HILL NUMBER CHECK")

n = int(input("Enter a number: "))

if is_hill_number(n):
    print("Yes")
else:
    print("No")


# ============================================================
# PROGRAM 11: BONUS - Stack
# ============================================================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        # Manually add an element without using list.append()
        new_items = [None] * (len(self.items) + 1)

        for i in range(len(self.items)):
            new_items[i] = self.items[i]

        new_items[len(self.items)] = x
        self.items = new_items

    def pop(self):
        if len(self.items) == 0:
            print("Stack is empty.")
            return None

        top = self.items[len(self.items) - 1]

        new_items = [None] * (len(self.items) - 1)

        for i in range(len(new_items)):
            new_items[i] = self.items[i]

        self.items = new_items

        return top

    def peek(self):
        if len(self.items) == 0:
            print("Stack is empty.")
            return None

        return self.items[len(self.items) - 1]

    def display(self):
        print("Stack:", self.items)


print("\nPROGRAM 11: BONUS - STACK")

stack = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value to push: ")
        stack.push(value)
        print("Element pushed.")

    elif choice == "2":
        value = stack.pop()
        if value is not None:
            print("Popped:", value)

    elif choice == "3":
        value = stack.peek()
        if value is not None:
            print("Top element:", value)

    elif choice == "4":
        stack.display()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")


# ============================================================
# PROGRAM 12: BONUS - Singly Linked List
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            print("Deleted:", deleted_value)
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data
        current.next = None

        print("Deleted:", deleted_value)

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print()


print("\nPROGRAM 12: BONUS - SINGLY LINKED LIST")

linked_list = LinkedList()

while True:
    print("\n1. Insert at end")
    print("2. Delete from end")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value to insert: ")
        linked_list.insert_end(value)
        print("Element inserted.")

    elif choice == "2":
        linked_list.delete_end()

    elif choice == "3":
        linked_list.display()

    elif choice == "4":
        break

    else:
        print("Invalid choice.")


# ============================================================
# END OF ALL 12 PROGRAMS
# ============================================================
