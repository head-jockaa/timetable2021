var selected_tv = "";
var selected_year = 2021;
var selected_month = 1;
var selected_day = 18;
var table_index = 0;
var hour_height = 6;
var hour_width = 200;
var fix_hour_height = true;

// 時刻のdecodeに用いる60進数
var base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"];

var date_list;

function create_calendar() {
	date_list = {};
	var column = 0;
	var row, days;
	for (var m = 1 ; m <= 12 ; m++) {
		column = 0;
		days = Array();
		row = Array();
		var startWeek = new Date(selected_year,m-1,1).getDay();
		for (var d = 0 ; d < startWeek ; d++) {
			row.push(0);
			column++;
		}
		var daysOfMonth = new Date(selected_year, m, 0).getDate();
		for (var d = 1 ; d <= daysOfMonth ; d++) {
			row.push(d);
			column++;
			if (column == 7) {
				days.push(row);
				row = Array();
				column = 0;
			}
		}
		if (row.length != 0) {
			days.push(row);
		}
		date_list[m] = days;
	}
}

var area_list = {
	10: "札幌",
	11: "函館",
	12: "旭川",
	13: "帯広",
	14: "釧路",
	15: "北見",
	16: "室蘭",
	22: "青森",
	20: "岩手",
	17: "宮城",
	18: "秋田",
	19: "山形",
	21: "福島",
	26: "茨城",
	28: "栃木",
	25: "群馬",
	29: "埼玉",
	27: "千葉",
	23: "東京",
	24: "神奈川",
	31: "新潟",
	37: "富山",
	34: "石川",
	36: "福井",
	32: "山梨",
	30: "長野",
	39: "岐阜",
	35: "静岡",
	33: "愛知",
	38: "三重",
	45: "滋賀",
	41: "京都",
	40: "大阪",
	42: "兵庫",
	44: "奈良",
	43: "和歌山",
	49: "鳥取",
	48: "島根",
	47: "岡山",
	46: "広島",
	50: "山口",
	53: "徳島",
	52: "香川",
	51: "愛媛",
	54: "高知",
	55: "福岡",
	61: "佐賀",
	57: "長崎",
	56: "熊本",
	60: "大分",
	59: "宮崎",
	58: "鹿児島",
	62: "沖縄"
}

var nhk_list = {
	G23: "NHK総合・東京",
	G10: "NHK総合・札幌",
	G11: "NHK総合・函館",
	G12: "NHK総合・旭川",
	G13: "NHK総合・帯広",
	G14: "NHK総合・釧路",
	G15: "NHK総合・北見",
	G16: "NHK総合・室蘭",
	G22: "NHK総合・青森",
	G20: "NHK総合・盛岡",
	G17: "NHK総合・仙台",
	G18: "NHK総合・秋田",
	G19: "NHK総合・山形",
	G21: "NHK総合・福島",
	G26: "NHK総合・水戸",
	G28: "NHK総合・宇都宮",
	G25: "NHK総合・前橋",
	G31: "NHK総合・新潟",
	G37: "NHK総合・富山",
	G34: "NHK総合・金沢",
	G36: "NHK総合・福井",
	G32: "NHK総合・甲府",
	G30: "NHK総合・長野",
	G39: "NHK総合・岐阜",
	G35: "NHK総合・静岡",
	G33: "NHK総合・名古屋",
	G38: "NHK総合・津",
	G45: "NHK総合・大津",
	G41: "NHK総合・京都",
	G40: "NHK総合・大阪",
	G42: "NHK総合・神戸",
	G44: "NHK総合・奈良",
	G43: "NHK総合・和歌山",
	G49: "NHK総合・鳥取",
	G48: "NHK総合・松江",
	G47: "NHK総合・岡山",
	G46: "NHK総合・広島",
	G50: "NHK総合・山口",
	G53: "NHK総合・徳島",
	G52: "NHK総合・高松",
	G51: "NHK総合・松山",
	G54: "NHK総合・高知",
	G55: "NHK総合・福岡",
	Gkk: "NHK総合・北九州",
	G61: "NHK総合・佐賀",
	G57: "NHK総合・長崎",
	G56: "NHK総合・熊本",
	G60: "NHK総合・大分",
	G59: "NHK総合・宮崎",
	G58: "NHK総合・鹿児島",
	G62: "NHK総合・沖縄"
};

var etv_list = {
	E23: "NHK教育・東京",
	E10: "NHK教育・札幌",
	E11: "NHK教育・函館",
	E12: "NHK教育・旭川",
	E13: "NHK教育・帯広",
	E14: "NHK教育・釧路",
	E15: "NHK教育・北見",
	E16: "NHK教育・室蘭",
	E22: "NHK教育・青森",
	E20: "NHK教育・盛岡",
	E17: "NHK教育・仙台",
	E18: "NHK教育・秋田",
	E19: "NHK教育・山形",
	E21: "NHK教育・福島",
	E31: "NHK教育・新潟",
	E37: "NHK教育・富山",
	E34: "NHK教育・金沢",
	E36: "NHK教育・福井",
	E32: "NHK教育・甲府",
	E30: "NHK教育・長野",
	E35: "NHK教育・静岡",
	E33: "NHK教育・名古屋",
	E40: "NHK教育・大阪",
	E49: "NHK教育・鳥取",
	E48: "NHK教育・松江",
	E47: "NHK教育・岡山",
	E46: "NHK教育・広島",
	E50: "NHK教育・山口",
	E53: "NHK教育・徳島",
	E52: "NHK教育・高松",
	E51: "NHK教育・松山",
	E54: "NHK教育・高知",
	E55: "NHK教育・福岡",
	Ekk: "NHK教育・北九州",
	E61: "NHK教育・佐賀",
	E57: "NHK教育・長崎",
	E56: "NHK教育・熊本",
	E60: "NHK教育・大分",
	E59: "NHK教育・宮崎",
	E58: "NHK教育・鹿児島",
	E62: "NHK教育・沖縄"
};

var ntv_list = {
	NTV:"日本テレビ",
	YTV: "読売テレビ",
	CTV: "中京テレビ",
	STV: "札幌テレビ",
	RAB: "青森放送",
	ABS: "秋田放送",
	TVI: "テレビ岩手",
	YBC: "山形放送",
	MMT: "ミヤギテレビ",
	FCT: "福島中央テレビ",
	YBS: "山梨放送",
	TENY: "テレビ新潟",
	TSB: "テレビ信州",
	SDT: "静岡第一テレビ",
	KNB: "北日本放送",
	KTK: "テレビ金沢",
	FBC: "福井放送",
	RNC: "西日本放送",
	HTV: "広島テレビ",
	NKT: "日本海テレビ",
	KRY: "山口放送",
	JRT: "四国放送",
	RNB: "南海放送",
	RKC: "高知放送",
	FBS: "福岡放送",
	NIB: "長崎国際テレビ",
	KKT: "熊本県民テレビ",
	TOS: "テレビ大分",
	UMK: "テレビ宮崎",
	KYT: "鹿児島読売テレビ"
};

var tbs_list = {
	TBS: "TBSテレビ",
	MBS: "毎日放送",
	CBC: "中部日本放送",
	HBC: "北海道放送",
	ATV: "青森テレビ",
	IBC: "岩手放送",
	TUY: "テレビユー山形",
	TBC: "東北放送",
	TUF: "テレビユー福島",
	UTY: "テレビ山梨",
	BSN: "新潟放送",
	SBC: "信越放送",
	SBS: "静岡放送",
	TUT: "チューリップテレビ",
	MRO: "北陸放送",
	RSK: "山陽放送",
	RCC: "中国放送",
	BSS: "山陰放送",
	TYS: "テレビ山口",
	ITV: "あいテレビ",
	KUTV: "テレビ高知",
	RKB: "RKB毎日放送",
	NBC: "長崎放送",
	RKK: "熊本放送",
	OBS: "大分放送",
	MRT: "宮崎放送",
	MBC: "南日本放送",
	RBC: "琉球放送"
};

var cx_list = {
	CX: "フジテレビ",
	KTV: "関西テレビ",
	THK: "東海テレビ",
	UHB: "北海道文化放送",
	AKT: "秋田テレビ",
	MIT: "岩手めんこいテレビ",
	SAY: "さくらんぼテレビ",
	OX: "仙台放送",
	FTV: "福島テレビ",
	NST: "新潟総合テレビ",
	NBS: "長野放送",
	SUT: "テレビ静岡",
	BBT: "富山テレビ",
	ITC: "石川テレビ",
	FTB: "福井テレビ",
	OHK: "岡山放送",
	TSS: "テレビ新広島",
	TSK: "山陰中央テレビ",
	EBC: "テレビ愛媛",
	KSS: "高知さんさんテレビ",
	TNC: "テレビ西日本",
	STS: "サガテレビ",
	KTN: "テレビ長崎",
	TKU: "テレビ熊本",
	TOS: "テレビ大分",
	UMK: "テレビ宮崎",
	KTS: "鹿児島テレビ",
	OTV: "沖縄テレビ"
};

var ex_list = {
	EX: "テレビ朝日",
	ABC: "朝日放送",
	NBN: "名古屋テレビ",
	HTB: "北海道テレビ",
	ABA: "青森朝日放送",
	AAB: "秋田朝日放送",
	IAT: "岩手朝日テレビ",
	YTS: "山形テレビ",
	KHB: "東日本放送",
	KFB: "福島放送",
	UX: "新潟テレビ21",
	ABN: "長野朝日放送",
	SATV: "静岡朝日テレビ",
	HAB: "北陸朝日放送",
	KSB: "瀬戸内海放送",
	HOME: "広島ホームテレビ",
	YAB: "山口朝日放送",
	EAT: "愛媛朝日テレビ",
	KBC: "九州朝日放送",
	NCC: "長崎文化放送",
	KAB: "熊本朝日放送",
	OAB: "大分朝日放送",
	KKB: "鹿児島放送",
	QAB: "琉球朝日放送"
};

var tx_list = {
	TX: "テレビ東京",
	TVO: "テレビ大阪",
	TVA: "テレビ愛知",
	TVH: "テレビ北海道",
	TSC: "テレビせとうち",
	TVQ: "TVQ九州放送",
};

var other_list = {
	MX: "TOKYO MX",
	TVK: "テレビ神奈川",
	TVS: "テレビ埼玉",
	CTC: "チバテレビ",
	GTV: "群馬テレビ",
	TTV: "とちぎテレビ",
	MTV: "三重テレビ",
	GBS: "岐阜放送",
	SUN: "サンテレビ",
	KBS: "KBS京都",
	BBC: "びわ湖放送",
	TVN: "奈良テレビ",
	WTV: "テレビ和歌山"
};

var bs_list = {
	BS1: "NHK BS1",
	BSp: "NHK BSプレミアム",
	BS4: "BS日テレ",
	BS6: "BS-TBS",
	BS8: "BSフジ",
	BS5: "BS朝日",
	BS7: "BSテレ東",
	WW1: "WOWOWプライム",
	WW2: "WOWOWライブ",
	WW3: "WOWOWシネマ",
	WW4: "WOWOWプラス",
	SC1: "スターチャンネル1",
	SC2: "スターチャンネル2",
	SC3: "スターチャンネル3",
	BS11: "BS11",
	BS12: "TwellV",
	OUJ: "放送大学",
	GCH: "グリーンチャンネル",
	BSA: "BSアニマックス",
	SKY: "BSスカパー!",
	JS1: "J SPORTS 1",
	JS2: "J SPORTS 2",
	JS3: "J SPORTS 3",
	JS4: "J SPORTS 4",
	BSF: "BS釣りビジョン",
	JMV: "BS日本映画専門チャンネル",
	DCH: "ディズニー・チャンネル",
	FK1: "NHK BS4K",
	FK4: "BS日テレ 4K",
	FK6: "BS-TBS 4K",
	FK8: "BSフジ 4K",
	FK5: "BS朝日 4K",
	FK7: "BSテレ東 4K",
	EK1: "NHK BS8K",
	FKC: "ザ・シネマ 4K",
	FKS: "ショップチャンネル 4K",
	QVC: "4K QVC"
};

/* 次の番組の開始時刻から、放映時間を求める(ただし同じ日付に限る) */
function get_interval(start_time_string, next_time_string) {
	var start_hour = parseInt(start_time_string.split(":")[0]);
	var start_minute = parseInt(start_time_string.split(":")[1]);
	var next_hour = parseInt(next_time_string.split(":")[0]);
	var next_minute = parseInt(next_time_string.split(":")[1]);
	var interval = 0;
	if (start_hour > next_hour) {
		interval = next_minute-60;
		next_minute = 0;
		start_hour--;
		interval += 60 * (next_hour - start_hour);
	}
	else if (start_hour < next_hour) {
		interval = 60-start_minute;
		start_minute = 0;
		start_hour++;
		interval += 60 * (next_hour - start_hour);
	}
	return interval + next_minute - start_minute;
}

/* キー局の番組表から同じ時刻の番組データを拾ってくる (番組開始時刻を2つ与えるとその間の番組も全て取得する、start_time2を与えなければstart_timeの番組ひとつだけ取得する) */
function  fetch_from_key_station(month, day, s, start_time, start_time2) {
	var keysta = "";
	if (s == "G10" || s == "G11" || s == "G12" || s == "G13" || s == "G14" || s == "G15" || s == "G16" || s == "G17" || s == "G18" || s == "G19" || s == "G20" || s == "G21" || s == "G22" || s == "G23" || s == "G25" || s == "G26" || s == "G28" || s == "G30" || s == "G31" || s == "G32" || s == "G33" || s == "G34" || s == "G35" || s == "G36" || s == "G37" || s == "G38" || s == "G39" || s == "G40" || s == "G41" || s == "G42" || s == "G43" || s == "G44" || s == "G45" || s == "G46" || s == "G47" || s == "G48" || s == "G49" || s == "G50" || s == "G51" || s == "G52" || s == "G53" || s == "G54" || s == "G55" || s == "G56" || s == "G57" || s == "G58" || s == "G59" || s == "G60" || s == "G61" || s == "G62" || s == "Gkk") {
		keysta = "G23";
	}
	else if (s == "E10" || s == "E11" || s == "E12" || s == "E13" || s == "E14" || s == "E15" || s == "E16" || s == "E17" || s == "E18" || s == "E19" || s == "E20" || s == "E21" || s == "E22" || s == "E23" || s == "E30" || s == "E31" || s == "E32" || s == "E33" || s == "E34" || s == "E35" || s == "E36" || s == "E37" || s == "E40" || s == "E46" || s == "E47" || s == "E48" || s == "E49" || s == "E50" || s == "E51" || s == "E52" || s == "E53" || s == "E54" || s == "E55" || s == "E56" || s == "E57" || s == "E58" || s == "E59" || s == "E60" || s == "E61" || s == "E62" || s == "Ekk") {
		keysta = "E23";
	}
	else if (s == "YTV" || s == "CTV" || s == "STV" || s == "RAB" || s == "ABS" || s == "TVI" || s == "YBC" || s == "MMT" || s == "FCT" || s == "YBS" || s == "TENY" || s == "TSB" || s == "SDT" || s == "KNB" || s == "KTK" || s == "FBC" || s == "RNC" || s == "HTV" || s == "NKT" || s == "KRY" || s == "JRT" || s == "RNB" || s == "RKC" || s == "FBS" || s == "NIB" || s == "KKT" || s == "KYT") {
		keysta = "NTV";
	}
	else if (s == "MBS" || s == "CBC" || s == "HBC" || s == "ATV" || s == "IBC" || s == "TUY" || s == "TBC" || s == "TUF" || s == "UTY" || s == "BSN" || s == "SBC" || s == "SBS" || s == "TUT" || s == "MRO" || s == "RSK" || s == "RCC" || s == "BSS" || s == "TYS" || s == "ITV" || s == "KUTV" || s == "RKB" || s == "NBC" || s == "RKK" || s == "OBS" || s == "MRT" || s == "MBC" || s == "RBC") {
		keysta = "TBS";
	}
	else if (s == "KTV" || s == "THK" || s == "UHB" || s == "AKT" || s == "MIT" || s == "SAY" || s == "OX" || s == "FTV" || s == "NST" || s == "NBS" || s == "SUT" || s == "BBT" || s == "ITC" || s == "FTB" || s == "OHK" || s == "TSS" || s == "TSK" || s == "EBC" || s == "KSS" || s == "TNC" || s == "STS" || s == "KTN" || s == "TKU" || s == "KTS" || s == "OTV") {
		keysta = "CX";
	}
	else if (s == "ABC" || s == "NBN" || s == "HTB" || s == "ABA" || s == "AAB" || s == "IAT" || s == "YTS" || s == "KHB" || s == "KFB" || s == "UX" || s == "ABN" || s == "SATV" || s == "HAB" || s == "KSB" || s == "HOME" || s == "YAB" || s == "EAT" || s == "KBC" || s == "NCC" || s == "KAB" || s == "OAB" || s == "KKB" || s == "QAB") {
		keysta = "EX";
	}
	else if (s == "TVO" || s == "TVA" || s == "TVH" || s == "TSC" || s == "TVQ") {
		keysta = "TX";
	}

	var monthTables = timetables[month];
	if (monthTables) {
		var dayTables = monthTables[day];
		if (dayTables) {
			var StationTables = dayTables[keysta];
			if (StationTables) {

				var splitedColon = timetables[month][day][keysta].split(":");
				var keystas_table = splitedColon[0].split(" ");
				var from = 0, to = 0;
				var result = Array();
				if (!start_time2) {
					start_time2 = start_time;
				}
				for (var i = 0 ; i < keystas_table.length ; i++) {
					if (keystas_table[i].substring(0, start_time.length) == start_time) {
						from = i;
					}
					if (keystas_table[i].substring(0, start_time2.length) == start_time2) {
						to = i;
					}
				}
				for (var i = from ; i <= to ; i++) {
					result.push(keystas_table[i]);
				}
				return result;

			}
		}
	}
	return "";
}

/* この地域のテレビ番組表をまとめて表示 */
function add_tv_area(area) {
	remove_modal();
	var keys;
	switch (area) {
		case "10": keys = ["G10","E10","STV","HBC","UHB","HTB","TVH"]; break;
		case "11": keys = ["G11","E11","STV","HBC","UHB","HTB","TVH"]; break;
		case "12": keys = ["G12","E12","STV","HBC","UHB","HTB","TVH"]; break;
		case "13": keys = ["G13","E13","STV","HBC","UHB","HTB","TVH"]; break;
		case "14": keys = ["G14","E14","STV","HBC","UHB","HTB","TVH"]; break;
		case "15": keys = ["G15","E15","STV","HBC","UHB","HTB","TVH"]; break;
		case "16": keys = ["G16","E16","STV","HBC","UHB","HTB","TVH"]; break;
		case "22": keys = ["G22","E22","RAB","ATV","ABA"]; break;
		case "20": keys = ["G20","E20","TVI","IBC","MIT","IAT"]; break;
		case "17": keys = ["G17","E17","MMT","TBC","OX","KHB"]; break;
		case "18": keys = ["G18","E18","ABS","AKT","AAB"]; break;
		case "19": keys = ["G19","E19","YBC","TUY","SAY","YTS"]; break;
		case "21": keys = ["G21","E21","FCT","TUF","FTB","KFB"]; break;
		case "26": keys = ["G26","E23","NTV","TBS","CX","EX","TX"]; break;
		case "28": keys = ["G28","E23","NTV","TBS","CX","EX","TX","TTV"]; break;
		case "25": keys = ["G25","E23","NTV","TBS","CX","EX","TX","GTV"]; break;
		case "29": keys = ["G13","E23","NTV","TBS","CX","EX","TX","TVS"]; break;
		case "27": keys = ["G13","E23","NTV","TBS","CX","EX","TX","CTC"]; break;
		case "23": keys = ["G13","E23","NTV","TBS","CX","EX","TX","MX"]; break;
		case "24": keys = ["G13","E23","NTV","TBS","CX","EX","TX","TVK"]; break;
		case "31": keys = ["G31","E31","TENY","BSN","NST","UX"]; break;
		case "37": keys = ["G37","E37","KNB","TUT","BBT"]; break;
		case "34": keys = ["G34","E34","KTK","MRO","ITV","HAB"]; break;
		case "36": keys = ["G36","E36","FBC","FTB"]; break;
		case "32": keys = ["G32","E32","YBS","UTY"]; break;
		case "30": keys = ["G30","E30","TSB","SBC","NBS","ABN"]; break;
		case "39": keys = ["G39","E33","CTV","CBC","THK","NBN","GBS"]; break;
		case "35": keys = ["G35","E35","SDT","SBS","SUT","SATV"]; break;
		case "33": keys = ["G33","E33","CTV","CBC","THK","NBN","TVA"]; break;
		case "38": keys = ["G38","E33","CTV","CBC","THK","NBN","MTV"]; break;
		case "45": keys = ["G45","E40","YTV","MBS","KTV","ABC","BBC"]; break;
		case "41": keys = ["G41","E40","YTV","MBS","KTV","ABC","KBS"]; break;
		case "40": keys = ["G40","E40","YTV","MBS","KTV","ABC","TVO"]; break;
		case "42": keys = ["G42","E40","YTV","MBS","KTV","ABC","SUN"]; break;
		case "44": keys = ["G44","E40","YTV","MBS","KTV","ABC","TVN"]; break;
		case "43": keys = ["G43","E40","YTV","MBS","KTV","ABC","WTV"]; break;
		case "49": keys = ["G49","E49","NKT","BSS","TSK"]; break;
		case "48": keys = ["G48","E48","NKT","BSS","TSK"]; break;
		case "47": keys = ["G47","E47","RNC","RSK","OHK","KSB","TSC"]; break;
		case "46": keys = ["G46","E46","HTV","RCC","TSS","HOME"]; break;
		case "50": keys = ["G50","E50","KRY","TYS","YAB"]; break;
		case "53": keys = ["G53","E53","JRT"]; break;
		case "52": keys = ["G52","E52","RNC","RSK","OHK","KSB","TSC"]; break;
		case "51": keys = ["G51","E51","RNB","ITV","EBC","EAT"]; break;
		case "50": keys = ["G50","E50","RKC","KUTV","KSS"]; break;
		case "55": keys = ["G55","E55","FBS","RKB","TNC","KBC","TVQ","Gkk","Ekk"]; break;
		case "61": keys = ["G61","E61","STS"]; break;
		case "57": keys = ["G57","E57","NIB","NBC","KTN","NCC"]; break;
		case "56": keys = ["G56","E56","KKT","RKK","TKU","KAB"]; break;
		case "60": keys = ["G60","E60","OBS","TOS","OAB"]; break;
		case "59": keys = ["G59","E59","MRT","UMK"]; break;
		case "58": keys = ["G58","E58","KYT","MBC","KTS","KKB"]; break;
		case "62": keys = ["G62","E62","RBC","OTV","QAB"]; break;
		default: break;
	}
	for (var i = 0 ; i < keys.length ; i++) {
		add_tv(keys[i]);
	}
}

/* 同じ系列のテレビ番組表をまとめて表示 */
function add_tv_net(tv) {
	remove_modal();
	var keys;
	switch (tv) {
		case "NHK": keys = Object.keys(nhk_list); break;
		case "ETV": keys = Object.keys(etv_list); break;
		case "NTV": keys = Object.keys(ntv_list); break;
		case "TBS": keys = Object.keys(tbs_list); break;
		case "CX": keys = Object.keys(cx_list); break;
		case "EX": keys = Object.keys(ex_list); break;
		case "TX": keys = Object.keys(tx_list); break;
		case "OTHER": keys = Object.keys(other_list); break;
		case "BS": keys = Object.keys(bs_list); break;
		default: break;
	}
	for (var i = 0 ; i < keys.length ; i++) {
		add_tv(keys[i]);
	}
}

/* timetable.jsのデータ読み込み */
function decompressProgramChunk(month, day, tv, chunk_string) {
	// フォーマット1 (例: 8FAB37C126)
	// 最初の2文字は固定。3文字目以降は英字、数字、英字、数字という順に並べてあり、文字種の違いが区切りを表す。
	// チャンク1 (例では8F) は開始時刻を表す2文字で、1文字目が「時」2文字目が「分」を示す。字数を減らすための60進数表記にしてある。
	// チャンク2 (例ではAB) は再放送や字幕放送などのアイコンを表す文字で、複数並べられる。どの文字が何を表すかは type_names.js による。何も無い場合は省略でき、3文字目が数字ならアイコン無しと解釈する。
	// チャンク3 (例では37) は番組名を表す数値で、titles.js の行数と一致する。
	// チャンク4 (例ではC) はジャンルを表す文字で、どの文字が何を表すかは categories.js による。デフォルトはZ。
	// チャンク5 (例では126) は番組概要を表す数値で、descriptions.js の行数と一致する。デフォルトは0。

	// フォーマット2 (例: BP)
	// 開始時刻を表す2文字のみ。キー局の同じ時刻の番組と全く同じ情報であることを意味する。

	// フォーマット3 (例: OP,8113)
	// コンマ区切りで、左側は開始時刻を表す2文字で、右側は番組概要を表す数値。キー局との同時放映ではあるが、番組表の概要の文章に違いがある場合。

	// フォーマット4 (例: 70-DP)
	// 「フォーマット2」が3つ以上連続する場合、間を全てハイフンひとつで省略できる。

	// また、1日の最後の番組データには RvA41Z0:23 などのように、コロン記号の後に放映時間を添えてある。

	var result = Array();
	var chunks = chunk_string.split(" ");
	for (var i = 0 ; i < chunks.length ; i++) {

		var splitedColon = chunks[i].split(":");
		var chunk = splitedColon[0];

		// フォーマット2
		if (chunk.length <= 2) {
			// キー局からフォーマット1のデータを得る
			chunk = fetch_from_key_station(month, day, tv, chunk)[0];
			result.push(decompress(chunk));
			// デバッグ用
			result[result.length-1].original = chunks[i];
			result[result.length-1].decompressed = chunk;
		}
		// フォーマット3
		else if (chunk.indexOf(',') != -1) {
			var splited = chunk.split(",");
			// キー局からフォーマット1のデータを得る
			chunk = fetch_from_key_station(month, day, tv, splited[0])[0];
			// desc_id を付け替える
			for (var c = chunk.length - 1 ; c >= 0 ; c--) {
				if (!(chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9')) {
					chunk = chunk.substring(0, c + 1) + splited[1];
					break;
				}
			}
			result.push(decompress(chunk));
			// デバッグ用
			result[result.length-1].original = chunks[i];
			result[result.length-1].decompressed = chunk;
		}
		// フォーマット4
		else if (chunk.indexOf('-') != -1) {
			var splited = chunk.split("-");
			// キー局からフォーマット1のデータを得る
			var chunklist = fetch_from_key_station(month, day, tv, splited[0], splited[1]);
			for (var c = 0 ; c < chunklist.length ; c++) {
				result.push(decompress(chunklist[c]));
				// デバッグ用
				result[result.length-1].original = chunklist[c];
				result[result.length-1].decompressed = chunk;
			}
		}
		// フォーマット1
		else {
			result.push(decompress(chunk));
			// デバッグ用
			result[result.length-1].original = chunks[i];
			result[result.length-1].decompressed = chunk;
		}
	}

	// 放映時間を計算する
	for (var i = 0 ; i < result.length - 1 ; i++) {
		result[i].interval = get_interval(result[i].start_time, result[i+1].start_time);
	}
	result[result.length-1].interval = splitedColon[1];

	return result;
}

function decompress(chunk) {
	if (!chunk) {
		return {};
	}

	var pointer = 2;
	var start_time = "";
	var title_id = "";
	var category_id = "";
	var desc_id = "";
	var types = Array();

	// 開始時刻
	var hour = base60.indexOf(chunk.charAt(0));
	var minute = base60.indexOf(chunk.charAt(1));
	start_time = (hour < 10 ? "0" : "") + hour + ":" + (minute < 10 ? "0" : "") + minute;

	// アイコン
	for (var c = pointer ; c < chunk.length ; c++) {
		if (chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9') {
			break;
		}
		types.push(chunk.charAt(c));
		pointer++;
	}

	// 題名
	for (var c = pointer ; c < chunk.length ; c++) {
		if (!(chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9')) {
			break;
		}
		title_id += chunk.charAt(c);
		pointer++;
	}

	// ジャンル
	category_id = chunk.charAt(pointer);
	pointer++;

	// 概要
	desc_id = chunk.substring(pointer);

	return {
		start_time: start_time,
		types: types,
		title_id: parseInt(title_id),
		category_id: category_id,
		desc_id: parseInt(desc_id),
	};
}

/* 番組表右上のxボタンを押した時 */
function remove_tv(n) {
	var a = document.getElementById("tv" + n);
	a.remove();
	a = document.getElementById("head" + n);
	a.remove();
}

/* 番組表の作成 */
function add_tv(tv) {
	remove_modal();
	var programs = [];

	if (typeof timetables != "undefined") {
		var monthTables = timetables[selected_month];
		if (monthTables) {
			var dayTables = monthTables[selected_day];
			if (dayTables) {
				var StationTables = dayTables[tv];
				if (StationTables) {
					programs = decompressProgramChunk(selected_month, selected_day, tv, timetables[selected_month][selected_day][tv]);
				}
			}
		}
	}

	var top_space = 0;
	table_index++;

	// テレビ局名のヘッダ
	var station_name = nhk_list[tv];
	if(!station_name)station_name = etv_list[tv];
	if(!station_name)station_name = ntv_list[tv];
	if(!station_name)station_name = tbs_list[tv];
	if(!station_name)station_name = cx_list[tv];
	if(!station_name)station_name = ex_list[tv];
	if(!station_name)station_name = tx_list[tv];
	if(!station_name)station_name = other_list[tv];
	if(!station_name)station_name = bs_list[tv];
	var fontclass = station_name.length > 8 ? "station_font_small" : "station_font";
	var result = '<div id="head' + table_index + '" class="tv_table_header" style="background-color:#404040;text-align:center;vertical-align:top;height:4em;position:relative;display:inline-block;">';
	result += '<div style="color:#d0d0d0;">' + selected_month + '月' + selected_day + '日' + '</div>';
	result += '<div style="font-weight:bold;" class="' + fontclass + '">' + station_name + '</div>';
	result += '<button onclick="remove_tv(' + table_index + ')" style="position:absolute;top:0px;right:0px;">x</button>';
	result += '</div>';
	document.getElementById("headers").insertAdjacentHTML("beforeend", result);

	// 最初の番組が4:00ちょうどから始まらない場合、頭の空白の縦幅を求める
	if (programs.length > 0) {
		top_space = get_interval("4:00", programs[0].start_time);
	}

	// ここから番組表
	result = '<div id="tv' + table_index + '" value="' + (top_space >= 0 ? top_space : 0) + '" class="tv_table" style="display:inline-block;white-space:normal;vertical-align:top;">';

	if (programs.length > 0) {
		for (var i = 0 ; i < programs.length ; i++) {
			var cell_height = programs[i].interval;

			// 開始時刻が午前4時より前の場合、表示調整
			if (i == 0 && top_space < 0) {
				cell_height += top_space;
			}

			// ジャンルによる背景色
			var bgcolor = "#f4f4ff";
			switch (programs[i].category_id) {
				case "H": bgcolor = "#ffb0b0"; break; // アニメ
				case "B": bgcolor = "#ffffff"; break; // スポーツ
				case "E": bgcolor = "#ffff80"; break; // 音楽
				case "D": bgcolor = "#80ff80"; break; // ドラマ
				case "F": bgcolor = "#c0c0ff"; break; // バラエティ
				case "G": bgcolor = "#00ffff"; break; // 映画
				default: break;
			}

			// show_program_modal() に与える引数
			var types_string = "";
			for (var j = 0 ; j < programs[i].types.length ; j++) {
				if (programs[i].types[j] != "Z") {
					types_string += "【" + type_names[programs[i].types[j]].name + "】";
				}
			}
			var args = "'" + programs[i].title_id + "','" + programs[i].start_time + "','" + programs[i].interval + "','" + types_string + "','" + programs[i].category_id + "','" + programs[i].desc_id + "'";

			result += '<div class="table_cell" value="' + cell_height + '" onclick="show_program_modal(' + args + ')">';
			result += '<div class="table_cell_inner" style="border:1px solid #a0a0ff;overflow:hidden;background-color:' + bgcolor + ';">';

			// 開始時刻
			result += '<span style="font-weight:bold;color:#008000;margin-right:2px;">' + programs[i].start_time + '</span>';

			// アイコン
			for (var j = 0 ; j < programs[i].types.length ; j++) {
				if (programs[i].types[j] == "Z") break;
				var iconcolor = "#4040ff";
				switch (type_names[programs[i].types[j]].icon) {
					case "新": iconcolor = "#ff0000"; break;
					case "終": iconcolor = "#000000"; break;
					case "再": iconcolor = "#808080"; break;
					default: break;
				}
				result += '<div style="background-color:' + iconcolor + ';color:white;width:1em;height:1em;line-height:1.2em;display:inline-block;text-align:center;margin-right:2px;">' + type_names[programs[i].types[j]].icon + '</div>';
			}

			// 番組名
			if (typeof titles != "undefined") {
				result += '<span style="color:#202020;">' + titles[programs[i].title_id] + '</span><br />';
			}

			// 番組概要
			if (typeof descriptions != "undefined") {
				result += '<span style="color:#505050;font-size:0.9em;">' + descriptions[programs[i].desc_id] + '</span>';
			}

			result += '</div></div>';
		}

	}
	result += "</div>";

	document.getElementById("new_table").insertAdjacentHTML("beforebegin", result);
	adjust_height(fix_hour_height);
	adjust_width();
}

/* fix=trueの場合は時間ごとの縦幅を統一する、fix=falseの場合は縦幅の指定を無くす */
function adjust_height(fix) {
	var headers = document.getElementsByClassName("tv_table_header");
	var tables = document.getElementsByClassName("tv_table");
	var cells = document.getElementsByClassName("table_cell");
	var cell_inners = document.getElementsByClassName("table_cell_inner");
	var hour_bar_header = document.getElementById("hour_bar_header");
	var hour_bar = document.getElementById("hour_bar");
	var hour_bar_cells = document.getElementsByClassName("hour_bar_cell");

	document.getElementById("tables").style.width = ((tables.length + 1) * 200 + 32) + "px";

	if (fix) {
		for(var i = 0 ; i < headers.length ; i++) {
			var value = parseInt(tables[i].getAttribute("value"));
			tables[i].style.paddingTop = (value * hour_height * 60 / 60) + "px";
		}
		for(var i = 0 ; i < cells.length ; i++) {
			var value = parseInt(cells[i].getAttribute("value"));
			cells[i].style.height = (value * hour_height * 60 / 60) + "px";
			cell_inners[i].style.height = "100%";
		}
		for(var i = 0 ; i < hour_bar_cells.length ; i++) {
			hour_bar_cells[i].style.height = (hour_height * 60) + "px";
		}
		hour_bar_header.style.display = "inline-block";
		hour_bar.style.display = "inline-block";
	} else {
		for(var i = 0 ; i < tables.length ; i++) {
			tables[i].style.paddingTop = "0px";
		}
		for(var i = 0 ; i < cells.length ; i++) {
			cells[i].style.height = "auto";
			cell_inners[i].style.height = "auto";
		}
		hour_bar_header.style.display = "none";
		hour_bar.style.display = "none";
	}
}

function adjust_width() {
	var headers = document.getElementsByClassName("tv_table_header");
	var tables = document.getElementsByClassName("tv_table");
	var station_font = document.getElementsByClassName("station_font");
	var station_font_small = document.getElementsByClassName("station_font_small");
	var fontsize = 1.5 * hour_width / 200;
	for(var i = 0 ; i < headers.length ; i++) {
		headers[i].style.width = hour_width + "px";
	}
	for(var i = 0 ; i < tables.length ; i++) {
		tables[i].style.width = hour_width + "px";
	}
	for(var i = 0 ; i < station_font.length ; i++) {
		station_font[i].style.fontSize = fontsize + "em";
	}
	for(var i = 0 ; i < station_font_small.length ; i++) {
		station_font_small[i].style.fontSize = (fontsize * 0.8) + "em";
	}
}

function change_fix_hour_height(checked) {
	fix_hour_height = checked;
	adjust_height(fix_hour_height);
}

function change_hour_height(value) {
	hour_height = value;
	adjust_height(fix_hour_height);
}

function change_hour_width(value) {
	hour_width = value;
	adjust_width(fix_hour_height);
}

function remove_modal() {
	var modal = document.getElementById("modal");
	if (modal) {
		modal.remove();
	}
}

/* 番組をクリックした時に見せる */
function show_program_modal(title_id, start_time, interval, types, category_id, desc_id) {
	remove_modal();
	var html = '';

	html += '<div id="modal" style="text-align:center;background-color:white;color:black;width:30%;height:80%;white-space:normal;position:fixed;left:35%;top:10%;">';
	html += '<div style="height:2.8em;"><button class="btn btn--green btn--emboss btn--cubic" onclick="remove_modal()">閉じる</button><hr /></div><div style="overflow-y:scroll;width:100%;height:calc(100% - 2.8em);">';
	html += '<table border="1" style="color:black;margin:auto;">';
	html += '<tr><th>番組名</th><td>' + (typeof titles != "undefined" ? titles[title_id] : "") + '</td></tr>';
	html += '<tr><th>開始時刻</th><td>' + start_time + '</td></tr>';
	//html += '<tr><th>放映時間</th><td>' + interval + '分</td></tr>';
	html += '<tr><th>放映形態</th><td>' + types + '</td></tr>';
	html += '<tr><th>ジャンル</th><td>' + categories[category_id] + '</td></tr>';
	html += '<tr><th>番組概要</th><td>' + (typeof descriptions != "undefined" ? descriptions[desc_id] : "") + '</td></tr>';
	html += '</table>';
	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
}

/* 「何々から選ぶ」の次のメニュー */
function show_tv_modal(group_name) {
	remove_modal();
	var html = '<div id="modal" style="text-align:center;background-color:white;color:black;width:50%;height:80%;white-space:normal;position:fixed;left:20%;top:10%;">';

	html += '<div style="height:2.3em;"><button class="btn btn--green btn--emboss btn--cubic" style="float:left;" onclick="show_menu_modal()">戻る</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="remove_modal()">閉じる</button><hr style="clear:both;" /></div>';
	html += '<div style="overflow-y:scroll;width:100%;height:calc(100% - 2.3em);">';

	if (group_name == "NHK") {
		keys = Object.keys(nhk_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + nhk_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'NHK\')">全部並べる</button>';
	}
	else if (group_name == "ETV") {
		keys = Object.keys(etv_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + etv_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'ETV\')">全部並べる</button>';
	}
	else if (group_name == "NTV") {
		keys = Object.keys(ntv_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + ntv_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'NTV\')">全部並べる</button>';
	}
	else if (group_name == "TBS") {
		keys = Object.keys(tbs_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + tbs_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'TBS\')">全部並べる</button>';
	}
	else if (group_name == "CX") {
		keys = Object.keys(cx_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + cx_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'CX\')">全部並べる</button>';
	}
	else if (group_name == "EX") {
		keys = Object.keys(ex_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + ex_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'EX\')">全部並べる</button>';
	}
	else if (group_name == "TX") {
		keys = Object.keys(tx_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + tx_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'TX\')">全部並べる</button>';
	}
	else if (group_name == "OTHER") {
		keys = Object.keys(other_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + other_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'OTHER\')">全部並べる</button>';
	}
	else if (group_name == "BS") {
		keys = Object.keys(bs_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv(\'' + keys[i] + '\')">' + bs_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'BS\')">全部並べる</button>';
	}
	else if (group_name == "AREA") {
		keys = Object.keys(area_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_area(\'' + keys[i] + '\')">' + area_list[keys[i]] + '</button>';
		}
	}

	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
}

/* 日付を選んだ後に表示 */
function show_menu_modal() {
	remove_modal();
	var html = '<div id="modal" style="text-align:center;background-color:white;color:black;width:50%;height:80%;white-space:normal;position:fixed;left:20%;top:10%;">';

	html += '<div style="height:2.3em;"><button class="btn btn--green btn--emboss btn--cubic" style="float:left;" onclick="show_calendar_modal()">戻る</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="remove_modal()">閉じる</button><hr style="clear:both;" /></div>';
	html += '<div style="overflow-y:scroll;width:100%;height:calc(100% - 2.3em);">';

	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'NHK\')">NHK総合から選ぶ</i></button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'ETV\')">NHK教育から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'NTV\')">日テレ系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'TBS\')">TBS系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'CX\')">フジ系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'EX\')">テレ朝系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'TX\')">テレ東系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'OTHER\')">独立局から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'BS\')">BSデジタルから選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_modal(\'AREA\')">地域から選ぶ</button>';

	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
}

/* 「クリックして番組表を追加」をクリックした時に見せる */
function show_calendar_modal() {
	remove_modal();

	var html = '<div id="modal" style="text-align:center;background-color:white;color:black;width:50%;height:80%;white-space:normal;position:fixed;left:20%;top:10%;">';

	html += '<div style="height:2.3em;"><button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="remove_modal()">閉じる</button><hr style="clear:both;" /></div>';
	html += '<div style="overflow-y:scroll;width:100%;height:calc(100% - 2.3em);">';

	// 日付選択
	for (var month = 1 ; month <= 12 ; month++) {
		html += '<h2>' + month + '月</h2>';
		html += '<table border="1" style="margin:auto;text-align:center;">';
		for (var i = 0 ; i < date_list[month].length ; i++) {
			html += '<tr>';
			for (var j = 0 ; j < date_list[month][i].length ; j++) {
				html += '<td style="width:3em;">';
				if (date_list[month][i][j] != 0) {
					var day = date_list[month][i][j];
					if (typeof timetables[month] != "undefined" && typeof timetables[month][day] != "undefined") {
						html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="selected_month=' + month + ';selected_day=' + day + ';show_menu_modal();">' + day + '</button>';
					} else {
						html += '<span style="font-size:1.5em;color:black;">' + day + '</span>';
					}
				}
				html += '</td>';
			}
			html += '</tr>';
		}
		html += '</table>';
	}

	html += '</div></div>';
	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
}

function setup_first_table() {
	var html = '';

	// 「縦幅の調整」チェックボックス
	html += '<input type="checkbox" id="fix_hour_height" onchange="change_fix_hour_height(checked)" checked></input><label for="fix_hour_height">縦幅の調整</label>';
	html += ' (<input type="number" id="hour_height" onchange="change_hour_height(value)" value="' + hour_height + '" checked></input>倍の縦幅)';
	html += ' : 横幅<input type="number" id="hour_width" onchange="change_hour_width(value)" value="' + hour_width + '" checked></input>px)';

	html += '<div style="white-space: nowrap;">';

	// 番組表ヘッダを表示する場所
	html += '<div id="headers">';
	html += '<div id="hour_bar_header" style="width:30px;height:4em;background-color:blue;display: none;vertical-align:top;"></div>';
	html += '</div><div style="clear:both;"></div>';

	// 番組表を表示する場所
	html += '<div id="tables" style="width:auto;height:75%;overflow-y:scroll;overflow-x:hidden;">';
	html += '<div id="hour_bar" style="width:30px;background-color:#000040;display: none;vertical-align:top;">';
	for (var i = 4 ; i <= 27 ; i++) {
		html += '<div class="hour_bar_cell" style="height:' + (hour_height * 60) + 'px;"><div style="height:100%;font-weight:bold;font-size:1.5em;text-align:center;border:solid 1px #0000ff;">' + i + '</div></div>';
	}
	html += '</div>';
	html += '<div id="new_table" style="width:200px;height:90%;border:1px dotted;display: inline-block;vertical-align:top;" onclick="show_calendar_modal()">';
	html += '<div style="font-size:5em;text-align:center;">+</div>クリックして番組表を追加';
	html += '</div>';
	html += '</div><div style="clear:both;"></div>';

	html += '</div>';

	document.getElementById("app").innerHTML = html;
}

function init() {
	create_calendar();
	setup_first_table();
}

init();
