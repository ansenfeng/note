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
#注释
      > create table test1 ( 
      > field_name int comment '字段的注释' 
      > )comment='表的注释'; 
      > 修改：alter table test1 comment '修改后的表的注释';
      > 修改字段：alter table test1 modify column field_name int comment '修改后的字段注释'; 
      > 查看：show  create  table  test1;
      > show  full  columns  from  test1;
      > select * from TABLES where TABLE_SCHEMA='my_db' and TABLE_NAME='test1' \G
      > select * from COLUMNS where TABLE_SCHEMA='my_db' and TABLE_NAME='test1' \G
