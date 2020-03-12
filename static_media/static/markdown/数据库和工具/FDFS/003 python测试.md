```
1. workon django_py3
2. 进入fdfs_client-py-master.zip所在目录
3. pip install fdfs_client-py-master.zip
4. 

>>> from fdfs_client.client import Fdfs_client
>>> client = Fdfs_client('/etc/fdfs/client.conf')
>>> ret = client.upload_by_filename('test')
>>> ret
{'Group name':'group1','Status':'Upload successed.', 'Remote file_id':'group1/M00/00/00/
	wKjzh0_xaR63RExnAAAaDqbNk5E1398.py','Uploaded size':'6.0KB','Local file name':'test'
	, 'Storage IP':'192.168.243.133'}

```

