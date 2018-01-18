steam_shop = 'http://store.steampowered.com/app/'

# 규칙
# game_number 딕셔너리
#  - key : 게임이름을 그대로 쓰면 됩니다.
#    * 만약 게임이름에 대문자가 있다면, 모두 소문자로 적어야 합니다.
#    * 만약 게임이름에 '가 있다면, 쌍따옴표를 쓰셔야합니다. (그냥 귀찮으면 다 쌍따옴표 쓰세요.)
#  - value : 원소가 2개인 배열입니다.
#    * [0] : 이 게임을 검색하면 말할 이름입니다. 0을 넣으면 기본값입니다.
#    * [1] : 그 게임의 고유번호입니다.

game_synonym 딕셔너리
  - key : game_number의 모든 key를 갖고 있어야 합니다. (두 딕셔너리의 key값이 완전히 같아야 합니다.)
  - value : key로 칭해지는 게임들의 별명들을 적으면 됩니다.
game_number = {
	"playerunknown's battlegrounds" : ['어쭈. 치킨 한번 먹어봤나보네?','578080'],
	'darkest dungeon' : ['정말 괜찮은 게임이지. 오늘도 의지를 시험해보자구!','262060'],
	'ftl: faster than light' : ['단 하나의 미사일로도, 무너질 수 있는법이야.','212680'],
	'the binding of issac: rebirth' : ['조금은 기괴하지만, 나름 쏘는 맛은 있는 게임이지.','250900'],
	'downwell' : [0,'360740'],
	'enter the gungeon' : ['그저 피하고 쏘면 돼. 그럼 엔-터 더 건전!','311690'],
	'titan souls' : ['기회는 단 한번인데, 그 기회도 스스로 쟁취해야 할거야.','297130'],
	'you must build a boat' : ['항해를 하다 보면 어느새 네 배도 커져 있을거야.','290890'],
	'doki doki literature club' : ['그래.. 참 두근두근한 게임이지.. (시선회피)','698780'],
	'paper, please' : ['그저 여권만 처리하는 게임이라면 얼마나 좋을까.','239030'],
	'reigns' : ['너의 선택이 너를 죽일수도, 나라를 살릴수도 있어.','474750'],
	'this war of mine' : ['전쟁. 전쟁은 변하지 않는, 최악의 사건이지.','282070'],
	'va-11 hall-a' : ['술을 섞고 삶을 바꿔줄 시간이군.','447530'],
	'dark souls' : ['죽음을 준비할 시간이야.','211420'],
	'dark souls ii' : ['그나마 캐주얼한 다크소울이 바로 2 아닐까.','236430'],
	'dark souls iii' : ['나는 먼저 간다, 이 군다들아!','374320'],
	'cuphead' : ['옛날에 보았던 만화들이 다시 생각날거야.','268910'],
	'shovel knight' : ['내가 보기에는 주인공이 싸움 좀 해봤어. 군인 아저씨들도 야전삽을 쓰잖아?','250760'],
	'to the moon' : ['흑.. 흐흑.. 아 소개만 하는데도 눈물이 나네..','206440']
}

game_synonym = {
	"playerunknown's battlegrounds" : ['배그','배틀그라운드'],
	'darkest dungeon' : ['다키스트 던전','다키스트던전','닼던'],
	'ftl: faster than light' : ['ftl'],
	'the biding of issac: rebirth' : ['아이작의 번제 리버스', '아이작의번제 리버스'],
	'downwell' : ['다운웰'],
	'enter the gungeon' : ['엔터 더 건전', '엔터더건전', '건전'],
	'titan souls' : ['타이탄 소울즈', '타이탄소울즈'],
	'you must build a boat' : ['유 머스트 빌드 어 보트'],
	'doki doki literature club' : ['두근두근 문예부', '두근두근문예부', '문예부'],
	'paper, please' : ['페이퍼 플리즈', '페이퍼플리즈', '동무 려권내라우', '동무려권내라우'],
	'reigns' : ['레인즈'],
	'this war of mine' : ['디스 워 오브 마인', '디스워오브마인'],
	'va-11 hall-a' : ['발할라'],
	'dark souls' : ['다크소울','닼소','다크소울','닼소','dark souls'],
	'dark souls ii' : ['다크소울2','닼소2','다크소울II','닼소II','dark souls 2'],
	'dark souls iii' : ['다크소울3','닼소3','다크소울III','닼소III','dark souls 3'],
	'cuphead' : ['컵헤드'],
	'shovel knight' : ['소벨 나이트','소벨나이트','삽질 기사','삽질기사'],
	'to the moon' : ['투 더 문', '투더문']
}
