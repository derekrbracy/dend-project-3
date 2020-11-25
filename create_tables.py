"""
This module connects to, drops and then creates new tables in the sparkifydb as specified by the
queries imported from 'sql_queries.py'
"""

import configparser
import psycopg2

from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn) -> None:
    """
    Drop tables in the sparkify database as specified by the queries in the 'drop_table_queries'
    list.

    Parameters
    ----------
    cur: pyscopg2 cursor for the sparkify database in Redshift
    conn: pyscopg2 connection for the sparkify database in Redshift

    Returns
    -------
    None
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn) -> None:
    """
    Creates tables in the sparkify database as specified by the queries in the
    'create_table_queries' list.

    Parameters
    ----------
    cur: pyscopg2 cursor for the sparkify database in Redshift
    conn: pyscopg2 connection for the sparkify database in Redshift

    Returns
    -------
    None
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main() -> None:
    """
    Reads in AWS configuration information from dwh.cfg, connects to the sparkify database, drops
    tables if they already exist and then creates new tables.

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

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
