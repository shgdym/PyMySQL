# 封装的一个mysql类
+ get_rows(self, query_sql):

        返回查询结果集
        :param query_sql: select sql
        :return: rows type:set
        
+ get_first_row(self, query_sql):

        返回查询结果集的第一行
        :param query_sql:
        :return: row  type:set
        
+ get_first_row_column(self, query_sql):

        返回查询结果集的第一行第一个字段
        :param query_sql:
        :return: first row column type: str
        
+ query(self, query_sql):

        执行sql
        :param query_sql: DDL, DML sql
        
+ is_table_exists(self, table_name): 

        判断表是否存在
        :param table_name:
        :return: boole
        
+ get_create_table_sql(self, table_name):
       
       获取指定表的建表sql
        :param table_name:
        :return: CreateTable Sql
        
+ duplicate_table(self, default_tb, new_tb):    
    
       复制一张表
        :param default_tb: default table name
        :param new_tb: new table name
