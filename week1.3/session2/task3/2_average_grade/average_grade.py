# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]
with open("week1.3/session2/task3/2_average_grade/student_data.csv", "r") as infile:
    # Read all lines from the file into a list called data
    data = infile.readlines()

# 2. Open the new report file in 'w' (write) mode to create a fresh report each time
with open("week1.3/session2/task3/2_average_grade/report.txt", "w") as outfile:
    
    # 3. Loop through the list, skipping the header row using data[1:]
    for line in data[1:]:
        
        # Strip invisible characters and split the CSV row by commas
        columns = line.strip().split(',')
        
        # 4. Extract data based on columns: ID (0), Name (1), Maths (2), Science (3), History (4)
        name = columns[1]
        # Convert the grade strings to int() for the math
        maths = int(columns[2])
        science = int(columns[3])
        history = int(columns[4])
        
        # 5. Calculate the average
        average = (maths + science + history) / 3
        
        # 6. Write the name and average to the report file, formatted to 2 decimal places with :.2f
        outfile.write(f"{name} - Average: {average:.2f}\n")
    

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
