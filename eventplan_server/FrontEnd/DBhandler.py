#!/usr/bin/python

import pymysql

class DBhandler():
    # TODO: fix this
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 db='db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    def __init__(self):
        return

    def insertPair(self, friend, adminFriend):
        # connect to DB
        # Read a single record
        sql = "SELECT * FROM `users` WHERE (`id1`="+friend+" AND `id2`="+adminFriend+") OR (`id1`="+adminFriend+" AND `id2`="+friend+")"
        found = self.selectDB(sql)
        if found:
            return
        else:
            # insert to DB
            # Create a new record
            sql = "INSERT INTO `users` (`id1`, `id2`) VALUES (friend, adminFriend)"
            self.insertDB(sql)


    def selectDB(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            self.connection.close()

    def executeQuery(self, sql):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                # connection is not autocommit by default. So you must commit to save your changes.
                self.connection.commit()
        finally:
            self.connection.close()
