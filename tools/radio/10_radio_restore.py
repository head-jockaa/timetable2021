# coding:utf-8
import os
import math
import datetime
import radio_util
import radiolist
import nhk_radio

base64_special = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","$","{","|","}",";","*","_","~","^","`","'"]

def get_station_name(s):
	if s == "HBC":
		return "ＨＢＣラジオ"
	elif s == "STV":
		return "ＳＴＶラジオ"
	elif s == "AIRG":
		return "AIR-G&#39;（FM北海道）"
	elif s == "NORTHWAVE":
		return "FM NORTH WAVE"
	elif s == "RAB":
		return "ＲＡＢ青森放送"
	elif s == "AFB":
		return "エフエム青森"
	elif s == "IBC":
		return "IBCラジオ"
	elif s == "FMI":
		return "エフエム岩手"
	elif s == "TBC":
		return "TBCラジオ"
	elif s == "DATEFM":
		return "Date fm エフエム仙台"
	elif s == "ABS":
		return "ＡＢＳ秋田放送"
	elif s == "AFM":
		return "エフエム秋田"
	elif s == "YBC":
		return "YBC山形放送"
	elif s == "RFM":
		return "Rhythm Station　エフエム山形"
	elif s == "RFC":
		return "RFCラジオ福島"
	elif s == "FMF":
		return "ふくしまFM"
	elif s == "TBS":
		return "TBSラジオ"
	elif s == "QRR":
		return "文化放送"
	elif s == "LFR":
		return "ニッポン放送"
	elif s == "INT":
		return "InterFM897"
	elif s == "FMT":
		return "TOKYO FM"
	elif s == "FMJ":
		return "J-WAVE"
	elif s == "JORF":
		return "ラジオ日本"
	elif s == "BAYFM78":
		return "bayfm78"
	elif s == "NACK5":
		return "NACK5"
	elif s == "YFM":
		return "ＦＭヨコハマ"
	elif s == "IBS":
		return "LuckyFM 茨城放送"
	elif s == "CRT":
		return "CRT栃木放送"
	elif s == "RADIOBERRY":
		return "RadioBerry"
	elif s == "FMGUNMA":
		return "FM GUNMA"
	elif s == "BSN":
		return "ＢＳＮラジオ"
	elif s == "FMNIIGATA":
		return "FM NIIGATA"
	elif s == "KNB":
		return "ＫＮＢラジオ"
	elif s == "FMTOYAMA":
		return "ＦＭとやま"
	elif s == "MRO":
		return "MROラジオ"
	elif s == "HELLOFIVE":
		return "エフエム石川"
	elif s == "FBC":
		return "FBCラジオ"
	elif s == "FMFUKUI":
		return "FM福井"
	elif s == "YBS":
		return "ＹＢＳラジオ"
	elif s == "FMFUJI":
		return "FM FUJI"
	elif s == "SBC":
		return "SBCラジオ"
	elif s == "FMN":
		return "ＦＭ長野"
	elif s == "CBC":
		return "CBCラジオ"
	elif s == "TOKAIRADIO":
		return "東海ラジオ"
	elif s == "GBS":
		return "ぎふチャン"
	elif s == "ZIPFM":
		return "ZIP-FM"
	elif s == "FMAICHI":
		return "FM AICHI"
	elif s == "FMGIFU":
		return "ＦＭ ＧＩＦＵ"
	elif s == "SBS":
		return "SBSラジオ"
	elif s == "KMIX":
		return "K-MIX SHIZUOKA"
	elif s == "FMMIE":
		return "レディオキューブ ＦＭ三重"
	elif s == "ABC":
		return "ABCラジオ"
	elif s == "MBS":
		return "MBSラジオ"
	elif s == "OBC":
		return "OBCラジオ大阪"
	elif s == "CCL":
		return "FM COCOLO"
	elif s == "802":
		return "FM802"
	elif s == "FMO":
		return "FM大阪"
	elif s == "KISSFMKOBE":
		return "Kiss FM KOBE"
	elif s == "CRK":
		return "ラジオ関西"
	elif s == "ERADIO":
		return "e-radio FM滋賀"
	elif s == "KBS":
		return "KBS京都ラジオ"
	elif s == "ALPHASTATION":
		return "α-STATION FM京都"
	elif s == "WBS":
		return "wbs和歌山放送"
	elif s == "BSS":
		return "BSSラジオ"
	elif s == "FMSANIN":
		return "エフエム山陰"
	elif s == "RSK":
		return "ＲＳＫラジオ"
	elif s == "FMOKAYAMA":
		return "ＦＭ岡山"
	elif s == "RCC":
		return "RCCラジオ"
	elif s == "HFM":
		return "広島FM"
	elif s == "KRY":
		return "ＫＲＹ山口放送"
	elif s == "FMY":
		return "エフエム山口"
	elif s == "JRT":
		return "ＪＲＴ四国放送"
	elif s == "FM807":
		return "FM徳島"
	elif s == "RNC":
		return "RNC西日本放送"
	elif s == "FMKAGAWA":
		return "エフエム香川"
	elif s == "RNB":
		return "RNB南海放送"
	elif s == "JOEUFM":
		return "FM愛媛"
	elif s == "RKC":
		return "RKC高知放送"
	elif s == "HISIX":
		return "エフエム高知"
	elif s == "RKB":
		return "RKBラジオ"
	elif s == "KBC":
		return "KBCラジオ"
	elif s == "LOVEFM":
		return "LOVE FM"
	elif s == "CROSSFM":
		return "CROSS FM"
	elif s == "FMFUKUOKA":
		return "FM FUKUOKA"
	elif s == "FMS":
		return "エフエム佐賀"
	elif s == "NBC":
		return "NBC長崎放送"
	elif s == "FMNAGASAKI":
		return "FM長崎"
	elif s == "RKK":
		return "RKKラジオ"
	elif s == "FMK":
		return "FMKエフエム熊本"
	elif s == "OBS":
		return "OBSラジオ"
	elif s == "FMOITA":
		return "エフエム大分"
	elif s == "MRT":
		return "宮崎放送"
	elif s == "JOYFM":
		return "エフエム宮崎"
	elif s == "MBC":
		return "ＭＢＣラジオ"
	elif s == "MYUFM":
		return "μＦＭ"
	elif s == "RBC":
		return "RBCiラジオ"
	elif s == "ROK":
		return "ラジオ沖縄"
	elif s == "FMOKINAWA":
		return "FM沖縄"
	elif s == "RN1":
		return "ラジオNIKKEI第1"
	elif s == "RN2":
		return "ラジオNIKKEI第2"
	elif s == "HOUSOUDAIGAKU":
		return "放送大学"
	return ""

def get_decoder():
	result = []
	f = open("scripts/radio_decoder.js", "r")
	aaa = f.read().split('"')
	result.append(aaa[1])
	result.append(aaa[3])
	result.append(aaa[5])
	f.close()
	return result

def load_hash_array(filename):
	f = open(filename, "r")
	jsfile = f.read()
	f.close()

	BEGIN = 0
	MAINKEY = 1
	MAINKEY_COLON = 2
	HASH_VALUE_KEY = 3
	HASH_VALUE_KEY_COLON = 4
	HASH_VALUE_VALUE = 5
	HASH_VALUE_COMMA = 6
	MAIN_COMMA = 7
	END = 8
	PLAIN_VALUE = 9
	HASH_VALUE_HASH_VALUE_KEY = 10
	HASH_VALUE_HASH_VALUE_KEY_COLON = 11
	HASH_VALUE_HASH_VALUE_VALUE = 12
	HASH_VALUE_HASH_VALUE_COMMA = 13
	ARRAY = 14
	ARRAY_VALUE = 15
	ARRAY_COMMA = 16
	ARRAY_TUPLE1 = 17
	ARRAY_TUPLE1_VALUE = 18
	ARRAY_TUPLE_COMMA = 19
	ARRAY_TUPLE2 = 20
	ARRAY_TUPLE2_ARRAY = 21
	ARRAY_TUPLE2_ARRAY_VALUE = 22
	ARRAY_TUPLE2_ARRAY_COMMA = 23

	mode = BEGIN
	s = ""
	keyname = ""
	keyname2 = ""
	keyname3 = ""
	tuple = ["",[]]
	result = None
	for a in jsfile:
		if mode == BEGIN:
			if a == "[":
				mode = ARRAY
				result = []
			elif a == "{":
				mode = MAINKEY
				s = ""
				result = {}
		elif mode == ARRAY:
			if a == "[":
				mode = ARRAY_TUPLE1
				tuple = ["",[]]
			elif a == "\"":
				mode = ARRAY_VALUE
				s = ""
		elif mode == ARRAY_VALUE:
			if a == "\"":
				mode = ARRAY_COMMA
				result.append(s)
			else:
				s += a
		elif mode == ARRAY_COMMA:
			if a == ",":
				mode = ARRAY
				s = ""
			elif a == "]":
				mode = END

		elif mode == ARRAY_TUPLE1:
			if a == "\"":
				mode = ARRAY_TUPLE1_VALUE
				s = ""
		elif mode == ARRAY_TUPLE1_VALUE:
			if a == "\"":
				mode = ARRAY_TUPLE_COMMA
				tuple[0] = s
			else:
				s += a
		elif mode == ARRAY_TUPLE_COMMA:
			if a == ",":
				mode = ARRAY_TUPLE2
			elif a == "]":
				mode = ARRAY
				result.append(tuple)
		elif mode == ARRAY_TUPLE2:
			if a == "[":
				mode = ARRAY_TUPLE2_ARRAY
				s = ""
		elif mode == ARRAY_TUPLE2_ARRAY:
			if a == "\"":
				mode = ARRAY_TUPLE2_ARRAY_VALUE
				s = ""
		elif mode == ARRAY_TUPLE2_ARRAY_VALUE:
			if a == "\"":
				mode = ARRAY_TUPLE2_ARRAY_COMMA
				tuple[1].append(s)
			else:
				s += a
		elif mode == ARRAY_TUPLE2_ARRAY_COMMA:
			if a == ",":
				mode = ARRAY_TUPLE2_ARRAY
			elif a == "]":
				mode = ARRAY_TUPLE_COMMA

		elif mode == MAINKEY:
			if a == ":":
				mode = MAINKEY_COLON
				keyname = s
			elif a not in [" ","\n","\r","\t"]:
				s += a
		elif mode == MAINKEY_COLON:
			if a == "{":
				mode = HASH_VALUE_KEY
				result[keyname] = {}
				s = ""
			elif a == "\"":
				mode = PLAIN_VALUE
				result[keyname] = ""
				s = ""
		elif mode == HASH_VALUE_KEY:
			if a == "}":
				mode = MAIN_COMMA
			elif a == ":":
				keyname2 = s
				mode = HASH_VALUE_KEY_COLON
			elif a not in [" ","\n","\r","\t"]:
				s += a
		elif mode == HASH_VALUE_KEY_COLON:
			if a == "{":
				mode = HASH_VALUE_HASH_VALUE_KEY
				result[keyname][keyname2] = {}
				s = ""
			elif a == "\"":
				mode = HASH_VALUE_VALUE
				s = ""
		elif mode == HASH_VALUE_VALUE:
			if a == "\"":
				mode = HASH_VALUE_COMMA
				result[keyname][keyname2] = s
			else:
				s += a
		elif mode == HASH_VALUE_HASH_VALUE_KEY:
			if a == "}":
				mode = HASH_VALUE_COMMA
			elif a == ":":
				keyname3 = s
				mode = HASH_VALUE_HASH_VALUE_KEY_COLON
			elif a not in [" ","\n","\r","\t"]:
				s += a
		elif mode == HASH_VALUE_HASH_VALUE_KEY_COLON:
			if a == "\"":
				mode = HASH_VALUE_HASH_VALUE_VALUE
				s = ""
		elif mode == HASH_VALUE_HASH_VALUE_VALUE:
			if a == "\"":
				mode = HASH_VALUE_HASH_VALUE_COMMA
				result[keyname][keyname2][keyname3] = s
			else:
				s += a
		elif mode == PLAIN_VALUE:
			if a == "\"":
				mode = MAIN_COMMA
				result[keyname] = s
			else:
				s += a
		elif mode == HASH_VALUE_COMMA:
			if a == ",":
				mode = HASH_VALUE_KEY
				s = ""
			elif a == "}":
				mode = MAIN_COMMA
		elif mode == HASH_VALUE_HASH_VALUE_COMMA:
			if a == ",":
				mode = HASH_VALUE_HASH_VALUE_KEY
				s = ""
			elif a == "}":
				mode = HASH_VALUE_COMMA
		elif mode == MAIN_COMMA:
			if a == ",":
				mode = MAINKEY
				s = ""
			elif a == "}":
				mode = END
	return result

def split_chunk(str):
	splited = []
	chunk = ""
	for s in str:
		if s == ":":
			chunk = splited[-1]
			splited.pop(-1)
		chunk += s
		if s == "." or s == ",":
			splited.append(chunk)
			chunk = ""
	splited.append(chunk)
	return splited

def decode_string(str):
	result = ""
	is_abc_mode = False
	is_kanji = False
	is_backslash = False
	code = 0
	for c in str:
		if is_backslash and c == 'n':
			result += "<br>"
			is_backslash = False
			continue
		if c == '\\':
			is_backslash = True
			continue
		if is_abc_mode:
			if c == '>':
				is_abc_mode = False
			else:
				result += c
		elif is_kanji:
			code = code * 64 + base64_special.index(c)
			if code < decoder1_range:
				result += decoder[0][code]
			elif code < decoder1_range + decoder2_range:
				result += decoder[1][(code - decoder1_range)*2] + decoder[1][(code - decoder1_range)*2+1]
			else:
				result += decoder[2][(code - decoder1_range - decoder2_range)*3] + decoder[2][(code - decoder1_range - decoder2_range)*3+1] + decoder[2][(code - decoder1_range - decoder2_range)*3+2]
			is_kanji = False
		elif c == '<':
			is_abc_mode = True
		elif c in base64_special:
			is_kanji = True
			code = base64_special.index(c)
		else:
			result += c
	return result

def decompressProgramChunk(month, day, tv, chunk_string):
	keysta = ""
	if tv in radiolist.NHK1_NET:
		keysta = "NHK1_130"
	elif tv in radiolist.NHKFM_NET:
		keysta = "NHKFM_130"
	elif tv in radiolist.FM_NET:
		keysta = "FMT"

	keystas_table = []
	keysta_string = ""

	if month in original_timetables and day in original_timetables[month]:
		if keysta in original_timetables[month][day]:
			keysta_string = original_timetables[month][day][keysta]

	splitedColon = keysta_string.split(":")
	keystas_table = split_chunk(splitedColon[0])

	if chunk_string == "":
		return []

	result = []
	chunks = split_chunk(chunk_string)
	for c in chunks:
		splitedColon2 = c.split(":")
		chunk = splitedColon2[0]

		splited_by_space = (chunk[-1] == ",")
		chunk = chunk[:-1]

		if len(chunk) <= 2:
			for k in keystas_table:
				if chunk == k[:2]:
					result.append(k)
		elif "*" in chunk:
			splited = chunk.split("*")
			for k in keystas_table:
				hit = False
				if splited[0] == k[:2]:
					hit = True
					for idx in reversed(range(len(k))):
						if not (k[idx] >= '0' and k[idx] <= '9') and k[idx] != '.' and k[idx] != ',':
							result.append(k[:idx+1] + splited[1] + k[-1])
							break
				if hit:
					break
		elif "-" in chunk:
			splited = chunk.split("-")
			start = False
			for k in keystas_table:
				if splited[0] == k[:2]:
					start = True
				if start:
					result.append(k)
				if splited[1] == k[:2]:
					break;
		else:
			result.append(chunk + ("," if splited_by_space else "."))

	if len(splitedColon2) == 1:
		return "".join(result)
	else:
		return "".join(result) + ":" + splitedColon2[1]

def read_chunk(chunk):
	RERUN = 0
	TITLE = 1
	CHAPTER = 2
	DESC = 3
	SPACE = 4
	INTERVAL = 5

	mode = RERUN
	s = ""
	rerun = False
	title_id = 0
	chapter_id = None
	desc_id = 0
	interval = 0
	splited_by_space = False
	for c in chunk[2:]:
		if mode == RERUN and c >= '0' and c<= '9':
			mode = TITLE
			s = ""
		elif mode == TITLE and not (c >= '0' and c<= '9'):
			title_id = int(s)
			mode = CHAPTER
		elif mode == CHAPTER and c >= '0' and c<= '9':
			mode = DESC
			s = ""
		elif mode == DESC and not (c >= '0' and c<= '9'):
			mode = SPACE
			desc_id = int(s)
			splited_by_space = (c == ',')
			continue
		elif mode == SPACE and c == ':':
			mode = INTERVAL
			s = ""
			continue

		if mode == RERUN:
			if c == "R":
				rerun = True
		elif mode == TITLE:
			s += c
		elif mode == CHAPTER:
			if c != "_":
				if chapter_id == None:
					chapter_id = 0
				chapter_id = chapter_id * 50 + abc_list.index(c)
		elif mode == DESC:
			s += c
		elif mode == INTERVAL:
			s += c

	if mode == DESC:
		desc_id = int(s)
	elif mode == INTERVAL:
		interval = int(s)

	return rerun, title_id, chapter_id, desc_id, interval, splited_by_space

def output_html(year, month, day, station):
	if not station in timetables[month][day]:
		return

	dir_path = "restore_radio" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	if station in radio_util.stations:
		url = radio_util.radiko_url_list[radio_util.stations.index(station)]
	else:
		url = station
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_" + url + ".html"
	outfile = open(file_path, "w")

	date_string = year + month + day
	outfile.write('<html><head><meta charset="utf-8" /></head><body>\n');
	outfile.write('<ul><li class="item ui-menu-accordion-title"><a data-day="' + date_string + '"></a></li></ul>\n');
	outfile.write('<ol class="breadcrumb__inner"><li></li><li></li><li>' + get_station_name(station) + '</li></ol>\n')

	outfile.write('<div class="item-outer" data-day="' + date_string + '" data-station_id="' + url + '">\n')

	idx = 0
	for chunk in timetables[month][day][station]:
		# 開始時刻
		hour = str(base60.index(chunk[0]))
		if len(hour) == 1:
			hour = "0" + str(hour)
		minute = str(base60.index(chunk[1]))
		if len(minute) == 1:
			minute = "0" + str(minute)
		start_time = hour + ":" + minute

		# 終了時刻
		if idx < len(timetables[month][day][station]) - 1:
			next_program = timetables[month][day][station][idx+1]
			hour = str(base60.index(next_program[0]))
			if len(hour) == 1:
				hour = "0" + str(hour)
			minute = str(base60.index(next_program[1]))
			if len(minute) == 1:
				minute = "0" + str(minute)
			end_time = hour + ":" + minute
		else:
			hour_int = (int)(hour)
			minute_int = (int)(minute)
			splited = chunk.split(":")
			interval = (int)(splited[1])
			while interval >= 60:
				hour_int += 1
				interval -= 60
			minute_int += interval
			if minute_int >= 60:
				hour_int += 1
				minute_int -= 60
			hour = str(hour_int)
			minute = str(minute_int)
			if len(hour) == 1:
				hour = "0" + str(hour)
			if len(minute) == 1:
				minute = "0" + str(minute)
			end_time = hour + ":" + minute
		idx += 1

		rerun, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk)

		type_string = ""
		if rerun:
			type_string = "[再]"

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		outfile.write('<div class="item"><a href="#colorbox--program" style="height: 0px;">\n');
		outfile.write('<p class="title">' + full_title + type_string + '</p>\n');
		outfile.write('<p class="cast">' + decode_string(descriptions[desc_id]) + '</p>\n');
		outfile.write('<p class="time">' + start_time + ' ～ ' + end_time + '</p>\n');
		outfile.write('</a></div>\n');

	outfile.write('</div>\n')
	outfile.write('</body></html>\n')
	outfile.close()

def output_html_nhk(year, month, day, area):
	if not "NHK1_"+area in timetables[month][day] and not "NHKFM_"+area in timetables[month][day]:
		return

	dir_path = "restore_radio" + year + "/" + month + "/" + day
	if not os.path.isdir(dir_path):
		os.makedirs(dir_path)
	file_path = dir_path + "/" + year + "_" + month + "_" + day + "_NHK" + area + ".html"
	outfile = open(file_path, "w")

	chunks = []
	if not "NHK1_"+area in timetables[month][day]:
		chunks.append({"column":0, "top":0, "height":60*30, "chunk":""})
	if not "NHKFM_"+area in timetables[month][day]:
		chunks.append({"column":2, "top":0, "height":60*30, "chunk":""})

	idx = 0
	height = 0
	if "NHK1_"+area in timetables[month][day]:
		for c in timetables[month][day]["NHK1_"+area]:
			splited = c.split(":")
			if len(splited) == 1:
				interval = radio_util.get_interval(radio_util.time_decode_base60(timetables[month][day]["NHK1_"+area][idx]), radio_util.time_decode_base60(timetables[month][day]["NHK1_"+area][idx+1]))
			else:
				interval = (int)(splited[1])
			h_m = (int)(radio_util.time_decode_base60(c))
			minute = math.floor(h_m/100)*60+(h_m%100)
			if minute-height != 0:
				chunks.append({"column":0, "top":height, "height":minute-height, "chunk":""})
				height += minute-height
			chunks.append({"column":0, "top":height, "height":interval, "chunk":c})
			height += interval
			idx += 1
		chunks.append({"column":0, "top":height, "height":60*30-height, "chunk":""})

	idx = 0
	height = 0
	if "NHKFM_"+area in timetables[month][day]:
		for c in timetables[month][day]["NHKFM_"+area]:
			splited = c.split(":")
			if len(splited) == 1:
				interval = radio_util.get_interval(radio_util.time_decode_base60(timetables[month][day]["NHKFM_"+area][idx]), radio_util.time_decode_base60(timetables[month][day]["NHKFM_"+area][idx+1]))
			else:
				interval = (int)(splited[1])
			h_m = (int)(radio_util.time_decode_base60(c))
			minute = math.floor(h_m/100)*60+(h_m%100)
			if minute-height != 0:
				chunks.append({"column":2, "top":height, "height":minute-height, "chunk":""})
				height += minute-height
			chunks.append({"column":2, "top":height, "height":interval, "chunk":c})
			height += interval
			idx += 1
		chunks.append({"column":2, "top":height, "height":60*30-height, "chunk":""})

	idx = 0
	height = 0
	if "NHK2" in timetables[month][day]:
		for c in timetables[month][day]["NHK2"]:
			splited = c.split(":")
			if len(splited) == 1:
				interval = radio_util.get_interval(radio_util.time_decode_base60(timetables[month][day]["NHK2"][idx]), radio_util.time_decode_base60(timetables[month][day]["NHK2"][idx+1]))
			else:
				interval = (int)(splited[1])
			h_m = (int)(radio_util.time_decode_base60(c))
			minute = math.floor(h_m/100)*60+(h_m%100)
			if minute-height != 0:
				chunks.append({"column":1, "top":height, "height":minute-height, "chunk":""})
				height += minute-height
			chunks.append({"column":1, "top":height, "height":interval, "chunk":c})
			height += interval
			idx += 1
		chunks.append({"column":1, "top":height, "height":60*30-height, "chunk":""})

	chunks_sorted = sorted(chunks, key=lambda x:(x["top"],x["column"]))

	outfile.write('<html><head><meta charset="utf-8" /></head><body><div area="' + nhk_area + '" date="' + year + month + day + '"><button>現在の時刻</button>\n')

	for chunk in chunks_sorted:

		rerun, title_id, chapter_id, desc_id, interval, splited_by_space = read_chunk(chunk["chunk"])

		types_string = ""
		if rerun:
			types_string += '<img src="' + nhk_radio.IMG_RE + '">'

		full_title = decode_string(titles[title_id][0])
		if splited_by_space:
			full_title += " "
		if chapter_id != None:
			full_title += decode_string(titles[title_id][1][chapter_id])

		outfile.write('<td data-v="" colspan="2" rowspan="' + str(chunk["height"]) + '">\n');
		if chunk["chunk"] != "":
			m = radio_util.time_decode_base60(chunk["chunk"])
			hour_int = math.floor((int)(m)/100)
			if hour_int < 12:
				hour = "午前" + str(hour_int)
			elif hour_int < 24:
				hour = "午後" + str(hour_int-12)
			else:
				hour = "午前" + str(hour_int-24)
			minute = str(m)[-2:]
			outfile.write('<p class="time">' + hour + ':' + minute + '</p>\n')
			outfile.write('<p><a class="to-dtl">' + full_title + '</a></p>' + types_string + '\n')
			outfile.write('<div class="arrow">' + decode_string(descriptions[desc_id]) + '</div>\n')
		outfile.write('</td>\n')

	outfile.write('</div></body></html>\n')
	outfile.close()



if __name__ == "__main__":
	global timetables, original_timetables, station_names, decoder
	global decoder1_range, decoder2_range, decoder3_range

	year = "2021"
	abc_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
	base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]

	decoder = get_decoder()
	decoder1_range = len(decoder[0])
	decoder2_range = (int)(len(decoder[1]) / 2)
	decoder3_range = (int)(len(decoder[2]) / 3)

	original_timetables = load_hash_array("scripts/radio_timetables.js")
	titles = load_hash_array("scripts/radio_titles.js")
	descriptions = load_hash_array("scripts/radio_descriptions.js")

	timetables = {}

	for month in original_timetables:
		timetables[month] = {}
		for day in original_timetables[month]:
			timetables[month][day] = {}
			for station in original_timetables[month][day]:
				result = decompressProgramChunk(month, day, station, original_timetables[month][day][station])
				timetables[month][day][station] = split_chunk(result)

	for month in timetables:
		for day in timetables[month]:
			print(year+"-"+month+"-"+day)
			for nhk_area in radio_util.nhk_areas:
				output_html_nhk(year, month, day, nhk_area)
			for station in radio_util.stations:
				output_html(year, month, day, station)
