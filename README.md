_[Udacity's Data Engineer Nano Degree](https://eu.udacity.com/course/data-engineer-nanodegree--nd027)_ | derekrbracy@gmail.com | 2020-11-23

# Project 3: AWS Data Warehouse
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They requested a data engineer build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Overview
In this project, I applied what I learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, I loaded data from S3 to staging tables on Redshift and then inserted them into a set of dimensional tables optimized for analytics. The end result is that the analytics team can now run desired queries on the data in the analytics database.

## Project Files
* `create_tables.py` creates star schema tables in the sparkify database
* `etl.py` copys data from S3 to staging tables on Redshift and then inserts data from the Redshift staging tables to the analytics tables on Redshift
* `sql_queries.py` contains SQL queries to drop and create tables, copy data from S3 to staging tables in Redshift and insert data from staging tables to analytics tables.

## Database Design
https://docs.microsoft.com/en-us/power-bi/guidance/star-schema

The Sparkify analytics database (sparkifydb) has a star schema design. Star schema is a mature modeling approach widely adopted by relational data warehouses. It requires modelers to classify their model tables as either dimension or fact.

**Dimension tables** describe business entities—the things you model. Entities can include products, people, places, and concepts including time itself. The most consistent table you'll find in a star schema is a date dimension table. A dimension table contains a key column (or columns) that acts as a unique identifier, and descriptive columns.

**Fact Tables** store observations or events, and can be sales orders, stock balances, exchange rates, temperatures, etc. A fact table contains dimension key columns that relate to dimension tables, and numeric measure columns. The dimension key columns determine the dimensionality of a fact table, while the dimension key values determine the granularity of a fact table. For example, consider a fact table designed to store sale targets that has two dimension key columns Date and ProductKey. It's easy to understand that the table has two dimensions. The granularity, however, can't be determined without considering the dimension key values. In this example, consider that the values stored in the Date column are the first day of each month. In this case, the granularity is at month-product level.

### Fact Table
songplays: song play data together with user, artist, and song info
Dimension Tables
users: user info
songs: song info
artists: artist info
time: detailed time info about song plays

### Dimension Tables

* **users**: user info
* **songs**: song info 
* **artists**: artist info
* **time**: detailed time info about song plays

## Schema
https://ibb.co/2M6h4Dg

![Sparkifydb schema as Entity Relationship Diagram](/udacity-project-1-diagram.png)

_*sparkifydb entity relationship diagram*_

## Instructions

Set up a configuration file `dwh.cfg` with the following structure based on an existing Redshift cluster

```
[CLUSTER]
HOST=hostname
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=password
DB_PORT=5439


[IAM_ROLE]
ARN=arn:aws:iam::<account_id>:role/<role>

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'

[AWS]
ACCESS_KEY=access_key
SECRET_KEY=secret_key
```

Then execute the following to create tables in the database and load the data

```
python create_tables.py
python etl.py
```

## Sample Queries

Once you've created the database and run the ETL pipeline, you can test out some
queries in Redshift console query editor:

```
--Number of song plays before Nov 15, 2018
select count(*) from songplays where start_time < '2018-11-15'
```

```
--Top artists by number of song plays
select a.name, count(a.name) as n_songplays
from songplays s
left join artists a on s.artist_id = a.artist_id
group by a.name
order by n_songplays desc
```