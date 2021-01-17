# coding:utf-8
import os
import math
import tvlist
import datetime
import re

htmldata = None
splitter_data = {}

year = "2021"
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
areas = ["23","24","25","26","27","28","29","10","11","12","13","14","15","16","17","18","19","20","21","22","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","bs1","bs2","bs3","bs4","bs4k8k_1","bs4k8k_2","23_MX2","27_CTC2","27_CTC3","23_EX2","bs2_ON"]

abc_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
trans_table = str.maketrans({
"０":"0","１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9",
"Ａ":"A","Ｂ":"B","Ｃ":"C","Ｄ":"D","Ｅ":"E","Ｆ":"F","Ｇ":"G","Ｈ":"H","Ｉ":"I","Ｊ":"J","Ｋ":"K","Ｌ":"L","Ｍ":"M","Ｎ":"N","Ｏ":"O","Ｐ":"P","Ｑ":"Q","Ｒ":"R","Ｓ":"S","Ｔ":"T","Ｕ":"U","Ｖ":"V","Ｗ":"W","Ｘ":"X","Ｙ":"Y","Ｚ":"Z",
"ａ":"a","ｂ":"b","ｃ":"c","ｄ":"d","ｅ":"e","ｆ":"f","ｇ":"g","ｈ":"h","ｉ":"i","ｊ":"j","ｋ":"k","ｌ":"l","ｍ":"m","ｎ":"n","ｏ":"o","ｐ":"p","ｑ":"q","ｒ":"r","ｓ":"s","ｔ":"t","ｕ":"u","ｖ":"v","ｗ":"w","ｘ":"x","ｙ":"y","ｚ":"z",
"！":"!","？":"?","＆":"&","＃":"#","＋":"+","，":",","：":":","（":"(","）":")","／":"/","％":"%","♯":"#","．":".","～":"〜"
})

already = set([])

type_names = ["新","再","終","手","字","双","デ","S","二","多","解","SS","B","N","天","交","映","料","前","後","初","生","HV","PV","PS","吹","契","幕","無","PG12","R15","4K","HDR","5.1ch","8K","22.2ch"]

# キー局との差分抽出に使う配列
main_channels = ["NTV", "TBS", "CX", "EX", "TX", "CTC", "MTV", "SUN", "ABS", "TSK", "KYT", "BS1", "BS4", "BS5", "BS6", "BS7", "BS8", "G10", "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20", "G21", "G22", "G23", "G25", "G26", "G28", "G30", "G31", "G32", "G33", "G34", "G35", "G36", "G37", "G38", "G39", "G40", "G41", "G42", "G43", "G44", "G45", "G46", "G47", "G48", "G49", "G50", "G51", "G52", "G53", "G54", "G55", "G56", "G57", "G58", "G59", "G60", "G61", "G62", "Gkk", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E40", "E46", "E47", "E48", "E49", "E50", "E51", "E52", "E53", "E54", "E55", "E56", "E57", "E58", "E59", "E60", "E61", "E62", "Ekk", "sG23", "sE23"]
# 並び順はどうでもよく、含むかどうかを調べたい場合はsetを使う
standard_programs_set = {}
# タイトルは同じだが概要文が違う物の検出に使う
standard_programs_set_nodesc = {}
# 並び順を持たせたい場合は普通の配列を使う
standard_programs_timeline = {}
# 最後の番組の放映時間
standard_lasttime_interval = {}


def reset_temporary_data():
	global already, main_channels, standard_programs_set, standard_programs_set_nodesc, standard_programs_timeline, standard_lasttime_interval

	already = set([])

	for c in main_channels:
		standard_programs_set[c] = set({})
		standard_programs_set_nodesc[c] = set({})
		standard_programs_timeline[c] = []
		standard_lasttime_interval[c] = 0

def sanitize(s):
	sanitized = s.replace("<wbr/>","").replace("<br>","\\n").replace("\"","\\\"").replace("　"," ").replace("\n","\\n").replace("\u3000", " ").replace("&amp;","&").replace("&quot;","”").replace("&lt;","＜").replace("&gt;","＞").replace("&#39;","’").replace("‼","!!").replace("⁉","!?").replace("🈀","ほか").strip().translate(trans_table)
	return " ".join(sanitized.split())

def to_base50(n,fix):
	# fix=Trueの時は2桁固定
	if n < 50:
		if fix:
			return "A" + abc_list[n]
		else:
			return abc_list[n]
	elif n < 2500:
		return abc_list[math.floor(n/50)] + abc_list[n%50]
	else:
		#print("OVERFLOW")
		return ""

def append_type_name(s):
	if s in type_names:
		return type_names.index(s)
	else:
		type_names.append(s)
	return len(type_names)-1

def time_base60(time):
	hour = base60[math.floor((int)(time) / 100)]
	minute = base60[(int)(time) % 100]
	return hour + minute

def time_decode_base60(string):
	hour = base60.index(string[0])
	minute = base60.index(string[1])
	if hour < 10:
		hour_string = "0" + str(hour)
	else:
		hour_string = str(hour)
	if minute < 10:
		minute_string = "0" + str(minute)
	else:
		minute_string = str(minute)
	return hour_string + minute_string

def get_my_key_station(station_tag):
	if station_tag in tvlist.NHK_NET:
		return "G23"
	elif station_tag in tvlist.ETV_NET:
		return "E23"
	elif station_tag in tvlist.NTV_NET:
		return "NTV"
	elif station_tag in tvlist.TBS_NET:
		return "TBS"
	elif station_tag in tvlist.CX_NET:
		return "CX"
	elif station_tag in tvlist.EX_NET or station_tag == "EX2":
		return "EX"
	elif station_tag in tvlist.TX_NET:
		return "TX"
	elif station_tag == "CTC2" or station_tag == "CTC3":
		return "CTC"
	elif station_tag == "MTV2":
		return "MTV"
	elif station_tag == "SUN2":
		return "SUN"
	elif station_tag == "ABS2":
		return "ABS"
	elif station_tag == "TSK2":
		return "TSK"
	elif station_tag == "KYT3":
		return "KYT"
	elif station_tag == "NB2":
		return "BS1"
	elif station_tag == "FK4" or station_tag == "BN2":
		return "BS4"
	elif station_tag == "FK5":
		return "BS5"
	elif station_tag == "FK6":
		return "BS6"
	elif station_tag == "FK7":
		return "BS7"
	elif station_tag == "FK8":
		return "BS8"
	elif station_tag.startswith("sG"):
		return station_tag[1:]
	elif station_tag.startswith("sE"):
		return station_tag[1:]
	else:
		return ""

def create_program_chunk(start_date, types, name_id, chapter_id, category, splited_by_space, desc_id = None):
	chunk = time_base60(start_date)

	# 番組情報なし
	if name_id == None:
		return chunk + "?."

	types = list(set(types))
	types.sort()
	for type in types:
		chunk += abc_list[type]
	chunk += str(name_id)
	chunk += encodeCategory(category)
	if chapter_id != None:
		chunk += to_base50(chapter_id,False)
	if desc_id != None:
		chunk += str(desc_id)
	if splited_by_space == True:
		chunk += ","
	else:
		chunk += "."

	return chunk

def get_target_html(year, month, day, area):
	global htmldata

	path = "./"+year+"/"+month+"/"+day+"/"+year+"_"+month+"_"+day+"_"+area+".html"
	if os.path.exists(path):
		f = open(path, 'r')
		htmldata = f.read()
		f.close()
		return area

	return 0

# キー局やメインチャンネルとの同時放映
def fetch_gaps(station_tag, time_from, time_to):
	if time_from != None and len(time_from) == 3:
		time_from = "0" + time_from
	if time_to != None and len(time_to) == 3:
		time_to = "0" + time_to
	keysta = get_my_key_station(station_tag)

	result = []
	fetching = False
	if time_from == None:
		fetching = True

	for chunk in standard_programs_timeline[keysta]:
		if time_from != None and time_from == time_decode_base60(chunk):
			fetching = True
		if time_to != None and time_to == time_decode_base60(chunk):
			fetching = False
		if fetching:
			result.append(chunk)
	return result

def create_diff(s, start_date, types, name_id, chapter_id, category, splited_by_space, desc_id):
	program = create_program_chunk(start_date, types, name_id, chapter_id, category, splited_by_space, desc_id)
	no_desc = create_program_chunk(start_date, types, name_id, chapter_id, category, splited_by_space)

	keysta = get_my_key_station(s)

	if s in tvlist.NHK_NET or s in tvlist.ETV_NET or s in ["ABS","TSK","KYT","sG23","sE23"]:
		standard_programs_set[s].add(program)
		standard_programs_set_nodesc[s].add(no_desc)
		standard_programs_timeline[s].append(program)
		if program in standard_programs_set[keysta]:
			return time_base60(start_date), True, True
		if no_desc in standard_programs_set_nodesc[keysta]:
			return time_base60(start_date) + "*" + str(desc_id) + ".", True, False
	elif s.startswith("sG"):
		if program in standard_programs_set["sG23"]:
			return time_base60(start_date)+"^.", True, True
	elif s.startswith("sE"):
		if program in standard_programs_set["sE23"]:
			return time_base60(start_date)+"^.", True, True
	elif s in main_channels:
		standard_programs_set[s].add(program)
		standard_programs_set_nodesc[s].add(no_desc)
		standard_programs_timeline[s].append(program)
		return program, False, False
	elif keysta != "":
		if program in standard_programs_set[keysta]:
			return time_base60(start_date), True, True
		if no_desc in standard_programs_set_nodesc[keysta]:
			return time_base60(start_date) + "*" + str(desc_id) + ".", True, False

	return program, False, False

def get_interval(start_time_string, next_time_string):
	start_hour = math.floor((int)(start_time_string) / 100)
	start_minute = (int)(start_time_string) % 100
	next_hour = math.floor((int)(next_time_string) / 100)
	next_minute = (int)(next_time_string) % 100

	interval = 0
	if start_hour < next_hour:
		interval = 60-start_minute
		start_minute = 0
		start_hour += 1
		interval += 60 * (next_hour - start_hour)

	return interval + next_minute - start_minute

def add_interval(is_yesterday, start_time_string, interval):
	start_hour = math.floor((int)(start_time_string) / 100)
	start_minute = (int)(start_time_string) % 100

	if is_yesterday and start_hour >= 20:
		start_hour = 5
		start_minute = 0

	while interval >= 60:
		start_hour += 1
		interval -= 60
	start_minute += interval
	if start_minute >= 60:
		start_hour += 1
		start_minute -= 60

	start_hour_str = str(start_hour)
	if len(start_hour_str) == 1:
		start_hour_str = "0" + start_hour_str
	start_minute_str = str(start_minute)
	if len(start_minute_str) == 1:
		start_minute_str = "0" + start_minute_str

	return start_hour_str + start_minute_str

def get_week_of_year(year, month, day):
	return datetime.date((int)(year), (int)(month), (int)(day)).isocalendar()[1]

def get_day_of_week(year, month, day):
	return datetime.date((int)(year), (int)(month), (int)(day)).weekday()

def get_splitter_data(year, month):
	global splitter_data

	lines = []
	if os.path.exists("./splitter.txt"):
		f = open("./splitter.txt", 'r')
		a = f.read()
		lines = a.split("\n")
		f.close()

	splitter_data = {}
	stations = []
	for line in lines:
		if line.startswith(">"):
			stations = line.split(" ")[1:]
		elif line.startswith("#"):
			continue
		elif "-" in line:
			splited1 = line.split(" ")
			splited2 = splited1[0].split("-")
			from_year = splited2[0][:4]
			from_month = splited2[0][4:]
			to_year = splited2[1][:4]
			to_month = splited2[1][4:]
			for station in stations:
				if from_year < year or (from_year == year and from_month <= month) and year < to_year or (year == from_year and month <= to_month):
					if station not in splitter_data:
						splitter_data[station] = ""
					if splitter_data[station] != "":
						splitter_data[station] += "|"
					splitter_data[station] += " ".join(splited1[1:])

def split_title_chapter(title_string, station_tag, year, month):
	chapterPointer = 0
	bracePointer = 0
	trianglePointer = 0
	splitPointer = 0

	# 決め打ち
	if station_tag in splitter_data:
		matchObj = re.search(splitter_data[station_tag], title_string)
		if matchObj:
			if matchObj.end() < len(title_string):
				splitPointer = matchObj.end()

	if splitPointer == 0:
		# 最も一般的なチャプター表記
		matchObj = re.search(r'#[0-9]+', title_string)
		if matchObj and matchObj.start() >= 2:
			chapterPointer = matchObj.start()

		# サンテレビ
		if chapterPointer == 0 and station_tag == "SUN":
			matchObj = re.search(r'\(第.{1,3}話\)', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		# 括弧数字よりは「第何話」を優先
		if chapterPointer == 0:
			matchObj = re.search(r'第.{1,4}(話|節|日|戦)', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		# 次に一般的な、括弧数字のチャプター表記
		if chapterPointer == 0:
			matchObj = re.search(r'\([0-9]+\)', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		# 丸数字
		if chapterPointer == 0:
			matchObj = re.search(r'①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩|⑪|⑫|⑬|⑭|⑮|⑯|⑰|⑱|⑲|⑳', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		# BS釣りビジョンのチャプター表記
		if chapterPointer == 0 and station_tag == "BSF":
			matchObj = re.search(r'[0-9]+ ', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		# 頭の「第何回」はタイトルの一部とみなす
		if chapterPointer == 0:
			matchObj = re.search(r'第.{1,4}回', title_string)
			if matchObj and matchObj.start() >= 1:
				chapterPointer = matchObj.start()

		if chapterPointer == 0:
			matchObj = re.search(r' [0-9]+話', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		if chapterPointer == 0:
			matchObj = re.search(r' 最終話| 最終回| 最終日| 準々決勝| 準決勝| 決勝', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		if chapterPointer == 0:
			matchObj = re.search(r'第[0-9]+章', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		if chapterPointer == 0:
			matchObj = re.search(r'[0-9]+回戦', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		if chapterPointer == 0 and station_tag in ["JS1","JS2","JS3","JS4"]:
			matchObj = re.search(r'\[*Part[0-9]\]*', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		if chapterPointer == 0:
			matchObj = re.search(r'※一部地域は放送休止', title_string)
			if matchObj:
				chapterPointer = matchObj.start()

		# 長野放送のサブタイトル
		if station_tag == "NBS":
			matchObj = re.search(r'＜[^＜＞]+(＞|…)(#[0-9]+)*$', title_string)
			if matchObj:
				bracePointer = matchObj.start()

		# 括弧書きのサブタイトル
		# r'】\s*第.{1,3}話' のような場合の括弧は、タイトル本体の可能性があるので除外
		if bracePointer == 0:
			matchObj = re.search(r'【', title_string)
			dontMatchObj1 = re.search(r'】\s*第.{1,3}話', title_string)
			if matchObj and matchObj.start() >= 1 and not dontMatchObj1:
				bracePointer = matchObj.start()

		if bracePointer == 0:
			matchObj = re.search(r'「', title_string)
			dontMatchObj1 = re.search(r'」\s*第.{1,3}話', title_string)
			if station_tag in ["FCT","NST"]:
				dontMatchObj2 = False
			else:
				dontMatchObj2 = re.search(r'」\s*#[0-9]+', title_string)
			dontMatchObj3 = re.search(r'(映画|ドラマ|アニメ|主演)「', title_string)
			if matchObj and matchObj.start() >= 1 and not dontMatchObj1 and not dontMatchObj2 and not dontMatchObj3:
				bracePointer = matchObj.start()

		if bracePointer == 0:
			matchObj = re.search(r'『', title_string)
			dontMatchObj1 = re.search(r'』\s*第.{1,3}話', title_string)
			dontMatchObj2 = re.search(r'』\s*#[0-9]+', title_string)
			dontMatchObj3 = re.search(r'(映画|ドラマ|アニメ|主演)『', title_string)
			if matchObj and matchObj.start() >= 1 and not dontMatchObj2 and not dontMatchObj3:
				bracePointer = matchObj.start()

		# 一般的なサブタイトル表記(ただしTOKYOMXは★マーク)
		if station_tag != "MX":
			matchObj = re.search(r'▽|▼', title_string)
			if matchObj and matchObj.start() >= 3:
				trianglePointer = matchObj.start()

		# TBS系などで多いサブタイトル表記(ただしディズニーチャンネルは必ずチャプター番号があるので星マークは無視する)
		if station_tag != "DCH":
			matchObj = re.search(r'★', title_string)
			if matchObj and matchObj.start() >= 4 and (trianglePointer == 0 or matchObj.start() < trianglePointer):
				trianglePointer = matchObj.start()

		# たまにあるサブタイトル表記（タイトル本体との区別が難しい）
		if station_tag != "DCH" and station_tag != "SUN":
			matchObj = re.search(r'☆', title_string)
			if matchObj and matchObj.start() >= 5 and (trianglePointer == 0 or matchObj.start() < trianglePointer):
				trianglePointer = matchObj.start()

		# たまにあるサブタイトル表記
		matchObj = re.search(r'◇', title_string)
		if matchObj and matchObj.start() >= 4 and (trianglePointer == 0 or matchObj.start() < trianglePointer):
			trianglePointer = matchObj.start()

		# 鹿児島のサブタイトル表記
		if station_tag == "KTS" or station_tag == "KKB":
			matchObj = re.search(r'◆', title_string)
			if matchObj and matchObj.start() >= 4 and (trianglePointer == 0 or matchObj.start() < trianglePointer):
				trianglePointer = matchObj.start()

		# チャプター・括弧・記号のどれを優先するか（仮）
		if chapterPointer !=0 and bracePointer != 0 and trianglePointer !=0:
			splitPointer = min(chapterPointer, bracePointer)
		elif chapterPointer !=0 and bracePointer != 0:
			splitPointer = min(chapterPointer, bracePointer)
		elif chapterPointer != 0 and trianglePointer !=0:
			splitPointer = min(chapterPointer, trianglePointer)
		elif trianglePointer !=0 and bracePointer != 0:
			splitPointer = min(trianglePointer, bracePointer)
		elif chapterPointer !=0:
			splitPointer = chapterPointer
		elif bracePointer !=0:
			splitPointer = bracePointer
		elif trianglePointer !=0:
			splitPointer = trianglePointer

	splited_by_space = False
	if splitPointer == 0:
		title_part = title_string
		chapter_part = None
	else:
		title_part = title_string[:splitPointer]
		chapter_part = title_string[splitPointer:]
		if title_part[-1] == " ":
			title_part = title_part[:-1]
			splited_by_space = True
		if chapter_part[0] == " ":
			chapter_part = chapter_part[1:]
			splited_by_space = True

	return title_part, chapter_part, splited_by_space

def encodeCategory(n):
	n1 = n[:3]
	n2 = n[3:]
	c1 = "P"
	c2 = "P"

	if n1 == "100":
		c1 = "A"
	elif n1 == "101":
		c1 = "B"
	elif n1 == "102":
		c1 = "C"
	elif n1 == "103":
		c1 = "D"
	elif n1 == "104":
		c1 = "E"
	elif n1 == "105":
		c1 = "F"
	elif n1 == "106":
		c1 = "G"
	elif n1 == "107":
		c1 = "H"
	elif n1 == "108":
		c1 = "I"
	elif n1 == "109":
		c1 = "J"
	elif n1 == "110":
		c1 = "K"
	elif n1 == "111":
		c1 = "L"
	elif n1 == "112":
		c1 = "M"
	elif n1 == "113":
		c1 = "N"
	elif n1 == "114":
		c1 = "O"
	elif n1 == "115":
		c1 = "P"

	if n2 == "100":
		c2 = "A"
	elif n2 == "101":
		c2 = "B"
	elif n2 == "102":
		c2 = "C"
	elif n2 == "103":
		c2 = "D"
	elif n2 == "104":
		c2 = "E"
	elif n2 == "105":
		c2 = "F"
	elif n2 == "106":
		c2 = "G"
	elif n2 == "107":
		c2 = "H"
	elif n2 == "108":
		c2 = "I"
	elif n2 == "109":
		c2 = "J"
	elif n2 == "110":
		c2 = "K"
	elif n2 == "111":
		c2 = "L"
	elif n2 == "112":
		c2 = "M"
	elif n2 == "113":
		c2 = "N"
	elif n2 == "114":
		c2 = "O"
	elif n2 == "115":
		c2 = "P"

	return c1 + c2
