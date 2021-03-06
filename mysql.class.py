#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
from const import const


class MySql:
    def __init__(self, host=const.DB_HOST, user=const.DB_USER, password=const.DB_PASS, db=const.DB_NAME,
                 port=const.DB_PORT):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.cache = []
        self.connect()

    def connect(self):
        if 'cursor' in locals().keys():
            pass
        else:
            self.dbconn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                          port=self.port, charset='utf8mb4')
            self.cursor = self.dbconn.cursor()

    def get_rows(self, query_sql):
        """
        返回查询结果集
        :param query_sql: select sql
        :return: rows type:set
        """
        self.cursor.execute(query_sql)
        results = self.cursor.fetchall()
        return results

    def get_first_row(self, query_sql):
        """
        返回查询结果集的第一行
        :param query_sql:
        :return: row  type:set
        """
        res = self.get_rows(query_sql)
        if len(res) == 0:
            return ""
        return res[0]

    def get_first_row_column(self, query_sql):
        """
        返回查询结果集的第一行第一个字段
        :param query_sql:
        :return: first row column type: str
        """
        row = self.get_first_row(query_sql)
        if row == "":
            return ""
        return row[0]

    def query(self, query_sql):
        """
        执行sql
        :param query_sql: DDL, DML sql
        """
        try:
            self.cursor.execute(query_sql)
            self.dbconn.commit()
        except:

            filename = 'test_text.txt'
            with open(filename, 'a') as file_object:
                file_object.write(query_sql)

    def is_table_exists(self, table_name):
        """
        判断表是否存在
        :param table_name:
        :return: boole
        """
        if table_name in self.cache:
            return True
        sql = "SHOW TABLES LIKE '" + table_name + "'"
        t = self.get_first_row(sql)
        if t:
            self.cache.append(t[0])
            return True
        return False

    def get_create_table_sql(self, table_name):
        """
       获取指定表的建表sql
        :param table_name:
        :return: CreateTable Sql
        """
        sql = "SHOW CREATE TABLE `" + table_name + "`"
        first_row = self.get_first_row(sql)
        return first_row[1]

    def duplicate_table(self, default_tb, new_tb):
        """
       复制一张表
        :param default_tb: default table name
        :param new_tb: new table name
        """
        create_sql = self.get_create_table_sql(default_tb)
        search_text = "CREATE TABLE `" + default_tb + "`"

        if search_text not in create_sql:
            import sys
            try:
                sys.exit(0)
            except:
                print('die')
                return
        new_str = "CREATE TABLE `" + new_tb + "`"
        self.query(create_sql.replace(search_text, new_str, 1))

    def close(self):
        self.cursor.close()
