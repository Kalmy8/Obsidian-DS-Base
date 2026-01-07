---
type: note
status: done
tags:
- tech/python
- tech/stack/pandas
sources:
- null
- '[[Pandas Basics Course]]'
authors:
- null
---
**Scenario 1: University Academic Performance Analysis**

**Mock DataFrames:**

```python
import pandas as pd
 
df_students_registry = pd.DataFrame({
	'student_id': ['S1001', 'S1002', 'S1003', 'S1004', 'S1005'],
	'student_name': ['Alice Wonderland', 'Robert "Bob" Builder', 'Charles Xavier', 'Diana Prince', 'Edward Scissorhands'],
	'program_major_code': ['CS', 'ENG', 'PSY', 'JRN', 'ART'],
	'enrollment_year': [2021, 2022, 2021, 2023, 2022]
})

df_program_details = pd.DataFrame({
	'major_code': ['CS', 'ENG', 'PSY', 'JRN', 'ART', 'BIO'],
	'department_name': ['Computer Science', 'Engineering', 'Psychology', 'Journalism', 'Fine Arts', 'Biology'],
	'faculty_head_name': ['Dr. Ada Lovelace', 'Dr. Nikola Tesla', 'Dr. Sigmund Freud', 'Dr. Lois Lane', 'Dr. Vincent Van Gogh', 'Dr. Charles Darwin']
})

df_course_grades_fall2023 = pd.DataFrame({
	'registration_id': ['F23-001', 'F23-002', 'F23-003', 'F23-004', 'F23-005', 'F23-006', 'F23-007'],
	'student_ref': ['S1001', 'S1002', 'S1001', 'S1003', 'S1004', 'S1002', 'S1005'],
	'course_subject_code': ['CS101', 'ENG202', 'MAT101', 'PSY201', 'JRN100', 'PHY101', 'ART101'],
	'grade_numeric_percent': [88, 92, 75, 95, 85, 78, 91],
	'grade_letter': ['B+', 'A', 'C', 'A+', 'B', 'C+', 'A-']
})

df_course_catalog = pd.DataFrame({
	'course_id': ['CS101', 'ENG202', 'MAT101', 'PSY201', 'JRN100', 'PHY101', 'ART101', 'BIO101'],
	'course_full_title': ['Intro to Programming', 'Thermodynamics', 'Calculus I', 'Social Psychology', 'Intro to Reporting', 'General Physics I', 'Drawing Fundamentals', 'Principles of Biology'],
	'credits_hours': [3, 4, 4, 3, 3, 4, 3, 4],
	'related_major_code': ['CS', 'ENG', 'CS', 'PSY', 'JRN', 'ENG', 'ART', 'BIO'] # Note: MAT101 related to CS, PHY101 to ENG for this example
})
```
**Tasks:**
 1. **Master Student Report:** Create a single DataFrame that combines student registry information with their full department name (from `df_program_details`). Then, merge this with their Fall 2023 course grades and full course titles. The final report should show `student_name`, `department_name`, `enrollment_year`, `course_full_title`, and `grade_numeric_percent` for all recorded grades.
 2. **High Achievers in CS:** From the master report (or by re-merging), filter to find all students majoring in 'Computer Science' who scored 90% or higher in any of their Fall 2023 courses. Display their `student_name`, `course_full_title`, and `grade_numeric_percent`.
 3. **Average Grade by Department:** Calculate the average `grade_numeric_percent` for each `department_name` in Fall 2023. Sort the results to show the department with the highest average grade first.
 4. **Reshape for Course Load Analysis:** Create a DataFrame where each row is a `student_name`, each column is a `course_full_title` taken in Fall 2023, and the values are their `grade_numeric_percent`. Use an appropriate reshaping method (`pivot_table`). Fill missing values (courses not taken by a student) with 0 or a suitable indicator.
 5. **Course Credits Analysis:** Merge the course catalog with program details to see which departments offer which courses. Then, using the `df_course_grades_fall2023`, calculate the total credit hours taken by each student in Fall 2023. List the student names and their total credit hours, sorted by total credit hours in descending order.

**Scenario 2: Online Bookstore Sales & Inventory**

**Mock DataFrames:**
```python
df_books_inventory = pd.DataFrame({
	'book_isbn13': ['978-0001', '978-0002', '978-0003', '978-0004', '978-0005'],
	'book_title_short': ['Pandas Basics', 'SQL Deep Dive', 'Python for AI', 'Data Viz Handbook', 'Machine Learning Intro'],
	'author_last_name': ['Penguin', 'Octopus', 'Anaconda', 'Plotly', 'Keras'],
	'genre_code': ['TECH', 'TECH', 'TECH', 'ART', 'TECH'],
	'publication_year': [2022, 2021, 2023, 2022, 2023],
	'stock_quantity_warehouse_A': [150, 200, 120, 80, 250],
	'stock_quantity_warehouse_B': [100, 50, 180, 120, 0],
	'unit_price_usd': [29.99, 39.99, 49.99, 24.99, 59.99]
})

df_genre_lookup = pd.DataFrame({
	'code': ['TECH', 'ART', 'SCI', 'HIST'],
	'genre_full_name': ['Technical & Programming', 'Art & Design', 'Science & Nature', 'History & Biography']
})

df_customer_orders = pd.DataFrame({
	'order_id': ['ORD001', 'ORD002', 'ORD003', 'ORD004', 'ORD005', 'ORD006'],
	'customer_id': ['CUST01', 'CUST02', 'CUST01', 'CUST03', 'CUST02', 'CUST01'],
	'book_isbn_ordered': ['978-0001', '978-0003', '978-0002', '978-0005', '978-0001', '978-0003'],
	'quantity_ordered': [1, 2, 1, 1, 3, 1],
	'order_date': pd.to_datetime(['2023-10-01', '2023-10-05', '2023-10-10', '2023-10-12', '2023-10-15', '2023-10-20'])
})

df_customer_details = pd.DataFrame({
	'cust_unique_id': ['CUST01', 'CUST02', 'CUST03', 'CUST04'],
	'customer_name': ['Jane Doe', 'John Smith', 'Emily White', 'Michael Brown'],
	'registration_date': pd.to_datetime(['2022-01-15', '2022-03-20', '2023-02-10', '2023-05-01']),
	'city_shipping': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})
```
**Tasks:**
 1. **Total Book Inventory:** Use `melt` to transform `df_books_inventory` so that warehouse stock quantities are in a long format (columns: `book_isbn13`, `warehouse_id`, `stock_quantity`). Then, calculate the total stock quantity for each book across all warehouses.
 2. **Detailed Order Report:** Create a report that combines customer orders with book details (title, price, full genre name) and customer details (name, city). Calculate the total price for each item in an order (quantity * unit price).
 3. **Top Selling Tech Books:** Filter the detailed order report for books in the 'Technical & Programming' genre. Then, find the top 3 best-selling tech books by total quantity ordered. Display the book title and total quantity.
 4. **Customer Spending:** Calculate the total amount spent by each customer. List customer names and their total spending, sorted from highest to lowest.
 5. **Sales by Genre and Month:** Create a pivot table showing total revenue (sum of item total prices) for each `genre_full_name` and for each month of ordering. Extract the month from `order_date` for this.

**Scenario 3: Employee Project Allocation & Performance**

**Mock DataFrames:**
```python

df_employees_hr = pd.DataFrame({
	'employee_id_hr': ['E101', 'E102', 'E103', 'E104', 'E105', 'E106'],
	'full_name': ['Ken Adams', 'Barbie Roberts', 'Skipper Roberts', 'Allan Sherwood', 'Midge Hadley', 'Ryan Gosling'],
	'department_code_hr': ['TECH', 'MKTG', 'MKTG', 'TECH', 'DSGN', 'TECH'],
	'hire_date': pd.to_datetime(['2020-01-15', '2019-06-01', '2021-03-10', '2020-01-20', '2022-07-01', '2023-01-01']),
	'salary_annual_k': [90, 120, 70, 95, 75, 150]
})

df_departments_info = pd.DataFrame({
	'dept_id': ['TECH', 'MKTG', 'DSGN', 'HR'],
	'department_name_full': ['Technology & Engineering', 'Marketing & Sales', 'Creative Design', 'Human Resources'],
	'department_manager_id': ['E106', 'E102', 'E105', 'E100'] # E100 might not be in df_employees_hr
})

df_project_assignments = pd.DataFrame({
	'assignment_id': range(1, 9),
	'project_tracking_code': ['P2023-01', 'P2023-01', 'P2023-02', 'P2023-03', 'P2023-02', 'P2023-01', 'P2023-03', 'P2023-04'],
	'employee_ref_id': ['E101', 'E104', 'E102', 'E103', 'E105', 'E106', 'E101', 'E106'],
	'hours_billed_monthly': [40, 60, 50, 30, 70, 80, 20, 90],
	'month_year_billing': ['Oct-2023', 'Oct-2023', 'Oct-2023', 'Nov-2023', 'Nov-2023', 'Nov-2023', 'Dec-2023', 'Dec-2023']
})

df_project_details_catalog = pd.DataFrame({
	'project_id': ['P2023-01', 'P2023-02', 'P2023-03', 'P2023-04'],
	'project_name_official': ['Alpha Initiative', 'Beta Launch', 'Gamma Prototype', 'Delta Platform'],
	'project_budget_usd': [50000, 75000, 30000, 120000],
	'client_name': ['Client X', 'Client Y', 'Client X', 'Client Z']
})
```
**Tasks:**
 1. **Full Employee-Project Report:** Create a comprehensive DataFrame that lists each employee's `full_name`, their `department_name_full`, the `project_name_official` they are assigned to, and their `hours_billed_monthly` for that project in that month. Handle the differently named ID columns carefully.
 2. **Tech Department Overtime:** Filter the report for employees in the 'Technology & Engineering' department who billed more than 70 hours in any single month on a project. Display their name, project name, and hours billed.
 3. **Total Hours per Project:** Calculate the total hours billed for each `project_name_official` across all employees and months. Sort the projects by total hours in descending order.
 4. **Department Workload Pivot:** Create a pivot table where the index is `department_name_full`, columns are `project_name_official`, and the values are the sum of `hours_billed_monthly`. This will show how many hours each department contributed to each project.
 5. **Salary vs. Project Involvement:** Merge employee HR data (including salary) with project assignments. For each employee, list their name, annual salary, and the number of distinct projects they were assigned to. Identify employees with a salary above 100K who are assigned to only one project. 

**Scenario 4: Multi-City Weather Data Aggregation**

**Mock DataFrames:**
```python

df_weather_stations_info = pd.DataFrame({
	'station_id_code': ['STN01', 'STN02', 'STN03', 'STN04'],
	'city_name_common': ['Springfield', 'Shelbyville', 'Capital City', 'Ogdenville'],
	'latitude': [39.78, 39.65, 38.52, 40.05],
	'longitude': [-89.65, -89.05, -77.03, -88.24]
})

# Weather readings in a WIDE format (one row per station per day, different metrics in columns)
df_daily_readings_wide = pd.DataFrame({
	'station_ref': ['STN01', 'STN02', 'STN01', 'STN03', 'STN02', 'STN04', 'STN03', 'STN01'],
	'reading_date_iso': pd.to_datetime(['2023-11-01', '2023-11-01', '2023-11-02', '2023-11-02', '2023-11-03', '2023-11-03', '2023-11-04', '2023-11-04']),
	'temperature_high_celsius': [15, 17, 14, 20, 18, 12, 22, 13],
	'temperature_low_celsius': [5, 7, 6, 10, 8, 4, 12, 5],
	'precipitation_mm_daily': [0, 5, 2, 0, 10, 1, 0, 3],
	'humidity_percent_avg': [60, 75, 65, 50, 80, 70, 55, 68]
})
 ```
**Tasks:**
 1. **Reshape to Long Format:** Use `melt` to transform `df_daily_readings_wide` into a long format. The identifier variables should be `station_ref` and `reading_date_iso`. The variable name column should capture the metric type (e.g., 'temperature_high_celsius'), and the value column should hold the reading.
 2. **Enrich with Station Details:** Merge the long-format weather readings with `df_weather_stations_info` to include `city_name_common`, `latitude`, and `longitude` for each reading.
 3. **Rainy Days Report:** Filter the enriched data to find all instances where `precipitation_mm_daily` was greater than 0. Display the `city_name_common`, `reading_date_iso`, and the amount of precipitation.
 4. **Average Temperatures by City:** Using the long-format data, calculate the average value for `temperature_high_celsius` and `temperature_low_celsius` for each `city_name_common`. (Hint: you might need to filter for these specific metrics before or after pivoting/grouping).
 5. **Hottest Day per City:** For each `city_name_common`, find the date with the highest `temperature_high_celsius`. Display the city, date, and the high temperature. Sort by city name.

**Scenario 5: Public Library User Activity**

**Mock DataFrames:**
```python

df_library_books_catalog = pd.DataFrame({
	'internal_book_id': ['BK001', 'BK002', 'BK003', 'BK004', 'BK005', 'BK006'],
	'title_primary': ['The Great Gatsby', 'Moby Dick', 'War and Peace', '1984', 'Pride and Prejudice', 'To Kill a Mockingbird'],
	'author_full_name': ['F. Scott Fitzgerald', 'Herman Melville', 'Leo Tolstoy', 'George Orwell', 'Jane Austen', 'Harper Lee'],
	'genre_main_category': ['Classic', 'Adventure', 'Historical', 'Dystopian', 'Romance', 'Classic'],
	'publication_year_original': [1925, 1851, 1869, 1949, 1813, 1960]
})

df_library_members_list = pd.DataFrame({
	'member_card_id': ['M01', 'M02', 'M03', 'M04', 'M05'],
	'member_name_registered': ['Reader One', 'Bookworm Two', 'Literary Three', 'Page Turner Four', 'Story Lover Five'],
	'membership_start_date': pd.to_datetime(['2020-01-01', '2021-06-15', '2019-11-30', '2022-03-10', '2020-08-01']),
	'member_city_zipcode': ['90210', '10001', '60606', '90210', '77001']
})

df_book_loans_records = pd.DataFrame({
	'loan_transaction_id': range(101, 109),
	'book_id_borrowed': ['BK001', 'BK003', 'BK001', 'BK004', 'BK005', 'BK002', 'BK001', 'BK006'],
	'member_id_borrower': ['M01', 'M02', 'M03', 'M01', 'M04', 'M02', 'M05', 'M03'],
	'date_loaned_out': pd.to_datetime(['2023-10-01', '2023-10-03', '2023-10-05', '2023-10-10', '2023-10-12', '2023-10-15', '2023-10-18', '2023-10-20']),
	'date_returned_actual': pd.to_datetime(['2023-10-15', '2023-10-17', '2023-10-19', '2023-10-24', '2023-10-26', '2023-10-30', None, None]) # Some books not yet returned
})
```
**Tasks:**
 1. **Loan Activity Report:** Create a detailed report by merging the three DataFrames. The report should include `member_name_registered`, `title_primary` of the book, `author_full_name`, `date_loaned_out`, and `date_returned_actual`.
 2. **Loan Duration:** For all returned books, calculate the duration of each loan in days. Add this as a new column `loan_duration_days` to the loan activity report. Filter out books that haven't been returned yet for this calculation.
 3. **Most Popular Genres:** Determine which `genre_main_category` is borrowed the most. List genres by the total number of times books from that genre have been loaned out, in descending order.
 4. **Active Borrowers in 90210:** Identify members from the `member_city_zipcode` '90210' who have borrowed at least one book. Display their names and the titles of the books they borrowed.
 5. **Books Loaned Over Time (Pivot):** Create a pivot table where the index is `member_name_registered`, columns are the `publication_year_original` of the books they borrowed, and the values are the count of books loaned. This will show if members prefer older or newer books.