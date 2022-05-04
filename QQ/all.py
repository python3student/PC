# -*- coding: UTF-8 -*-
from send_msg import send_msg
from get_group import get_group

resp_dict1 = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://python3student.github.io/" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="http://music.163.com/song/media/outer/url?id=31365604" /><title>你从未离去</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]'}

resp_dict = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:at,qq=1692851288]'}
resp_dict2 = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://python3student.github.io/" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="http://music.163.com/song/media/outer/url?id=31365604" /><title>你从未离去</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]'}
resp_dict3 = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:tts,text=谢军敏这是一条测试消息]'}
liwu = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:gift,qq=1642883508,id=2]'}
card = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="https://i.y.qq.com/v8/playsong.html?_wv=1&amp;songid=4830342&amp;souce=qqshare&amp;source=qqshare&amp;ADTAG=qqshare" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="http://imgcache.qq.com/music/photo/album_500/26/500_albumpic_89526_0.jpg" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>十年</title><summary>陈奕迅</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>]'}
music = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:music,type=163,id=28949129]'}


# send_msg(resp_dict3)
# send_msg(resp_dict2)
# for i in range(5):
#     send_msg(resp_dict)
# get_group(543303513)
# send_msg(card)
send_msg(music)