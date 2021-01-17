# coding:utf-8
import re
import util

def checkContent(html, year, month, day):
	if not "month=" + str((int)(month)) + "&date=" + str((int)(day)) in html:
		print(year + "_" + month + "_" + day + "_OUJ.htmlの内容が間違っています")

def extractOujOn(html):
	splited = html.split("<TABLE class='tbl-ct-program'>")
	return splited[2]

# extractOujOnで切り分けたhtmlを与える
def splitByItem(html):
	splited = html.split("<span class='time-program'>")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html):
	splited = html.split("</span>")
	return splited[0].replace(":","")

# splitByItemで切り分けたhtmlを与える
def extractTitle(html):
	title = ""
	splited1 = html.split("<dt>")
	splited2 =  splited1[1].split("</dt>")
	if "<A " in splited2[0]:
		splited3 = splited2[0].split(" style='color:blue'>")
		splited4 = splited3[1].split("</A>")
		title = util.sanitize(splited4[0])
	else:
		title = util.sanitize(splited2[0])

	matchObj = re.search(r'\(’[0-9]{2}\)$', title)
	if matchObj:
		title = title[:matchObj.start()]

	splited1 = html.split("<dd>")
	splited2 = splited1[1].split("</dd>")
	ep = util.sanitize(splited2[0])
	matchObj = re.search(r'^第[0-9]+回', ep)
	if matchObj:
		ep = ep[matchObj.start():matchObj.end()]
		title = title + " " + ep

	return title

# splitByItemで切り分けたhtmlを与える
def extractDescriptions(html):
	desc = ""

	splited1 = html.split("<dd>")
	splited2 = splited1[1].split("</dd>")
	splited3 = splited2[0].split("\");\n              document.write(\"")
	desc = util.sanitize(splited3[0].rstrip("<br>"))

	matchObj = re.search(r'第[0-9]+回 ', desc)
	if matchObj:
		desc = desc[matchObj.end():]

	return "「" + desc + "」"

def getCategoryCode():
	# 趣味・教育
	return "110111"
