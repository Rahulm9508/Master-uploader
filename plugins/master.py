from pyrogram import Client as bot, filters
from config import Config
import shutil
import os
from master import masterdl

@bot.on_message(filters.command("drm"))
async def account_login(bot, m):
    try:
        Credit = Config.CREDIT
        editable = await m.reply_text('__Send 🗂️Master TXT🗂️ file for download__')
        
        # Listen for the document file
        input = await bot.listen(chat_id=m.chat.id, filters=filters.document & filters.user(m.from_user.id))
        
        # Check if the received message contains a document
        if not input.document:
            await editable.edit("Please send a document file.")
            return
        
        path = f"./downloads/{m.chat.id}"
        temp_dir = "./temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        
        # Process the received document file or input
        links, file_name = await masterdl.process_text_file_or_input(input)
        
        await editable.edit(f"Total links🔗 found are __{len(links)}__\n\nSend From where you want to download initial is __1__")
        input0 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text = input0.text
        await input0.delete(True)

        await editable.edit("__Enter Batch Name or send 1 for grabbing from text filename.__")
        input1 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '1':
            b_name = file_name
        else:
            b_name = raw_text0

        await editable.edit("__Enter resolution__\n\nEg - `360` or `480` or `720`")
        input2 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text2 = input2.text
        await input2.delete(True)

        await editable.edit(f"__Enter Your Name\n\nSend 1 for `{Credit}`")
        input3 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text3 = input3.text
        await input3.delete(True)
        if raw_text3 == '1':
            MR = Credit
        else:
            MR = raw_text3

        token = f"eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTU1Mjk2MDUxLCJvcmdJZCI6NzYxOCwib3JnQ29kZSI6ImZtaGNqIiwib3JnTmFtZSI6IklJTSBKYWlwdXIiLCJuYW1lIjoiQW5keVNYIiwiZW1haWwiOiJtYWl0eXN1cHJpeWEwODNAZ21haWwuY29tIiwibW9iaWxlIjoiOTE3NDMwOTQ0ODM5IiwidHlwZSI6MSwiaXNEaXkiOnRydWUsImlzSW50ZXJuYXRpb25hbCI6MCwiZGVmYXVsdExhbmd1YWdlIjoiRU4iLCJjb3VudHJ5Q29kZSI6IklOIiwidGltZXpvbmUiOiJHTVQrNTozMCIsImNvdW50cnlJU08iOiI5MSIsImlzRGl5U3ViYWRtaW4iOjAsImZpbmdlcnByaW50SWQiOiIyZmJmZWI5NzgwZDExM2FjZWMzZjYxZWZjNjRhZTFiYiIsImlhdCI6MTc1MjI0MjczNiwiZXhwIjoxNzUyODQ3NTM2fQ.rrSkUDOjdX7ur3ZntC3m1bZjE8jONVKI4Hf1wiAx2SnwFurVMzVkokwbJJrMRmiq"
        await editable.edit("Now send the __Thumb URL__\n\nor Send `no`")
        input6 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        thumb = input6.text
        await input6.delete(True)
        
        await editable.edit("__Please Provide Channel id to Upload video otherwise `/d` __\n\n__And make me admin in this channel then I can able to Upload otherwise I can't__")
        input7 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        if "/d" in input7.text:
            channel_id = m.chat.id
        else:
            channel_id = input7.text

        await input7.delete()
        try:
            await bot.send_message(chat_id=channel_id, text=f'🎯<blockquote>**Target Batch - {b_name}**</blockquote>')
        except Exception as e:
            await m.reply_text(f"**Please remake a admin in channel..**\n\n**Bot Made By** 🔰『 {Credit} 』🔰")
            channel_id = m.chat.id
        await editable.delete()
        await masterdl.process_links(links, raw_text, raw_text2, token, b_name, MR, channel_id, bot, m, path, thumb, Credit)
    except Exception as e:
        await m.reply_text(f"**⚠️Downloading Failed⚠️**\n\n**Fail Reason »** {e}\n\n**╰────⌈✨❤️ 『{Credit}』 ❤️✨**⌋────╯")
        return
