from abc import ABCMeta, abstractmethod
from typing import Optional
import os


"""
USERS=[("学号","密码","姓名/昵称",0)]
WECOM=("企业ID③", "应用ID①", "应用secret②")
"""
USERS = eval(os.environ['USERS'])
WECOM = eval(os.environ['WECOM'])

LOGIN_API = 'https://auth.bupt.edu.cn/authserver/login'
GET_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'
# 重要: CAS认证的跳转地址记录
SERVICE = 'https://app.bupt.edu.cn/a_bupt/api/sso/cas?redirect=https%3A%2F%2Fapp.bupt.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex&from=wap'
# 模拟浏览器信息
USER_AGENT = 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'
# Execution信息的xpath
EXECUTION_XPATH = '/html/body/div[1]/div/form/div[5]/input[2]/@value'
GETEven_API = 'https://app.bupt.edu.cn/xisuncov/wap/open-report/index'
POSTEven_API = 'https://app.bupt.edu.cn/xisuncov/wap/open-report/save'


# 当今日没有填报时，在https://app.bupt.edu.cn/ncov/wap/default/index下进行填报，
# 全部填完，不要提交，f12打开控制台，在Console页面下输入代码 console.log(vm.info) 就会得到以下信息，之后每天就默认填以下信息
INFO = r"""{
        "address":"北京市海淀区北太平庄街道北京邮电大学计算机学院北京邮电大学海淀校区",
        "area":"北京市  海淀区",
        "bztcyy":"",
        "city":"北京市",
        "csmjry":"0",
        "fjqszgjdq":"",
        "geo_api_info":"{\"type\":\"complete\",\"position\":{\"Q\":39.960390625,\"R\":116.356397569445,\"lng\":116.356398,\"lat\":39.960391},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":23,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"北下关\",\"id\":\"110108\",\"location\":{\"Q\":39.955976,\"R\":116.33873,\"lng\":116.33873,\"lat\":39.955976}},{\"name\":\"西直门\",\"id\":\"110102\",\"location\":{\"Q\":39.942856,\"R\":116.34666099999998,\"lng\":116.346661,\"lat\":39.942856}},{\"name\":\"小西天\",\"id\":\"110108\",\"location\":{\"Q\":39.957147,\"R\":116.364058,\"lng\":116.364058,\"lat\":39.957147}}],\"neighborhoodType\":\"科教文化服务;学校;高等院校\",\"neighborhood\":\"北京邮电大学\",\"building\":\"北京邮电大学计算机学院\",\"buildingType\":\"科教文化服务;学校;高等院校\",\"street\":\"西土城路\",\"streetNumber\":\"10号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"township\":\"北太平庄街道\"},\"formattedAddress\":\"北京市海淀区北太平庄街道北京邮电大学计算机学院北京邮电大学海淀校区\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}",
        "glksrq":"",
        "gllx":"",
        "gtjzzchdfh":"",
        "gtjzzfjsj":"",
        "ismoved":"0",
        "jcbhlx":"",
        "jcbhrq":"",
        "jchbryfs":"",
        "jcjgqr":"0",
        "jcwhryfs":"",
        "jhfjhbcc":"",
        "jhfjjtgj":"",
        "jhfjrq":"",
        "mjry":"0",
        "province":"北京市",
        "qksm":"",
        "remark":"",
        "sfcxtz":"0",
        "sfcxzysx":"0",
        "sfcyglq":"0",
        "sfjcbh":"0",
        "sfjchbry":"0",
        "sfjcwhry":"0",
        "sfjzdezxgym":"1",
        "sfjzxgym":"1",
        "sfsfbh":"0",
        "sftjhb":"0",
        "sftjwh":"0",
        "sfxk":"0",
        "sfygtjzzfj":"",
        "sfyyjc":"0",
        "sfzx":1,
        "szcs":"",
        "szgj":"",
        "szsqsfybl":"0",
        "tw":"2",
        "xjzd":"",
        "xkqq":"",
        "xwxgymjzqk":"3",
        "ymjzxgqk":"已接种",
        "zgfxdq":"0"
        }"""

INFO_E = r"""{
    "sfzx": "0",
    "tw":"1",
    "area":"北京市  海淀区",
    "city":"北京市",
    "province":"北京市",
    "address":"北京市海淀区北太平庄街道北京邮电大学计算机学院北京邮电大学海淀校区",
    "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"fEa\":\"jsonp_940261_\",\"position\":{\"Q\":39.960,\"R\":116.35640,\"lng\":116.356340,\"lat\":39.960},\"message\":\"Get geolocation time out.Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"100876\",\"businessAreas\":[],\"neighborhoodType\":\"科教文化服务;学校;高等院校\",\"neighborhood\":\"北京邮电大学\",\"building\":\"北京邮电大学计算机学院\",\"buildingType\":\"科教文化服务;学校;高等院校\",\"street\":\"西土城路\",\"streetNumber\":\"10号\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"towncode\":\"\",\"township\":\"北太平庄街道\"},\"formattedAddress\":\"北京市海淀区北太平庄街道北京邮电大学计算机学院北京邮电大学海淀校区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
    "sfcyglq": "0",
    "sfyzz": "0","qtqk": "","askforleave": "0"
    }"""


REASONABLE_LENGTH = 24
TIMEOUT_SECOND = 25


class HEADERS:
    REFERER_LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login'
    REFERER_POST_API = 'https://app.bupt.edu.cn/ncov/wap/default/index'
    ORIGIN_BUPTAPP = 'https://app.bupt.edu.cn'

    UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
          'Mobile/15E148 MicroMessenger/7.0.11(0x17000b21) NetType/4G Language/zh_CN')
    ACCEPT_JSON = 'application/json'
    ACCEPT_HTML = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    REQUEST_WITH_XHR = 'XMLHttpRequest'
    ACCEPT_LANG = 'zh-cn'
    CONTENT_TYPE_UTF8 = 'application/x-www-form-urlencoded; charset=UTF-8'

    def __init__(self) -> None:
        raise NotImplementedError


COMMON_HEADERS = {
    'User-Agent': HEADERS.UA,
    'Accept-Language': HEADERS.ACCEPT_LANG,
}
COMMON_POST_HEADERS = {
    'Accept': HEADERS.ACCEPT_JSON,
    'Origin': HEADERS.ORIGIN_BUPTAPP,
    'X-Requested-With': HEADERS.REQUEST_WITH_XHR,
    'Content-Type': HEADERS.CONTENT_TYPE_UTF8,
}