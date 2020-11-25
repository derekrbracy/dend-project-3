"""
This module copys data from S3 to staging tables on Redshift and then inserts data from the Redshift
staging tables to the analytics tables on Redshift.
"""


import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn) -> None:
    """
    Copys data from S3 to staging tables on Redshift

    Parameters
    ----------
    cur: pyscopg2 cursor for the sparkify database in Redshift
    conn: pyscopg2 connection for the sparkify database in Redshift

    Returns
    -------
    None
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn) -> None:
    """
    Inserts data from staging tables to analytics tables on Redshift

    Parameters
    ----------
    cur: pyscopg2 cursor for the sparkify database in Redshift
    conn: pyscopg2 connection for the sparkify database in Redshift

    Returns
    -------
    None
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main() -> None:
    """
    Reads in AWS configuration information from dwh.cfg, connects to the sparkify database, copys
    data from S3 to the staging tables in Redshift and then inserts data from the staging tables
    to the analytics tables in Redshift.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["CLUSTER"].values()
        )
    )
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
