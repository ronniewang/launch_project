# -*-coding:utf-8-*-

log_time = '2016103115'

request_id = '456091550'


def find_log(request_id):
    log_file_path = '/Users/ronniewang/PycharmProjects/tomcat_mobile_1.%s.log' % log_time

    log_info_list = []
    with open(log_file_path) as log_file:
        for line in log_file:
            if line.find(request_id) != -1:
                log_info_list.append(line)
    return log_info_list

