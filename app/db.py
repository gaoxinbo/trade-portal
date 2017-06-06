import pymysql

RDS_ENDPOINT="free-1.cwvczwd58ova.us-east-1.rds.amazonaws.com"
USERNAME="gaoxinbo"
DB="trade"

def get_connection(passwd):
    connection = pymysql.connect(host=RDS_ENDPOINT,
                                 user=USERNAME,
                                 db=DB,
                                 password=passwd)
    return connection
