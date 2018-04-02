#!/usr/bin/python
#-*- coding:utf-8 -*-
import argparse
import os
import json
import urllib.request
import ssl
import re
import sys
import socket
from datetime import datetime

PURPOSE_CODES   = ['ADULT', '0X00'] # 成人票，学生票
ADDR_CACHE_FILE = '.addr'
CITY_CACHE = None
CITY_CACHE_FILE = '.cities'
CITY_LIST_URL = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
ACTION_URL = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={train_time}&leftTicketDTO.from_station={from_city}&leftTicketDTO.to_station={to_city}&purpose_codes={ticket_type}'
SSL_CTX = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

# 对数字进行补零
def add_zero(num):
    if int(num) < 10:
        num = '0'+str(int(num))
    return num

# 默认为今天
def default_date():
    now = datetime.now()
    return '-'.join([str(now.year),str(add_zero(now.month)),str(add_zero(now.day))])

# 格式化输入日期
# 4-2 => 2018-04-02
# 2018:04:02 => 2018-04-02

def date_format(input_date):
    if not input_date:
        return default_date()
    res = re.match(r'(([0-9]{4})[-|\\|:\.])?([0-9]{1,2})[-|\\|:\.]([0-9]{1,2})',input_date)
    if res:
        year = res.group(2)
        month = res.group(3)
        day = res.group(4)

        now = datetime.now()
        if not year:
            year = now.year
        if not month:
            month = now.month
        if not day:
            day = now.day
        return '-'.join([str(year),add_zero(str(month)),add_zero(str(day))])
    else:
        print('输入日期格式错误')
        sys.exit(-1)

# 加载城市列表
def load_cities():
    global CITY_CACHE
    if CITY_CACHE is not None:
        return CITY_CACHE
    cache_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),CITY_CACHE_FILE)
    need_reload = True
    cities = {}
    if os.path.exists(cache_file):
        with open(cache_file,'rb') as fp:
            cities = json.load(fp)
        if cities:
            need_reload = False

    if need_reload:
        city_info = urllib.request.urlopen(CITY_LIST_URL,context=SSL_CTX).read()
        for res in re.finditer(r'@[a-z]{3}\|(.+?)\|([A-Z]{3})\|[a-z]+?\|[a-z]+?\|',city_info.decode('utf-8')):
            city = res.group(1)
            code = res.group(2)
            cities[city] = code
        with open(cache_file,'w') as fp:
            json.dump(cities,fp)
    CITY_CACHE = cities
    return cities

def search(from_city,to_city,train_time,ticket_type='ADULT'):
    cities = load_cities()
    try:
        from_code = cities[from_city]
    except KeyError:
        print('指定的起点%s不存在' % from_city)
        sys.exit(-1)
    try:
        to_code = cities[to_city]
    except KeyError:
        print('指定的目标地点%s不存在' % to_city)
        sys.exit(-1)
    url = ACTION_URL.format(from_city=from_code,to_city=to_code,train_time=train_time,ticket_type=ticket_type)
    print(url)
    ret = json.loads(urllib.request.urlopen(url,context=SSL_CTX).read())
    if not ret or ret == -1 or not ret['data'] or len(ret['data']) == 0:
        print('没有找到相关车次信息')
        sys.exit(-1)
    print('车次序号    起始站  出发站 终点站 时间 一等座 二等座')
    for r in ret['data']:
        r = r['queryLeftNewDTO']
        if (not r['zy_num'].encode('utf-8').isdigit()
            and not r['ze_num'].encode('utf-8').isdigit()
            or r['from_station_name'].encode('utf-8') != from_city):
            continue
        print(u'%s %s->%s->%s %s %s %s' % (
            r['train_no'],
            r['start_station_name'],
            r['from_station_name'],
            r['to_station_name'],
            r['arrive_time'],
            r['zy_num'],
            r['ze_num']
        ))

# 获取ip地址
def getip():
    url = 'http://jsonip.com'
    ip_info = urllib.request.urlopen(url, timeout=20,context=ssl._create_unverified_context()).read()
    res = re.search('\d+\.\d+\.\d+\.\d+',ip_info.decode('utf-8'))
    if res:
        return res.group(0)
    return None

# 根据ip获取地址
def getaddr(fresh=False):
    addr_cache_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),ADDR_CACHE_FILE)
    if not fresh and os.path.exists(addr_cache_file):
        addr = None
        with open(addr_cache_file,'r') as fp:
            addr = fp.read()
        if addr:
            return addr

    ip = getip()

    if not ip:
        return None
    addr_info = urllib.request.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip,timeout=5).read()
    city = None
    if addr_info:
        addr_info = json.loads(addr_info)
        city = addr_info['data']['city']
        city = city.replace('市','')
        with open(addr_cache_file,'w') as fp:
            fp.write(city)
    return city

def get_yn_input(msg):
    while True:
        res = input('%s ,是请按回车,不是请输入n:' % msg)
        if res in ('','n'):
            break
    return True if res == None else False

# 默认模式
def guide():
    try:
        cities = load_cities()
        city = getaddr()
    except:
        print('请求超时')
        sys.exit(-1)

    if city and city in cities:
        from_city = input('请输入起始站点(输入回车为%s):' % city)
        if not from_city:
            from_city = city
    else:
        from_city = input('请输入起始站点:')
    while True:
        to_city = input('请输入目的站点:')
        if to_city:
            break

    dd = default_date()
    train_time = input('请输入出发日期(输入回车为%s):' % dd)
    train_time = date_format(train_time) if train_time else dd
    ticket_type = '0X00' if get_yn_input('是否是成人票') else 'ADULT'
    print('正在查询...\n')
    search(from_city,to_city,train_time,ticket_type)

if __name__ == '__main__':
    # cities = load_cities()
    # print(cities)

    # print(default_date())

    # print(date_format('4.1'))
    # guide()
    parser = argparse.ArgumentParser(description='查询12306车次余票')
    parser.add_argument('-f','--from_city',type=str,help='起始城市')
    parser.add_argument('-t','--to_city',type=str,help='目标城市')
    parser.add_argument('-d','--train_time',type=str,help='日期,格式如:2018-04-02')
    parser.add_argument('-s','--student',help='学生票')
    parser.add_argument('-l','--list_city',help='查看支持城市列表')

    args = parser.parse_args()
    from_city = args.from_city
    to_city = args.to_city
    train_time = args.train_time
    ticket_type = PURPOSE_CODES[1] if args.student else PURPOSE_CODES[0]
    list_city = args.list_city

    if from_city is None and to_city is None and list_city is False:
        guide()
    else:
        if list_city:
            for city,code in load_cities().items():
                print(city)
        elif from_city and to_city and ticket_type:
            search(from_city,to_city,train_time,ticket_type)
        else:
            print('参数错误')