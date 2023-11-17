import python    
import time 

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
    
    
HELP_STRINGS = """
🎛 *Here you can get all of the Help Commands!*

 ❍ /help: PM's you this message.
 ❍ /help <module name>: PM's you info about that module.
 ❍ /donate: information on how to donate!
 ❍ /settings:
  in PM: will send you your settings for all supported modules.
  in a group: will redirect you to pm, with all that chat's settings.
 
All commands can either be used with / or !.
And the following:
"""



Start = """ 
I am Bots develpoders 
Made By shanks
"""


@Bot.on_message(filters.command('start') & filters.private)
reply(client: Client, message: Message):
print(Start)

@Bot.on_message(filters.command('help') & filters.private)
reply(client: Client, message: Message):
print(HELP_STRINGS)

    if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    main()
