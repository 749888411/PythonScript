import commands
import time
from log import Logger

ORACLE_TO_HIVE = "sqoop import --hive-import --connect jdbc:oracle:thin:@{ip}:{port}:{sid} --username {username}" \
                 " --password {pwd} --verbose --query 'select * from {table} where $CONDITIONS' --target-dir /usr/{dir} " \
                 " --split-by {split_by}  --hive-table {hive_table} --hive-database sourcedata --hive-partition-key 'dt' " \
                 " --hive-partition-value '{pvalue}' --fields-terminated-by '\\t'"
MYSQL_TO_HIVE = "sqoop import --hive-import --connect jdbc:mysql://{ip}:{port}/{db} --username {username} " \
                "--password {pwd} --verbose --query 'select * from {table} where $CONDITIONS' --target-dir /usr/{dir}  " \
                "--split-by {split_by}  --hive-table {hive_table} --hive-database sourcedata --hive-partition-key 'dt' " \
                "--hive-partition-value '{pvalue}' --fields-terminated-by '\\t'"


def exec_oracle_cmd():
    for line in open("../docs/oracle.txt"):
        placed_line = line.replace('\r\n', '').split('\t')
        cmd = ORACLE_TO_HIVE.format(ip=placed_line[0], port=placed_line[1], sid=placed_line[2], username=placed_line[3], pwd=placed_line[4], table=placed_line[7], dir=placed_line[6], hive_table=placed_line[6], split_by=placed_line[8], pvalue=get_day("%Y-%m-%d", -1))
        print(cmd)
        Logger.info("Starting import table: " + placed_line[6])
        #(status, text) = commands.getstatusoutput(cmd)
        #print(cmd)
        #if status != 0:
        #    Logger.info("End of import, status: " + str(status))
        #    Logger.info("End of import, content: " + text)


def exec_mysql_cmd():
    for line in open("../docs/mysql.txt"):
        placed_line = line.replace('\r\n', '').split('\t')
        cmd = MYSQL_TO_HIVE.format(ip=placed_line[0], port=placed_line[1], db=placed_line[2], username=placed_line[3], pwd=placed_line[4], table=placed_line[6], dir=placed_line[5], hive_table=placed_line[5], split_by=placed_line[7], pvalue=get_day("%Y-%m-%d", -1))
        Logger.info("Starting import table: " + placed_line[6])
        (status, text) = commands.getstatusoutput(cmd)
        print(cmd)
        if status != 0:
            Logger.info("End of import, status: " + str(status))
            Logger.info("End of import, content: " + text)


def get_day(fmt, ndays):
    day = time.strftime(fmt, time.localtime(time.time() + ndays * 24 * 60 * 60))
    return day


def main():
    exec_oracle_cmd()
    #exec_mysql_cmd()


if __name__ == "__main__":
    main()
