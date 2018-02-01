import re
import requests
import random
import time
import asyncio
import discord
from discord.ext import commands
import quadrabot_config

bot_token = quadrabot_config.TOKEN_DISCORD_DEFQUAD
bot = commands.Bot(description="거점을 지키는데 내가 도와줄거야!", command_prefix="!")
timer_elep = [600,"코끼리"]
timer_flag = [1800,"축퇴"]

def change_size(time):
	temp = time
	hour = temp // 3600
	temp -= hour * 3600
	min = temp // 60
	temp -= min * 60
	sec = temp
	return [int(hour),int(min),int(sec)]

def log_append(_chat_id, _text, _type, _subtype):
	global bot
	_now = time.localtime()
	if _subtype!=0 : what_type = _type +'_' +_subtype
	else : what_type = _type
	target = "[%04d-%02d-%02d %02d:%02d:%02d] trgd [%10s] from [%20s] : %s" % (_now.tm_year, _now.tm_mon, _now.tm_mday, _now.tm_hour, _now.tm_min, _now.tm_sec, what_type,str(_chat_id),_text)
	fp = open("def_quadra_bot_log.txt", 'a')
	print(target)
	fp.write(target+"\n")
	fp.close()
	return _now

@bot.command(pass_context=True)
async def ping(ctx):
	"""for debugging"""
	now = log_append(str(ctx.message.server.id), str(ctx.message.server.name), 'ping',0)
	await bot.say("Pong!")
	await bot.say("나 안자고 있어! 걱정마!")

@bot.command(pass_context=True)
@commands.cooldown(rate=1, per=int(timer_elep[0]*0.9), type=commands.BucketType.server)
async def 코끼리(ctx):
	"""for debugging"""
	timer = timer_elep[0]
	name = timer_elep[1]
	now = log_append(str(ctx.message.server.id), str(ctx.message.server.name)+" called "+name+" "+str(timer), 'elph',0)
	await bot.say("[ "+name+" ] 알람 "+str(timer)+"초 시작!")
	current_time = timer
	sum = 0
	time_check = [timer*0.25,timer*0.5,timer*0.75,timer*0.85,timer*0.9,timer*0.95,timer]
	time_name = ["25%","50%","75%","85%","90%","95%","100%"]
	for i in range(0,len(time_check),1):
		time_check[i] -= sum
		sum += time_check[i]
	for i in range(0,len(time_check),1):
		sum -= time_check[i]
		await asyncio.sleep(time_check[i])
		if time_name[i] == "100%":
			now = log_append(str(ctx.message.server.id), str(ctx.message.server.name)+" called "+name+" "+time_name[i], 'system',0)
			em = discord.Embed(title=name+" 완성!!",description="코끼리가 완성되었어!", colour=discord.Colour.blue())
			em.set_image(url="https://i.imgur.com/71zsypQ.png")
			await bot.say("[ "+name+" ] 가 완성되었어!",embed=em)
		else :
			now = log_append(str(ctx.message.server.id), str(ctx.message.server.name)+" called "+name+" "+time_name[i]+" "+str(sum), 'system',0)
			temp_time = change_size(sum)
			if temp_time[0] > 0:
				if temp_time[1] > 0: 
					if temp_time[2] > 0: await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 "+str(temp_time[1])+"분 "+str(temp_time[2])+"초 남았어!")
					else : await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 "+str(temp_time[1])+"분 남았어!")
				else:
					if temp_time[2] > 0: await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 "+str(temp_time[2])+"초 남았어!")
					else : await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 남았어!")
			else:
				if temp_time[1] > 0: 
					if temp_time[2] > 0: await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[1])+"분 "+str(temp_time[2])+"초 남았어!")
					else : await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[1])+"분 남았어!")
				else:
					await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[2])+"초 남았어!")

@bot.command(pass_context=True, aliases=["깃발"])
@commands.cooldown(rate=1, per=int(timer_flag[0]*0.9), type=commands.BucketType.server)
async def 축퇴(ctx):
	"""for debugging"""
	timer = timer_flag[0]
	name = timer_flag[1]
	now = log_append(str(ctx.message.server.id), str(ctx.message.server.name)+" called "+name+" "+str(timer), 'flag',0)
	await bot.say("[ "+name+" ] 알람 "+str(timer)+"초 시작!")
	current_time = timer
	sum = 0
	time_check = [timer*0.25,timer*0.5,timer*0.75,timer*0.85,timer*0.9,timer*0.95,timer]
	time_name = ["25%","50%","75%","85%","90%","95%","100%"]
	for i in range(0,len(time_check),1):
		time_check[i] -= sum
		sum += time_check[i]
	for i in range(0,len(time_check),1):
		sum -= time_check[i]
		await asyncio.sleep(time_check[i])
		if time_name[i] == "100%":
			now = log_append(str(ctx.message.server.id), str(ctx.message.server.name)+" called "+name+" "+time_name[i], 'system',0)
			em = discord.Embed(title=name+" 완성!!",description="코끼리가 완성되었어!", colour=discord.Colour.blue())
			em.set_image(url="https://i.imgur.com/71zsypQ.png")
			await bot.say("[ "+name+" ] 가 완성되었어!",embed=em)
		else :
			now = log_append(str(ctx.message.server.id), str(ctx.message.server.name)+" called "+name+" "+time_name[i]+" "+str(sum), 'system',0)
			temp_time = change_size(sum)
			if temp_time[0] > 0:
				if temp_time[1] > 0: 
					if temp_time[2] > 0: await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 "+str(temp_time[1])+"분 "+str(temp_time[2])+"초 남았어!")
					else : await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 "+str(temp_time[1])+"분 남았어!")
				else:
					if temp_time[2] > 0: await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 "+str(temp_time[2])+"초 남았어!")
					else : await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[0])+"시간 남았어!")
			else:
				if temp_time[1] > 0: 
					if temp_time[2] > 0: await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[1])+"분 "+str(temp_time[2])+"초 남았어!")
					else : await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[1])+"분 남았어!")
				else:
					await bot.say("[ "+name+" ] 가 "+time_name[i]+" 만큼 완성되었어. 앞으로 "+str(temp_time[2])+"초 남았어!")

@bot.event
async def on_ready():
	now = log_append('system', 'Bot running Start', 'system',0)
	
bot.run(bot_token)