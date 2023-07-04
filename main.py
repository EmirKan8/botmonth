from aiogram import executor
import logging
from config import dp, bot, admins
from handlers import commands, callback, extra, admin, fsm_mentor, apsheduler
import dicegame
from sql_tablet.bot_dp import sql_create


async def on_startup(_):
    await apsheduler.set_scheduler()
    await bot.send_message(chat_id=admins[0], text='Bot started!')
    sql_create()


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
dicegame.register_handlers_1commands(dp)
fsm_mentor.register_handlers_fsm_mentor(dp)

# extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
