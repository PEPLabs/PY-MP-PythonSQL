# PY-MP-PythonSQL

## Background 

A database connection is an integral part of any modern API. Many required functionalities of modern backend application aren't possible to implement without durable long term data storage. Remember the acronym "CRUD". A baseline API will typically be able to Create, Read, Update, and Delete data. In this mini project, we'll explore how to use python to create a connection to a database, create a database table, and insert/read the data in the database. 

The primary technologies you will leverage in this project are Python and SQL. The project will be written in Python.

## Database Tables 

The following table will be initialized in your project's create_dogs_table() function.

### dogs
```

```

# Technical Requirements

### SQLite

- The app will already be a Python project with SQLite tables created at runtime. 
- You will be responsible for cleaning and inserting data into the database, as well as selecting and modifying that data for analysis.  



# User Stories


### Load user data into users table
- Load the users.csv file found in /resources into the users table
- Clean the data before insertion. In this project, you just have to leave out any records with missing values or too many values.

### Load call data into callLogs table
- Load the callLogs.csv file found in /resources into the callLogs table 
- Clean the data before insertion. In this project, you just have to leave out any records with missing values or too many values.

### Save user analytic data into userAnalytics.csv
- Save analytic data for users into a csv file. The file must be named userAnalytics.csv, and it must be in the /resources folder
- Records must include userId, avgDuration, numCalls. Example:
  ```
  userId,avgDuration,numCalls
  1,105.0,4
  ```
- HINT: This data will be selected from the callLogs table.
- HINT 2: Dictionaries will be very helpful for matching data with userIds. Consider one for average call duration and one for number of calls. 

### Save ordered call logs into orderedCallLogs.csv
- Save call logs into csv files, ordered by userId, then start time. The file must be named orderedCallLogs.csv
- HINT: This data will be selected from the callLogs table.
- HINT 2: You can make use of ORDER BY to greatly simplify your python logic
