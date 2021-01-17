# coding:utf-8
import radio_util

IMG_RE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAZpJREFUeNrsWdGRgyAQxZs0YAu2YAtagi3Ygpagf/n2R7+1BC1BW7AELYFjc8G544TABXHnxp1hwgSEl919y5MQSilhdmeNImv3JzaU4DaQ5PsXdV3Tsw0wCCDxgNsD6W0on/HGYp7nPT4/CHK7qQaHYXACIgxD4vu+dJx+RfinpWnqjK1BEPzan49JQ8wechZG8KDKdj1oan3fU1traXkQi6EHqBXicRxpkiTWSMFyjrZtqxViLYA2wfHGyoo9gHxOlmVvkwQ8x+fBM1ZJEkXR2/nEovG/SHIzmdx1HZmmaXdsnuetX5alWxYfdcTp5KCRB9n5LD0CwYNVVT36RVEo18nz/BgPqn6xyVF3GIuvo86ExcBEUbBC7siE5bquWz+OY63N+Xogt2R5K30n4e8EzgSBZH+pB1kCbzWPs07FYhMT13u1phUW/0WMXiy+AJqKBVOD0iOKC5nYOIUkTD8qxcKyLOeSRHVbAIVZNf6yUIs6ENQKk/zGIPeuT3SUOS/U1+2WtTLTNA0aUCIW9FfAuC/Rsf8N8SnAANZNZZfq9eAgAAAAAElFTkSuQmCC"

def checkContent(html, year, month, day, area):
	if not "area=\"" + area + "\"" in html or not "date=\"" + year + month + day + "\"" in html:
		print(year + "_" + month + "_" + day + "_NHK" + area + ".htmlの内容が間違っています")

def getTargetPrograms(nhk_area):
	result = ["", "", ""]
	if not nhk_area in ["080","090","100","110","120","140","210","240","260","280","290","300"]:
		result[0] = "NHK1_" + nhk_area
	if nhk_area == "130":
		result[1] = "NHK2"
	result[2] = "NHKFM_" + nhk_area

	return result

def extractTodays(html):
	splited = html.split("現在の時刻")
	if len(splited) == 1:
		return ""
	return splited[1]

# extractTodaysで切り分けたhtmlを与える
def splitByItem(html):
	splited = html.split("<td data-")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def getInterval(html):
	splited = html.split("rowspan=\"")
	splited2 = splited[1].split("\"")
	return (int)(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html, isAfternoon):
	splited = html.split("class=\"time\">")
	if len(splited) == 1:
		return "", isAfternoon
	splited2 = splited[1].split("<")
	splited3 = splited2[0].replace("午前","").replace("午後","").strip()
	start_hour = splited3.split(":")[0]
	start_minute = splited3.split(":")[1]
	if "午後" in splited2[0]:
		isAfternoon = True
		start_hour = str((int)(start_hour) + 12)
	elif isAfternoon and "午前" in splited2[0]:
		start_hour = str((int)(start_hour) + 24)
	elif len(start_hour) == 1:
		start_hour = "0" + start_hour
	return start_hour + start_minute, isAfternoon

# splitByItemで切り分けたhtmlを与える
def extractTitle(html):
	splited1 = html.split("class=\"to-dtl\">")
	if len(splited1) == 1:
		return ""
	else:
		splited2 = splited1[1].split("</a>")
		result = radio_util.sanitize(splited2[0])
		return result.replace(" ［終］","")

# splitByItemで切り分けたhtmlを与える
def extractDescription(html):
	splited1 = html.split("class=\"arrow\">")
	if len(splited1) == 1:
		return ""
	else:
		splited2 = splited1[1].split("</div>")
		return radio_util.sanitize(splited2[0])
