---
type: note
status: inbox
tags:
- tech/python
- tech/stack/pandas
sources:
- null
- '[[Pandas Basics Course]]'
authors:
- null
---
#🃏/semantic/pandas #🃏/source/pandas-basics-course

**Codewords:** Merge, Join, Concatenate, SQL-style Joins, Combining DataFrames

todo simplify last task (NO GROUPBY )
## Mock Dataframes

```python
import pandas as pd

data1 = {
 'student_id': [1, 2, 3],
 'name': ['John', 'Anna', 'Peter'],
 'age': [20, 22, 21],
 'grade_math': [85, 92, 78]
---
}
df1 = pd.DataFrame(data1)
```

![[Pasted image 20250518121103.png|300]]

```python
data2 = {
 'student_id': [3, 4, 5],
 'name': ['Peter', 'Sarah', 'Michael'],
 'age': [21, 19, 23],
 'grade_physics': [75, 90, 85]
}
df2 = pd.DataFrame(data2)
```

![[Pasted image 20250518121202.png|300]]
## 1. Concatenating DataFrames

**Vertical concatenation:**
![[Pasted image 20250511221625.png]]

```python
# Basic Vertical concatenation (adding rows)
df3 = pd.concat([df1, df2], axis=0)
```

![[Pasted image 20250518121434.png|500]]

>[!Note]
>Resulting DataFrame could have duplicated indexes (like in example above), which may be counterintuitive
>
>You have 3 options here:
>1) If indexes does not carry any useful information, simplty reset the index: `df.reset_index()`
>2) If you expect indexes to be unique for each table and they should not overlap, you can prevent this: `pd.concat(..., verify_integrity = Bool)`
>3) If you expect `pd.concat` to "squash" entries with same indexes (like with "Peter" from the example above) that won't be possible: you should instead use `pd.merge()`

```python
# Keep only common columns
df3 = pd.concat([df1, df2], join='inner') 
```
![[Pasted image 20250518123803.png|200]]

**Horizontal Concatenation:**
![[Pasted image 20250511221551.png]]

```python
# Horizontal concatenation (adding columns)
df3 = pd.concat([df1, df2], axis=1)
```

![[Pasted image 20250518124222.png]]

>[!Note]
>Horizontal concatenation is being done based on entries indexes. So make sure that entries do align together by the index
>
>If not so, sometimes can fix them, by applying `sort()` method and then `df.reset_index()` method

>[!Warning] 
>`pd.concat()` is a rather expensive operation. Do not apply in within a loop: it's better to first gather all dataframes in a single list and then execute `concat()` ones

### Exercises

**Practice Problem: Combining Club Membership Lists**

Let's work with a few DataFrames representing student involvement in different clubs and their contact information.

```python
import pandas as pd

# Math Club Roster for Spring 2024
df_math_club_spring24 = pd.DataFrame({
 'student_id': [101, 102, 103],
 'student_name_math': ['Alice Wonderland', 'Bob The Builder', 'Charlie Chaplin'],
 'activity_math_club': ['Calculus Challenge', 'Geometry Gems', 'Statistics Stars']
})

# Science Club Roster for Spring 2024
df_science_club_spring24 = pd.DataFrame({
 'student_id': [102, 103, 104],
 'student_name_science': ['Bob The Builder', 'Charlie Chaplin', 'Diana Prince'],
 'project_science_club': ['Volcano Model', 'Robotics Arm', 'Plant Growth Study']
})

# Student Email Addresses
df_student_emails = pd.DataFrame({
 'student_id': [101, 102, 103, 105],
 'email_address': ['alice.w@example.com', 'bob.b@example.com', 'charlie.c@example.com', 'eva.e@example.com']
})

# Test Rosters with student_id as index
df_roster1 = pd.DataFrame({'score_test1': [85, 92, 78]}, index=pd.Index([201, 202, 203], name='student_id'))
df_roster2 = pd.DataFrame({'score_test2': [88, 75, 95]}, index=pd.Index([202, 203, 204], name='student_id')) 
```

**Tasks:**

1. **Task 1: Comprehensive Club Roster**
 * Combine `df_math_club_spring24` and `df_science_club_spring24` to create a single list of all student activities.
 ```python
 #Expected Output Example for Task 1 (conceptual)
 # student_id student_name_math activity_math_club student_name_science project_science_club
 #0 101 Alice Wonderland Calculus Challenge NaN NaN
 #1 102 Bob The Builder Geometry Gems NaN NaN
 #2 103 Charlie Chaplin Statistics Stars NaN NaN
 #3 102 NaN NaN Bob The Builder Volcano Model
 #4 103 NaN NaN Charlie Chaplin Robotics Arm
 #5 104 NaN NaN Diana Prince Plant Growth Study
 ```

2. **Task 2: Roster with Only Common Columns**
 * Concatenate `df_math_club_spring24` and `df_science_club_spring24` only keep columns that are common to both DataFrames
 * **Expected Output Snapshot:** A DataFrame with 6 rows and 1 column (`student_id`)

 ```python
 #Expected Output Example for Task 2 (conceptual)
 # student_id
 #0 101
 #1 102
 #2 103
 #0 102 # Original index from df_science_club_spring24
 #1 103
 #2 104
 ```

3. **Task 3: Student Profiles**
 * First, set `student_id` as the index for `df_math_club_spring24` and `df_student_emails`.
 * Then, concatenate these two modified DataFrames horizontally to combine math club activities with email addresses.
 ```python
 #Expected Output Example for Task 3 (conceptual)
 # student_name_math activity_math_club email_address
 #student_id 
 #101 Alice Wonderland Calculus Challenge alice.w@example.com
 #102 Bob The Builder Geometry Gems bob.b@example.com
 #103 Charlie Chaplin Statistics Stars charlie.c@example.com
 #105 NaN NaN eva.e@example.com
 ```

4. **Task 4: Combining Test Rosters**
 * You are given `df_roster1` and `df_roster2`, which use `student_id` as their index. These rosters might contain scores for the same students from different tests.
 * Combine dataframes only if indexes are unique
 * If not so, drop duplicated indexes and try again

 ```python
 #Conceptual output after achieving the desired state:
 # student_id score_test1 score_test2
 #0 201 85.0 NaN
 #1 202 92.0 NaN
 #2 203 78.0 NaN
 #3 202 NaN 88.0
 #4 203 NaN 75.0
 #5 204 NaN 95.0
 ```

## 2. Merging DataFrames

Similar to SQL "joins"
Match 2 tables against some common column usually called "key"

![[Pasted image 20250511222520.png]]
### Basic Merges
```python
# Inner join - only keep rows with matching keys in both frames
df3 = pd.merge(df1, df2, on='student_id')

# Outer join - keep all rows from both frames
df3 = pd.merge(df1, df2, on='student_id', how='outer')

# Left join - keep all rows from left frame
df3 = pd.merge(df1, df2, on='student_id', how='left')

# Right join - keep all rows from right frame
df3 = pd.merge(df1, df2, on='student_id', how='right')
```

>[!Note]
>Pandas does also provide `df.join()` operation, similar to `pd.merge()`. Although we do only cover `merge()` since it is more general-applicable compared to `join()` and will meet all of your needs

### Cross Joins: Generating All Combinations

A **cross join** (or Cartesian product) creates a DataFrame that includes every possible combination of rows from two DataFrames. It's useful when you want to generate a complete set of pairings between two distinct sets of items, often as a starting point for further filtering or calculations.

For example, if you have a list of products and a list of available colors, a cross join can generate all possible product-color variations.

**When to use:**
- Generating all possible pairings (e.g., all shirt sizes with all available colors).
- Creating a base for scenarios where you need to evaluate or score every combination.
- As an initial step before filtering down to specific valid combinations based on more complex criteria (though often an outer join with conditions might be more direct for this).

**Mock DataFrames for Cross Join Example:**

```python
import pandas as pd

df_tshirt_styles = pd.DataFrame({
 'style_id': ['TS01', 'TS02'],
 'style_name': ['V-Neck', 'Crew Neck']
})

df_available_colors = pd.DataFrame({
 'color_code': ['RED', 'BLUE', 'GREEN'],
 'color_name': ['Red', 'Blue', 'Green']
})

df_all_tshirt_variations = pd.merge(df_tshirt_styles, df_available_colors, how='cross')
```

### Common problems

#### Different column names
```python
import pandas as pd

df_left = pd.DataFrame({'student_names': ['Alex', 'Victor'], 'math_grade': [100, 50]})
df_right = pd.DataFrame({'names': ['Alex', 'Victor'], 'history_grade': [56, 78]})
```
![[Pasted image 20250518132831.png|250]]
![[Pasted image 20250518132846.png|250]]
```python
pd.merge(df_left, df_right, left_on='student_names', right_on='names', how='inner')
```
![[Pasted image 20250518132813.png|500]]

#### Duplicated columns
If DataFrames share non-key column names, `suffixes` helps distinguish them.
```python
# Student contact details from two different school systems
df_system_A_contacts = pd.DataFrame({
 'student_id': [101, 102, 103],
 'email_address': ['alice@schoolA.com', 'bob@schoolA.com', 'charlie@schoolA.com'],
 'emergency_contact_name': ['Ms. Smith', 'Mr. Johnson', 'Ms. Brown']
})

df_system_B_contacts = pd.DataFrame({
 'student_id': [101, 102, 104],
 'email_address': ['alice@schoolB.org', 'bob.j@schoolB.org', 'diana@schoolB.org'],
 'emergency_contact_name': ['Alice Smith Sr.', 'Robert Johnson', 'Diana Prince Sr.']
})
```

![[Pasted image 20250518134308.png|350]]
```python
pd.merge(df_system_A_contacts, df_system_B_contacts, on='student_id', how='outer', suffixes=['_systemA', '_systemB'])
```
![[Pasted image 20250518134326.png]]

#### Duplicated rows (1:M Merges)
When a key in one DataFrame matches multiple rows in another (e.g., one student, many enrolled courses)

```python
df_students = pd.DataFrame({
 'student_id': [201, 202, 203],
 'student_name': ['Eve', 'Frank', 'Grace']
})

df_enrollments = pd.DataFrame({
 'enrollment_id': ['E01', 'E02', 'E03', 'E04'],
 'student_id': [201, 201, 202, 204], # Student 201 is in two courses
 'course_code': ['MATH101', 'PHY202', 'CHEM101', 'HIST301']
})
```

![[Pasted image 20250518134533.png|270]]

```python
# One-to-many merge: student details will be duplicated for each course enrollment
pd.merge(df_students, df_enrollments, on='student_id', how='left')
```

![[Pasted image 20250518134550.png|400]]

>[!Warning]
>Unexpected duplication (due to hidden 1:M relationships) cause many problems which are hard to detect later!
>
>So always be cautious and double-check everything during merges
>
>And **Always use `validate()` parameter** to explicitly define what are you expecting from the merge

```python
# Example of a failing validation if expectation is '1:1'
pd.merge(df_students, df_enrollments, on='student_id', how='left', validate='1:1')

# MergeError here...
```

#### Exercises

**Task 0: Basics:**
```python
# Students basic info
students_info = pd.DataFrame({
 'student_id': [1, 2, 3, 4, 5],
 'name': ['John', 'Anna', 'Peter', 'Sarah', 'Mike'],
 'age': [20, 22, 21, 19, 23]
})

# Students grades
students_grades = pd.DataFrame({
 'student_id': [1, 2, 3, 6, 7],
 'math': [85, 92, 78, 90, 85],
 'physics': [90, 88, 75, 92, 80]
})

# Students attendance
students_attendance = pd.DataFrame({
 'student_id': [1, 2, 4, 5, 8],
 'days_present': [42, 45, 40, 38, 41],
 'days_total': [45, 45, 45, 45, 45]
})
```
Experiment with merges:
- Find students who have info in all three DataFrames
- Find only students presented in `students_info`
- Merge all DataFrames to preserve all the information

**Task 0.1: Basics**

```python
df_main_courses = pd.DataFrame({'main_course': ['Chicken', 'Beef', 'Tofu']})
df_side_dishes = pd.DataFrame({'side_dish': ['Rice', 'Salad', 'Fries']})
```

- **Task:** Generate a DataFrame showing all possible meal combinations by pairing each main course with each side dish.
- **Expected Output:** A DataFrame with 9 rows, showing all main course and side dish pairings.

**1. Task: Combining Student Names and Activities**

```python
import pandas as pd

df_student_roster = pd.DataFrame({
	'student_id_school': ['S001', 'S002', 'S003'],
	'student_full_name': ['Alice Wonderland', 'Bob The Builder', 'Charlie Chaplin']
})

df_extracurriculars = pd.DataFrame({
	'participant_ref_id': ['S002', 'S003', 'S004'],
	'activity_joined': ['Chess Club', 'Debate Team', 'Science Fair Volunteer']
})
```
* **Your Goal:** Create a DataFrame that lists the full names of students and the activities they are involved in. Only include students for whom you have both their name from the roster and an activity they joined

**2. Task: Consolidating Feedback**

```python
df_midterm_eval = pd.DataFrame({
	'student_id': ['S001', 'S002'],
	'course_code': ['MATH101', 'CS202'],
	'general_feedback': ['Progressing well', 'Shows good understanding']
})

df_final_eval = pd.DataFrame({
	'student_id': ['S001', 'S002'],
	'course_code': ['MATH101', 'CS202'],
	'general_feedback': ['Excellent final project!', 'Mastered the concepts.']
})
```
* **Your Goal:** Combine the midterm and final evaluations for students into a single DataFrame. It is crucial that the `general_feedback` from the midterm is clearly distinguishable from the `general_feedback` from the final evaluation.

**3. Task: Listing Faculty by Department** 

```python
df_university_departments = pd.DataFrame({
	'dept_code': ['DPT01', 'DPT02'],
	'department_official_name': ['Department of Applied Mathematics', 'Department of Computer Engineering']
})

df_department_faculty = pd.DataFrame({
	'faculty_employee_id': ['F1010', 'F1022', 'F1035', 'F1047'],
	'faculty_member_name': ['Dr. Elara Vance', 'Dr. Marcus Thorne', 'Dr. Lena Petrova', 'Dr. Samuel Green'],
	'assigned_dept_code': ['DPT01', 'DPT02', 'DPT01', 'DPT02']
})
```
* **Your Goal:** Produce a list showing each faculty member and their respective full department name. 
 * Consider the relationship: 
 * Can one department have multiple faculty members? 
 * Can one faculty member be in multiple departments (based on this data)? 
 * How can you perform the merge in a way that confirms your understanding of this relationship? 
 * What might go wrong if you assumed a different kind of relationship (e.g., one faculty member per department, one department per faculty member) and how could you check for that?

**4. Task: Advanced relationship modeling:**
```python
TODO BROKEN TASK CAN NOT SOLVE WITHOUT GROUPBY
# Authors
authors = pd.DataFrame({
 'author_id': [1, 2, 3, 4, 5],
 'author_name': ['John Smith', 'Emily Jones', 'David Brown', 'Sarah Wilson', 'Michael Taylor']
})

# Books
books = pd.DataFrame({
 'book_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
 'title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E', 'Book F', 'Book G', 'Book H', 'Book I', 'Book J'],
 'genre': ['Fiction', 'Science', 'Fiction', 'Biography', 'Science', 'History', 'Fiction', 'Science', 'Fiction', 'Science']
})

# Authorship (mapping authors to books, including co-authorship)
authorship = pd.DataFrame({
 'author_id': [1, 2, 2, 3, 4, 4, 5, 5, 1, 3, 2, 4, 2, 4],
 'book_id': [101, 101, 102, 103, 104, 105, 105, 106, 107, 107, 108, 109, 110, 110]
})

# Book sales
sales = pd.DataFrame({
 'book_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
 'copies_sold': [5000, 7500, 3000, 8000, 6000, 4500, 4000, 9000, 2500, 12000],
 'revenue': [50000, 90000, 30000, 120000, 72000, 54000, 48000, 110000, 25000, 150000]
})
```
Tasks:
- Create a complete book catalog with titles, authors, genres, and sales information
- Handle co-authorship by creating a proper relationship between authors and books
- Calculate each author's total sales and revenue
- Find the most successful author-genre combination
- Create a summary showing each author's books, sales, and revenue share (for co-authored books, split revenue proportionally)

**Key Questions:**

How does `pd.concat()` method works for vertical and horizontal concatenation?
?
- Vertical: append rows from one dataframe into another, creating new columns if needed
- Horizontal: use indexes to append columns from one dataframe into another
<!--SR:!2026-01-09,4,270-->

What are the "key columns" during the merge?
?
Columns which are used to align two tables together
<!--SR:!2026-01-09,4,270-->

How does the join types (inner, outer, etc..) work in general?
Describe the differences between
- inner,
- outer,
- left,
- right,
- cartesian
?
- In general: join types define which rows should we drop after the merge is done, based on key:
- Inner: keep only rows with keys presented in both tables
- Outer: keep all rows
- Left: keep only rows from the left table
- Right: keep only rows from the right table
- Cartezian: pair every row from the left table with every row from the right table
<!--SR:!2026-01-09,4,270-->

How do you handle duplicate columns when merging DataFrames?
?
By using `pd.merge(..., suffixes)` parameter
<!--SR:!2026-01-06,1,230-->

How do you handle different column names when merging DataFrames?
?
By using `pd.merge(..., left_on, right_on)` parameters
<!--SR:!2026-01-06,1,230-->

Why are merge operations "risky"? What safety parameter should you ALWAYS include in merge operations and why?
?
- Risky, because the resulting table often contains duplicates
- `pd.merge(..., validate = '1:1'/'1:m'/'m:1'/'m:m') parameter
- This parameter will raise errors if unexpected behaviour occurs
<!--SR:!2026-01-09,4,270-->

Why would you use a cartezian product?
?
It's helpful when you need to create a whole set of entry combinations
from the first and the second tables
<!--SR:!2026-01-09,4,270-->

