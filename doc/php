 #  php config
    <?php
    header("Content-Type: text/html;charset=utf-8");
    $sql_host="localhost";
    $sql_user="root";
    $sql_passwd="123456";
    $sql_database="diy";
    $enable_rewrite=1;
    ?>
#  php文件

   <?php 
   require_once dirname(__FILE__).'/con/config.php';
   		# php <php
   		$mysqli = new mysqli($sql_host,$sql_user,$sql_passwd,$sql_database);  # 主机 用户名。密码  数据库名
   
   		
   			#判断是否连接成功
   
   		if ($mysqli->connect_error) {
   
   			# 只要不为0，就要是连接失败
   		  die(connect_error);
   		}
   		#  $mysqli->query +sql 语句
   		
   	$result = $mysqli->query(" SELECT * FROM test ");   # 返回一个对象 object.
      $row =$result->fetch_all(MYSQLI_ASSOC);
       $json1 =  json_encode($row,JSON_UNESCAPED_UNICODE);//json编码的时候会改变中文编码，需要这个选项
       $json2 =  json_decode(json1);
       echo ('{"data":'.$json1.'}');
    ?>
