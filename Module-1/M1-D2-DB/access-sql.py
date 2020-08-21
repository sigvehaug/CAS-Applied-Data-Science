#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("university.db")

STMT_INST_ID_FOR_NAME = """
    select name
    from instructor
    where ID =:id
    """

STMT_INST_BUILDING_FOR_NAME = """
    select building
    from instructor, department
    where instructor.dept_name = department.dept_name and name = :name
    """

STMT_INST_NAME_BUILDING = """
    select name, building
    from instructor natural join  department
    """


def get_instructor_name(id):
    c = conn.execute(STMT_INST_ID_FOR_NAME, {'id': id})
    return c.fetchone()


def get_instructor_building(name):
    c = conn.execute(STMT_INST_BUILDING_FOR_NAME, {'name': name})
    return c.fetchall()


def get_instructor_building_list():
    c = conn.execute(STMT_INST_NAME_BUILDING)
    return c.fetchall()


if __name__ == '__main__':

    print(get_instructor_name('22222'))

    print(get_instructor_building('Einstein'))

    print(get_instructor_building_list())

