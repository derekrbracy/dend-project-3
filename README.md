_[Udacity's Data Engineer Nano Degree](https://eu.udacity.com/course/data-engineer-nanodegree--nd027)_ | derekrbracy@gmail.com | 2020-10-11

# Project 3: Data Modeling with Cassandra
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They would like a data engineer to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Project Overview
In this project, I applied what I learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, I loaded data from S3 to staging tables on Redshift and executed SQL statements that created the analytics tables from the staging tables.