<h2 align="center">:helicopter:北邮疫情自动填报（Python+Github Actions）长期维护</h2>
<p align="center">
    <a href="https://github.com/zzp-seeker/bupt-ncov-auto-report/actions/workflows/main.yml">
        <img src="https://github.com/zzp-seeker/bupt-ncov-auto-report/actions/workflows/main.yml/badge.svg?branch=master" alt="Action Badge">
    </a>
    <img src="https://img.shields.io/badge/python-%3d%203.7-blue" alt="Python Version">
</p>



## 特点：

- 每天7-8点自动多次填报（可通过main.yml修改）
- 运行失败会自动往邮箱（注册github所用邮箱）发送邮件
- 可以多人同时填报（可以帮小伙伴一起打卡哦）
- 填报情况可以使用上一次打卡数据（如需更换请于当日脚本运行前手动打卡），也可以使用固定数据（地点始终位于北邮）
- **（可选）** 填报结果通过Server酱推送至微信
  ​

<div align="center">
<img src='img/0.png' width=55%/>
</div>




## 使用详解

1. 点击右上角的 **Use this template** <img src="img/2.png" width="50%">然后给仓库随便起一个名字，点击 **Create repository from template**
2. 点击 **Settings** ，进入 **Secrets** 页面，点击右上角的 **New repository secret**，流程如下图所示
<div align="center">
<img src="img/3.png" width="90%">
</div>

3. 一共有**两**个secret，第一个Name填**USERS**，Value按照如下格式填写：

```python
[
    (学号:str,密码:str,用户名:str,0 or 1),
    (学号:str,密码:str,用户名:str,0 or 1),
    (学号:str,密码:str,用户名:str,0 or 1),
    ... 如果还有则继续往后面加
]
```

相当于**列表**里面有很多**元组**，每个元组代表一个用户，可以有任意多个。每个元组有**四个元素**，前两个分别为**学号**和**密码**，字符串格式（可自行通过 [https://app.bupt.edu.cn/ncov/wap/default/index](https://app.bupt.edu.cn/ncov/wap/default/index) 登陆验证账号密码正确性，密码一般为身份证后8位），第三个为**用户名**（随便填，用于控制台与Server显示），第四个为是否用上一次打卡数据，**0或者1**，0代表使用上一次打卡数据（**某一次自己在脚本运行前打卡之后都采用这次打卡数据**），1代表使用固定数据（固定数据的地点始终位于北邮）。该USERS在代码中会以python的eval(USERS)执行，故USERS符合python语法即可。以下是一个样例：

<div align="center">
	<img src="img/4.png" width="55%">
</div>


4. 第二个secret的Name填写**SERVER_KEY**，如果不配置Server酱微信推送，那么Value里填写**0**即可，如果想配置的话看下一点
5. **（可选）** Value填写Server酱的SendKey（在这里查看 [https://sct.ftqq.com/sendkey](https://sct.ftqq.com/sendkey)），在此之前需要微信注册企业号，并加入Server酱内部应用，具体流程见 [https://sct.ftqq.com/forward](https://sct.ftqq.com/forward)，看起来比较多，但也不是很麻烦，一步步照做即可

最后Actions secrets效果：

<div align="center">
<img src="img/5.png" width="100%">
</div>

6. 点击上方**Actions**按钮：

<img src="img/6.png" width="100%">

点击左侧的**BUPT ncov auto-report Python**,再点击右侧的**Run workflow**,如下图所示：

<div align="center">
<img src="img/7.png" width="100%">
</div>

点击这个workflow（没看到的话请刷新一下），然后再次点进去jobs查看执行情况

<div align="center">
<img src="img/8.png" >
</div>

7. 如果准确按照上述步骤执行，你应该会看到类似的如下输出：

<div align="center">
<img src="img/9.png" width="95%">
</div>

若想查看上图一样具体填报信息需要取消注释main.py的75行

**恭喜你，你还有你的小伙伴不用为被催打卡而烦恼了~**


## 参数更改：
### 更改每日打卡时间
在 .github/workflows/main.yml 中来设置每天运行的时间：
```python
on:
  schedule:
    - cron: "*/20 16,23 * * *"
```
cron里的"\*/20 16,23 * * \*"代表 at every 20th minute past hour 16 and 23，然而这是UTC，北京时间为UTC+8，代表0点与7点之后每隔20分钟
[https://crontab.guru/#*/10_16,23_*_*_*](https://crontab.guru/#*/10_16,23_*_*_*) 用这个网站来选取你想要的时间
### 更改打卡的固定数据
在 [https://app.bupt.edu.cn/ncov/wap/default/index](https://app.bupt.edu.cn/ncov/wap/default/index) 进行填报，全部填完后最后不要提交，f12打开控制台，在Console页面下输入代码vm.info回车得到填报数据，替换掉 constant.py 里的INFO变量


## Credit
参考了[ipid/bupt-ncov-report](https://github.com/ipid/bupt-ncov-report) 与 [imtsuki/bupt-ncov-report-action](https://github.com/imtsuki/bupt-ncov-report-action), 十分感谢

## License
MIT © [zzp-seeker](https://github.com/zzp-seeker)

### 好用的话别忘了:star:哦 :wink:


