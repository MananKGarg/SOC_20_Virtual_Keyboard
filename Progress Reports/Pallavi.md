# Virtual-Keyboard-Documentation
# Github:
## 1. What is Github?
GitHub is a code hosting platform for version control and collaboration. It lets people work together on projects from anywhere.
## 2. Creating repositories(used to organise a single project)
Repositories can contain folders and files, images, videos, spreadsheets, and data sets – anything your project needs. Hello-world repository can be a place where you store ideas, resources, or even share and discuss things with others. Creating branches(working on various parts/versions of the same repository) Make and commit changes(if one wishes to change any particular part of code or some statements ) Pull request(propsing your changes to someone else to get reviewed) Merge request(merging the branch reviewed by others into the master branch) This is how a particular project can be made organized and working on it becomes simpler and more collaberative.
## 3. Creating branch(work on different versions of a repository at one time)
By default repositoy has a branch named master which is considered to be the definitive branch. We use branches to experiment and make edits before committing them to master. If someone else made changes to the master branch while we were working on your branch, we could pull in those updates.
##### References: https://guides.github.com/activities/hello-world/
# Dual boot: 
##### Reference: https://www.youtube.com/watch?v=u5QyjHIYwTQ
# Markdown:
Any files with .md extension are markdown files. Markdown language is extensively used to write files precisely. Markdown Files are very easy to write and handle. It has its own cheatsheet to follow.Markdown is often used to format readme files, for writing messages in online forums,and to create rich text using a plain text editor. 
##### References: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
# PYTHON:
Python is a high level programming language which is easy to understand by its code. It is widely used by software developers, programmers, etc.
## 1. An Informal Introduction to Python
1. Using Python as a Calculator  
  1.1. Numbers 
  1.2. Strings 
  1.3. Lists
2. First Steps Towards Programming

#### NOTE: 
1. a/b  # classic division returns a float
2. a//b  # floor division discards the fractional part
3. a%b  # the % operator returns the remainder of the division
4. a** b  # a to the power of b
5. Python supports numbers of type int, float, Decimal and Fraction
6. Has built-in support for complex numbers, and uses the j or J suffix to indicate the imaginary part (a+bj).
7. 'doesn\'t'  # use \' to escape the single quote..."doesn't"
8.  print('C:\some\name')  # here \n means newline!...C:\some
9.  print(r'C:\some\name')  # note the r before the quote...C:\some\name (raw strings)
10. s[:i] + s[i:] is always equal to s:
11. The while loop executes as long as the condition remains true.
12. The keyword argument end can be used to avoid the newline after the output


## 2. More Control Flow Tools
1. if Statements
2. for Statements
3. The range() Function
4. break and continue Statements, and else Clauses on Loops
5. pass Statements
6. Defining Functions
7. More on Defining Functions 
  7.1. Default Argument Values
  7.2. Keyword Arguments 
  7.3. Special parameters
    7.3.1. Positional-or-Keyword Arguments
    7.3.2. Positional-Only Parameters
    7.3.3. Keyword-Only Arguments
    7.3.4. Function Examples
    7.3.5. Recap
  7.4. Arbitrary Argument Lists
  7.5. Unpacking Argument Lists
  7.6. Lambda Expressions
  7.7. Documentation Strings
  7.8. Function Annotations
8. Intermezzo: Coding Style

### NOTE:
1. x = int(input(" "))
2. if x < 0: [note the colon]
3. The keyword ‘elif’ is short for ‘else if’
4. Python’s for statement iterates over the items of any sequence (a list or a string)
5. range(5)  0, 1, 2, 3, 4
6. range(5, 10)  5, 6, 7, 8, 9
7. range(0, 10, 3)  0, 3, 6, 9
8. sum(range(4))  # 0 + 1 + 2 + 3 = 6
9. list(range(4))  [0, 1, 2, 3]
10. The break statement breaks out of the innermost enclosing for or while loop.
11. Loop statements may have an else clause i.e. the else clause belongs to the for loop, not the if statement
12. The pass can be used when a statement is required syntactically but the program requires no action.
13. The keyword def introduces a function definition
14. The return statement returns with a value from a function
15. The statement result.append(a) calls a method of the list object result
16. A method is a function that ‘belongs’ to an object and is named obj.methodname
17. The method append() adds a new element at the end of the list
18. Functions can also be called using keyword arguments of the form kwarg=value
19. When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter
20. write the function call with the *-operator to unpack the arguments out of a list or tuple
21. list(range(3, 6))     # normal call with separate arguments [3, 4, 5]
22. args = [3, 6] >>> list(range(*args))   # call with arguments unpacked from a list [3, 4, 5]
23. Small anonymous functions can be created with the lambda keyword #lambda a, b: a+b
24. Another use of lambda is to pass a small function as an argument
25. Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function

## 3. Data Structures
1. More on Lists
  1.1. Using Lists as Stacks
  1.2. Using Lists as Queues
  1.3. List Comprehensions
  1.4. Nested List Comprehensions
2. The del statement
3. Tuples and Sequences
4. Sets
5. Dictionaries
6. Looping Techniques
7. More on Conditions
8. Comparing Sequences and Other Types

### NOTE:
1. list.append(x) Add an item to the end of the list. Equivalent to a[len(a):] = [x].
2. list.extend(iterable) Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable
3. ist.insert(i, x) Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
4. list.remove(x) Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
5. list.pop([i]) Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. 
6. list.clear() Remove all items from the list. Equivalent to del a[:].
7. list.index(x[, start[, end]]) Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
8. list.count(x) Return the number of times x appears in the list.
9. list.sort(key=None, reverse=False) Sort the items of the list in place 
10. list.reverse() Reverse the elements of the list in place.
11. list.copy() Return a shallow copy of the list. Equivalent to a[:].
12. The list methods make it very easy to use a list as a stack, (“last-in, first-out”)
13. To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends...  from collections import deque
14. List comprehensions provide a concise way to create lists
15. squares = list(map(lambda x: x**2, range(10))) or = [x**2 for x in range(10)]
16. 


## 4. Input and Output
1. Fancier Output Formatting
  1.1. Formatted String Literals
  1.2. The String format() Method
  1.3. Manual String Formatting
  1.4. Old string formatting
2. Reading and Writing Files
  2.1. Methods of File Objects
  2.2. Saving structured data with json

### NOTE:

## 5. Errors and Exceptions
1. Syntax Errors
2. Exceptions
3. Handling Exceptions
4. Raising Exceptions
5. User-defined Exceptions
6. Defining Clean-up Actions
7. Predefined Clean-up Actions

### NOTE:

## 6. Classes
1. A Word About Names and Objects
2. Python Scopes and Namespaces 
  2.1. Scopes and Namespaces Example
3. A First Look at Classes 
  3.1. Class Definition Syntax 
  3.2. Class Objects 
  3.3. Instance Objects 
  3.4. Method Objects 
  3.5. Class and Instance Variables
4. Random Remarks
5. Inheritance
  5.1. Multiple Inheritance
6. Private Variables
7. Odds and Ends
8. Iterators
9. Generators
10. Generator Expressions
##### References: https://docs.python.org/3/tutorial/ , https://www.learnpython.org/
# OpenCV [open source computer vision library]:
Computer Vision is the way of teaching intelligence to machines and making them see thing just like humans. 
OpenCV is image processwing library. Available on windows, linux, mac. Works in C, C++, Python.
Digital images are typically stored in a matrix. PPI - pixel per inch. Computer sees an image in the form of pixel matrix. Grey scaled images[each pixel represents the intensity of nly one shade][it has only 1 channel] and coloured images[has 3 channels- R[red] G[green] B[blue]]. Standard digital camera has 3 channels.
### Numpy: 
NumPy is the fundamental package for scientific computing with Python. It contains among other things: a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code, useful linear algebra, Fourier transform, and random number capabilities.

### Invisibility cloak code

