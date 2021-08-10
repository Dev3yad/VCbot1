from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from YuiHirasawaMusicBot.helpers.decorators import authorized_users_only
from YuiHirasawaMusicBot.helpers.decorators import errors
from YuiHirasawaMusicBot.services.callsmusic import client as USER
from YuiHirasawaMusicBot.config import SUDO_USERS

@Client.on_message(filters.command(["انضم"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني كمسؤول في مجموعتك أولاً</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "انضممت هنا كما طلبت")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>الحساب المساعد بالفعل في الدردشة الخاصة بك</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطأ كثره الطلبات 🛑 \n المستخدم {user.first_name} تعذر الانضمام إلى مجموعتك بسبب كثرة طلبات الانضمام للمستخدم تأكد من عدم حظر المستخدم في المجموعة."
            "\n\nأو أضف يدويًا @Rengoku_Kyujoro_Helper إلى مجموعتك وحاول مرة أخرى</b>",
        )
        return
    await message.reply_text(
        "<b>انضم الحساب المساعد إلى محادثتك</b>",
    )


@USER.on_message(filters.group & filters.command(["غادر"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>لا يمكن للمستخدم مغادرة مجموعتك! قد يكون بسبب الضغط."
            "\n\nأو اطردني يدويًا من مجموعتك</b>",
        )
        return
    
@Client.on_message(filters.command(["مغادره"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("مساعد مغادرة جميع الدردشات")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"ترك المساعد... متبقى: {left} الدردشات. باءت بالفشل: {failed} الدردشات.")
            except:
                failed=failed+1
                await lol.edit(f"ترك المساعد... متبقى: {left} الدردشات. باءت بالفشل: {failed} الدردشات.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("لم يتم ربط القناه")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني كمشرف في قناتك أولاً</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Rengoku_Kyujoro_Helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "انضممت هنا كما طلبت")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>الحساب المساعد بالفعل في الدردشة الخاصة بك</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطأ كثره الطلبات 🛑 \n المستخدم {user.first_name} تعذر الانضمام إلى قناتك بسبب كثرة طلبات الانضمام علي الحساب المساعد او تأكد من عدم حظر المستخدم في القناة."
            "\n\nأو أضف يدويًا @Rengoku_Kyujoro_Helper إلى مجموعتك وحاول مرة أخرى</b>",
        )
        return
    await message.reply_text(
        "<b>انضم الحساب المساعد إلى قناتك</b>",
    )
    
