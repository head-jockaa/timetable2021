# coding:utf-8
import os
import util

htmldata_bs141 = None
htmldata_bs142 = None

def get_html_bs141(year, month, day):
	global htmldata_bs141
	w = util.get_week_of_year(year, month, day)
	path = "./"+year+"/"+month+"/"+year+"_"+str(w)+"week_bs141.html"
	if os.path.exists(path):
		f = open(path, 'r')
		htmldata_bs141 = f.read()
		f.close()
		return True

	return False

def get_html_bs142(year, month, day):
	global htmldata_bs142
	w = util.get_week_of_year(year, month, day)
	path = "./"+year+"/"+month+"/"+year+"_"+str(w)+"week_bs142.html"
	if os.path.exists(path):
		f = open(path, 'r')
		htmldata_bs142 = f.read()
		f.close()
		return True

	return False

def extractTimetableOf(html, year, month, day):
	splited1 = html.split("rowspan=\"")
	splited1.pop(0)

	result = []
	rowspan = [0,0,0,0,0,0,0,0,0]
	target_column = util.get_day_of_week(year, month, day) + 1

	for s in splited1:

		splited2 = s.split("\"")
		interval = (int)(splited2[0])

		idx = 0
		min_row = 10000
		for i in reversed(range(9)):
			if min_row >= rowspan[i]:
				min_row = rowspan[i]
				idx = i
		rowspan[idx] += interval

		if idx != target_column:
			continue

		splited2 = s.split("__starttime\">\n          ")
		if len(splited2) == 1:
			continue
		splited3 = splited2[1].split("\n")
		start_time = splited3[0].replace("：","")

		types = []
		splited2 = s.split("__title\">")
		if "icon-new" in splited2[0]:
			types.append(util.append_type_name("新"))
		if "icon-end" in splited2[0]:
			types.append(util.append_type_name("終"))
		if "icon-fpart" in splited2[0]:
			types.append(util.append_type_name("前"))
		if "icon-lpart" in splited2[0]:
			types.append(util.append_type_name("後"))
		if "icon-live" in splited2[0]:
			types.append(util.append_type_name("生"))
		if "icon-repeat" in splited2[0]:
			types.append(util.append_type_name("再"))
		if "icon-bilingual" in splited2[0]:
			types.append(util.append_type_name("二"))
		if "icon-multiplex" in splited2[0]:
			types.append(util.append_type_name("多"))
		if "icon-stereo" in splited2[0]:
			types.append(util.append_type_name("S"))
		if "icon-ss" in splited2[0]:
			types.append(util.append_type_name("SS"))
		if "icon-caption" in splited2[0]:
			types.append(util.append_type_name("字"))
		if "icon-data" in splited2[0]:
			types.append(util.append_type_name("デ"))
		if "icon-bidirectional" in splited2[0]:
			types.append(util.append_type_name("双"))

		title_name = ""
		splited2 = s.split("__title\">")
		if len(splited2) != 1:
			splited3 = splited2[1].split("</div>")
			title_name = splited3[0].replace("[新]","").replace("[終]","").replace("[再]","").replace("[字]","").replace("[デ]","").replace("[多]","")
			title_name = util.sanitize(title_name)

		result.append({"start":start_time, "interval":interval, "types":types, "title":title_name})

	return result

def getCategoryCode(title_name):
	if "Music" in title_name or "MUSIC" in title_name or "サウンド" in title_name or "歌謡曲" in title_name or "最新曲" in title_name or title_name == "ヒーリングデイズ" or title_name == "J−POPヒストリー":
		return "104100"
	elif "BASEBALL" in title_name:
		return "101101"
	elif "ラグビー" in title_name or "B.LEAGUE" in title_name:
		return "101104"
	elif "バスケットボールワールドカップ" in title_name:
		return "101106"
	elif "お得α" == title_name:
		return "102104"
	else:
		return "115115"
