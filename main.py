from serverJiang import *
from constant import *

import requests, re, json, copy, traceback


session = requests.Session()


def ncov_report(username, password, name, is_useold):
    print('登录北邮 nCoV 上报网站')
    login_res = session.post(
        LOGIN_API,
        data={'username': username, 'password': password, },
        headers={**COMMON_HEADERS, **COMMON_POST_HEADERS, 'Referer': HEADERS.REFERER_LOGIN_API,
                 })
    if login_res.status_code != 200:
        raise RuntimeError('login_res 状态码不是 200')
    get_res = session.get(
        GET_API,
        headers={**COMMON_HEADERS, 'Accept': HEADERS.ACCEPT_HTML},
    )
    if get_res.status_code != 200:
        raise RuntimeError('get_res 状态码不是 200')
    try:
        old_data = json.loads('{' + re.search(r'(?<=oldInfo: {).+(?=})', get_res.text)[0] + '}')
    except:
        raise RuntimeError('未获取到昨日打卡数据，请今日手动打卡明日再执行脚本或使用固定打卡数据')
    post_data = json.loads(copy.deepcopy(INFO).replace("\n", "").replace(" ", ""))
    if is_useold:
        try:
            for k, v in old_data.items():
                if k in post_data:
                    post_data[k] = v
            geo = json.loads(old_data['geo_api_info'])

            province = geo['addressComponent']['province']
            city = geo['addressComponent']['city']
            if geo['addressComponent']['city'].strip() == "" and len(re.findall(r'北京市|上海市|重庆市|天津市', province)) != 0:
                city = geo['addressComponent']['province']
            area = province + " " + city + " " + geo['addressComponent']['district']
            address = geo['formattedAddress']
            post_data['province'] = province
            post_data['city'] = city
            post_data['area'] = area
            post_data['address'] = address

            # 强行覆盖一些字段
            post_data['ismoved'] = 0  # 是否移动了位置？否
            post_data['bztcyy'] = ''  # 不在同城原因？空
            post_data['sfsfbh'] = 0  # 是否省份不合？否
        except:
            print("加载昨日数据错误，采用固定数据")
            post_data = json.loads(copy.deepcopy(INFO).replace("\n", "").replace(" ", ""))
    report_res = session.post(
        REPORT_API,
        data=post_data,
        headers={**COMMON_HEADERS,**COMMON_POST_HEADERS,'Referer': HEADERS.REFERER_POST_API,},
    )
    if report_res.status_code != 200:
        raise RuntimeError('report_res 状态码不是 200')
    return post_data,report_res.text

successs,ress,usernames,names,datas = [],[],[],[],[]
for user in  USERS:
    success=True
    username,password,name,useold=user
    try:
        data,res = ncov_report(username=username,password=password,name=name,is_useold=(useold==0))
    except:
        success = False
        data,res = '',traceback.format_exc()

    print(f'{name}填报成功!服务器返回数据:\n{res}' if success else f'{name}填报失败!发生如下异常:\n{res}')
    # print(f'填报数据:\n{data}\n')

    successs+=[success]
    ress+=[res]
    datas+=[data]
    usernames+=[username]
    names+=[name]

try:
    notifier = ServerJiangNotifier(
        sckey=SERVER_KEY,
        sess=requests.Session()
    )
    print(f'通过「{notifier.PLATFORM_NAME}」给用户发送通知')
    notifier.notify(success=successs, msg=ress,data=datas,username=usernames,name=names)
except:
    print(r"可能由于 「SERVER_KEY未设置」 或 「SERVER_KEY不正确」 或 「网络波动」 ，SERVER酱发送失败")


