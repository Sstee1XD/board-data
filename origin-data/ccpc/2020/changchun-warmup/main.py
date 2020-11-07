import xlrd
from os import path
import os
import json
import time

def json_output(data):
    return json.dumps(data, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)

def mkdir(_path):
    if not path.exists(_path):
        os.makedirs(_path)

def get_timestamp(dt):
    #转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    return int(timestamp)

def output(filename, data):
    with open(path.join(data_dir, filename), 'w') as f:
        f.write(json_output(data))

data_dir = "../../../../data/ccpc/2020/changchun-warmup"
problem_num = 4
problem_id = [chr(ord('A') + i) for i in range(problem_num)] 
group = {
    'official': '正式队伍',
    'unofficial': '打星队伍',
    'girl': '女队',
}
status_time_display = {
    'correct': 1,
    'incorrect': 1,
}
balloon_color = [
    {'background_color': '#bd0e0e', 'color': '#fff' },
    {'background_color': '#ff90e4', 'color': '#fff' },
    {'background_color': '#ffffff', 'color': '#000' },
    {'background_color': '#26b93c', 'color': '#fff' },
]

config = {
    'contest_name': 'CCPC2020-第六届中国大学生程序设计竞赛（长春） 热身赛',
    'start_time': get_timestamp("2020-11-7 15:00:00"),
    'end_time': get_timestamp("2020-11-7 18:00:00"),
    'frozen_time' : 0,
    'problem_id': problem_id,
    'group': group,
    'organization': 'School',
    'status_time_display': status_time_display,
    'penalty': 20 * 60,
    'balloon_color': balloon_color,
}

def config_out():
    output("config.json", config)

mkdir(data_dir)
config_out()