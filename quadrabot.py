import re
import requests
import telegram
import random
import time
import os
import glob
from telegram.ext import Updater, RegexHandler, CommandHandler
from urllib import parse
import quadra_search_list
import quadra_search_vocab
import quadra_dialog_list
import quadra_game_list
import quadrabot_config
import quadra_baseball
import quadra_lifetime
import quadra_love
import quadra_updown

my_token = quadrabot_config.TOKEN_TELEGRAM
updater = Updater(my_token)

def onGame(user_id):
	if quadra_baseball.enable(user_id) : return "야구게임을"
	if quadra_updown.enable(user_id) : return "업다운을"
	else : return ""

def log_append(_chat_id, _text, _type, _subtype):
	_now = time.localtime()
	if _subtype!=0 : what_type = _type +'_' +_subtype
	else : what_type = _type
	target = "[%04d-%02d-%02d %02d:%02d:%02d] trgd [%10s] from [%15s] : %s" % (_now.tm_year, _now.tm_mon, _now.tm_mday, _now.tm_hour, _now.tm_min, _now.tm_sec, what_type,str(_chat_id),_text)	
	fp = open("log/quadra_bot_log.txt", 'a')
	if os.path.getsize("log/quadra_bot_log.txt") >= 102400:
		fp.close()
		filelist = glob.glob("log/*.*")
		filenum = len(filelist)
		filename = "log/quadra_bot_log_"+str(filenum)+".txt"
		os.rename("log/quadra_bot_log.txt",filename)
		fp = open("log/quadra_bot_log.txt", 'a')
	print(target)
	fp.write(target+"\n")
	fp.close()
	return _now

def url_encode(data):
	return (parse.quote(data).replace('/', '%2F'))
	
def version(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "help",0)
	update.message.reply_text(
		"반가워! 나는 사잽이라고해! 지금은 0.1.1 버전이야! \n나는 이런것들을 할 수 있어!\n * 쫑긋\n * 사잽아 ~~ 찾아줘/알려줘\n   * 지원 엔진 : 구글, 네이버, 나무위키, 리브레위키, 위키백과, 구스위키, 진보위키, 백괴사전\n * 사잽아 ~ 해줘/하자/어때/사줘\n * 사잽아 (게임이름) 하자\n   * 지원 게임 : 야구게임, 업다운\n * 사잽아 나 어때")
	quadra_love.process(update.message.from_user.id,1,0)

def lifetime(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "lifetime",0)
	text = quadra_lifetime.checkSwitch(now)
	update.message.reply_text(text)
	quadra_love.process(update.message.from_user.id,0,0)

def dialog_how(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_how",0)
	target = re.search('^사잽아 ((?:(?! 어때).)*) 어때(\?)?', str(update.message.text))
	target = target.groups()
	
	if target[0] == "나":
		data = quadra_love.check(update.message.from_user.id)
		userpri = str(update.message.from_user.first_name)+" "+str(update.message.from_user.last_name)+" ("+str(update.message.from_user.username)+") ["+str(update.message.from_user.id)+"]"
		now = log_append(chat_id,userpri+" : "+str(data[0]), "d_how","l")
		text = quadra_love.checkSwitch(data[0])
		update.message.reply_text(text)
	elif target[0] in quadra_search_vocab.dis_list: 
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_dis_how))
		quadra_love.process(update.message.from_user.id,3,0)
	elif target[0] in quadra_search_vocab.adult_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_hentai_how))
		quadra_love.process(update.message.from_user.id,4,0)
	elif target[0] in quadra_dialog_list.dialog_how_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_how_list[target[0]]))
		quadra_love.process(update.message.from_user.id,1,0)
	else:
		update.message.reply_text("미안. 무슨 말인지 모르겠어.")
		quadra_love.process(update.message.from_user.id,1,0)

def dialog_please(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_plz",0)
	target = re.search('사잽아 ((?:(?! (해줘|할래)).)*) (해줘|할래)', str(update.message.text))
	target = target.groups()

	if target[0] in quadra_search_vocab.dis_list: 
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_dis_please))
		quadra_love.process(update.message.from_user.id,3,0)
	elif target[0] in quadra_search_vocab.adult_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_hentai_please))
		quadra_love.process(update.message.from_user.id,4,0)
	elif target[0] in quadra_dialog_list.dialog_please_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_please_list[target[0]]))
		quadra_love.process(update.message.from_user.id,1,0)
	else:
		update.message.reply_text("미안. 뭘 해달라는건지 모르겠어.")
		quadra_love.process(update.message.from_user.id,1,0)
	
def dialog_do(bot, update):
	chat_id = update.message.chat_id
	target = re.search('^사잽아 ((?:(?! 하자).)*) 하자', str(update.message.text))
	target = target.groups()
	
	if target[0] == "야구게임":
		if onGame(update.message.from_user.id) == "야구게임을":
			update.message.reply_text("이미 플레이중인거 같은데?\n3자리 수를 생각해서 \"사잽아 ~ 맞아?\" 라고 말해줘.\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘.")
		elif onGame(update.message.from_user.id) !="" :
			update.message.reply_text("이미 "+onGame(update.message.from_user.id)+" 플레이중인거 같은데?")
		else:
			now = log_append(chat_id,str(update.message.text), "bb","start1")
			temp = quadra_baseball.start(update.message.from_user.id)
			now = log_append(chat_id,str(update.message.from_user.id)+" "+str(temp), "bb","start2")
			update.message.reply_text("좋아! 이제 시작해보자~\n \"사잽아 ~ 맞아?\" 라고 말해줘!\n그만하고 싶다면 \"사잽아\ 그만할래\"라고 말해줘!")
			quadra_love.process(update.message.from_user.id,1,0)
	elif target[0] == "업다운":
		if onGame(update.message.from_user.id) == "업다운을":
			update.message.reply_text("이미 플레이중인거 같은데?\n3자리 수를 생각해서 \"사잽아 ~ 맞아?\" 라고 말해줘.\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘.")
		elif onGame(update.message.from_user.id)!= "" :
			update.message.reply_text("이미 "+onGame(update.message.from_user.id)+" 플레이중인거 같은데?")
		else:
			now = log_append(chat_id, str(update.message.text), "ud","start1")
			temp = quadra_updown.start(update.message.from_user.id)
			now = log_append(chat_id,str(update.message.from_user.id)+" "+str(temp), "ud","start2")
			update.message.reply_text("좋아! 이제 시작해보자~\n \"사잽아 ~ 맞아?\" 라고 말해줘!\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
			quadra_love.process(update.message.from_user.id,1,0)
	else:
		log_append(chat_id, str(update.message.text), "d_do",0)
		if target[0] in quadra_search_vocab.dis_list: 
			update.message.reply_text(random.choice(quadra_dialog_list.dialog_dis_do))
			quadra_love.process(update.message.from_user.id,3,0)
		elif target[0] in quadra_search_vocab.adult_list:
			update.message.reply_text(random.choice(quadra_dialog_list.dialog_hentai_do))
			quadra_love.process(update.message.from_user.id,4,0)
		elif target[0] in quadra_dialog_list.dialog_do_list:
			update.message.reply_text(random.choice(quadra_dialog_list.dialog_do_list[target[0]]))
			quadra_love.process(update.message.from_user.id,1,0)
		else:
			update.message.reply_text("미안. 뭘 하자는건지 모르겠어.")
			quadra_love.process(update.message.from_user.id,1,0)

def dialog_buy(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_buy",0)
	target = re.search('사잽아 ((?:(?! 사줘).)*) 사줘', str(update.message.text))
	target = target.groups()

	if target[0] in quadra_search_vocab.dis_list: 
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_dis_buy))
		quadra_love.process(update.message.from_user.id,3,0)
	elif target[0] in quadra_search_vocab.adult_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_hentai_buy))
		quadra_love.process(update.message.from_user.id,4,0)
	elif target[0] in quadra_dialog_list.dialog_buy_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_buy_list[target[0]]))
		quadra_love.process(update.message.from_user.id,1,0)
	else:
		update.message.reply_text("그건 니돈으로 사는게 어때?")
		quadra_love.process(update.message.from_user.id,1,0)

def game_prog(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "gm","prog")
	user_id = update.message.from_user.id
	game_name = onGame(user_id)
	if game_name == "야구게임을":
		target = re.search('^사잽아 ((?:(?! 맞아\?).)*) 맞아\?', str(update.message.text))
		target = target.groups()
		if len(target[0]) != 3:
			log_append(chat_id,"you have to give answer 000 ~ 999", "bb","p_e1")
			update.message.reply_text("혹시 하는말인데, 수는 3자리로 써야해. 까먹은건 아니지?\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
		else:
			data = quadra_baseball.check(user_id)
			temp_bool = quadra_baseball.check_equal(int(target[0]))
			if temp_bool:
				result = quadra_baseball.gameManager(int(target[0]),int(data[0]))
				data[0] = int(data[0])
				if result[0] == 3:
					log_append(chat_id,"answer is "+str(data[0]), "bb","p_cor")
					update.message.reply_text("정답이야! "+str(int(data[1])+1)+"번만에 맞췄는걸!")
					quadra_baseball.end(user_id)
					quadra_love.process(update.message.from_user.id,10,int(data[1])+1)
				else:
					log_append(chat_id,str(result[0])+"-"+str(result[1])+", answer is "+str(data[0]), "bb","p_no")
					update.message.reply_text(str(result[0])+"스트라이크 "+str(result[1])+"볼! 이번이 "+str(int(data[1])+1)+"번째야!\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
					quadra_baseball.lose(user_id)
					quadra_love.process(update.message.from_user.id,1,0)
			else:
				log_append(chat_id,"there are duplication", "bb","p_e2")
				update.message.reply_text("혹시 하는말인데, 각 자리수에 같은 숫자가 들어가면 안돼. 까먹은건 아니지?\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
	elif game_name == "업다운을":
		target = re.search('^사잽아 ((?:(?! 맞아\?).)*) 맞아\?', str(update.message.text))
		target = target.groups()
		if int(target[0]) < 0 or int(target[0]) > 1000:
			log_append(chat_id,"you have to give answer 000 ~ 999", "ud","p_e1")
			update.message.reply_text("혹시 하는말인데, 수는 1000 미만의 자연수로 써야해. 까먹은건 아니지?\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
		else:
			data = quadra_updown.check(user_id)
			result = quadra_updown.gameManager(int(target[0]),int(data[0]))
			if result == 0:
				log_append(chat_id,"answer is "+str(data[0]), "ud","p_cor")
				update.message.reply_text("정답이야! "+str(int(data[1])+1)+"번만에 맞췄는걸!")
				quadra_updown.end(user_id)
				quadra_love.process(update.message.from_user.id,11,int(data[1])+1)
			elif result == 1:
				log_append(chat_id,"down, answer is "+str(data[0]), "ud","p_no")
				update.message.reply_text("다운! 정답은 그거보다 낮은 수야! 이번이 "+str(int(data[1])+1)+"번째야!\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
				quadra_updown.lose(user_id)
				quadra_love.process(update.message.from_user.id,1,0)
			elif result == -1:
				log_append(chat_id,"up, answer is "+str(data[0]), "ud","p_no")
				update.message.reply_text("업! 정답은 그거보다 높은 수야! 이번이 "+str(int(data[1])+1)+"번째야!\n그만하고 싶다면 \"사잽아 그만할래\"라고 말해줘!")
				quadra_updown.lose(user_id)
				quadra_love.process(update.message.from_user.id,1,0)
	else: 
		log_append(chat_id,"up, answer is "+str(data[0]), "gm","p_no")
		update.message.reply_text("게임을 안하고 있는것같은데?")

def game_end(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "bb","end")
	user_id = update.message.from_user.id
	game_name = onGame(user_id)
	if game_name == "야구게임을":
		data = quadra_baseball.check(user_id)
		data[0] = int(data[0])
		log_append(chat_id,"answer is "+str(data[0]), "bb","end2")
		update.message.reply_text("야구게임을 그만하려고? 하는수없지. 정답은 "+str(data[0])+"이었고, 너는 "+str(data[1])+"번 시도했어!")
		quadra_baseball.end(user_id)
	elif game_name == "업다운을":
		data = quadra_updown.check(user_id)
		log_append(chat_id,"answer is "+str(data[0]), "ud","end2")
		update.message.reply_text("업다운을 그만하려고? 하는수없지. 정답은 "+str(data[0])+"이었고, 너는 "+str(data[1])+"번 시도했어!")
		quadra_updown.end(user_id)
	else:
		log_append(chat_id,str(user_id)+" isn't playing baseball", "gm","e_e")
		update.message.reply_text("애초에 안하고 있었던 것 같은데.. 게임을 하고 싶다면 먼저 \"사잽아 (게임이름) 하자\" 라고 말해줘!")

def dial001(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial001",0)
	update.message.reply_text("쫑긋!")

def dial002(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial002",0)
	update.message.reply_text("후에엥..ㅠㅠ")
	quadra_love.process(update.message.from_user.id,4,0)

def dial003(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial003",0)
	switch = random.randrange(1, 4)
	if switch == 1:
		update.message.reply_text("(..피식)")
	elif switch == 2:
		update.message.reply_text("하하! 그렇게도 볼 수 있구나..")
	else:
		update.message.reply_text("그거 장난치려고 일부러 그러는거지?")
	quadra_love.process(update.message.from_user.id,1,0)

def dial004(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial004",0)
	update.message.reply_text(random.choice(quadra_dialog_list.dialog_lone_list))
	quadra_love.process(update.message.from_user.id,3,0)

def searching(bot, update):
	chat_id = update.message.chat_id
	target = re.search('^사잽아 (?:((?:(?!에서).)*)에서 )?((?:(?! (알려줘|찾아줘)).)*) (알려줘|찾아줘)', str(update.message.text))
	target = target.groups()

	if target[0] == '스팀':
		search_target = target[1].lower()
		term_switch = 0
		game_dict = quadra_game_list.game_synonym.items()
		for i in game_dict :
			if search_target in i[1]:
				term_switch = 1
				game_real_name = i[0]
			if search_target == i[0]:
				term_switch = 1
				game_real_name = i[0]
		if term_switch == 0:
			now = log_append(chat_id, str(update.message.text), "sch", "g_e")
			bot.send_message(chat_id=chat_id, text="미안해. 무슨 게임인지 잘 몰라서 대신 검색해줄게! (" + quadra_search_list.search_engine["스팀"] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,2,0)
		else : 
			now = log_append(chat_id, str(update.message.text), "sch", "g")
			game_target = quadra_game_list.game_number[game_real_name]
			if game_target[0] == 0:
				bot.send_message(chat_id=chat_id, text="혹시 이 게임 찾으려는거 맞아? (" + quadra_game_list.steam_shop+game_target[1] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
				quadra_love.process(update.message.from_user.id,2,0)
			else :
				bot.send_message(chat_id=chat_id, text=game_target[0]+" (" + quadra_game_list.steam_shop+game_target[1] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
				quadra_love.process(update.message.from_user.id,2,0)
			
	
	elif target[0] in quadra_search_list.search_engine:
		if target[1] in quadra_search_vocab.adult_list:
			now = log_append(chat_id, str(update.message.text), "sch", "ad")
			update.message.reply_text("(사잽이가 당신을 경멸합니다.)")
			bot.send_message(chat_id=chat_id, text="변태.. 이런거까지 찾아줘야해? (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,5,0)
		elif target[1] in quadra_search_vocab.dis_list:
			now = log_append(chat_id, str(update.message.text), "sch", "dis")
			bot.send_message(chat_id=chat_id, text="... 이런걸 생각중이라면 그만둬. ..내가 너랑 함께 있어줄테니까. (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,3,0)
		elif target[1] in quadra_search_vocab.wonder_list:
			now = log_append(chat_id, str(update.message.text), "sch", "won")
			bot.send_message(chat_id=chat_id, text=quadra_search_vocab.wonder_list[target[1]] + " (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,2,0)
		else:
			now = log_append(chat_id, str(update.message.text), "sch", 0)
			bot.send_message(chat_id=chat_id, text="이거 찾으려는거 맞지? (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,2,0)
	elif target[1] in quadra_search_list.hentai_url:
		now = log_append(chat_id, str(update.message.text), "sch", "d_ad")
		update.message.reply_text("(사잽이가 당신을 경멸합니다.)")
		bot.send_message(chat_id=chat_id, text="너는 정말 최악의 변태구나.. 자, 여깄어. (" + quadra_search_list.hentai_url[target[1]] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		quadra_love.process(update.message.from_user.id,5,0)
	elif target[1] in quadra_search_list.direct_url:
		now = log_append(chat_id, str(update.message.text), "sch", "d")
		bot.send_message(chat_id=chat_id, text="거기라면 나도 알고있어! 바로 보내줄께! (" + quadra_search_list.direct_url[target[1]] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		quadra_love.process(update.message.from_user.id,2,0)
	else:
		if target[1] in quadra_search_vocab.adult_list:
			now = log_append(chat_id, str(update.message.text), "sch", "n_ad")
			update.message.reply_text("(사잽이가 당신을 경멸합니다.)")
			bot.send_message(chat_id=chat_id, text=target[1] + "라니... 변태! 이런거까지 찾아줘야해? (" + quadra_search_list.search_engine["구글"] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,5,0)
		elif target[1] in quadra_search_vocab.dis_list:
			now = log_append(chat_id, str(update.message.text), "sch", "n_dis")
			bot.send_message(chat_id=chat_id, text=target[1] + "같은걸 생각중이라면 그만둬. ..내가 너랑 함께 있어줄테니까. (" + quadra_search_list.search_engine['구글'] + url_encode( target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,3,0)
		elif target[1] in quadra_search_vocab.wonder_list:
			now = log_append(chat_id, str(update.message.text), "sch", "n_won")
			bot.send_message(chat_id=chat_id, text=quadra_search_vocab.wonder_list[target[1]] + " (" + quadra_search_list.search_engine['구글'] + url_encode(target[1]) + ")", 	 parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,2,0)
		else:
			now = log_append(chat_id, str(update.message.text), "sch", "n")
			bot.send_message(chat_id=chat_id, text="이거 찾으려는거 맞지? (" + quadra_search_list.search_engine["구글"] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			quadra_love.process(update.message.from_user.id,2,0)
	
updater.dispatcher.add_handler(RegexHandler('^사잽아 (?:((?:(?!에서).)*)에서 )?((?:(?! (알려줘|찾아줘)).)*) (알려줘|찾아줘)', searching))

updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! (해줘|할래)).)*) (해줘|할래)', dialog_please))
updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! 하자).)*) 하자', dialog_do))
updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! 어때).)*) 어때', dialog_how))
updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! 사줘).)*) 사줘', dialog_buy))

updater.dispatcher.add_handler(RegexHandler('^사잽아 뭐하니$', lifetime))
updater.dispatcher.add_handler(RegexHandler('^사잽아$', lifetime))
updater.dispatcher.add_handler(RegexHandler('^사잽아 놀아줘$', lifetime))

updater.dispatcher.add_handler(RegexHandler('^사잽아 도와줘$', version))
help_handler = CommandHandler('help', version)
updater.dispatcher.add_handler(help_handler)

updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! 맞아\?).)*) 맞아\?', game_prog))
updater.dispatcher.add_handler(RegexHandler('^사잽아 그만할래$', game_end))
updater.dispatcher.add_handler(RegexHandler('^쫑긋$',dial001))
updater.dispatcher.add_handler(RegexHandler('^줘팸$',dial002))
updater.dispatcher.add_handler(RegexHandler('^사잽이는 잽을 4번 날린다고 사잽이야\?$', dial003))
updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! 외로워).)* )?외로워$', dial004))

updater.start_polling()
log_append('system', 'Bot running Start', 'system',0)
updater.idle()
