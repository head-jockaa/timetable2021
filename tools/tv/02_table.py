# coding:utf-8
import os
import sys
import tvlist
import util
import tvkingdom
import patch
import ouj
import mxtv
import mietv
import suntv
import nhk
import bs4

def create_diff(s, start_date, types, name_id, chapter_id, category, splited_by_space, desc_id):
	result, title_omitted, desc_omitted = util.create_diff(s, start_date, types, name_id, chapter_id, category, splited_by_space, desc_id)

	return result

def get_title_id(title_name, chapter_name):
	if chapter_name == None:
		return titles[title_name][0], None
	else:
		return titles[title_name][0], titles[title_name][1][chapter_name]

def get_description_id(d):
	return descriptions[d]

def get_timetable(year, month, day, area):
	result = util.get_target_html(year, month, day, area)
	if result == 0:
		return []

	stations = []
	tvkingdom.checkContent(util.htmldata, year, month, day, area)
	program_parts = tvkingdom.splitByStation(util.htmldata)

	for program_part in program_parts:
		last_programs_interval = 0
		pre_start_time = ""
		start_time = ""
		station_tag = tvlist.get_station_name_tag(tvkingdom.extractStationName(program_part))
		if station_tag == "" or station_tag in util.already:
			continue
		util.already.add(station_tag)

		chunk = ""
		isFirst = True
		isYesterday = False
		pre_esterday = False
		gap_from = None
		gap_to = None
		programs = []
		item_parts = tvkingdom.splitByItem(program_part)
		for item_part in item_parts:
			# 時刻
			pre_start_time_rollback = start_time
			pre_start_time = start_time
			pre_yesterday = isYesterday
			start_time, isYesterday = tvkingdom.extractStartTime(item_part)

			if start_time == "":
				if not isFirst and not (station_tag in ["EX2","CTC2","CTC3","ABS2","TSK2","KYT3"] and (year >= "2022" or month >= "10" or month == "09" and day >= "29")):
					# 番組情報なし
					start_time = util.add_interval(pre_yesterday, pre_start_time, last_programs_interval)
					# パッチあて(情報なしを埋める)
					add_time, add_code, add_title_with_icon, add_desc, add_interval = patch.pad(station_tag, start_time)
					toDelete, delete_interval = patch.delete(station_tag, start_time)
					if add_time != None:
						add_types, add_title_string = tvkingdom.extractIconsFromTitle(add_title_with_icon)
						add_title_name, add_chapter_name, splited_by_space = util.split_title_chapter(add_title_string, station_tag, year, month)
						add_name_id, add_chapter_id = get_title_id(add_title_name, add_chapter_name)
						add_desc_id = get_description_id(add_desc)
						last_programs_interval = add_interval
						chunk = create_diff(station_tag, add_time, add_types, add_name_id, add_chapter_id, add_code, splited_by_space, add_desc_id)
						programs.append(chunk)
					elif not toDelete:
						chunk = create_diff(station_tag, start_time, [], None, None, None, None, None)
						programs.append(chunk)
					else:
						start_time = pre_start_time_rollback
				continue

			# パッチあて(削除)
			toDelete, delete_interval = patch.delete(station_tag, start_time)
			if toDelete:
				start_time = pre_start_time_rollback
				if delete_interval != None:
					last_programs_interval += delete_interval
				else:
					last_programs_interval += tvkingdom.extractInterval(item_part)
				continue

			# 放映時間
			last_programs_interval = tvkingdom.extractInterval(item_part)

			# チバテレ2などの穴埋め
			if station_tag in ["EX2","CTC2","CTC3","ABS2","TSK2","KYT3"] and (year >= "2022" or month >= "10" or month == "09" and day >= "29"):
				gap_to = start_time
				for chunk in util.fetch_gaps(station_tag, gap_from, gap_to):
					programs.append(chunk[:2])
				gap_from = util.add_interval(False, start_time, last_programs_interval)

			# ジャンル
			genre_code = tvkingdom.extractCategoryCode(item_part)
			# 題名(アイコン付き)
			name_with_icon = tvkingdom.extractTitleWithIcons(item_part)
			if name_with_icon == "":
				continue
			# アイコン
			types, title_string = tvkingdom.extractIconsFromTitle(name_with_icon)
			# アイコンを取り除いた題名
			title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, station_tag, year, month)
			# 概要(アイコンを含む場合がある)
			summary_with_icon = tvkingdom.extractDescriptionsWithIcons(item_part)
			types2, summary = tvkingdom.extractIconsFromTitle(summary_with_icon)
			types.extend(types2)

			# パッチあて(修正)
			mod_time, mod_code, mod_title_with_icon, mod_desc, mod_interval = patch.modify(station_tag, start_time)
			if mod_time != None:
				start_time = mod_time
			if mod_code != None:
				genre_code = mod_code
			if mod_title_with_icon != None:
				types, title_string = tvkingdom.extractIconsFromTitle(mod_title_with_icon)
				title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, station_tag, year, month)
			if mod_desc != None:
				summary = mod_desc
			if mod_interval != None:
				last_programs_interval = mod_interval

			# パッチあて(追加)
			if not isYesterday:
				add_list = patch.add(station_tag, pre_start_time, start_time)
				for one in add_list:
					add_types, add_title_string = tvkingdom.extractIconsFromTitle(one["title"])
					add_title_name, add_chapter_name, splited_by_space = util.split_title_chapter(add_title_string, station_tag, year, month)
					add_name_id, add_chapter_id = get_title_id(add_title_name, add_chapter_name)
					add_desc_id = get_description_id(one["desc"])
					#last_programs_interval = one["interval"]
					chunk = create_diff(station_tag, one["time"], add_types, add_name_id, add_chapter_id, one["code"], splited_by_space, add_desc_id)
					programs.append(chunk)

			# ID作成
			name_id, chapter_id = get_title_id(title_name, chapter_name)
			desc_id = get_description_id(summary)

			chunk = create_diff(station_tag, start_time, types, name_id, chapter_id, genre_code, splited_by_space, desc_id)
			programs.append(chunk)
			isFirst = False

		# 最後の「情報なし」は省略する
		if "?" in chunk:
			start_time = pre_start_time
			del programs[-1]
			if station_tag in util.main_channels:
				util.standard_programs_set[station_tag].remove(chunk)
				util.standard_programs_set_nodesc[station_tag].remove(chunk)
				del util.standard_programs_timeline[station_tag][-1]

		# パッチあて(末尾に追加)
		add_list = patch.add(station_tag, start_time,None)
		for one in add_list:
			add_types, add_title_string = tvkingdom.extractIconsFromTitle(one["title"])
			add_title_name, add_chapter_name, splited_by_space = util.split_title_chapter(add_title_string, station_tag, year, month)
			add_name_id, add_chapter_id = get_title_id(add_title_name, add_chapter_name)
			add_desc_id = get_description_id(one["desc"])
			last_programs_interval = one["interval"]
			chunk = create_diff(station_tag, one["time"], add_types, add_name_id, add_chapter_id, one["code"], splited_by_space, add_desc_id)
			programs.append(chunk)

		# チバテレ2などの穴埋め
		if station_tag in ["EX2","CTC2","CTC3","ABS2","TSK2","KYT3"] and (year >= "2022" or month >= "10" or month == "09" and day >= "29"):
			gap_to = None
			for chunk in util.fetch_gaps(station_tag, gap_from, gap_to):
				programs.append(chunk[:2])

		# 連続する「フォーマット2」の間をハイフンで省略
		standards_sorted = []
		keysta = util.get_my_key_station(station_tag)
		if keysta != "":
			for p in util.standard_programs_timeline[keysta]:
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
						#print(util.time_decode_base60(program) + " " + station_tag)
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
					programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")
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
			programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")

		# 放映時間
		if len(programs2) >= 1:
			a = last_programs_interval
			if not (station_tag in ["EX2","CTC2","CTC3","ABS2","TSK2","KYT3"] and (year >= "2022" or month >= "10" or month == "09" and day >= "29")):
				programs2[-1] += ":" + str(a)
			if station_tag in util.main_channels:
				util.standard_lasttime_interval[station_tag] = a

		if station_tag in ["EX2","CTC2","CTC3","ABS2","TSK2","KYT3"] and (year >= "2022" or month >= "10" or month == "09" and day >= "29"):
			if len(programs2) !=0 and len(util.standard_programs_timeline[keysta]) != 0:
				programs2[-1] += ":" + str(util.standard_lasttime_interval[keysta])

		stations.append({"name":station_tag, "programs":programs2})

	return stations

def get_timetable_ouj(year, month, day):
	result = util.get_target_html(year, month, day, "OUJ")
	if result == 0:
		return {"name":"OU2", "programs":[]}

	ouj.checkContent(util.htmldata, year, month, day)
	program_part = ouj.extractOujOn(util.htmldata)

	programs = []
	item_parts = ouj.splitByItem(program_part)
	for item_part in item_parts:
		# 時刻
		start_time = ouj.extractStartTime(item_part)
		# ジャンル
		genre_code = ouj.getCategoryCode()
		# アイコン
		types = []
		# 題名
		title_string = ouj.extractTitle(item_part)
		if title_string == "":
			continue
		title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, "OU2", year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)
		# 概要
		summary = ouj.extractDescriptions(item_part)
		desc_id = get_description_id(summary)

		chunk = create_diff("OU2", start_time, types, name_id, chapter_id, genre_code, splited_by_space, desc_id)
		programs.append(chunk)

	# 放映時間(仮)
	programs[-1] += ":45"
	return {"name":"OU2", "programs":programs}

def get_timetable_mxtv(year, month, day):
	if "MX2" in util.already:
		return None
	result = util.get_target_html(year, month, day, "MX")
	if result == 0:
		return None

	mxtv.checkContent(util.htmldata, year, month, day)
	program_part = util.htmldata

	programs = []
	item_parts = mxtv.splitByItem(program_part)
	for item_part in item_parts:
		# 時刻
		start_time = mxtv.extractStartTime(item_part)
		# アイコン
		types = mxtv.extractIcons(item_part)
		# 題名
		title_string = mxtv.extractTitle(item_part)
		if title_string == "":
			continue
		title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, "MX2", year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)
		# ジャンル
		genre_code = mxtv.getCategoryCode(title_name)
		# 概要
		summary = mxtv.extractDescriptions(item_part)
		desc_id = get_description_id(summary)

		chunk = create_diff("MX2", start_time, types, name_id, chapter_id, genre_code, splited_by_space, desc_id)
		programs.append(chunk)

	# 放映時間(仮)
	if len(programs) != 0:
		programs[-1] += ":60"
	return {"name":"MX2", "programs":programs}

def get_timetable_mietv(year, month, day):
	result = util.get_target_html(year, month, day, "MTV")
	if result == 0:
		return {"name":"MTV2", "programs":[]}

	mietv.checkContent(util.htmldata, year, month, day)
	program_part = mietv.extractMtv2(util.htmldata)

	gap_from = None
	gap_to = None
	programs = []
	item_parts = mietv.splitByItem(program_part)
	for item_part in item_parts:
		# 時刻
		start_time = mietv.extractStartTime(item_part)
		if gap_from != None:
			pre_interval = util.get_interval(gap_from, start_time)
			gap_from = util.add_interval(False, gap_from, pre_interval)
		if start_time == "":
			# マルチ放送なし
			continue
		# アイコン付き題名
		title_with_icon = mietv.extractTitleWithIcons(item_part)
		if title_with_icon == "":
			# 題名のない項目は、マルチ放送終了時点
			gap_from = start_time
			continue
		# アイコン
		types, title_string = mietv.extractIcons(title_with_icon)
		# 題名
		title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, "MTV2", year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)
		# ジャンル
		genre_code = mietv.getCategoryCode(title_name)
		# 概要
		summary = mietv.extractDescriptions(item_part)
		desc_id = get_description_id(summary)

		# 三重テレビ1の番組を埋める
		gap_to = start_time
		for chunk in util.fetch_gaps("MTV2", gap_from, gap_to):
			programs.append(chunk[:2])
		gap_from = start_time

		chunk = create_diff("MTV2", start_time, types, name_id, chapter_id, genre_code, splited_by_space, desc_id)
		programs.append(chunk)

	# 三重テレビ1の番組を埋める
	gap_to = None
	for chunk in util.fetch_gaps("MTV2", gap_from, gap_to):
		programs.append(chunk[:2])

	# 連続する「フォーマット2」の間をハイフンで省略
	programs2 = []
	idx = 0
	foundNum = 0
	fountAt = 0
	for program in programs:
		if (len(program)) <= 2:
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
				programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")
			programs2.append(program)
			foundNum = 0
		idx += 1
	if foundNum == 1:
		programs2.append(programs[idx-1]+".")
	elif foundNum == 2:
		programs2.append(programs[idx-2]+".")
		programs2.append(programs[idx-1]+".")
	elif foundNum >= 3:
		programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")

	if len(programs2) !=0 and len(util.standard_programs_timeline["MTV"]) != 0:
		programs2[-1] += ":" + str(util.standard_lasttime_interval["MTV"])

	return {"name":"MTV2", "programs":programs2}

def get_timetable_suntv(year, month, day):
	result = util.get_target_html(year, month, day, "SUN")
	if result == 0:
		return {"name":"SUN2", "programs":[]}

	suntv.checkContent(util.htmldata, year, month, day)
	program_part = suntv.extractTodays(util.htmldata)

	gap_from = None
	gap_to = None
	programs = []
	item_parts = suntv.splitByItem(program_part)
	for item_part in item_parts:
		# 時刻
		start_time = suntv.extractStartTime(item_part)
		if start_time == "":
			continue
		# アイコン
		types = suntv.extractIcons(item_part)
		# 題名
		title_string = suntv.extractTitle(item_part)
		title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, "SUN2", year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)
		# ジャンル
		genre_code = suntv.getCategoryCode(title_name)
		# 概要
		summary = suntv.extractDescription(item_part)
		desc_id = get_description_id(summary)
		# 放映時間
		interval = suntv.getInterval(item_part)

		# サンテレビ1の番組を埋める
		gap_to = start_time
		for chunk in util.fetch_gaps("SUN2", gap_from, gap_to):
			programs.append(chunk[:2])
		gap_from = util.add_interval(False, start_time, interval)

		chunk = create_diff("SUN2", start_time, types, name_id, chapter_id, genre_code, splited_by_space, desc_id)
		programs.append(chunk)

	# サンテレビ1の番組を埋める
	gap_to = None
	for chunk in util.fetch_gaps("SUN2", gap_from, gap_to):
		programs.append(chunk[:2])

	# 連続する「フォーマット2」の間をハイフンで省略
	programs2 = []
	idx = 0
	foundNum = 0
	fountAt = 0
	for program in programs:
		if (len(program)) <= 2:
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
				programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")
			programs2.append(program)
			foundNum = 0
		idx += 1
	if foundNum == 1:
		programs2.append(programs[idx-1]+".")
	elif foundNum == 2:
		programs2.append(programs[idx-2]+".")
		programs2.append(programs[idx-1]+".")
	elif foundNum >= 3:
		programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")

	if len(programs2) !=0 and len(util.standard_programs_timeline["SUN"]) != 0:
		programs2[-1] += ":" + str(util.standard_lasttime_interval["SUN"])

	return {"name":"SUN2", "programs":programs2}



def get_timetable_nhk(year, month, day, nhk_area):
	result = util.get_target_html(year, month, day, "NHK"+nhk_area)
	if result == 0:
		return {}

	nhk.checkContent(util.htmldata, year, month, day, nhk_area)

	stations = {}
	station_tags = nhk.getTargetPrograms(nhk_area)
	rowspan = [0,0,0,0,0,0,0,0,0,0,0,0]
	last_programs_interval = [0,0,0,0,0,0,0,0,0,0,0,0]
	gap_from = [None, None, None, None, None, None, None, None, None, None, None, None]
	gap_to = [None, None, None, None, None, None, None, None, None, None, None, None]

	program_part = nhk.extractTodays(util.htmldata)
	program_cells = nhk.splitByItem(program_part)

	for program_cell in program_cells:

		# 放映時間
		interval = nhk.getInterval(program_cell)
		# サブチャンネル放送があるか
		colspan = nhk.getColspan(program_cell)

		idx = 0
		min_row = 10000
		for i in reversed(range(12)):
			if min_row >= rowspan[i]:
				min_row = rowspan[i]
				idx = i
		rowspan[idx] += interval
		if colspan == 2:
			rowspan[idx+1] += interval

		if station_tags[idx] == "":
			continue		

		# 時刻
		start_time = nhk.extractStartTime(program_cell, rowspan[idx])

		# パッチあて(削除)
		toDelete, delete_interval = patch.delete(station_tags[idx], start_time)
		if toDelete:
			continue

		if start_time == "" or start_time >= "2800":

			# パッチあて(追加)
			pad_minute_from = (rowspan[idx]-interval-45)%60
			pad_hour_from = (int)((rowspan[idx]-interval-45-pad_minute_from)/60)+5
			pad_minute_from_str = str(pad_minute_from)
			if pad_hour_from < 10:
				pad_hour_from_str = "0" + str(pad_hour_from)
			else:
				pad_hour_from_str = str(pad_hour_from)
			if pad_minute_from < 10:
				pad_minute_from_str = "0" + str(pad_minute_from)
			else:
				pad_minute_from_str = str(pad_minute_from)

			pad_minute_to = (rowspan[idx]-45)%60
			pad_hour_to = (int)((rowspan[idx]-45-pad_minute_to)/60)+5
			pad_minute_to_str = str(pad_minute_to)
			if pad_hour_to < 10:
				pad_hour_to_str = "0" + str(pad_hour_to)
			else:
				pad_hour_to_str = str(pad_hour_to)
			if pad_minute_to < 10:
				pad_minute_to_str = "0" + str(pad_minute_to)
			else:
				pad_minute_to_str = str(pad_minute_to)
			pad_from = pad_hour_from_str+pad_minute_from_str
			pad_to = pad_hour_to_str+pad_minute_to_str

			if pad_from == "0415":
				pad_from = nhk.get_first_time(station_tags[idx])

			add_time, add_code, add_title_with_icon, add_desc, add_interval = patch.pad(station_tags[idx], pad_from)
			if add_time != None:
				if station_tags[idx] not in stations:
					stations[station_tags[idx]] = []
				gap_to[idx] = pad_from
				for chunk in util.fetch_gaps(station_tags[idx], gap_from[idx], gap_to[idx]):
					stations[station_tags[idx]].append(chunk[:2])
				gap_from[idx] = pad_to

				add_types, add_title_string = tvkingdom.extractIconsFromTitle(add_title_with_icon)
				add_title_name, add_chapter_name, splited_by_space = util.split_title_chapter(add_title_string, station_tags[idx], year, month)
				add_name_id, add_chapter_id = get_title_id(add_title_name, add_chapter_name)
				add_desc_id = get_description_id(add_desc)
				bar = create_diff(station_tags[idx], add_time, add_types, add_name_id, add_chapter_id, add_code, splited_by_space, add_desc_id)
				stations[station_tags[idx]].append(bar)

				add_list = patch.add(station_tags[idx], pad_from, pad_to)
				for one in add_list:
					add_types, add_title_string = tvkingdom.extractIconsFromTitle(one["title"])
					add_title_name, add_chapter_name, splited_by_space = util.split_title_chapter(add_title_string, station_tags[idx], year, month)
					add_name_id, add_chapter_id = get_title_id(add_title_name, add_chapter_name)
					add_desc_id = get_description_id(one["desc"])
					bar = create_diff(station_tags[idx], one["time"], add_types, add_name_id, add_chapter_id, one["code"], splited_by_space, add_desc_id)
					stations[station_tags[idx]].append(bar)

			continue

		# アイコン
		types = nhk.extractIcons(program_cell)

		# 題名
		title_string = nhk.extractTitle(program_cell)
		title_name, chapter_name, splited_by_space = util.split_title_chapter(title_string, station_tags[idx], year, month)
		name_id, chapter_id = get_title_id(title_name, chapter_name)

		# ジャンル
		genre_code = nhk.getCategoryCode(title_name)

		# 概要
		description = nhk.extractDescription(program_cell)
		desc_id = get_description_id(description)

		if station_tags[idx] not in stations:
			stations[station_tags[idx]] = []

		# チャンネル1の番組を埋める
		gap_to[idx] = start_time
		for chunk in util.fetch_gaps(station_tags[idx], gap_from[idx], gap_to[idx]):
			stations[station_tags[idx]].append(chunk[:2])
		gap_from[idx] = util.add_interval(False, start_time, interval)

		bar = create_diff(station_tags[idx], start_time, types, name_id, chapter_id, genre_code, splited_by_space, desc_id)
		last_programs_interval[idx] = interval

		stations[station_tags[idx]].append(bar)

	# チャンネル1の番組を埋める
	for idx in range(12):
		if station_tags[idx] == "":
			continue
		gap_to[idx] = None
		for chunk in util.fetch_gaps(station_tags[idx], gap_from[idx], gap_to[idx]):
			if station_tags[idx] not in stations:
				stations[station_tags[idx]] = []
			stations[station_tags[idx]].append(chunk[:2])

	# 連続する「フォーマット2」の間をハイフンで省略
	for sta in station_tags:
		if sta not in stations:
			continue
		programs2 = []
		idx = 0
		foundNum = 0
		fountAt = 0
		for program in stations[sta]:
			if (len(program)) <= 2:
				if foundNum == 0:
					foundAt = idx
				foundNum += 1
			else:
				if foundNum == 1:
					programs2.append(stations[sta][idx-1]+".")
				elif foundNum == 2:
					programs2.append(stations[sta][idx-2]+".")
					programs2.append(stations[sta][idx-1]+".")
				elif foundNum >= 3:
					programs2.append(stations[sta][foundAt]+"-"+stations[sta][idx-1]+".")
				programs2.append(program)
				foundNum = 0
			idx += 1
		if foundNum == 1:
			programs2.append(stations[sta][idx-1]+".")
		elif foundNum == 2:
			programs2.append(stations[sta][idx-2]+".")
			programs2.append(stations[sta][idx-1]+".")
		elif foundNum >= 3:
			programs2.append(stations[sta][foundAt]+"-"+stations[sta][idx-1]+".")

		stations[sta] = programs2

	# 最後の番組の放映時間
	if station_tags[1] != "":
		stations[station_tags[1]][-1] += ":" + str(util.standard_lasttime_interval[station_tags[1][1:]])
	if station_tags[3] != "":
		stations[station_tags[3]][-1] += ":" + str(util.standard_lasttime_interval[station_tags[3][1:]])
	if station_tags[5] != "":
		stations[station_tags[5]][-1] += ":" + str(util.standard_lasttime_interval["BS1"])

	return stations



def get_timetable_bs4(year, month, day):
	result1 = bs4.get_html_bs141(year, month, day)
	result2 = bs4.get_html_bs142(year, month, day)
	if not result1 or not result2:
		return {"name":"BN2", "programs":[]}

	result1 = bs4.extractTimetableOf(bs4.htmldata_bs141, year, month, day)
	result2 = bs4.extractTimetableOf(bs4.htmldata_bs142, year, month, day)
	diff = []
	for r in result2:
		if r not in result1:
			diff.append(r)

	gap_from = None
	gap_to = None
	programs = []
	for d in diff:

		# チャンネル1の番組を埋める
		gap_to = d["start"]
		for chunk in util.fetch_gaps("BN2", gap_from, gap_to):
			programs.append(chunk[:2])
		gap_from = util.add_interval(False, d["start"], d["interval"])

		title_name, chapter_name, splited_by_space = util.split_title_chapter(d["title"], "BN2", year, month)
		genre_code = bs4.getCategoryCode(title_name)
		name_id, chapter_id = get_title_id(title_name, chapter_name)
		desc_id = get_description_id(" ")
		bar = create_diff("BN2", d["start"], d["types"], name_id, chapter_id, genre_code, splited_by_space, desc_id)
		programs.append(bar)

	# チャンネル1の番組を埋める
	gap_to = None
	for chunk in util.fetch_gaps("BN2", gap_from, gap_to):
		programs.append(chunk[:2])

	# 連続する「フォーマット2」の間をハイフンで省略
	programs2 = []
	idx = 0
	foundNum = 0
	fountAt = 0
	for program in programs:
		if (len(program)) <= 2:
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
				programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")
			programs2.append(program)
			foundNum = 0
		idx += 1
	if foundNum == 1:
		programs2.append(programs[idx-1]+".")
	elif foundNum == 2:
		programs2.append(programs[idx-2]+".")
		programs2.append(programs[idx-1]+".")
	elif foundNum >= 3:
		programs2.append(programs[foundAt]+"-"+programs[idx-1]+".")

	# 最後の番組の放映時間
	programs2[-1] += ":" + str(util.standard_lasttime_interval["BS4"])

	return {"name":"BN2", "programs":programs2}


def write_type_names():
	outfile = open("scripts/type_names.js", 'w')
	i = 0
	for t in util.type_names:
		if i == 0:
			outfile.write("var type_names={")
		else:
			outfile.write(",\r\n")
		name = ""
		if t == "":
			outfile.write(util.abc_list[i] + ":{}")
			i += 1
			continue
		elif t == "新":
			name = "新番組"
		elif t == "再":
			name = "再放送"
		elif t == "終":
			name = "最終回"
		elif t == "手":
			name = "手話通訳放送"
		elif t == "字":
			name = "字幕放送"
		elif t == "双":
			name = "双方向放送"
		elif t == "デ":
			name = "番組連動データ放送"
		elif t == "S":
			name = "ステレオ放送"
		elif t == "二":
			name = "二ヶ国語放送"
		elif t == "多":
			name = "音声多重放送"
		elif t == "解":
			name = "音声解説"
		elif t == "SS":
			name = "サラウンドステレオ"
		elif t == "B":
			name = "圧縮Bモードステレオ"
		elif t == "N":
			name = "ニュース"
		elif t == "天":
			name = "天気予報"
		elif t == "交":
			name = "交通情報"
		elif t == "映":
			name = "劇場映画"
		elif t == "料":
			name = "有料放送"
		elif t == "前":
			name = "前編"
		elif t == "後":
			name = "後編"
		elif t == "初":
			name = "初回放送"
		elif t == "生":
			name = "生放送"
		elif t == "HV":
			name = "ハイビジョン放送"
		elif t == "PV":
			name = "Pay Per View"
		elif t == "PS":
			name = "Pay Per Series"
		elif t == "PG12":
			name = "PG12指定"
		elif t == "R15":
			name = "R15指定"
		elif t == "吹":
			name = "吹き替え"
		elif t == "幕":
			name = "字幕スーパー"
		elif t == "契":
			name = "契約"
		elif t == "無":
			name = "無料"
		elif t == "22.2ch":
			name = "22.2ch"
		elif t == "5.1ch":
			name = "5.1ch"
		elif t == "HDR":
			name = "HDR"
		else:
			name=t
		outfile.write(util.abc_list[i] + ":{icon:\"" + t + "\",name:\"" + name + "\"}")
		i += 1
	outfile.write("};")
	outfile.close()

def read_titles():
	global titles
	f = open("scripts/titles_raw.js", 'r')
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
	f = open("scripts/descriptions_raw.js", 'r')
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
	global titles
	global descriptions

	if len(sys.argv) > 1 and len(sys.argv[1]) == 8:
		util.year = sys.argv[1][:4]
		util.months = [sys.argv[1][4:6]]
		util.days = [sys.argv[1][6:]]

	read_titles()
	read_descriptions()

	if not os.path.isdir("scripts"):
		os.makedirs("scripts")
	outfile = open("scripts/timetables.js", 'w')
	outfile.write("var timetables={")
	isFirstMonth = True
	for month in util.months:
		if not os.path.exists("./" + util.year + "/" + month + "/"):
			continue

		util.get_splitter_data(util.year, month)

		if not isFirstMonth:
			outfile.write(",\r\n")
		isFirstMonth = False
		outfile.write(month + ":{")

		isFirstDay = True
		for day in util.days:
			if not os.path.exists("./" + util.year + "/" + month + "/" + day + "/"):
				continue
			if not isFirstDay:
				outfile.write(",\r\n")
			isFirstDay = False
			util.reset_temporary_data()
			patch.read_patch_file(util.year, month, day)
			outfile.write(day + ":{")

			isFirstStation = True
			# テレビ王国
			for area in util.areas:
				stations = get_timetable(util.year, month, day, area)
				for station in stations:
					if not isFirstStation:
						outfile.write(",\r\n")
					isFirstStation = False
					outfile.write(station["name"] + ":\"")
					for program in station["programs"]:
						outfile.write(program)
					outfile.write("\"")
			# NHK
			for area in nhk.nhk_areas:
				stations = get_timetable_nhk(util.year, month, day, area)
				for station in stations:
					if not isFirstStation:
						outfile.write(",\r\n")
					isFirstStation = False
					outfile.write(station + ":\"")
					for program in stations[station]:
						outfile.write(program)
					outfile.write("\"")
			# BS日テレ
			station = get_timetable_bs4(util.year, month, day)
			if not isFirstStation:
				outfile.write(",\r\n")
			isFirstStation = False
			outfile.write(station["name"] + ":\"")
			for program in station["programs"]:
				outfile.write(program)
			outfile.write("\"")
			# TOKYO MX2
			station = get_timetable_mxtv(util.year, month, day)
			if station != None:
				if not isFirstStation:
					outfile.write(",\r\n")
				isFirstStation = False
				outfile.write(station["name"] + ":\"")
				for program in station["programs"]:
					outfile.write(program)
				outfile.write("\"")
			# 三重テレビ2
			station = get_timetable_mietv(util.year, month, day)
			if not isFirstStation:
				outfile.write(",\r\n")
			isFirstStation = False
			outfile.write(station["name"] + ":\"")
			for program in station["programs"]:
				outfile.write(program)
			outfile.write("\"")
			# サンテレビ2
			station = get_timetable_suntv(util.year, month, day)
			if not isFirstStation:
				outfile.write(",\r\n")
			isFirstStation = False
			outfile.write(station["name"] + ":\"")
			for program in station["programs"]:
				outfile.write(program)
			outfile.write("\"")
			# 放送大学
			station = get_timetable_ouj(util.year, month, day)
			if len(station["programs"]) > 1:
				if not isFirstStation:
					outfile.write(",\r\n")
				isFirstStation = False
				outfile.write(station["name"] + ":\"")
				for program in station["programs"]:
					outfile.write(program)
				outfile.write("\"")
			outfile.write("}")
			print(util.year + "-" + month + "-" + day)
		outfile.write("}")

	outfile.write("};")
	outfile.close()

	write_type_names()
