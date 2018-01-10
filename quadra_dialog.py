#사잽아 치킨사줘
def dial001(bot,update):
	now = time.localtime()
	print("[%04d-%02d-%02d %02d:%02d:%02d] " % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),end='')
	print("dial001  : "+str(update.message.text))
	switch = random.randrange(1,4)
	if switch == 1:	update.message.reply_text("그럼 99명이랑 싸워서 1등해오시던가.")
	elif switch == 2: update.message.reply_text("M416도 반동제어 못하는놈이 뭔 치킨이야!")
	else: update.message.reply_text("이겼닭! 오늘 저녁은 치킨이닭!")
	
#사잽이는 잽을 4번 날린다고 사잽이야?
def dial002(bot,update):
	now = time.localtime()
	print("[%04d-%02d-%02d %02d:%02d:%02d] " % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),end='')
	print("dial002  : "+str(update.message.text))
	switch = random.randrange(1,4)
	if switch == 1:	update.message.reply_text("(..피식)")
	elif switch == 2: update.message.reply_text("하하! 그렇게도 볼 수 있구나..")
	else: update.message.reply_text("그거 장난치려고 일부러 그러는거지?")

#사잽아 창조 어때?
def dial003(bot,update):
	now = time.localtime()
	print("[%04d-%02d-%02d %02d:%02d:%02d] " % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),end='')
	print("dial003  : "+str(update.message.text))
	switch = random.randrange(1,4)
	if switch == 1:	update.message.reply_text("위키계 최악의 다중계정 악용 사용자. 난 그렇게 알고있어.")
	elif switch == 2: update.message.reply_text("뭐.. 요즘도 그러는지 안그러는지는 모르겠지만, 정말 딱한 사람이야.")
	else: update.message.reply_text("왜 그렇게 위키에 집착하는걸까, 알 수 없는 사람.")
	
#사잽아 카티노르 어때?
def dial004(bot,update):
	now = time.localtime()
	print("[%04d-%02d-%02d %02d:%02d:%02d] " % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),end='')
	print("dial004  : "+str(update.message.text))
	switch = random.randrange(1,4)
	if switch == 1:	update.message.reply_text("그사람? 바보잖아")
	elif switch == 2: update.message.reply_text("날 빙자해서 대체 얼마나 더 사고치려는건지 원..")
	else: update.message.reply_text("커서 뭐가 될련지 걱정이다 걱정...")