# 建立表
    sql ="""
      CREATE TABLE if not exists `beike40`(
      `id`    INT UNSIGNED AUTO_INCREMENT,
      `name`    VARCHAR(255)  NULL,
      `address` VARCHAR(255)  NULL,
      `area`    VARCHAR(255)  NULL,
      `price1` VARCHAR(255)  NULL,
      `price2` VARCHAR(255)  NULL,
      `ting`   VARCHAR(255)  NULL,
      `lv`     VARCHAR(255)  NULL,
      `tm2`    VARCHAR(255)  NULL,
      `tm`    VARCHAR(255)  NULL,
      `url`    VARCHAR(255) NULL,
      `Time1` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (`id`)
      )ENGINE=InnoDB DEFAULT CHARSET=utf8;
      """
# 删除表
DROP TABLE table_name ;
# 清空表
    truncate gk_portal;  
    delete from  gk_portal;
       这两者都是将gk_portal表中数据清空，不过也是有区别的，如下：
    
    truncate是整体删除（速度较快）， delete是逐条删除（速度较慢）。
    truncate不写服务器log，delete写服务器log，也就是truncate效率比delete高的原因。
    truncate不激活trigger(触发器)，但是会重置Identity（标识列、自增字段），
            相当于自增列会被置为初始值，又重新从1开始记录，而不是接着原来的ID数。
            而delete删除以后，Identity依旧是接着被删除的最近的那一条记录ID加1后进行记录。
    如果只需删除表中的部分记录，只能使用DELETE语句配合where条件。 DELETE FROM gk_portal  WHERE…
# 注释
    create table test1 ( 
    field_name int comment '字段的注释' 
    )comment='表的注释'; 
    修改：alter table test1 comment '修改后的表的注释';
    修改字段：alter table test1 modify column field_name int comment '修改后的字段注释'; 
    查看：show  create  table  test1;
         show  full  columns  from  test1;
         select * from TABLES where TABLE_SCHEMA='my_db' and TABLE_NAME='test1' \G
         select * from COLUMNS where TABLE_SCHEMA='my_db' and TABLE_NAME='test1' \G

# 统计重复信息
    SELECT COUNT(*) as repetitions, name, nums #name,nums列 
    FROM beike_xiaoqu_08 #表名
    GROUP BY name, nums  #列名
    HAVING repetitions > 1;
# 查看数据库大小
查看路径
ps -ef|grep mysql

进入数据库
/usr/local/mysql/bin/mysql -u root -p

查看数据库大小

    1、进入information_schema 数据库（存放了其他的数据库的信息）
    use information_schema;

    2、查询所有数据的大小：
    select concat(round(sum(data_length/1024/1024),2),'MB') as data from tables;
 
    3、查看指定数据库的大小：
    比如查看数据库home的大小

    select concat(round(sum(data_length/1024/1024),2),'MB') as data from tables where table_schema='home';
 
    4、查看指定数据库的某个表的大小
    比如查看数据库home中 members 表的大小
    select concat(round(sum(data_length/1024/1024),2),'MB') as data from tables where table_schema='home' and   table_name='members';

# import pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    sql ="""
    CREATE TABLE if not exists `IBRD_gdp_T`(
    `id`    INT UNSIGNED AUTO_INCREMENT,
    `country`    VARCHAR(255)  NULL,
    `code` VARCHAR(255)  NULL,
    `1960-12-31` double  NULL,
    `1961-12-31` double  NULL,
    `1962-12-31` double  NULL,
    `1963-12-31` double  NULL,
    `1964-12-31` double  NULL,
    `1965-12-31` double  NULL,
    `1966-12-31` double  NULL,
    `1967-12-31` double  NULL,
    `1968-12-31` double  NULL,
    `1969-12-31` double  NULL,
    `1970-12-31` double  NULL,
    `1971-12-31` double  NULL,
    `1972-12-31` double  NULL,
    `1973-12-31` double  NULL,
    `1974-12-31` double  NULL,
    `1975-12-31` double  NULL,
    `1976-12-31` double  NULL,
    `1977-12-31` double  NULL,
    `1978-12-31` double  NULL,
    `1979-12-31` double  NULL,
    `1980-12-31` double  NULL,
    `1981-12-31` double  NULL,
    `1982-12-31` double  NULL,
    `1983-12-31` double  NULL,
    `1984-12-31` double  NULL,
    `1985-12-31` double  NULL,
    `1986-12-31` double  NULL,
    `1987-12-31` double  NULL,
    `1988-12-31` double  NULL,
    `1989-12-31` double  NULL,
    `1990-12-31` double  NULL,
    `1991-12-31` double  NULL,
    `1992-12-31` double  NULL,
    `1993-12-31` double  NULL,
    `1994-12-31` double  NULL,
    `1995-12-31` double  NULL,
    `1996-12-31` double  NULL,
    `1997-12-31` double  NULL,
    `1998-12-31` double  NULL,
    `1999-12-31` double  NULL,
    `2000-12-31` double  NULL,
    `2001-12-31` double  NULL,
    `2002-12-31` double  NULL,
    `2003-12-31` double  NULL,
    `2004-12-31` double  NULL,
    `2005-12-31` double  NULL,
    `2006-12-31` double  NULL,
    `2007-12-31` double  NULL,
    `2008-12-31` double  NULL,
    `2009-12-31` double  NULL,
    `2010-12-31` double  NULL,
    `2011-12-31` double  NULL,
    `2012-12-31` double  NULL,
    `2013-12-31` double  NULL,
    `2014-12-31` double  NULL,
    `2015-12-31` double  NULL,
    `2016-12-31` double  NULL,
    `2017-12-31` double  NULL,
    `2018-12-31` double  NULL,
    `2019-12-31` double  NULL,
    `2020-12-31` double  NULL,
    `Time1` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
