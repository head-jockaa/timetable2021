# coding:utf-8
import os
import sys
import radio_util
import radiolist
import nhk_radio
import radiko


def create_diff(st, start_date, rerun, name_id, chapter_id, splited_by_space, desc_id):
	result, title_omitted, desc_omitted = radio_util.create_diff(st, start_date, rerun, name_id, chapter_id, splited_by_space, desc_id)

	return result

def get_title_id(title_name, chapter_name):
	if chapter_name == None:
		return titles[title_name][0], None
	else:
		return titles[title_name][0], titles[title_name][1][chapter_name]

def get_description_id(d):
	return descriptions[d]

def get_timetable_nhk(year, month, day, area):
	result = radio_util.get_target_html(year, month, day, "NHK"+area)
	if result == 0:
		return None

	nhk_radio.checkContent(radio_util.htmldata, year, month, day, area)

	nhk_stations = {}
	station_tags = nhk_radio.getTargetPrograms(area)
	rowspan = [0,0,0]
	isFirst = [True, True, True]
	isAfternoon = [False, False, False]
	last_programs_interval = [0,0,0]

	program_part = nhk_radio.extractTodays(radio_util.htmldata)
	program_cells = nhk_radio.splitByItem(program_part)

	for program_cell in program_cells:

		# 放映時間
		interval = nhk_radio.getInterval(program_cell)

		idx = 0
		min_row = 10000
		for i in reversed(range(3)):
			if min_row >= rowspan[i]:
				min_row = rowspan[i]
				idx = i
		rowspan[idx] += interval

		# スキップ
		if station_tags[idx] == "":
			continue

		# 時刻
		start_time, isAfternoon[idx] = nhk_radio.extractStartTime(program_cell, isAfternoon[idx])
		if start_time == "":
			continue
		if isFirst[idx]:
			isAfternoon[idx] = False		

		# 題名
		title_string = nhk_radio.extractTitle(program_cell)
		title_name, chapter_name, rerun, splited_by_space = radio_util.split_title_chapter(title_string, station_tags[idx], year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)

		# 概要
		description = nhk_radio.extractDescription(program_cell)
		desc_id = get_description_id(description)

		# 再放送
		if nhk_radio.IMG_RE in program_cell:
			rerun = True

		bar = create_diff(station_tags[idx], start_time, rerun, name_id, chapter_id, splited_by_space, desc_id)
		last_programs_interval[idx] = interval

		if station_tags[idx] not in nhk_stations:
			nhk_stations[station_tags[idx]] = []
		nhk_stations[station_tags[idx]].append(bar)

		isFirst[idx] = False

	# 連続する「フォーマット2」の間をハイフンで省略
	for sta in station_tags:
		if sta not in nhk_stations:
			continue

		standards_sorted = []
		my_standard_programs = radio_util.get_my_standard_programs(sta)
		for p in my_standard_programs:
			standards_sorted.append(p[:2])

		programs2 = []
		idx = 0
		foundNum = 0
		fountAt = 0
		pre_program = ""

		for program in nhk_stations[sta]:
			if (len(program)) <= 2:

				if foundNum != 0 and program in standards_sorted and pre_program in standards_sorted:
					if standards_sorted.index(pre_program) + 1 != standards_sorted.index(program):
						#print(radio_util.time_decode_base60(program) + " " + sta)
						programs2.append(nhk_stations[sta][foundAt]+"-"+pre_program+".")
						foundNum = 0

				if foundNum == 0:
					foundAt = idx
				foundNum += 1
			else:
				if foundNum == 1:
					programs2.append(nhk_stations[sta][idx-1]+".")
				elif foundNum == 2:
					programs2.append(nhk_stations[sta][idx-2]+".")
					programs2.append(nhk_stations[sta][idx-1]+".")
				elif foundNum >= 3:
					programs2.append(nhk_stations[sta][foundAt]+"-"+nhk_stations[sta][idx-1]+".")
				programs2.append(program)
				foundNum = 0
			idx += 1
			pre_program = program

		if foundNum == 1:
			programs2.append(nhk_stations[sta][idx-1]+".")
		elif foundNum == 2:
			programs2.append(nhk_stations[sta][idx-2]+".")
			programs2.append(nhk_stations[sta][idx-1]+".")
		elif foundNum >= 3:
			programs2.append(nhk_stations[sta][foundAt]+"-"+nhk_stations[sta][idx-1]+".")

		nhk_stations[sta] = programs2

	# 最後の番組の放映時間
	for i in range(3):
		if station_tags[i] not in nhk_stations:
			continue
		nhk_stations[station_tags[i]][-1] = nhk_stations[station_tags[i]][-1] + ":" + str(last_programs_interval[i])

	return nhk_stations

def get_timetable(year,month,day,station):
	result = radio_util.get_target_html(year,month,day,station)
	if result == 0:
		return None

	radiko.checkContent(radio_util.htmldata, year, month, day, station)

	station_tag = radiolist.get_station_name_tag(radiko.extractStationName(radio_util.htmldata))

	todays_program = radiko.extractTodays(radio_util.htmldata, year, month, day)

	program_parts = radiko.splitByItem(todays_program)
	programs = []
	for program_part in program_parts:

		# 時刻
		start_time, end_time = radiko.extractStartAndEndTime(program_part)

		# 題名
		title_string = radiko.extractTitle(program_part)
		title_name, chapter_name, rerun, splited_by_space = radio_util.split_title_chapter(title_string, station_tag, year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)

		# 概要
		description = radiko.extractDescription(program_part)
		desc_id = get_description_id(description)

		bar = create_diff(station_tag, start_time, rerun, name_id, chapter_id, splited_by_space, desc_id)
		programs.append(bar)

	# 連続する「フォーマット2」の間をハイフンで省略
	standards_sorted = []
	my_standard_programs = radio_util.get_my_standard_programs(station_tag)
	for p in my_standard_programs:
		standards_sorted.append(p[:2])

	programs2 = []
	idx = 0
	foundNum = 0
	fountAt = 0
	pre_program = ""

	for program in programs:
		if (len(program)) <= 2:

			if foundNum != 0 and program in standards_sorted and pre_program in standards_sorted:
				if standards_sorted.index(pre_program) + 1 != standards_sorted.index(program):
					#print(radio_util.time_decode_base60(program) + " " + station_tag)
					programs2.append(programs[foundAt]+"-"+pre_program+".")
					foundNum = 0

			if foundNum == 0:
				foundAt = idx
			foundNum += 1
		else:
			if foundNum == 1:
				programs2.append(programs[idx-1]+".")
			elif foundNum == 2:
				programs2.append(programs[idx-2]+".")
				programs2.append(programs[idx-1]+".")
			elif foundNum >= 3:
				programs2.append(programs[foundAt] + "-" + programs[idx-1]+".")
			programs2.append(program)
			foundNum = 0
		idx += 1
		pre_program = program

	if foundNum == 1:
		programs2.append(programs[idx-1]+".")
	elif foundNum == 2:
		programs2.append(programs[idx-2]+".")
		programs2.append(programs[idx-1]+".")
	elif foundNum >= 3:
		programs2.append(programs[foundAt] + "-" + programs[idx-1]+".")

	# 最後の番組の放映時間
	programs2[-1] = programs2[-1] + ":" + str(radio_util.get_interval(start_time, end_time))

	return {"name":station_tag, "programs":programs2}

def read_titles():
	global titles
	f = open("scripts/radio_titles_raw.js", 'r')
	jsdata = f.read()
	f.close()

	BRACE0 = 1
	BRACE1 = 2
	BRACE1_QUOT = 3
	BRACE2 = 4
	BRACE2_QUOT = 5

	mode = 0
	title_id = 0
	chapter_id = 0
	titles = {}
	title_name = ""
	chapter_name = ""

	for c in jsdata:
		if mode == 0:
			if c == "[":
				mode = BRACE0
		elif mode == BRACE0:
			if c == "[":
				mode = BRACE1
		elif mode == BRACE1:
			if c == "\"":
				mode = BRACE1_QUOT
				title_name = ""
			elif c == "[":
				mode = BRACE2
				chapter_id = 0
			elif c == "]":
				mode = BRACE0
		elif mode == BRACE1_QUOT:
			if c == "\"":
				titles[title_name] = [title_id, {}]
				title_id += 1
				mode = BRACE1
			else:
				title_name += c
		elif mode == BRACE2:
			if c == "\"":
				mode = BRACE2_QUOT
				chapter_name = ""
			elif c == "]":
				mode = BRACE1
		elif mode == BRACE2_QUOT:
			if c == "\"":
				titles[title_name][1][chapter_name] = chapter_id
				mode = BRACE2
				chapter_id += 1
			else:
				chapter_name += c

def read_descriptions():
	global descriptions
	f = open("scripts/radio_descriptions_raw.js", 'r')
	jsdata = f.read()
	f.close()
	jsdata = jsdata.replace("var descriptions=[\"","").replace("\"];","")
	splited = jsdata.split("\",\n\"")
	descriptions = {}
	idx = 0
	for item in splited:
		descriptions[item] = idx
		idx += 1



if __name__ == "__main__":

	if len(sys.argv) > 1 and len(sys.argv[1]) == 8:
		radio_util.year = sys.argv[1][:4]
		radio_util.months = [sys.argv[1][4:6]]
		radio_util.days = [sys.argv[1][6:]]

	read_titles()
	read_descriptions()


	outfile = open("scripts/radio_timetables.js", 'w')
	outfile.write("var timetables={")
	isFirstMonth = True
	for month in radio_util.months:
		if not os.path.exists("./radio"+radio_util.year+"/"+month+"/"):
			continue
		if not isFirstMonth:
			outfile.write(",\r\n")
		isFirstMonth = False
		outfile.write(month + ":{")

		radio_util.get_splitter_data(radio_util.year, month)

		isFirstDay = True
		for day in radio_util.days:
			if not os.path.exists("./radio"+radio_util.year+"/"+month+"/"+day+"/"):
				continue
			if not isFirstDay:
				outfile.write(",\r\n")
			isFirstDay = False
			radio_util.reset_temporary_data()
			outfile.write(day + ":{")

			isFirstStation = True
			for nhk_area in radio_util.nhk_areas:
				result = get_timetable_nhk(radio_util.year,month,day,nhk_area)
				if result == None:
					continue
				for key in result.keys():
					if not isFirstStation:
						outfile.write(",\r\n")
					isFirstStation = False
					outfile.write(key + ":\"")
					for program in result[key]:
						outfile.write(program)
					outfile.write("\"")
					is_output_nhk = True

			for station in radio_util.stations:
				result = get_timetable(radio_util.year,month,day,station)
				if result == None:
					continue
				if not isFirstStation:
					outfile.write(",\r\n")
				isFirstStation = False
				outfile.write(result["name"] + ":\"")
				for program in result["programs"]:
					outfile.write(program)
				outfile.write("\"")

			outfile.write("}")
			print(radio_util.year+"-"+month+"-"+day)
		outfile.write("}")

	outfile.write("};")
	outfile.close()
