import re
import requests
import telegram
import random
import time
from telegram.ext import Updater, RegexHandler, CommandHandler
from urllib import parse
import quadra_search_list
import quadra_search_vocab
import quadra_dialog_list
import quadra_game_list
import quadrabot_config

my_token = quadrabot_config.TOKEN_TELEGRAM
updater = Updater(my_token)

def log_append(_chat_id, _text, _type, _subtype):
	_now = time.localtime()
	if _subtype!=0 : what_type = _type +'_' +_subtype
	else : what_type = _type
	target = "[%04d-%02d-%02d %02d:%02d:%02d] trgd [%10s] from [%15s] : %s" % (_now.tm_year, _now.tm_mon, _now.tm_mday, _now.tm_hour, _now.tm_min, _now.tm_sec, what_type,str(_chat_id),_text)
	fp = open("quadra_bot_log.txt", 'a')
	print(target)
	fp.write(target+"\n")
	fp.close()
	return _now

def version(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "help",0)
	update.message.reply_text(
		"반가워! 나는 사잽이라고해! 지금은 0.1.1 버전이야! \n나는 이런것들을 할 수 있어!\n * 쫑긋\n * 사잽아 ~~ 찾아줘/알려줘\n   * 지원 엔진 : (위키들이랑) 구글, 네이버, 나무위키, 리브레위키, 위키백과, 구스위키, 진보위키, 백괴사전\n * 사잽아 ~ 해줘/하자/어때/사줘")

def hentai_back(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "ht_back",0)
	switch = random.randrange(1, 5)
	if switch == 1:
		update.message.reply_text("변태.. 저리 꺼져!")
	elif switch == 2:
		update.message.reply_text("으으.. 날 그런 눈으로 쳐다본거야?")
	elif switch == 3:
		update.message.reply_text("변태랑은 놀아줄 시간이 없는걸.")
	else:
		update.message.reply_text("경찰 불러버릴거야.. 흑...")

def dis_back(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dis_back",0)
	switch = random.randrange(1, 7)
	if switch == 1:
		update.message.reply_text("그러지 마. 내가 곁에 있어줄게.")
	elif switch == 2:
		update.message.reply_text("힘들어도 내가 옆에서 지켜줄테니까..")
	elif switch == 3:
		update.message.reply_text(".. 약한 척 하지마. 너도 강한 용사야.")
	elif switch == 4:
		update.message.reply_text("지금 당장이 쓸쓸하더라도, 봄은 다시 찾아오게 되어있어.")
	elif switch == 5:
		update.message.reply_text("그러지마. 내가 대신 행복을 빌어줄게.")
	else:
		update.message.reply_text("나를 봐서라도 그런 생각은 접어줘.")

def lifetime(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "lifetime",0)
	if 0 <= now.tm_hour < 6:
		timer = 0
	elif 6 <= now.tm_hour < 7:
		timer = 1
	elif 7 <= now.tm_hour < 8:
		timer = 2
	elif 8 <= now.tm_hour < 12:
		timer = 3
	elif 12 <= now.tm_hour < 13:
		timer = 4
	elif 13 <= now.tm_hour < 18:
		timer = 5
	elif 18 <= now.tm_hour < 19:
		timer = 6
	elif 19 <= now.tm_hour < 22:
		timer = 7
	elif now.tm_hour >= 22:
		timer = 8

	if timer == 0:
		switch = random.randrange(1, 5)
		if switch == 1:
			update.message.reply_text("쿠울..쿨..zzZ")
		elif switch == 2:
			update.message.reply_text("으으..깨우지마아...zzZ")
		elif switch == 3:
			update.message.reply_text("헤헤..민트초코오..zzZ")
		else:
			update.message.reply_text("새근새근..")
	elif timer == 1:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("흐아암.. 아침은 힘들어어...")
		elif switch == 2:
			update.message.reply_text("오늘도 좋은아침..zzZ")
		else:
			update.message.reply_text("끄아아~ 아침이다아~!")
	elif timer == 2:
		switch = random.randrange(1, 5)
		if switch == 1:
			update.message.reply_text("아침먹을 준비! 헤헤..")
		elif switch == 2:
			update.message.reply_text("아침을 든든하게 먹어야 하루가 든든한거야!")
		elif switch == 3:
			update.message.reply_text("당연히 식사준비지! 오늘 아침은 뭐야~?")
		else:
			update.message.reply_text("기운나는 아침의 표효! 꺄아아아아앙!")
	elif timer == 3:
		switch = random.randrange(1, 5)
		if switch == 1:
			update.message.reply_text("독서는 아침을 깨워준다구")
		elif switch == 2:
			update.message.reply_text("오늘도 모든 세계에 축복이 가득하게 해주세요..")
		elif switch == 3:
			update.message.reply_text("모닝민초 한잔은 최고의 휴식이지!")
		else:
			update.message.reply_text("그것보다 너야말로 일할 시간 아냐? 어디서 땡땡이야!")
	elif timer == 4:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("헤헤.. 나에게 더 맛있는 식사를 대접해달라구!")
		elif switch == 2:
			update.message.reply_text("점심은 무얼 먹어볼까나~")
		else:
			update.message.reply_text("여~ 식사는 했어?")
	elif timer == 5:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("역시 낮에는 낮잠이지..zzZ")
		elif switch == 2:
			update.message.reply_text("우리 같이 노래부를래? 헤헤..")
		else:
			update.message.reply_text("오늘도 행복하게 마무리짓자구!")
	elif timer == 6:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("오늘 저녁은 뭐야~? 헤헤...")
		elif switch == 2:
			update.message.reply_text("역시 하루의 마지막은 풍성하게 먹어야지!")
		else:
			update.message.reply_text("흐아암~ 이제야 쉬겠는걸?")
	elif timer == 7:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("하루가 끝나가면 쉬어야지. 게임이라던가?")
		elif switch == 2:
			update.message.reply_text("배부르니까 한숨 더 자볼까나~")
		else:
			update.message.reply_text("오늘을 마무리하는데에는 역시 콜라 한잔이지!")
	elif timer == 8:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("오늘 하루도 수고했어. 그렇게 내일도 더 멋지게 살아보자.")
		elif switch == 2:
			update.message.reply_text("잘자! 내일도 행복하자구")
		else:
			update.message.reply_text("오늘도 이렇게 지나가는구나...")
	else:
		update.message.reply_text("오늘도 행복한 하루!")

def dialog_how(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_how",0)
	target = re.search('^사잽아 ((?:(?! 어때).)*) 어때(\?)?', str(update.message.text))
	target = target.groups()

	if target[0] in quadra_search_vocab.dis_list:
		switch = random.randrange(1, 5)
		if switch == 1:
			update.message.reply_text("그런 건 궁금해 하지마. 대신 날 보는게 어때?")
		elif switch == 2:
			update.message.reply_text("왜 이런걸 묻는거야.. 요즘 힘들어?")
		elif switch == 3:
			update.message.reply_text("묻지마. 안궁금하도록 함께 해줄께.")
		else:
			update.message.reply_text("나를 봐서라도 그런건 묻지말아줘.")
	elif target[0] in quadra_search_vocab.adult_list:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("변태.. 날 그런 눈으로 본거야?")
		elif switch == 2:
			update.message.reply_text("흥. 응큼한 눈으로 장난치지마.")
		else:
			update.message.reply_text("변태.. 저리 꺼져!")
	elif target[0] in quadra_dialog_list.dialog_how_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_how_list[target[0]]))
	else:
		update.message.reply_text("미안. 무슨 말인지 모르겠어.")

def dialog_please(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_plz",0)
	target = re.search('사잽아 ((?:(?! (해줘|할래)).)*) (해줘|할래)', str(update.message.text))
	target = target.groups()

	if target[0] in quadra_search_vocab.dis_list:
		switch = random.randrange(1, 5)
		if switch == 1:
			update.message.reply_text("그런 건 부탁하지마. 대신 날 보는게 어때?")
		elif switch == 2:
			update.message.reply_text("왜 이런걸 부탁하는거야.. 요즘 힘들어?")
		elif switch == 3:
			update.message.reply_text("많이 힘들었구나..")
		else:
			update.message.reply_text("나를 봐서라도 그런건 부탁하지 말아줘.")
	elif target[0] in quadra_search_vocab.adult_list:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("하겠냐! 이 변태..")
		elif switch == 2:
			update.message.reply_text("웃기지마! 니 혼자 해!")
		else:
			update.message.reply_text("변태.. 저리 꺼져!")
	elif target[0] in quadra_dialog_list.dialog_please_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_please_list[target[0]]))
	else:
		update.message.reply_text("미안. 뭘 해달라는건지 모르겠어.")

def dialog_do(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_do",0)
	target = re.search('^사잽아 ((?:(?! 하자).)*) 하자', str(update.message.text))
	target = target.groups()

	if target[0] in quadra_search_vocab.dis_list:
		switch = random.randrange(1, 7)
		if switch == 1:
			update.message.reply_text("그러지 마. 내가 곁에 있어줄게.")
		elif switch == 2:
			update.message.reply_text("힘들어도 내가 옆에서 지켜줄테니까..")
		elif switch == 3:
			update.message.reply_text(".. 약한 척 하지마. 너도 강한 용사야.")
		elif switch == 4:
			update.message.reply_text("지금 당장이 쓸쓸하더라도, 봄은 다시 찾아오게 되어있어.")
		elif switch == 5:
			update.message.reply_text("그러지마. 내가 대신 행복을 빌어줄게.")
		else:
			update.message.reply_text("나를 봐서라도 그런 생각은 접어줘.")
	elif target[0] in quadra_search_vocab.adult_list:
		switch = random.randrange(1, 8)
		if switch == 1:
			update.message.reply_text("하겠냐! 이 변태..")
		elif switch == 2:
			update.message.reply_text("웃기지마! 니 혼자 해!")
		elif switch == 3:
			update.message.reply_text("변태.. 저리 꺼져!")
		elif switch == 4:
			update.message.reply_text("으으.. 날 그런 눈으로 쳐다본거야?")
		elif switch == 5:
			update.message.reply_text("변태랑은 놀아줄 시간이 없는걸.")
		elif switch == 6:
			update.message.reply_text("경찰 불러버릴거야.. 흑...")
		else:
			update.message.reply_text("변태.. 저리 꺼져!")
	elif target[0] in quadra_dialog_list.dialog_do_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_do_list[target[0]]))
	else:
		update.message.reply_text("미안. 뭘 하자는건지 모르겠어.")

def dialog_buy(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "d_buy",0)
	target = re.search('사잽아 ((?:(?! 사줘).)*) 사줘', str(update.message.text))
	target = target.groups()

	if target[0] in quadra_search_vocab.adult_list:
		switch = random.randrange(1, 4)
		if switch == 1:
			update.message.reply_text("변태.. 날 그런 눈으로 본거야?")
		elif switch == 2:
			update.message.reply_text("흥. 응큼한 눈으로 장난치지마.")
		else:
			update.message.reply_text("변태.. 저리 꺼져!")
	elif target[0] in quadra_dialog_list.dialog_buy_list:
		update.message.reply_text(random.choice(quadra_dialog_list.dialog_buy_list[target[0]]))
	else:
		update.message.reply_text("그건 니돈으로 사는게 어때?")

def dial001(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial001",0)
	update.message.reply_text("쫑긋!")

def dial002(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial002",0)
	update.message.reply_text("후에엥..ㅠㅠ")

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

def dial004(bot, update):
	chat_id = update.message.chat_id
	now = log_append(chat_id, str(update.message.text), "dial004",0)
	switch = random.randrange(1, 4)
	if switch == 1:
		update.message.reply_text("정말이지.. 나로는 부족한거야?")
	elif switch == 2:
		update.message.reply_text("내가 같이 있는걸.. 힘내!")
	else:
		update.message.reply_text("걱정마. 나는 널 떠나지 않을거니까.")

def url_encode(data):
	return (parse.quote(data).replace('/', '%2F'))

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
		else : 
			
			now = log_append(chat_id, str(update.message.text), "sch", "g")
			game_target = quadra_game_list.game_number[game_real_name]
			if game_target[0] == 0:
				bot.send_message(chat_id=chat_id, text="혹시 이 게임 찾으려는거 맞아? (" + quadra_game_list.steam_shop+game_target[1] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			else :
				bot.send_message(chat_id=chat_id, text=game_target[0]+" (" + quadra_game_list.steam_shop+game_target[1] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
			
	
	elif target[0] in quadra_search_list.search_engine:
		if target[1] in quadra_search_vocab.adult_list:
			now = log_append(chat_id, str(update.message.text), "sch", "ad")
			update.message.reply_text("(사잽이가 당신을 경멸합니다.)")
			bot.send_message(chat_id=chat_id, text="변태.. 이런거까지 찾아줘야해? (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		elif target[1] in quadra_search_vocab.dis_list:
			now = log_append(chat_id, str(update.message.text), "sch", "dis")
			bot.send_message(chat_id=chat_id, text="... 이런걸 생각중이라면 그만둬. ..내가 너랑 함께 있어줄테니까. (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		elif target[1] in quadra_search_vocab.wonder_list:
			now = log_append(chat_id, str(update.message.text), "sch", "won")
			bot.send_message(chat_id=chat_id, text=quadra_search_vocab.wonder_list[target[1]] + " (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		else:
			now = log_append(chat_id, str(update.message.text), "sch", 0)
			bot.send_message(chat_id=chat_id, text="이거 찾으려는거 맞지? (" + quadra_search_list.search_engine[target[0]] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
	elif target[1] in quadra_search_list.hentai_url:
		now = log_append(chat_id, str(update.message.text), "sch", "d_ad")
		update.message.reply_text("(사잽이가 당신을 경멸합니다.)")
		bot.send_message(chat_id=chat_id, text="너는 정말 최악의 변태구나.. 자, 여깄어. (" + quadra_search_list.hentai_url[target[1]] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
	elif target[1] in quadra_search_list.direct_url:
		now = log_append(chat_id, str(update.message.text), "sch", "d")
		bot.send_message(chat_id=chat_id, text="거기라면 나도 알고있어! 바로 보내줄께! (" + quadra_search_list.direct_url[target[1]] + ")", parse_mode=telegram.ParseMode.MARKDOWN)
	else:
		if target[1] in quadra_search_vocab.adult_list:
			now = log_append(chat_id, str(update.message.text), "sch", "n_ad")
			update.message.reply_text("(사잽이가 당신을 경멸합니다.)")
			bot.send_message(chat_id=chat_id, text=target[1] + "라니... 변태! 이런거까지 찾아줘야해? (" + quadra_search_list.search_engine["구글"] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		elif target[1] in quadra_search_vocab.dis_list:
			now = log_append(chat_id, str(update.message.text), "sch", "n_dis")
			bot.send_message(chat_id=chat_id, text=target[1] + "같은걸 생각중이라면 그만둬. ..내가 너랑 함께 있어줄테니까. (" + quadra_search_list.search_engine['구글'] + url_encode( target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)
		elif target[1] in quadra_search_vocab.wonder_list:
			now = log_append(chat_id, str(update.message.text), "sch", "n_won")
			bot.send_message(chat_id=chat_id, text=quadra_search_vocab.wonder_list[target[1]] + " (" + quadra_search_list.search_engine['구글'] + url_encode(target[1]) + ")", 	 parse_mode=telegram.ParseMode.MARKDOWN)
		else:
			now = log_append(chat_id, str(update.message.text), "sch", "n")
			bot.send_message(chat_id=chat_id, text="이거 찾으려는거 맞지? (" + quadra_search_list.search_engine["구글"] + url_encode(target[1]) + ")", parse_mode=telegram.ParseMode.MARKDOWN)


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

updater.dispatcher.add_handler(RegexHandler('^사잽아 따먹자$', hentai_back))

updater.dispatcher.add_handler(RegexHandler('^사잽아 한강 가즈아$', dis_back))
updater.dispatcher.add_handler(RegexHandler('^사잽아 한강 가자$', dis_back))
updater.dispatcher.add_handler(RegexHandler('^사잽아 한강가자$', dis_back))

updater.dispatcher.add_handler(RegexHandler('^쫑긋$',dial001))
updater.dispatcher.add_handler(RegexHandler('^줘팸$',dial002))
updater.dispatcher.add_handler(RegexHandler('^사잽이는 잽을 4번 날린다고 사잽이야\?$', dial003))
updater.dispatcher.add_handler(RegexHandler('^사잽아 ((?:(?! 외로워).)* )?외로워$', dial004))

updater.start_polling()
log_append('system', 'Bot running Start', 'system',0)
updater.idle()
