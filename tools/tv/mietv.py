# coding:utf-8
import util

def checkContent(html, year, month, day):
	if not "class=\"current\">" + str((int)(month)) + "月" + str((int)(day)) + "日" in html:
		print(year + "_" + month + "_" + day + "_MTV.htmlの内容が間違っています")

def extractMtv2(html):
	splited = html.split("<div id=\"ch2\"")
	return splited[1]

# extractMtv2で切り分けたhtmlを与える
def splitByItem(html):
	splited = html.split("<tr>")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html):
	if "class=\"noprogram\"" in html:
		return ""
	splited1 = html.split(">")
	splited2 = splited1[1].split("</td")
	return splited2[0].replace(":","")

# splitByItemで切り分けたhtmlを与える
def extractTitleWithIcons(html):
	splited1 = html.split("<p class=\"title\">")
	if len(splited1) == 1:
		return ""
	else:
		splited2 =  splited1[1].split("<")
		return util.sanitize(splited2[0])

# extractTitleWithIconsの返した文字列を与える
def extractIcons(title_string):
	idx = len(title_string)-1
	found = False
	types = []
	while idx>=2:
		if title_string[idx] == "】" and title_string[idx-2] == "【":
			types.insert(0, util.append_type_name(title_string[idx-1]))
			found_icon = "【" + title_string[idx-1] + "】"
			replaced = title_string.replace(found_icon,"")
			idx -= len(title_string)-len(replaced)
			title_string = replaced
		else:
			idx -= 1

	return types, title_string

# splitByItemで切り分けたhtmlを与える
def extractDescriptions(html):
	splited1 = html.split("</p><p>")
	if len(splited1) == 1:
		return ""
	else:
		splited2 =  splited1[1].split("</p>")
		return util.sanitize(splited2[0])

def getCategoryCode(title_name):
	if "ウェザー" in title_name:
		return "100101"
	elif "マーケット" in title_name:
		return "100106"
	elif "野球" in title_name:
		return "101101"
	elif "伊勢神宮" in title_name:
		return "108101"
	elif "伊勢 美し国から" in title_name:
		return "108100"
	elif "県政" in title_name or "よか＊イチ!" in title_name or "旬感" in title_name:
		return "102102"
	else:
		return "102115"
