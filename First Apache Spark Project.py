#!/usr/bin/env python
# coding: utf-8

# # Understanding SparkContext
# A SparkContext represents the entry point to Spark functionality. It's like a key to your car. PySpark automatically creates a SparkContext for you in the PySpark shell (so you don't have to create it by yourself) and is exposed via a variable sc.
# 
# In this simple exercise, you'll find out the attributes of the SparkContext in your PySpark shell which you'll be using for the rest of the course.
# 
# Instructions
# 100 XP
# Print the version of SparkContext in the PySpark shell.
# Print the Python version of SparkContext in the PySpark shell.
# What is the master of SparkContext in the PySpark shell?

# In[1]:


from pyspark import SparkContext
# !pip install findspark
# !pip install pyspark
import findspark
import pyspark
findspark.init('C:/Users/fahmida/Anaconda3/Lib/site-packages/pyspark')
sc = pyspark.SparkContext.getOrCreate()
# Print the version of SparkContext
print("The version of Spark Context in the PySpark shell is", sc.version)

# Print the Python version of SparkContext
print("The Python version of Spark Context in the PySpark shell is", sc.pythonVer)

# Print the master of SparkContext
print("The master of Spark Context in the PySpark shell is", sc.master)


# # Interactive Use of PySpark
# Spark comes with an interactive python shell in which PySpark is already installed in it. PySpark shell is useful for basic testing and debugging and it is quite powerful. The easiest way to demonstrate the power of PySpark’s shell is to start using it. In this example, you'll load a simple list containing numbers ranging from 1 to 100 in the PySpark shell.
# 
# The most important thing to understand here is that we are not creating any SparkContext object because PySpark automatically creates the SparkContext object named sc, by default in the PySpark shell.
# # 1. Create a python list named numb containing the numbers 1 to 100.
# # 2. Load the list into Spark using Spark Context's parallelize method and assign it to a variable spark_data.

# In[2]:


# Create a python list of numbers from 1 to 100  
numb = range(1, 101)

# Load the list into PySpark
spark_data = sc.parallelize(numb)


# # Loading data in PySpark shell
# In PySpark, we express our computation through operations on distributed collections that are automatically parallelized across the cluster. In the previous exercise, you have seen an example of loading a list as parallelized collections and in this exercise, you'll load the data from a local file in PySpark shell.
# 
# Remember you already have a SparkContext sc and file_path variable (which is the path to the README.md file) already available in your workspace.
# 
# # 3. Load a local text file README.md in PySpark shell.
# 
# SparkContext's textFile() method is quite powerful for creating distributed collections of unstructured data which you'll see in the next chapter.

# In[3]:


# Load a local file into PySpark shell
filepath='C:/Users/fahmida/Github/Big Data PySpark/README.md'
lines = sc.textFile(filepath)


# # Use of lambda() with map()
# The map() function in Python returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.). The general syntax of map() function is map(fun, iter). We can also use lambda functions with map(). The general syntax of map() function with lambda() is map(lambda <agument>:<expression>, iter). Refer to slide 5 of video 1.7 for general help of map() function with lambda().
# 
# In this exercise, you'll be using lambda function inside the map() built-in function to square all numbers in the list.
# 1. Print my_list which is available in your environment.
# 2. Square each item in my_list using map() and lambda().
# 3. Print the result of map function.

# In[4]:


# Print my_list in the console
my_list= range(1,10)
print("Input list is", my_list)

# Square all numbers in my_list
squared_list_lambda = list(map(lambda x: x**2, my_list))

# Print the result of the map function
print("The squared numbers are", squared_list_lambda)


# # Use of lambda() with filter()
# Another function that is used extensively in Python is the filter() function. The filter() function in Python takes in a function and a list as arguments. The general syntax of the filter() function is filter(function, list_of_input). Similar to the map(), filter() can be used with lambda() function. The general syntax of the filter() function with lambda() is filter(lambda <argument>:<expression>, list). Refer to slide 6 of video 1.7 for general help of the filter() function with lambda().
# 
# In this exercise, you'll be using lambda() function inside the filter() built-in function to find all the numbers divisible by 10 in the list.
# 
# 1. Print my_list2 which is available in your environment.
# 2. Filter the numbers divisible by 10 from my_list2 using filter() and lambda().
# 3. Print the numbers divisible by 10 from my_list2.

# In[5]:


# Print my_list2 in the console
my_list2=range(0,101,10)
print("Input list is:", my_list2)

# Filter numbers divisible by 10
filtered_list = list(filter(lambda x: (x%10 == 0), my_list2))

# Print the numbers divisible by 10
print("Numbers divisible by 10 are:",filtered_list)


# # RDDs from Parallelized collections
# Resilient Distributed Dataset (RDD) is the basic abstraction in Spark. It is an immutable distributed collection of objects. Since RDD is a fundamental and backbone data type in Spark, it is important that you understand how to create it. In this exercise, you'll create your first RDD in PySpark from a collection of words.
# 
# Remember you already have a SparkContext sc available in your workspace.
# 
# 1. Create an RDD named RDD from a list of words.
# 2. Confirm the object created is RDD.

# In[6]:


# Create an RDD from a list of words
RDD = sc.parallelize(["Spark", "is", "a", "framework", "for", "Big Data processing"])

# Print out the type of the created object
print("The type of RDD is", type(RDD))


# # RDDs from External Datasets
# PySpark can easily create RDDs from files that are stored in external storage devices such as HDFS (Hadoop Distributed File System), Amazon S3 buckets, etc. However, the most common method of creating RDD's is from files stored in your local file system. This method takes a file path and reads it as a collection of lines. In this exercise, you'll create an RDD from the file path (file_path) with the file name README.md which is already available in your workspace.
# 
# Remember you already have a SparkContext sc available in your workspace.
# 
# 1. Print the file_path in the PySpark shell.
# 2. Create an RDD named fileRDD from a file_path with the file name README.md.
# 3. Print the type of the fileRDD created.

# In[7]:


# Print the file_path
print("The file_path is", filepath)

# Create a fileRDD from file_path
fileRDD = sc.textFile(filepath)

# Check the type of fileRDD
print("The file type of fileRDD is", type(fileRDD))


# # Partitions in your data
# SparkContext's textFile() method takes an optional second argument called minPartitions for specifying the minimum number of partitions. In this exercise, you'll create an RDD named fileRDD_part with 5 partitions and then compare that with fileRDD that you created in the previous exercise. Refer to the "Understanding Partition" slide in video 2.1 to know the methods for creating and getting the number of partitions in an RDD.
# 
# Remember, you already have a SparkContext sc, file_path and fileRDD available in your workspace.
# 
# 1. Find the number of partitions that support fileRDD RDD.
# 2. Create an RDD named fileRDD_part from the file path but create 5 partitions.
# 3. Confirm the number of partitions in the new fileRDD_part RDD.
# 
# Modifying the number of partitions may result in faster performance due to parallelization.

# In[8]:


# Check the number of partitions in fileRDD
print("Number of partitions in fileRDD is", fileRDD.getNumPartitions())

# Create a fileRDD_part from file_path with 5 partitions
fileRDD_part = sc.textFile(filepath, minPartitions = 5)

# Check the number of partitions in fileRDD_part
print("Number of partitions in fileRDD_part is", fileRDD_part.getNumPartitions())


# # Map and Collect
# The main method by which you can manipulate data in PySpark is using map(). The map() transformation takes in a function and applies it to each element in the RDD. It can be used to do any number of things, from fetching the website associated with each URL in our collection to just squaring the numbers. In this simple exercise, you'll use map() transformation to cube each number of the numbRDD RDD that you created earlier. Next, you'll return all the elements to a variable and finally print the output.
# 
# 1. Create map() transformation that cubes all of the numbers in numbRDD.
# 2. Collect the results in a numbers_all variable.
# 3. Print the output from numbers_all variable.

# In[9]:


# Create a python list of numbers from 1 to 100  
numb = range(1,5)
# Load the list into PySpark
numbRDD = sc.parallelize(numb)
cubedRDD = numbRDD.map(lambda x: x**3)

# Collect the results
numbers_all = cubedRDD.collect()

# Print the numbers from numbers_all
for numb in numbers_all:
	print(numb)


# # Filter and Count
# The RDD transformation filter() returns a new RDD containing only the elements that satisfy a particular function. It is useful for filtering large datasets based on a keyword. For this exercise, you'll filter out lines containing keyword Spark from fileRDD RDD which consists of lines of text from the README.md file. Next, you'll count the total number of lines containing the keyword Spark and finally print the first 4 lines of the filtered RDD.
# 
# 1.Create filter() transformation to select the lines containing the keyword Spark.
# 
# 2.How many lines in fileRDD_filter contains the keyword Spark?
# 
# 3.Print the first four lines of the resulting RDD.

# In[10]:


# Filter the fileRDD to select lines with Spark keyword
# Create a fileRDD from file_path
fileRDD = sc.textFile(filepath, minPartitions =10 )

fileRDD_filter = fileRDD.filter(lambda line: 'a' in line)

# How many lines are there in fileRDD?
print("The total number of lines with the keyword Spark is", fileRDD_filter.count())

# Print the first four lines of fileRDD
for line in fileRDD_filter.take(4): 
    print(line)


# # ReduceBykey and Collect
# One of the most popular pair RDD transformations is reduceByKey() which operates on key, 
# value (k,v) pairs and merges the values for each key. In this exercise, you'll first create 
# a pair RDD from a list of tuples, then combine the values with the same key and finally print 
# out the result.
# 
# 1. Create a pair RDD named Rdd with tuples (1,2),(3,4),(3,6),(4,5).
# 2. Transform the Rdd with reduceByKey() into a pair RDD Rdd_Reduced by adding the values with the same key.
# 3. Collect the contents of pair RDD Rdd_Reduced and iterate to print the output.
# 

# In[11]:


# Create PairRDD Rdd with key value pairs
Rdd = sc.parallelize([(1,2),(3,4),(3,6),(4,5)])

# Apply reduceByKey() operation on Rdd
Rdd_Reduced = Rdd.reduceByKey(lambda x, y : x + y )

# Iterate over the result and print the output
for num in Rdd_Reduced.collect(): 
    print("Key {} has {} Counts".format(num[0], num[1]))


# # SortByKey and Collect
# Many times it is useful to sort the pair RDD based on the key (for example word count which you'll see later in the chapter). In this exercise, you'll sort the pair RDD Rdd_Reduced that you created in the previous exercise into descending order and print the final output.
# 
# 1. Sort the Rdd_Reduced RDD using the key in descending order.
# 2. Collect the contents and iterate to print the output.
# 

# In[12]:


# Sort the reduced RDD with the key by descending order
Rdd_Reduced_Sort = Rdd_Reduced.sortByKey(ascending=False)

# Iterate over the result and print the output
for num in Rdd_Reduced_Sort.collect():
  print("Key {} has {} Counts".format(num[0], num[1]))


# # CountingBykeys
# For many datasets, it is important to count the number of keys in a key/value dataset. For example, counting the number of countries where the product was sold or to show the most popular baby names. In this simple exercise, you'll use the Rdd pair RDD that you created earlier and count the number of unique keys in that pair RDD.
# 
# Remember, you already have a SparkContext sc and Rdd available in your workspace.
# 1. What is the type of total?
# 2. Iterate over the total and print the keys and their counts.

# In[13]:


# Transform the rdd with countByKey()
Rdd = sc.parallelize([(1,2),(3,4),(3,6),(4,5)])
total = Rdd.countByKey()
# What is the type of total?
print("The type of total is", type(total))

# Iterate over the total and print the output (total is dictionary)
for k, v in total.items(): 
  print("key", k, "has", v, "counts")


# # Create a base RDD and transform it
# The volume of unstructured data (log lines, images, binary files) in existence is growing dramatically, and PySpark is an excellent framework for analyzing this type of data through RDDs. In this 3 part exercise, you will write code that calculates the most common words from Complete Works of William Shakespeare.
# 
# Here are the brief steps for writing the word counting program:
# 
# Create a base RDD from Complete_Shakespeare.txt file.
# Use RDD transformation to create a long list of words from each element of the base RDD.
# Remove stop words from your data.
# Create pair RDD where each element is a pair tuple of ('w', 1)
# Group the elements of the pair RDD by key (word) and add up their values.
# Swap the keys (word) and values (counts) so that keys is count and value is the word.
# Finally, sort the RDD by descending order and print the 10 most frequent words and their frequencies.
# In this first exercise, you'll create a base RDD from Complete_Shakespeare.txt file and transform it to create a long list of words.
# 
# 1. Create an RDD called baseRDD that reads lines from file_path.
# 2. Transform the baseRDD into a long list of words and create a new splitRDD.
# 3. Count the total words in splitRDD.

# In[17]:


# Filter the fileRDD to select lines with Spark keyword
# Create a fileRDD from file_path
filepath='C:/Users/fahmida/Github/Big Data PySpark/Shakespeare/Complete_Shakespeare.txt'
baseRDD= sc.textFile(filepath)

# Split the lines of baseRDD into words
splitRDD = baseRDD.flatMap(lambda x: x.split())

# Count the total number of words
print("Total number of words in splitRDD:", splitRDD.count())


# # Remove stop words and reduce the dataset
# After splitting the lines in the file into a long list of words using flatMap() transformation, in the next step, you'll remove stop words from your data. Stop words are common words that are often uninteresting. For example "I", "the", "a" etc., are stop words. You can remove many obvious stop words with a list of your own. But for this exercise, you will just remove the stop words from a curated list stop_words provided to you in your environment.
# 
# After removing stop words, you'll next create a pair RDD where each element is a pair tuple (k, v) where k is the key and v is the value. In this example, pair RDD is composed of (w, 1) where w is for each word in the RDD and 1 is a number. Finally, you'll combine the values with the same key from the pair RDD using reduceByKey() operation
# 
# 
# 1. Convert the words in splitRDD in lower case and then remove stop words from stop_words.
# 2. Create a pair RDD tuple containing the word and the number 1 from each word element in splitRDD.
# 3. Get the count of the number of occurrences of each word (word frequency) in the pair RDD using reduceByKey()

# In[18]:


# Convert the words in lower case and remove stop words from stop_words
stopwords=['this','in','it', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 'should', 'now']

splitRDD_no_stop = splitRDD.filter(lambda x: x.lower() not in stop_words)

# Create a tuple of the word and 1 
splitRDD_no_stop_words = splitRDD_no_stop.map(lambda w: (w, 1))

# Count of the number of occurences of each word 
resultRDD = splitRDD_no_stop_words.reduceByKey(lambda x, y: x + y)


# # Print word frequencies
# After combining the values (counts) with the same key (word), you'll print the word frequencies using the take(N) action. You could have used the collect() action but as a best practice, it is not recommended as collect() returns all the elements from your RDD. You'll use take(N) instead, to return N elements from your RDD.
# 
# What if we want to return the top 10 words? For this first, you'll need to swap the key (word) and values (counts) so that keys is count and value is the word. After you swap the key and value in the tuple, you'll sort the pair RDD based on the key (count) and print the top 10 words in descending order.
# 
# 1. Print the first 10 words and their frequencies from the resultRDD.
# 2. Swap the keys and values in the resultRDD.
# 3. Sort the keys according to descending order.
# 5. Print the top 10 most frequent words and their frequencies.

# In[19]:


# Display the first 10 words and their frequencies
for word in resultRDD.take(10):
	print(word)

# Swap the keys and values
resultRDD_swap = resultRDD.map(lambda x: (x[1], x[0]))

# Sort the keys in descending order
resultRDD_swap_sort = resultRDD_swap.sortByKey(ascending=False)

# Show the top 10 most frequent words and their frequencies
for word in resultRDD_swap_sort.take(10):
	print("{} has {} counts". format(word[1], word[0]))


# # RDD to DataFrame
# Similar to RDDs, DataFrames are immutable and distributed data structures in Spark. Even though RDDs are a fundamental data structure in Spark, working with data in DataFrame is easier than RDD most of the time and so understanding of how to convert RDD to DataFrame is necessary.
# 
# In this exercise, you'll first make an RDD using the sample_list which contains the list of tuples ('Mona',20), ('Jennifer',34),('John',20), ('Jim',26) with each tuple contains the name of the person and their age. Next, you'll create a DataFrame using the RDD and the schema (which is the list of 'Name' and 'Age') and finally confirm the output as PySpark DataFrame.
# 
# Remember, you already have a SparkContext sc and SparkSession spark available in your workspace.
# 
# 1. Create a sample_list from tuples - ('Mona',20), ('Jennifer',34), ('John',20), ('Jim',26).
# 2. Create an RDD from the sample_list.
# 3. Create a PySpark DataFrame using the above RDD and schema.
# 4. Confirm the output as PySpark DataFrame.

# In[20]:


from pyspark import SQLContext
from pyspark.sql import Row
# Create a list of tuples
sample_list = [('Mona',20), ('Jennifer',34), ('John',20), ('Jim',26)]

# Create a RDD from the list
rdd = sc.parallelize(sample_list)

sqlContext = SQLContext(sc)
# Create a PySpark DataFrame
names_df = sqlContext.createDataFrame(rdd, schema=['Name', 'Age'])

# Check the type of names_df
print("The type of names_df is", type(names_df))


# # Loading CSV into DataFrame
# In the previous exercise, you have seen a method of creating DataFrame but generally, loading data from CSV file is the most common method of creating DataFrames. In this exercise, you'll create a PySpark DataFrame from a people.csv file that is already provided to you as a file_path and confirm the created object is a PySpark DataFrame.
# 
# Remember, you already have SparkSession spark and file_path variable (which is the path to the people.csv file) available in your workspace.
# 
# 1. Create a DataFrame from file_path variable which is the path to the people.csv file.
# 2. Confirm the output as PySpark DataFrame.
# 

# In[21]:


# Create an DataFrame from file_path
file_path='C:/Users/fahmida/Desktop/New Dataset/Final Data/From Image/Hexanol_3.csv'
people_df =sqlContext.read.csv(file_path, header=True, inferSchema=True)

# Check the type of people_df
print("The type of people_df is", type(people_df))


# # Inspecting data in PySpark DataFrame
# Inspecting data is very crucial before performing analysis such as plotting, modeling, training etc., In this simple exercise, you'll inspect the data in the people_df DataFrame that you have created in the previous exercise using basic DataFrame operators.
# 
# Remember, you already have SparkSession spark and people_df DataFrame available in your workspace.
# 
# 1. Print the first 10 observations in the people_df DataFrame.
# 2. Count the number of rows in the people_df DataFrame.
# 3. How many columns does people_df DataFrame have and what are their names?
# 

# In[22]:


# Print the first 10 observations 
people_df.show(10)

# Count the number of rows 
print("There are {} rows in the people_df DataFrame.".format(people_df.count()))

# Count the number of columns and their names 
print("There are {} columns in the people_df DataFrame and their names are {}".format(len(people_df.columns), people_df.columns))


# # PySpark DataFrame subsetting and cleaning
# After data inspection, it is often necessary to clean the data which mainly involves subsetting, renaming the columns, removing duplicated rows etc., PySpark DataFrame API provides several operators to do this. In this exercise, your job is to subset 'name', 'sex' and 'date of birth' columns from people_df DataFrame, remove any duplicate rows from that dataset and count the number of rows before and after duplicates removal step.
# 
# Remember, you already have SparkSession spark and people_df DataFrames available in your workspace.
# 
# 
# 1. Select 'name', 'sex' and 'date of birth' columns from people_df and create people_df_sub DataFrame.
# 2. Print the first 10 observations in the people_df DataFrame.
# 3. Remove duplicate entries from people_df_sub DataFrame and create people_df_sub_nodup DataFrame.
# 4. How many rows are there before and after duplicates are removed?
# 

# In[23]:


# Select name, sex and date of birth columns
people_df_sub = people_df.select( 'PulseDuration', 'EchoTime', 'Voltage')

# Print the first 10 observations from people_df_sub
people_df_sub.show(10)

# Remove duplicate entries from people_df_sub
people_df_sub_nodup = people_df_sub.dropDuplicates()

# Count the number of rows
print("There were {} rows before removing duplicates, and {} rows after removing duplicates".format(people_df_sub.count(), people_df_sub_nodup.count()))


# # Filtering your DataFrame
# In the previous exercise, you have subset the data using select() operator which is mainly used to subset the DataFrame column-wise. What if you want to subset the DataFrame based on a condition (for example, select all rows where the sex is Female). In this exercise, you will filter the rows in the people_df DataFrame in which 'sex' is female and male and create two different datasets. Finally, you'll count the number of rows in each of those datasets.
# 
# Remember, you already have SparkSession spark and people_df DataFrame available in your workspace.
# 
# 
# 1. Filter the people_df DataFrame to select all rows where sex is female into people_df_female DataFrame.
# 2. Filter the people_df DataFrame to select all rows where sex is male into people_df_male DataFrame.
# 3. Count the number of rows in people_df_female and people_df_male DataFrames.
# 

# In[24]:


# Filter people_df to select females 
people_df_female = people_df.filter(people_df.WaveformType == "Bipolar")

# Filter people_df to select males
people_df_male = people_df.filter(people_df.Printer == "Microfab")

# Count the number of rows 
print("There are {} rows in the people_df_female DataFrame and {} rows in the people_df_male DataFrame".format(people_df_female.count(), people_df_male.count()))


# # Running SQL Queries Programmatically
# DataFrames can easily be manipulated using SQL queries in PySpark. The sql() function on a SparkSession enables applications to run SQL queries programmatically and returns the result as another DataFrame. In this exercise, you'll create a temporary table of the people_df DataFrame that you created previously, then construct a query to select the names of the people from the temporary table and assign the result to a new DataFrame.
# 
# Remember, you already have SparkSession spark and people_df DataFrame available in your workspace.
# 
# 
# 1. Create a temporary table people that's a pointer to the people_df DataFrame.
# 2. Construct a query to select the names of the people from the temporary table people.
# 3. Assign the result of Spark's query to a new DataFrame - people_df_names.
# 4. Print the top 10 names of the people from people_df_names DataFrame.
# 
# 
# # Spark SQL operations generally return DataFrames. This means you can freely mix DataFrames and SQL.

# In[25]:


# Create a temporary table "people"
people_df_sub.createOrReplaceTempView("people")

# Construct a query to select the names of the people from the temporary table "people"
query = '''SELECT PulseDuration FROM people'''

# Assign the result of Spark's query to people_df_names
people_df_sub_names = sqlContext.sql(query)

# Print the top 10 names of the people
people_df_sub_names.show(10)


# # SQL queries for filtering Table
# In the previous exercise, you have run a simple SQL query on a DataFrame. There are more sophisticated queries you can construct to obtain the result that you want and use it for downstream analysis such as data visualization and Machine Learning. In this exercise, we will use the temporary table people that you created previously and filter out the rows where the "sex" is male and female and create two DataFrames.
# 
# Remember, you already have SparkSession spark and people temporary table available in your workspace.
# 
# 1. Filter the people table to select all rows where sex is female into people_female_df DataFrame.
# 2. Filter the people table to select all rows where sex is male into people_male_df DataFrame.
# 3. Count the number of rows in both people_female and people_male DataFrames.

# In[26]:


# Filter the people table to select female sex 
people_female_df = sqlContext.sql('SELECT * FROM people WHERE PulseDuration < 15')

# Filter the people table DataFrame to select male sex
people_male_df = sqlContext.sql('SELECT * FROM people WHERE EchoTime > 10 ')

# Count the number of rows in both people_df_female and people_male_df DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(people_female_df.count(), people_male_df.count()))


# # PySpark DataFrame visualization
# Graphical representations or visualization of data is imperative for understanding as well as interpreting the data. In this simple data visualization exercise, you'll first print the column names of names_df DataFrame that you created earlier, then convert the names_df to Pandas DataFrame and finally plot the contents as horizontal bar plot with names of the people on the x-axis and their age on the y-axis.
# 
# Remember, you already have SparkSession spark and names_df DataFrame available in your workspace.
# 
# 
# 1. Print the names of the columns in names_df DataFrame.
# 2. Convert names_df DataFrame to df_pandas Pandas DataFrame.
# 3. Use matplotlib's plot() method to create a horizontal bar plot with 'Name' on x-axis and 'Age' on y-axis.

# In[27]:


import matplotlib.pyplot as plt
# Check the column names of names_df
people_df_sub.createOrReplaceTempView("Plot")
# Construct a query to select the names of the people from the temporary table "people"
query = '''SELECT PulseDuration, EchoTime FROM plot'''

# Assign the result of Spark's query to people_df_names
new_df = sqlContext.sql(query)
new_df.show(10)
print("The column names of names_df are", new_df.columns)

# Convert to Pandas DataFrame  
df_pandas =new_df.toPandas()

# Create a horizontal bar plot
df_pandas.plot(kind='barh', x='PulseDuration', y='EchoTime', colormap='winter_r')
plt.show()


# # Part 1: Create a DataFrame from CSV file
# 
# Every 4 years, the soccer fans throughout the world celebrates a festival called “Fifa World Cup” and with that, everything seems to change in many countries. In this 3 part exercise, you'll be doing some exploratory data analysis (EDA) on the "FIFA 2018 World Cup Player" dataset using PySpark SQL which involve DataFrame operations, SQL queries and visualization.
# 
# In the first part, you'll load FIFA 2018 World Cup Players dataset (Fifa2018_dataset.csv) which is in CSV format into a PySpark's dataFrame and inspect the data using basic DataFrame operations.
# 
# Remember, you already have SparkSession spark and file_path variable (which is the path to the Fifa2018_dataset.csv file) available in your workspace.
# 
# 1. Create a PySpark DataFrame from file_path which is the path to the Fifa2018_dataset.csv file.
# 2. Print the schema of the DataFrame.
# 3. Print the first 10 observations.
# 4. How many rows are in there in the DataFrame?

# In[28]:


# Load the Dataframe 
from pyspark import SparkContext
# !pip install findspark
# !pip install pyspark
import findspark
import pyspark
from pyspark import SQLContext
file_path='C:/Users/fahmida/Github/Big Data PySpark/fifa-world-cup-2018-players/wc2018-players.csv'
findspark.init('C:/Users/fahmida/Anaconda3/Lib/site-packages/pyspark')
sc = pyspark.SparkContext.getOrCreate()
sqlContext = SQLContext(sc)
fifa_df = sqlContext.read.csv(file_path, header=True, inferSchema=True)
# Check the schema of columns 
fifa_df.printSchema()

# Show the first 10 observations
fifa_df.show(10)

# Print the total number of rows
print("There are {} rows in the fifa_df DataFrame".format(fifa_df.count()))


# # Part 2: SQL Queries on DataFrame
# The fifa_df DataFrame that we created has additional information about datatypes and names of columns associated with it. This additional information allows PySpark SQL to run SQL queries on DataFrame. SQL queries are concise and easy to run compared to DataFrame operations. But in order to apply SQL queries on DataFrame first, you need to create a temporary view of DataFrame as a table and then apply SQL queries on the created table (Running SQL Queries Programmatically).
# 
# In the second part, you'll create a temporary table of fifa_df DataFrame and run SQL queries to extract the 'Age' column of players from Germany.
# 
# You already have a SparkContext spark and fifa_df available in your workspace.
# 
# 1. Create temporary table fifa_df from fifa_df_table DataFrame.
# 2. Construct a "query" to extract the "Age" column from Germany players.
# 3. Apply the SQL "query" to the temporary view table and create a new DataFrame.
# 4. Computes basic statistics of the created DataFrame.

# In[34]:


# Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

# Construct the "query"
query = '''SELECT Age FROM fifa_df_table WHERE Nationality == "Germany"'''

# Apply the SQL "query"
fifa_df_germany_age = sqlContext.sql(query)

# Generate basic statistics
fifa_df_germany_age.describe().show()


# # Part 3: Data visualization
# Data visualization is important for exploratory data analysis (EDA). PySpark DataFrame is a perfect for data visualization compared to RDDs because of its inherent structure and schema.
# 
# In this third part, you'll create a histogram of the ages of all the players from Germany from the DataFrame that you created in the previous exercise. For this, you'll first convert the PySpark DataFrame into Pandas DataFrame and use matplotlib's plot() function to create a density plot of ages of all players from Germany.
# 
# Remember, you already have SparkSession spark, fifa_df_table temporary table and fifa_df_germany_age DataFrame available in your workspace.
# 
# 1. Convert fifa_df_germany_age to fifa_df_germany_age_pandas Pandas DataFrame.
# 2. Generate a density plot of the 'Age' column from the fifa_df_germany_age_pandas Pandas DataFrame.

# In[35]:


# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()


# # PySpark MLlib algorithms
# Before using any Machine learning algorithms in PySpark shell, you'll have to import the submodules of pyspark.mllib library and then choose the appropriate class that is needed for a specific machine learning task.
# 
# In this simple exercise, you'll learn how to import the different submodules of pyspark.mllib along with the classes that are needed for performing Collaborative filtering, Classification and Clustering algorithms.
# 
# 
# 1. Import pyspark.mllib recommendation submodule and Alternating Least Squares class.
# 2. Import pyspark.mllib classification submodule and Logistic Regression with LBFGS class.
# 3. Import pyspark.mllib clustering submodule and kmeans class.

# In[36]:


# Import the library for ALS
from pyspark.mllib.recommendation import ALS

# Import the library for Logistic Regression
from pyspark.mllib.classification import LogisticRegressionWithLBFGS

# Import the library for Kmeans
from pyspark.mllib.clustering import KMeans


# # Loading Movie Lens dataset into RDDs
# Collaborative filtering is a technique for recommender systems wherein users' ratings and interactions with various products are used to recommend new ones. With the advent of Machine Learning and parallelized processing of data, Recommender systems have become widely popular in recent years, and are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags. In this 3-part exercise, your goal is to develop a simple movie recommendation system using PySpark MLlib using a subset of MovieLens 100k dataset.
# 
# In the first part, you'll first load the MovieLens data (ratings.csv) into RDD and from each line in the RDD which is formatted as userId,movieId,rating,timestamp, you'll need to map the MovieLens data to a Ratings object (userID, productID, rating) after removing timestamp column and finally you'll split the RDD into training and test RDDs.
# 
# Remember, you have a SparkContext sc available in your workspace. Also file_path variable (which is the path to the ratings.csv file), and ALS class are already available in your workspace.
# 
# 1. Load the ratings.csv dataset into an RDD.
# 2. Split the RDD using , as a delimiter.
# 3. For each line of the RDD, using Rating() class create a tuple of userID, productID, rating.
# 4. Randomly split the data into training data and test data (0.8 and 0.2).

# In[37]:


# Load the Dataframe 
from pyspark.mllib.recommendation import ALS, Rating
from pyspark import SparkContext
import findspark
import pyspark
from pyspark import SQLContext
file_path='C:/Users/fahmida/Github/Big Data PySpark/Movie Lens Dataset/ratings.csv'
findspark.init('C:/Users/fahmida/Anaconda3/Lib/site-packages/pyspark')
sc = pyspark.SparkContext.getOrCreate()
# Load the data into RDD
data = sc.textFile(file_path)
#sqlContext = SQLContext(sc)
#data  =sqlContext.read.csv(file_path, header=True, inferSchema=True)
#ratings_final=data 
# Split the RDD 
ratings = data.map(lambda l: l.split(','))
# Transform the ratings RDD
ratings_final = ratings.map(lambda line: Rating(float(line[0]), float(line[1]), float(line[2])))
# Split the data into training and test
training_data, test_data = ratings_final.randomSplit([0.8, 0.2])


# # Model training and predictions
# After splitting the data into training and test data, in the second part of the exercise, you'll train the ALS algorithm using the training data. PySpark MLlib's ALS algorithm has the following mandatory parameters - rank (the number of latent factors in the model) and iterations (number of iterations to run). After training the ALS model, you can use the model to predict the ratings from the test data. For this, you will provide the user and item columns from the test dataset and finally print the first 2 rows of predictAll() output.
# 
# Remember, you have SparkContext sc, training_data and test_data are already available in your workspace.
# 1. Train ALS algorithm with training data and configured parameters (rank = 10 and iterations = 10).
# 2. Drop the rating column in the test data.
# 3. Test the model by predicting the rating from the test data.
# 4. Print the first two rows of the predicted ratings.

# In[38]:


######First run the Java
from pyspark.mllib.recommendation import ALS
# Create the ALS model on the training data
model = ALS.train(training_data, rank=10, iterations=10)

# Drop the ratings column 
testdata_no_rating = test_data.map(lambda p: (p[0], p[1]))

# Predict the model  
predictions = model.predictAll(testdata_no_rating)

# Print the first rows of the RDD
predictions.take(2)


# In[ ]:


# from py4j.java_gateway import JavaGateway

# def main():

#     print("Hello")
#     gateway = JavaGateway()                   # connect to the JVM
#     random = gateway.jvm.java.util.Random()   # create a java.util.Random instance
#     number1 = random.nextInt(10)              # call the Random.nextInt method
#     number2 = random.nextInt(10)
#     print(number1,number2)

# if __name__ == '__main__':
#     main()


# # Model evaluation using MSE
# After generating the predicted ratings from the test data using ALS model, in this final part of the exercise, you'll prepare the data for calculating Mean Square Error (MSE) of the model. The MSE is the average value of (original rating – predicted rating)^2 for all users and indicates the absolute fit of the model to the data. To do this, first, you'll organize both the ratings and prediction RDDs to make a tuple of ((user, product), rating)), then join the ratings RDD with prediction RDD and finally apply a squared difference function along with mean() to get the MSE.
# 
# Remember, you have a SparkContext sc available in your workspace. Also, ratings_final and predictions RDD are already available in your workspace.
# 
# 1. Organize ratings RDD to make ((user, product), rating).
# 2. Organize predictions RDD to make ((user, product), rating).
# 3. Join the prediction RDD with the ratings RDD.
# 4. Evaluate the model using MSE between original rating and predicted rating and print it.

# In[39]:


# Prepare ratings data
rates = ratings_final.map(lambda r: ((r[0], r[1]), r[2]))

# Prepare predictions data
preds = predictions.map(lambda r: ((r[0], r[1]), r[2]))

# Join the ratings data with predictions data
rates_and_preds = rates.join(preds)

# Calculate and print MSE
MSE = rates_and_preds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error of the model for the test data = {:.2f}".format(MSE))


# # Loading spam and non-spam data
# Logistic Regression is a popular method to predict a categorical response. Probably one of the most common applications of the logistic regression is the message or email spam classification. In this 3-part exercise, you'll create an email spam classifier with logistic regression using Spark MLlib. Here are the brief steps for creating a spam classifier.
# 
# Create an RDD of strings representing email.
# Run MLlib’s feature extraction algorithms to convert text into an RDD of vectors.
# Call a classification algorithm on the RDD of vectors to return a model object to classify new points.
# Evaluate the model on a test dataset using one of MLlib’s evaluation functions.
# In the first part of the exercise, you'll load the 'spam' and 'ham' (non-spam) files into RDDs, split the emails into individual words and look at the first element in each of the RDD.
# 
# Remember, you have a SparkContext sc available in your workspace. 
# Also file_path_spam variable (which is the path to the 'spam' file) and
# file_path_non_spam (which is the path to the 'non-spam' file) is already available in your workspace.
# 1. Create two RDDS, one for 'spam' and one for 'non-spam (ham)'.
# 2. Split each email in 'spam' and 'non-spam' RDDs into words.
# 3. Print the first element in the split RDD of both 'spam' and 'non-spam'.
# 

# In[6]:


# Load the datasets into RDDs
file_path_spam=file_path='C:/Users/fahmida/Github/Big Data PySpark/Email/email.spam.txt'
file_path_non_spam=file_path='C:/Users/fahmida/Github/Big Data PySpark/Email/emails.notspam.txt'

#sc = SparkContext("local", "first app")
#spark = SparkSession(sc)
spam_rdd = sc.textFile(file_path_spam)
non_spam_rdd = sc.textFile(file_path_non_spam)

# Split the email messages into words
spam_words = spam_rdd.flatMap(lambda email: email.split(' '))
non_spam_words = non_spam_rdd.flatMap(lambda email: email.split(' '))

# Print the first element in the split RDD
print("The first element in spam_words is", spam_words.take(4))
print("The first element in non_spam_words is", non_spam_words.take(4))


# # Feature hashing and LabelPoint
# After splitting the emails into words, our raw data set of 'spam' and 'non-spam' is currently composed of 1-line messages consisting of spam and non-spam messages. In order to classify these messages, we need to convert text into features.
# 
# In the second part of the exercise, you'll first create a HashingTF() instance to map text to vectors of 200 features, then for each message in 'spam' and 'non-spam' files you'll split them into words, and each word is mapped to one feature. These are the features that will be used to decide whether a message is 'spam' or 'non-spam'. Next, you'll create labels for features. For a valid message, the label will be 0 (i.e. the message is not spam) and for a 'spam' message, the label will be 1 (i.e. the message is spam). Finally, you'll combine both the labeled datasets.
# 
# Remember, you have a SparkContext sc available in your workspace. Also spam_words and non_spam_words variables are already available in your workspace.
# 
# 
# 1. Create a HashingTF() instance to map email text to vectors of 200 features.
# 2. Each message in 'spam' and 'non-spam' datasets are split into words, and each word is mapped to one feature.
# 3. Label the features: 1 for spam, 0 for non-spam.
# 4. Combine both the spam and non-spam samples into a single dataset.

# In[7]:


from pyspark.ml.feature import *
from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
from pyspark.ml.feature import StopWordsRemover
from pyspark.ml.clustering import LDA
# Create a HashingTf instance with 200 features
tf = HashingTF(numFeatures=100)

# Map each word to one feature
spam_features = tf.transform(spam_words)
non_spam_features = tf.transform(non_spam_words)

# Label the features: 1 for spam, 0 for non-spam
spam_samples = spam_features.map(lambda features:LabeledPoint(1, features))
non_spam_samples = non_spam_features.map(lambda features:LabeledPoint(0, features))

# Combine the two datasets
samples = spam_samples.union(non_spam_samples)


# # Logistic Regression model training
# After creating labels and features for the data, we’re ready to build a model that can learn from it (training). But before you train the model, you'll split the combined dataset into training and testing dataset because it can assign a probability of being spam to each data point. We can then decide to classify messages as spam or not, depending on how high the probability.
# 
# In this final part of the exercise, you'll split the data into training and test, run Logistic Regression on the training data, apply the same HashingTF() feature transformation to get vectors on a positive example (spam) and a negative one (non-spam) and finally check the accuracy of the model trained.
# 
# Remember, you have a SparkContext sc available in your workspace, as well as the samples variable.
# 
# 
# 1. Split the combined data into training and test sets (80/20).
# 2. Train the Logistic Regression (LBFGS variant) model with the training dataset.
# 3. Create a prediction label from the trained model on the test dataset.
# 4. Combine the labels in the test dataset with the labels in the prediction dataset.
# 5. Calculate the accuracy of the trained model using original and predicted labels on the labels_and_preds

# In[9]:


# Split the data into training and testing
train_samples,test_samples = samples.randomSplit([0.8, 0.2])

# Train the model
model = LogisticRegressionWithLBFGS.train(train_samples)

# Create a prediction label from the test data
predictions = model.predict(test_samples.map(lambda x: x.features))

# Combine original labels with the predicted labels
labels_and_preds = test_samples.map(lambda x: x.label).zip(predictions)

# Check the accuracy of the model on the test data
accuracy = labels_and_preds.filter(lambda x: x[0] == x[1]).count() / float(test_samples.count())
print("Model accuracy : {:.2f}".format(accuracy))


# # Loading and parsing the 5000 points data
# Clustering is the unsupervised learning task that involves grouping objects into clusters of high similarity. Unlike the supervised tasks, where data is labeled, clustering can be used to make sense of unlabeled data. PySpark MLlib includes the popular K-means algorithm for clustering. In this 3 part exercise, you'll find out how many clusters are there in a dataset containing 5000 rows and 2 columns. For this you'll first load the data into an RDD, parse the RDD based on the delimiter, run the KMeans model, evaluate the model and finally visualize the clusters.
# 
# In the first part, you'll load the data into RDD, parse the RDD based on the delimiter and convert the string type of the data to an integer.
# 
# Remember, you have a SparkContext sc available in your workspace. Also file_path variable (which is the path to the 5000_points.txt file) is already available in your workspace.
# 
# 1. Load the 5000_points dataset into a RDD named clusterRDD.
# 2. Transform the clusterRDD by splitting the lines based on the tab ("\t").
# 3. Transform the split RDD to create a list of integers for the two columns.
# 4. Confirm that there are 5000 rows in the dataset.

# In[10]:


# Load the dataset into a RDD
file_path='C:/Users/fahmida/Github/Big Data PySpark/clustering/5000points.txt'
clusterRDD = sc.textFile(file_path)

# Split the RDD based on tab
rdd_split = clusterRDD.map(lambda x: x.split("\t"))

# Transform the split RDD by creating a list of integers
rdd_split_int = rdd_split.map(lambda x: [int(x[0]), int(x[1])])

# Count the number of rows in RDD 
print("There are {} rows in the rdd_split_int dataset".format(rdd_split_int.count()))


# # K-means training
# Now that the RDD is ready for training, in the second part of the exercise, you'll train the RDD with PySpark's MLlib's KMeans algorithm. The algorithm is somewhat naive--it clusters the data into k clusters, even if k is not the right number of clusters to use. Therefore, when using k-means clustering, the most important parameter is a target number of clusters to generate, k. In practice, you rarely know the “true” number of clusters in advance, so the best practice is to try several values of k until the average intracluster distance stops decreasing dramatically
# 
# In this 2nd part, you'll test with k's ranging from 13 to 16 and use the elbow method to chose the correct k. The idea of the elbow method is to run k-means clustering on the dataset for a range of values of k, calculate Within Set Sum of Squared Error (WSSSE, this function is already provided to you) and select the best k based on the sudden drop in WSSSE. Finally, you'll retrain the model with the best k (15 in this case) and print the centroids (cluster centers).
# 
# Remember, you already have a SparkContext sc and rdd_split_int RDD available in your workspace.
# 
# 1. Train the KMeans model with clusters from 13 to 16 and print the WSSSE for each cluster.
# 2. Train the KMeans model again with the best cluster (k=15).
# 3. Get the Cluster Centers (centroids) of KMeans model trained with k=15.

# In[12]:


# Train the model with clusters from 13 to 16 and compute WSSSE 
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

for clst in range(13, 17):
    model = KMeans.train(rdd_split_int, clst, seed=1)
    WSSSE = rdd_split_int.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("The cluster {} has Within Set Sum of Squared Error {}".format(clst, WSSSE))

# Train the model again with the best k 
model = KMeans.train(rdd_split_int, k=15, seed=1)

# Get cluster centers
cluster_centers = model.clusterCenters


# # Visualizing clusters
# After KMeans model training with an optimum K value (K = 15), in this final part of the exercise, you will visualize the clusters and their cluster centers (centroids) and see if they overlap with each other. For this, you'll first convert rdd_split_int RDD into spark DataFrame and then into Pandas DataFrame for plotting. Similarly, you'll convert cluster_centers into Pandas DataFrame. Once the DataFrames are created, you'll use matplotlib library to create scatter plots.
# 
# Remember, you already have a SparkContext sc, rdd_split_int and cluster_centers variables available in your workspace.
# 
# 
# 1. Convert rdd_split_int RDD into a Spark DataFrame.
# 2. Convert Spark DataFrame into a Pandas DataFrame.
# 3. Create a Pandas DataFrame from cluster_centers list.
# 4. Create a scatter plot of the raw data and an overlaid scatter plot with centroids for k = 15.

# In[13]:


# Convert rdd_split_int RDD into Spark DataFrame
import pandas as pd
sqlContext = SQLContext(sc)
#data  =sqlContext.read.csv(file_path, header=True, inferSchema=True)
#ratings_final=data 
# Split the RDD 
rdd_split_int_df = sqlContext.createDataFrame(rdd_split_int, schema=["col1", "col2"])

# Convert Spark DataFrame into Pandas DataFrame
rdd_split_int_df_pandas = rdd_split_int_df.toPandas()

# Convert "cluster_centers" that you generated earlier into Pandas DataFrame
cluster_centers_pandas = pd.DataFrame(cluster_centers, columns=["col1", "col2"])

# Create an overlaid scatter plot
plt.scatter(rdd_split_int_df_pandas["col1"], rdd_split_int_df_pandas["col2"])
plt.scatter(cluster_centers_pandas["col1"], cluster_centers_pandas["col2"], color="red", marker="x")
plt.show()


# In[ ]:




