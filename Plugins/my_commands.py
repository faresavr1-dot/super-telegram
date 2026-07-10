# ملف: Plugins/my_commands.py

from pyrogram import Client, filters
from config import *
import re

@Client.on_message(filters.text & filters.group)
async def my_commands(c, m):
    text = m.text
    
    # البحث عن كلمة "هاي" في أي مكان بالجملة
    if re.search(r'\bهاي\b', text):
        await m.reply("مسوي فيها اجنبي؟🦦")
        return
    
    # البحث عن كلمة "حلو" في أي مكان بالجملة
    if re.search(r'\bحلو\b', text):
        await m.reply("احسن منك 🦦.")
        return
    
    # البحث عن كلمة "لا" في أي مكان بالجملة
    if re.search(r'\bلا\b', text):
        await m.reply("تمزح!")
        return
    
    # البحث عن كلمة "أها" في أي مكان بالجملة (الأمر الجديد)
    if re.search(r'\bاها\b', text):
        await m.reply("مسوي فيها فهمت🦦")
        return