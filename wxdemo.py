#!/usr/bin/python3
# _*_ coding: utf-8 _*_
import re
import sys
import itchat
from threading import Timer
from datetime import datetime

# 验证好友信息正则，关键词中有Python，Py和加群的关键字就可以了
add_friend_compile = re.compile(r'Python|Py|加群|进群')
# 获取用户昵称的正则的
nickname_compile = re.compile(r'NickName\':\'(.*)\'', re.S)


def run():
    """ 主程序入口"""

    # 判断当前环境是否为 python 3
    if sys.version_info[0] == 2:
        print('此项目不支持 Python 2 版本！')
        return

    # 检查依赖库是否都已经安装上
    try:
        import itchat
        import apscheduler

        if itchat.__version__ != '1.3.10':
            print('当前 itchat 版本为：{} ，本项目需要 itchat 的版本为 1.3.10。请升级至最新版本！\n'
                  '升级方法 1：pip install itchat --upgrade \n'
                  '或者方法 2: pip install -U itchat'.format(itchat.__version__))
            return

    except (ModuleNotFoundError, ImportError) as error:
        if isinstance(error, ModuleNotFoundError):
            no_modules = re.findall(r"named '(.*?)'$", str(error))
            if no_modules:
                print('当前运行环境缺少 {} 库'.format(no_modules[0]))
            print(str(error))
        elif isinstance(error, ImportError):
            print('当前运行环境引入库出错')
            print(str(error))
        return

    _date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('当前时间：{}'.format(_date))

    itchat.auto_login(hotReload=True)
    itchat.run()
    loop_send()



def getUserName(usName):
    #get firend
    friends = itchat.get_friends()
    for texts in friends:
        # print(texts)
        if texts['NickName'] == usName:
            return texts['UserName']
    return ''


def getNickName(usName):
    #get firend
    friends = itchat.get_friends()
    for texts in friends:
        # print(texts)
        if texts['UserName'] == usName:
            return texts['NickName']
    return ''


def appMenber(UserName):
    itchat.add_member_into_chatroom(get_group_id('富金通App团队'),[{'UserName': UserName}], useInvitation=True)
    # print(aooduserroom)

# 获得群聊id
def get_group_id(group_name):
    group_list = itchat.search_chatrooms(name=group_name)
    # print(group_list)
    return group_list[0]['UserName']


# 获得群聊NickName
def get_group_name(UseName):

    try:
        group_list = itchat.search_chatrooms(userName=UseName)
        # print(group_list)
        return group_list['NickName']
    except Exception:
        return ''

# 自动通过加好友
@itchat.msg_register(itchat.content.FRIENDS)
def deal_with_friend(msg):
    if add_friend_compile.search(msg['Content']) is not None:
        itchat.add_friend(**msg['Text'])  # 自动将新好友的消息录入，不需要重载通讯录
        itchat.send_msg('回复关键字:\n 加群，进群, Python\n 来继续我们的故事！',msg['RecommendInfo']['UserName'])

# 每个半个小时发依次信息貌似能防止掉线
def loop_send():
    global count
    itchat.send('大扎好，我系轱天乐，我四渣嘎辉，探挽懒月，介四里没有挽过的船新版本，挤需体验三番钟，里造会干我一样，爱像借款游戏。'
                , toUserName='filehelper')
    count += 1
    if count < 10000:
        Timer(1800, loop_send).start()


@itchat.msg_register(itchat.content.TEXT,isFriendChat = True)
def text_reply(msg):
    text = msg['Content']
    if '加群' in text :
        appMenber( msg['FromUserName'])
    elif '进群' in text:
        appMenber(msg['FromUserName'])
    elif 'Python' in text:
        appMenber(msg['FromUserName'])
    elif 'python' in text:
        appMenber(msg['FromUserName'])
    else:
        pass

    userName = msg['FromUserName']
    print('{}:{}'.format(getNickName(userName),text))



# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#
#     return '自动回复：你好，主人不在请留言'


@itchat.msg_register(itchat.content.TEXT,isGroupChat = True)
def group_text(msg):

    fromUserName = msg['FromUserName']
    group_name = get_group_name(fromUserName)
    person_nickName = msg['ActualNickName']
    text = msg['Content']

    print('微信群:{}'.format(group_name))
    print('{}:{}'.format(person_nickName,text))


if __name__ == '__main__':

    run()