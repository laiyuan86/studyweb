#操作数据库

import pymysql


class execmysql():

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    #创建数据连接
    def connectdb(self):
        db = pymysql.connect(self.host, self.user, self.password, self.db)

        return db

    #查看数据库信息
    def get_db_info(self):
        db = self.connectdb()
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)
        db.close()

    #查看数据
    def search_data(self):
        db = self.connectdb()
        cursor = db.cursor()
        SQL = "SELECT * FROM CreateVM"
        try:
            cursor.execute(SQL)
            result = cursor.fetchall()
            vmsinfo = []
            for row in result:
                vminfo = []
                vminfo.append(row[1])
                vminfo.append(row[2])
                vminfo.append(row[3])
                vminfo.append(row[4])
                vminfo.append(row[5])
                vminfo.append(row[6])
                vminfo.append(row[7])
                vmsinfo.append(vminfo)
        except:
            print("Some this is error!")

        db.close()
        return vmsinfo

    #插入数据
    def insert_data(self, IP, YW, BM, SN, YN, CT, ET):
        db = self.connectdb()
        cursor = db.cursor()
        sql = "INSERT INTO CreateVM(IP, YW, BM, YEWUJK, YUNWEIJK, CTIME, ETIME) \
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (IP, YW, BM, SN, YN, CT, ET)
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException as e:
            print("出现错误: %s" % e)
            db.rollback()
        db.close()




if __name__ == '__main__':
    host = '127.0.0.1'
    user = 'root'
    password = 'qwe123'
    db = 'studyweb'
    exmysql = execmysql(host, user, password, db)
    exmysql.search_data()