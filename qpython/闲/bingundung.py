�ҵ��ֻ� 2022/2/9 12:31:55
import random

import re
from qqbot import QQBotSlot as qqbotslot, RunBot

from dictList import dictList


@qqbotslot
def onQQMessage(bot, contact, member, content):
    res_url = '[^.*?[]]'
    link = re.findall(res_url, str(content), re.I | re.S | re.M)
    res_url2 = '/Emoji.*?'
    link2 = re.findall(res_url2, str(content), re.I | re.S | re.M)
    print('*****',link)
    if 'hello' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["niHao"])))
    elif '��' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["zai"])))
    elif '���' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["niHao"])))
    elif '��' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["a"])))
    elif '��' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["en"])))
    elif 'Ŷ' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif 'û��' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["everyThing"])))
    elif '/����' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["everyThing"])))
    elif '/����' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["baiYan"])))
    elif 'ʲô' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["shenMe"])))
    elif 'ȷ' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["everyThing"])))
    elif '�ݰ�' in str(content):
        bot.SendTo(contact, '��ȷ��Ҫ����˵�ټ�����')
    elif len(link):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '/͵Ц' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '..' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '������' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif len(link2):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '��' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    #�������ַ���ֹͣ����
    elif '++' in content:
        bot.SendTo(contact, '��������')
        bot.Stop()


if __name__ == '__main__':
    RunBot()
