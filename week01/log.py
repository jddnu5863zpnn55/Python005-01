import os
from datetime import datetime


def write_log():
    """
    写入日志
    """
    now_date = datetime.strftime(datetime.now(), "%Y-%m-%d")
    file_dir = '/var/log/'
    file_name = 'python-' + now_date + '.log'
    # 判断路径是否存在，没有则创建该路径
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    # 打开文件写入时间
    with open(file_dir + file_name, mode='a+', encoding="utf-8") as w:
        w.write(str(datetime.now()) + '\n')


write_log()
