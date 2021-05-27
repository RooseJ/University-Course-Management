from typing import Any, Union

import mysql.connector
from mysql.connector import Error, CMySQLConnection, MySQLConnection

conn: Union[Union[CMySQLConnection, MySQLConnection], Any] = mysql.connector.connect(host='localhost',
                                                                                     database='course_management',
                                                                                     user='root',
                                                                                     password='')
