# -*- coding:utf-8 -*-
from minio import Minio
minioClient = Minio('minio.xuguoxu.cn',access_key='minioadmin',secret_key='minioadmin',secure=True)
'''
服务为HTTP时secure使用False，服务为HTTPs时secure使用Ture。
否则会报urllib3.exceptions.MaxRetryError: 
HTTPSConnectionPool(host='192.8.21.87', port=9000): 
Max retries exceeded with url:
 /new/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:833)'),))的错误
'''
minioClient.make_bucket("mybucket1")#生成一个bucket，类似文件夹