from os import path
import os
import json
import time

def json_output(data):
    return json.dumps(data, sort_keys=False, indent=4, separators=(',', ':'), ensure_ascii=False)

def json_input(path):
    with open(path, 'r') as f:
        return json.load(f)

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


raw_dir = "raw"
data_dir = "../../../../data/provincial-contest/2019/sdcpc"
team_data_filename = "team.json"
run_data_filename = "run.json"
problem_num = 13
problem_id = [chr(ord('A') + i) for i in range(problem_num)] 
group = {
    'official': '正式队伍',
    'unofficial': '打星队伍',
    'girl': '女队',
}
status_time_display = {
    'correct': 1,
    'incorrect': 1,
    'pending': 1,
}
config = {
    'contest_name': 'The 10th Shandong Provincial Collegiate Programming Contest',
    'start_time': get_timestamp("2019-5-2 12:00:00"),
    'end_time': get_timestamp("2019-5-2 17:00:00"),
    'frozen_time' : 60 * 60,
    'problem_id': problem_id,
    'group': group,
    'organization': 'School',
    'status_time_display': status_time_display,
    'penalty': 20 * 60,
}

def config_out():
    output("config.json", config)
    
def team_out():
    team_dic = json_input(path.join(raw_dir, team_data_filename))
    team = {}
    for key in team_dic:
        item = team_dic[key]
        team[key] = {}
        new_item = team[key]
        new_item['organization'] = item['school']
        new_item['name'] = item['team']
        new_item['info'] = item['members']
        type = item['type'].split(" ")
        for tp in type:
            if tp == 'girls':
                new_item['girl'] = 1
            else:
                new_item[tp] = 1
    output("team.json", team)
        
def run_out():
    run_list = json_input(path.join(raw_dir, run_data_filename))
    run = []
    for item in run_list:
        new_item = {}
        new_item['team_id'] = item[0]
        new_item['problem_id'] = problem_id.index(item[1])
        new_item['timestamp'] = (int(item[2] // 1000) // 60) * 60
        status = item[3]
        if status == 'AC':
            new_item['status'] = 'correct'
        elif status == 'NO':
            new_item['status'] = 'incorrect'
        elif status == 'NEW':
            new_item['status'] = 'pending'
        run.append(new_item)
    output("run.json", run)
            

mkdir(data_dir)
config_out()
team_out()
run_out()