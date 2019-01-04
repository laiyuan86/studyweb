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
            ips = []
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
                ips.append(row[1])
        except:
            print("Some this is error!")

        db.close()
        info = [vmsinfo, ips]
        return info

    #插入开通虚机信息数据
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

    #插入故障处理信息
    def insert_deal_event(self, ip, event, dealtime):
        db = self.connectdb()
        cursor = db.cursor()
        sql = "INSERT INTO DealThing(IP, EVENT, CUTIME) VALUES ('%s', '%s', '%s')" % (ip, event, dealtime)
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException as e:
            print("出现错误：%s" %e)
            db.rollback()
        db.close()

    #插入变更信息
    def insert_vmchange(self, ip, event, bgtime):
        db = self.connectdb()
        cursor = db.cursor()
        sql = "INSERT INTO VMChange(IP, EVENT, BGTIME) VALUES ('%s', '%s', '%s')" % (ip, event, bgtime)
        try:
            cursor.execute(sql)
            db.commit()
        except BaseException as e:
            print("出现错误：%s" % e)
            db.rollback()
        db.close()


    #获取表中数据条数
    def get_events_nums(self):
        db = self.connectdb()
        cursor = db.cursor()
        vmcreate_sql = "SELECT COUNT(*) FROM CreateVM"
        dealthing_sql = "SELECT COUNT(*) FROM DealThing"
        vmchange_sql = "SELECT COUNT(*) FROM VMChange"
        nums = []
        try:
            cursor.execute(vmcreate_sql)
            vmcreate_nums = cursor.fetchone()
            nums.append(vmcreate_nums[0])
            cursor.execute(dealthing_sql)
            dealthing_nums = cursor.fetchone()
            nums.append(dealthing_nums[0])
            cursor.execute(vmchange_sql)
            vmchange_nums = cursor.fetchone()
            nums.append(vmchange_nums[0])
        except BaseException as e:
            print("出现错误：%s" % e)
        db.close()

        print(nums)
        return nums

    #按日期范围查找
    def get_events_nums_date(self, *setimes):
        db = self.connectdb()
        cursor = db.cursor()
        startime = setimes[0]
        overtime = setimes[1]
        vmcreate_sql = "SELECT COUNT(*) FROM CreateVM WHERE date(CTIME) BETWEEN '%s' AND '%s'" % (startime, overtime)
        dealthing_sql = "SELECT COUNT(*) FROM DealThing WHERE date(CUTIME) BETWEEN '%s' AND '%s'" % (startime, overtime)
        vmchange_sql = "SELECT COUNT(*) FROM VMChange WHERE date(BGTIME) BETWEEN '%s' AND '%s'" % (startime, overtime)
        nums = []
        try:
            cursor.execute(vmcreate_sql)
            vmcreate_nums = cursor.fetchone()
            nums.append(vmcreate_nums[0])
            cursor.execute(dealthing_sql)
            dealthing_nums = cursor.fetchone()
            nums.append(dealthing_nums[0])
            cursor.execute(vmchange_sql)
            vmchange_nums = cursor.fetchone()
            nums.append(vmchange_nums[0])
        except BaseException as e:
            print("出现错误：%s" % e)
        db.close()

        print(nums)
        return nums

    #按IP查询
    def get_vminfo_forip(self, ip):
        db = self.connectdb()
        cursor = db.cursor()
        sql = "SELECT * FROM CreateVM WHERE IP = '%s'" % ip
        vminfo = []
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            vminfo.append(res[0][1])
            vminfo.append(res[0][2])
            vminfo.append(res[0][3])
            vminfo.append(res[0][4])
            vminfo.append(res[0][5])
            vminfo.append(res[0][6])
            vminfo.append(res[0][7])
        except BaseException as e:
            vminfo = None
            print("出现错误：%s" % e)
            return vminfo
        db.close()
        return vminfo


if __name__ == '__main__':
    host = '127.0.0.1'
    user = 'root'
    password = 'qwe123'
    db = 'studyweb'
    setimes = ['2019-01-01', '2019-01-03']
    exmysql = execmysql(host, user, password, db)
    exmysql.get_vminfo_forip('172.24.132.185')
