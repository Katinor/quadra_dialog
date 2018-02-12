import os

def enable(user_id):
	profile_name = "baseball_telegram_database/"+str(user_id)+".txt"
	if os.path.exists(profile_name):
		return True
	else:
		return False

def start(user_id):
	profile_name = "baseball_telegram_database/"+str(user_id)+".txt"
	if enable(user_id):
		return -1
	else:
		answer = random.randrange(0, 1000)
		fp = open(profile_name, 'a')		
		fp.write(answer)
		fp.write("\n")
		fp.write("0")
		return answer

def gameManager(target,answer):
	strike = 0
	ball = 0
	for i in range(0,3,1):
		for j in range(0,3,1):
			if target[i] == answer[j]:
				if i == j: strike += 1
				else: ball += 1
	return [strike,ball]

def check(user_id):
	profile_name = "baseball_telegram_database/"+str(user_id)+".txt"
	if enable(user_id):
		fp = open(profile_name,'r')
		target = fp.readlines()
		target[1] = int(target[1])
		return target

def lose(user_id):
	profile_name = "baseball_telegram_database/"+str(user_id)+".txt"
	temp = check(user_id)
	temp[1] += 1
	fp = open(profile_name,'r')
	fp.write(temp[0])
	fp.write("\n")
	fp.write(str(temp[1]))

def end(user_id):
	profile_name = "baseball_telegram_database/"+str(user_id)+".txt"
	os.remove(profile_name)