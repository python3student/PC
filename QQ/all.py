# -*- coding: UTF-8 -*-
from send_msg import send_msg
from get_group import get_group

resp_dict1 = {'msg_type': 'private', 'number': 2207082899,
              'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" '
                     'templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=HpooctxyP4208KfcB7tU7YfQw_Xc4D1q" '
                     'flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio '
                     'cover="https://qlogo4.store.qq.com/qzone/2207082899/2207082899/100?1651840987" '
                     'src="http://music.163.com/song/media/outer/url?id=1901371647" '
                     '/><title>孤勇者</title><summary>『作者』胡岩</summary></item><source name="胡岩永远的神！" '
                     'icon="https://qlogo4.store.qq.com/qzone/2207082899/2207082899/100?1651840987" '
                     'url="https://qlogo4.store.qq.com/qzone/2207082899/2207082899/100?1651840987" action="app" '
                     'a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" '
                     '/></msg>,resid=60]'}

resp_dict = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:at,qq=1692851288]'}
resp_dict2 = {'msg_type': 'group', 'number': 1143107466,
              'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" '
                     'templateID="1" action="web" brief="" sourceMsgId="0" url="https://python3student.github.io/" '
                     'flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio '
                     'cover="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703" '
                     'src="http://music.163.com/song/media/outer/url?id=31365604" '
                     '/><title>你从未离去</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" '
                     'icon="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703" '
                     'url="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703ttps://python3student.github.io/img/avatar.jpg" action="app" '
                     'a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" '
                     '/></msg>,resid=60]'}
resp_dict3 = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:tts,text=谢军敏这是一条测试消息]'}
resp_dict4 = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:tts,text=谢军敏这是一条测试消息]'}
liwu = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:gift,qq=1642883508,id=2]'}
card = {'msg_type': 'private', 'number': 1679194340,
        'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="https://i.y.qq.com/v8/playsong.html?_wv=1&amp;songid=4830342&amp;souce=qqshare&amp;source=qqshare&amp;ADTAG=qqshare" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="http://imgcache.qq.com/music/photo/album_500/26/500_albumpic_89526_0.jpg" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>十年</title><summary>陈奕迅</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>]'}
music = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:music,type=163,id=28949129]'}
j = {'msg_type': 'private', 'number': 1679194340,
     'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<msg serviceID="1">'
            '<item layout="4">'
            '<title>神奇666</title>'
            '<picture cover="https://python3student.github.io/img/top.jpg"/>'
            '</item>'
            '</msg>]'}
q = {'msg_type': 'private', 'number': 1679194340,
     'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<msg serviceID="1">'
            '<item><title>生死8秒！女司机高速急刹, 他一个操作救下一车性命</title></item>'
            '<source name="官方认证消息" icon="https://python3student.github.io/img/top.jpg" action="" appid="-1" />'
            '</msg>'}
ban = {'msg_type': 'group', 'number': 1143107466,
       'msg': '[CQ:record,file=https://music.163.com/song/media/outer/url?id=28613172.mp3]'}
face = {'msg_type': 'private', 'number': 3225685814, 'msg': '[CQ:face,id={}]'}

json_msg = '[CQ:json,data={"app":"com.tencent.miniapp_01"&#44;"config":{"autoSize":0&#44;"ctime":1652082785&#44;"forward":1&#44;"height":0&#44;"token":"b4c065b52082a74bea5f8a77e72db43b"&#44;"type":"normal"&#44;"width":0}&#44;"desc":"哔哩哔哩"&#44;"extra":{"app_type":1&#44;"appid":100951776&#44;"uin":1642883508}&#44;"meta":{"detail_1":{"appType":0&#44;"appid":"1109937557"&#44;"desc":"手冲 VS 器冲"&#44;"gamePoints":""&#44;"gamePointsUrl":""&#44;"host":{"nick":"pToTq"&#44;"uin":1642883508}&#44;"icon":"http://miniapp.gtimg.cn/public/appicon/432b76be3a548fc128acaa6c1ec90131_200.jpg"&#44;"preview":"pubminishare-30161.picsz.qpic.cn/c332dbdc-0b82-4243-86fe-1c7fb046dee7"&#44;"qqdocurl":"https://qm.qq.com/cgi-bin/qm/qr?k=HpooctxyP4208KfcB7tU7YfQw_Xc4D1q"&#44;"scene":1036&#44;"shareTemplateData":{}&#44;"shareTemplateId":"8C8E89B49BE609866298ADDFF2DBABA4"&#44;"showLittleTail":""&#44;"title":"哔哩哔哩"&#44;"url":"m.q.qq.com/a/s/ea0700e588015fc8b87633156c4ba9fb"}}&#44;"needShareCallBack":false&#44;"prompt":"&#91;QQ小程序&#93;哔哩哔哩"&#44;"ver":"1.0.0.19"&#44;"view":"view_8C8E89B49BE609866298ADDFF2DBABA4"}]'
# https://music.163.com/song/media/outer/url?id=28613172.mp3
# send_msg(resp_dict3)
# send_msg(resp_dict2)
# for i in range(5):
#     send_msg(resp_dict)
# get_group(543303513)
# send_msg(card)
# for i in range(400):
#     face['msg'] = face['msg'].format(i)
#     send_msg(face)
#     face = {'msg_type': 'private', 'number': 3225685814, 'msg': '[CQ:face,id={}]'}
# send_msg(ban)
# send_msg(resp_dict1)
send_msg( {'msg_type': 'group', 'number': 1143107466,
       'msg': json_msg})