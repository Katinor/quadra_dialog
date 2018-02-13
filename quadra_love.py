import os
import random
import quadrabot_config
import time

MAX_LOVE = 300
MIN_LOVE = -100

def enable(user_id):
	profile_name = "love_telegram_database/"+str(user_id)+".txt"
	if os.path.exists(profile_name):
		return True
	else:
		return False
		
def isAdmin(user_id):
	if user_id in quadrabot_config.ADMIN:
		return True
	else: return False

def createNew(user_id):
	now = time.time()
	profile_name = "love_telegram_database/"+str(user_id)+".txt"
	fp = open(profile_name, 'a')
	fp.write("0\n")
	fp.write(str(now))
	fp.close()

def mody(user_id,value,now):
	profile_name = "love_telegram_database/"+str(user_id)+".txt"
	fp = open(profile_name, 'w')
	fp.write(str(value)+'\n')
	fp.write(str(now))
	fp.close()

def check(user_id):
	profile_name = "love_telegram_database/"+str(user_id)+".txt"
	if enable(user_id) == False: createNew(user_id)
	fp = open(profile_name,'r')
	target = fp.readlines()
	fp.close()
	target[0] = int(target[0])
	target[1] = float(target[1])
	return target

def checkUser(user_id,forward_id):
	if isAdmin(user_id):
		if enable(forward_id) == False: createNew(forward_id)
		return check(forward_id)[0]
	else: return False

#switch
#0 = lifetime
#1 = talk
#2 = search
#3 = dis
#4 = hentai
#5 = hentai_search
#10 = baseball
def process(user_id,switch,ref):
	if enable(user_id) == False: createNew(user_id)
	data = check(user_id)
	now = data[1]
	proc = False
	if switch < 3:
		if now+2 < time.time():
			if switch == 0:
				now = time.time()
				value = data[0] + 1
				proc = True
			if switch == 1:
				now = time.time()
				value = data[0] + 1
				proc = True
			if switch == 2:
				now = time.time()
				value = data[0] + 1
				proc = True
			if switch == 3:
				now = time.time()
				value = data[0] + 2
				proc = True
	else:
		if switch == 4:
			value = data[0] - 10 - (5*MAX_LOVE - data[0]) / (MAX_LOVE-MIN_LOVE)
			proc = True
		if switch == 5:
			value = data[0] - 5 - (5*MAX_LOVE - data[0]) / (MAX_LOVE-MIN_LOVE)
			proc = True
		if switch == 10:
			if ref > 10: ref = 10
			temp1 = 11 - ref
			temp1 = temp1//10 + temp1//9 + (temp1//7)*2 + (temp1//6)*3
			inc = temp1 * (MAX_LOVE - data[0]) / (MAX_LOVE-MIN_LOVE)
			if inc < 2: inc = 2
			value = data[0] + inc
			proc = True
		if switch == 11:
			if ref > 10: ref = 10
			temp1 = 11 - ref
			temp1 = temp1//10 + temp1//9 + (temp1//7)*2 + (temp1//6)*3
			inc = temp1 * (MAX_LOVE - data[0]) / (MAX_LOVE-MIN_LOVE)
			if inc < 2: inc = 2
			value = data[0] + inc
			proc = True
	if proc: 
		if value > MAX_LOVE: value = MAX_LOVE
		if value < MIN_LOVE: value = MIN_LOVE
		mody(user_id,int(value),now)

love_0 = ["무슨 낯짝으로 내 앞에 서있는건지 모르겠는데?","저리 가. 별로 보고싶지 않으니까.","굳이 내 앞에 서 있는 이유가 뭐야?"]
love_1 = ["참을 인도 쓰다보면 팔이 아프단것만 알아둬.","어.. 너구나. 안녕.","글쎄.. 굳이 표정을 찡그려줘야해?"]
love_2 = ["글쎄.. 어떨까나?","서로 알아갈 시간이 더 필요할거같아.","굳이 말하자면, 좋지도 싫지도 않은 정도?"]
love_3 = ["조금은 더 알아가고 싶은 사람, 정도로 괜찮을까?","적어도 밉지는 않아."]
love_4 = ["친구 정도로 생각하고 있어.","더 친해져보고 싶은사람!","음.. 문자 정도는 주고받을 수 있는 사이?"]
love_5 = ["너 정도면 믿음직한 친구지.","친구, 오늘은 어떻게 나와 놀아줄거야?","쫑긋! 너 정도면 좋은 친구지!"]
love_6 = ["쫑긋! ..헤헤","..부끄러워! 너무 가까이 오진 마..","친구 이상, 연인 이하의.. 그냥 좋아 네가.","넌 최고의 친구 중 한명이야!"]

def checkSwitch(data):
	if data < MIN_LOVE * 0.7:
		return random.choice(love_0)
	elif data < MIN_LOVE * 0.2:
		return random.choice(love_1)
	elif data < MAX_LOVE * 0.1:
		return random.choice(love_2)
	elif data < MAX_LOVE * 0.3:
		return random.choice(love_3)
	elif data < MAX_LOVE * 0.7:
		return random.choice(love_4)
	elif data < MAX_LOVE * 0.9:
		return random.choice(love_5)
	else:
		return random.choice(love_6)