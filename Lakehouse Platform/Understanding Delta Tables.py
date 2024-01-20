# Databricks notebook source
# MAGIC %md
# MAGIC ### Creating Delta Lake Tables

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE employees
# MAGIC (
# MAGIC     id INT, 
# MAGIC     name STRING, 
# MAGIC     salary DOUBLE
# MAGIC );

# COMMAND ----------

# MAGIC  %md
# MAGIC ### Inserting Data

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employees
# MAGIC VALUES 
# MAGIC   (1, "Adam", 3500.0),
# MAGIC   (2, "Sarah", 4020.5),
# MAGIC   (3, "John", 2999.3),
# MAGIC   (4, "Thomas", 4000.3),
# MAGIC   (5, "Anna", 2500.0),
# MAGIC   (6, "Kim", 6200.3);
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Retrieve Records

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Fetch Metadata Info for a Table

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail employees

# COMMAND ----------

# MAGIC %md
# MAGIC ### Check the hive data file

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "dbfs:/user/hive/warehouse/employees"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Update Command

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE employees
# MAGIC SET salary = salary + 100
# MAGIC WHERE 
# MAGIC   name LIKE 'A%';

# COMMAND ----------

# MAGIC %md
# MAGIC ### Check the history of a table (transaction log)

# COMMAND ----------

# MAGIC %sql 
# MAGIC describe history employees

# COMMAND ----------

# MAGIC %md
# MAGIC ### Check the transaction log

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "dbfs:/user/hive/warehouse/employees/_delta_log"

# COMMAND ----------

# MAGIC %fs 
# MAGIC head 'dbfs:/user/hive/warehouse/employees/_delta_log/00000000000000000003.json'
