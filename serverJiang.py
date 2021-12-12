import time
import requests,datetime

from constant import *


class ServerJiangNotifier(INotifier):
    PLATFORM_NAME = 'Server 酱'

    def __init__(self, *, sckey: str, sess: requests.Session):
        self._sckey = sckey
        self._sess = sess

    def notify(self, *, success, msg, data, username, name) -> None:
        """发送消息。"""
        title_suc,title_eor,bodys=[],[],[]
        title_suc_str,title_eor_str,body_str='','',''

        for i in range(len(USERS)):
            if success[i]:
                title_suc += [f'{name[i]}']
                if msg[i] is not None:
                    body = f'\n学号{username[i]},{name[i]} 填报成功, 服务器的返回是:\n{msg[i]}\n 填报数据:\n{data[i]}\n'
                else:
                    body = '成功'
            else:
                title_eor += [f'{name[i]}']
                if msg[i] is not None:
                    body = f'学号{username[i]} 填报失败：产生如下异常：\n{msg[i]}\n 填报数据:\n{data[i]}\n'
                else:
                    body = '失败'
            bodys+=[body]
        
        for i in range(len(title_suc)):
            title_suc_str+=title_suc[i]
            if i!= len(title_suc)-1:
                title_suc_str+='、'
            else:
                title_suc_str+="填报成功!"

        if len(title_eor)==0:
            title_suc_str="所有填报成功"

        for i in range(len(title_eor)):
            title_eor_str+=title_eor[i]
            if i!= len(title_eor)-1:
                title_eor_str+='、'
            else:
                title_eor_str+="填报失败!"

        for i in range(len(bodys)):
            body_str+=bodys[i]
        
        # Server 不允许短时间重复发送相同内容，故加上时间
        time_str = str(int(time.time()))[-3:]


        # 调用 Server 酱接口发送消息
        sc_res_raw = self._sess.post(
            f'https://sctapi.ftqq.com/{self._sckey}.send',
            data={
                'title': f'{datetime.date.today()}:{title_suc_str}{title_eor_str}',
                'desp': f'{body_str}\n{time_str}',
            },
            timeout=TIMEOUT_SECOND,
        )

