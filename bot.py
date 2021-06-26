# import the module
from discord.ext import commands
from prsaw import RandomStuff
bot= commands.Bot(command_prefix=">")
# initiate the object
api_key = "wGAZFfRDxERY"
rs= RandomStuff(async_mode=True, api_key= api_key)

@bot.event
# get a response from an endpoint
async def on_message(message):
      if message.author == bot.user:
           return
      if message.channel.id==798556779892965376 or message.channel.id==855841358735867904:
          async with message.channel.typing():
              #try:
                  ######msg = message.content
                 ##### if message.mentions != []:
                   ####   for i in message.mentions:
                  ###        msg = msg.replace(f'<@!{i.id}>', i.name)

                ##  response = await rs.get_ai_response(msg)
           #   except json.decoder.JSONDecodeError:
                #  await asyncio.sleep(3)
               #   response = await rs.get_ai_response(msg)

         # await message.reply("**"+response[0]["message"]+"**")
TOKEN ="NzgxOTAyMjc1NDcxNDc0NzE5.X8EZPQ.EZ1W2nAIG7TAK9Ch-vc6C3Y7vqs"
bot.run(TOKEN)
# while True:
#   user_input=input("< ")
#   response = rs.get_ai_response(user_input)
#   print(response)
#
# # close the object once done (recommended)
# rs.close()
