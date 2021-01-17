var selected_tv = "";
var selected_year = 2021;
var selected_month = 4;
var selected_day = 1;
var selected_station = "";
var station_select_mode = "";
var adding_way_mode = 0;
var table_index = 0;
var hour_height = 3;
var hour_width = 200;
var font_size = 16;
var fix_hour_height = true;
var now_showing = Array();

var search_title = "";
var search_description = "";
var search_month = Array();
var search_station = Array();
var mutable_station_form = Array();
var searching_month = 1;
var searching_day = 1;
var search_hits = 0;
var search_progress = 0;
var search_progress_max = 0;
var searching_process;

decoder1_range = decoder1.length;
decoder2_range = decoder2.length / 2;
decoder3_range = decoder3.length / 3;

// 時刻のdecodeに用いる60進数
var base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"];
// チャプター番号のdecodeに用いる50進数
var base50 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"];
// タイトル・番組概要のdecodeに用いる50進数
var base64_special = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","$","{","|","}",";","*","_","~","^","`","'"];

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

var nhk1_list = {
	NHK1_010: "NHKラジオ第1・札幌",
	NHK1_011: "NHKラジオ第1・函館",
	NHK1_012: "NHKラジオ第1・旭川",
	NHK1_013: "NHKラジオ第1・帯広",
	NHK1_014: "NHKラジオ第1・釧路",
	NHK1_015: "NHKラジオ第1・北見",
	NHK1_016: "NHKラジオ第1・室蘭",
	NHK1_020: "NHKラジオ第1・青森",
	NHK1_030: "NHKラジオ第1・盛岡",
	NHK1_040: "NHKラジオ第1・仙台",
	NHK1_050: "NHKラジオ第1・秋田",
	NHK1_060: "NHKラジオ第1・山形",
	NHK1_070: "NHKラジオ第1・福島",
	NHK1_130: "NHKラジオ第1・東京",
	NHK1_150: "NHKラジオ第1・新潟",
	NHK1_160: "NHKラジオ第1・富山",
	NHK1_170: "NHKラジオ第1・石川",
	NHK1_180: "NHKラジオ第1・福井",
	NHK1_190: "NHKラジオ第1・甲府",
	NHK1_200: "NHKラジオ第1・長野",
	NHK1_220: "NHKラジオ第1・静岡",
	NHK1_230: "NHKラジオ第1・名古屋",
	NHK1_250: "NHKラジオ第1・大津",
	NHK1_270: "NHKラジオ第1・大阪",
	NHK1_310: "NHKラジオ第1・鳥取",
	NHK1_320: "NHKラジオ第1・松江",
	NHK1_330: "NHKラジオ第1・岡山",
	NHK1_340: "NHKラジオ第1・広島",
	NHK1_350: "NHKラジオ第1・山口",
	NHK1_360: "NHKラジオ第1・徳島",
	NHK1_370: "NHKラジオ第1・高松",
	NHK1_380: "NHKラジオ第1・松山",
	NHK1_390: "NHKラジオ第1・高知",
	NHK1_400: "NHKラジオ第1・福岡",
	NHK1_401: "NHKラジオ第1・北九州",
	NHK1_410: "NHKラジオ第1・佐賀",
	NHK1_420: "NHKラジオ第1・長崎",
	NHK1_430: "NHKラジオ第1・熊本",
	NHK1_440: "NHKラジオ第1・大分",
	NHK1_450: "NHKラジオ第1・宮崎",
	NHK1_460: "NHKラジオ第1・鹿児島",
	NHK1_470: "NHKラジオ第1・沖縄"
};

var nhkfm_list = {
	NHKFM_010: "NHK-FM・札幌",
	NHKFM_011: "NHK-FM・函館",
	NHKFM_012: "NHK-FM・旭川",
	NHKFM_013: "NHK-FM・帯広",
	NHKFM_014: "NHK-FM・釧路",
	NHKFM_015: "NHK-FM・北見",
	NHKFM_016: "NHK-FM・室蘭",
	NHKFM_020: "NHK-FM・青森",
	NHKFM_030: "NHK-FM・盛岡",
	NHKFM_040: "NHK-FM・仙台",
	NHKFM_050: "NHK-FM・秋田",
	NHKFM_060: "NHK-FM・山形",
	NHKFM_070: "NHK-FM・福島",
	NHKFM_080: "NHK-FM・水戸",
	NHKFM_090: "NHK-FM・宇都宮",
	NHKFM_100: "NHK-FM・前橋",
	NHKFM_110: "NHK-FM・さいたま",
	NHKFM_120: "NHK-FM・千葉",
	NHKFM_130: "NHK-FM・東京",
	NHKFM_140: "NHK-FM・横浜",
	NHKFM_150: "NHK-FM・新潟",
	NHKFM_160: "NHK-FM・富山",
	NHKFM_170: "NHK-FM・石川",
	NHKFM_180: "NHK-FM・福井",
	NHKFM_190: "NHK-FM・甲府",
	NHKFM_200: "NHK-FM・長野",
	NHKFM_210: "NHK-FM・岐阜",
	NHKFM_220: "NHK-FM・静岡",
	NHKFM_230: "NHK-FM・名古屋",
	NHKFM_240: "NHK-FM・津",
	NHKFM_250: "NHK-FM・大津",
	NHKFM_260: "NHK-FM・京都",
	NHKFM_270: "NHK-FM・大阪",
	NHKFM_280: "NHK-FM・神戸",
	NHKFM_290: "NHK-FM・奈良",
	NHKFM_300: "NHK-FM・和歌山",
	NHKFM_310: "NHK-FM・鳥取",
	NHKFM_320: "NHK-FM・松江",
	NHKFM_330: "NHK-FM・岡山",
	NHKFM_340: "NHK-FM・広島",
	NHKFM_350: "NHK-FM・山口",
	NHKFM_360: "NHK-FM・徳島",
	NHKFM_370: "NHK-FM・高松",
	NHKFM_380: "NHK-FM・松山",
	NHKFM_390: "NHK-FM・高知",
	NHKFM_400: "NHK-FM・福岡",
	NHKFM_401: "NHK-FM・北九州",
	NHKFM_410: "NHK-FM・佐賀",
	NHKFM_420: "NHK-FM・長崎",
	NHKFM_430: "NHK-FM・熊本",
	NHKFM_440: "NHK-FM・大分",
	NHKFM_450: "NHK-FM・宮崎",
	NHKFM_460: "NHK-FM・鹿児島",
	NHKFM_470: "NHK-FM・沖縄"
};

var am_list = {
	HBC: "HBCラジオ",
	STV: "STVラジオ",
	RAB: "RAB青森放送",
	IBC: "IBCラジオ",
	TBC: "TBCラジオ",
	ABS: "ABS秋田放送",
	YBC: "YBC山形放送",
	RFC: "RFCラジオ福島",
	IBS: "IBS茨城放送",
	CRT: "CRT栃木放送",
	TBS: "TBSラジオ",
	QRR: "文化放送",
	LFR: "ニッポン放送",
	JORF: "ラジオ日本",
	YBS: "YBSラジオ",
	BSN: "BSNラジオ",
	SBC: "SBCラジオ",
	MRO: "MROラジオ",
	KNB: "KNBラジオ",
	FBC: "FBCラジオ",
	SBS: "SBSラジオ",
	CBC: "CBCラジオ",
	TOKAIRADIO: "東海ラジオ",
	GBS: "ぎふチャン",
	ABC: "ABCラジオ",
	MBS: "MBSラジオ",
	OBC: "OBCラジオ大阪",
	KBS: "KBS京都ラジオ",
	CRK: "ラジオ関西",
	WBS: "WBS和歌山放送",
	BSS: "BSSラジオ",
	RSK: "RSKラジオ",
	RCC: "RCCラジオ",
	KRY: "KRY山口放送",
	RNC: "RNC西日本放送",
	JRT: "JRT四国放送",
	RNB: "RNB南海放送",
	RKC: "RKC高知放送",
	RKB: "RKBラジオ",
	KBC: "KBCラジオ",
	NBC: "NBC長崎放送",
	RKK: "RKKラジオ",
	OBS: "OBSラジオ",
	MRT: "宮崎放送",
	MBC: "MBCラジオ",
	RBC: "RBCiラジオ",
	ROK: "ラジオ沖縄"
};

var fm_list = {
	AIRG: "AIR-G’ FM北海道",
	NORTHWAVE: "FM NORTH WAVE",
	AFB: "エフエム青森",
	FMI: "エフエム岩手",
	DATEFM: "Date fm エフエム仙台",
	AFM: "エフエム秋田",
	RFM: "Rhythm Station エフエム山形",
	FMF: "ふくしまFM",
	INT: "InterFM897",
	FMT: "TOKYO FM",
	FMJ: "J-WAVE",
	BAYFM78: "bayfm78",
	NACK5: "NACK5",
	YFM: "FMヨコハマ",
	RADIOBERRY: "RadioBerry",
	FMGUNMA: "FM GUNMA",
	FMNIIGATA: "FM NIIGATA",
	FMTOYAMA: "FMとやま",
	HELLOFIVE: "エフエム石川",
	FMFUKUI: "FM福井",
	FMFUJI: "FM FUJI",
	FMN: "FM長野",
	ZIPFM: "ZIP-FM",
	FMAICHI: "FM AICHI",
	FMGIFU: "FM GIFU",
	KMIX: "K-MIX SHIZUOKA",
	FMMIE: "レディオキューブ FM三重",
	CCL: "FM COCOLO",
	802: "FM802",
	FMO: "FM大阪",
	KISSFMKOBE: "Kiss FM KOBE",
	ERADIO: "e-radio FM滋賀",
	ALPHASTATION: "α-STATION FM京都",
	FMSANIN: "エフエム山陰",
	FMOKAYAMA: "FM岡山",
	HFM: "広島FM",
	FMY: "エフエム山口",
	FM807: "FM徳島",
	FMKAGAWA: "エフエム香川",
	JOEUFM: "FM愛媛",
	HISIX: "エフエム高知",
	LOVEFM: "LOVE FM",
	CROSSFM: "CROSS FM",
	FMFUKUOKA: "FM FUKUOKA",
	FMS: "エフエム佐賀",
	FMNAGASAKI: "FM長崎",
	FMK: "FMKエフエム熊本",
	FMOITA: "エフエム大分",
	JOYFM: "エフエム宮崎",
	MYUFM: "μFM",
	FMOKINAWA: "FM沖縄"
};

var other_list = {
	NHK2: "NHKラジオ第2",
	RN1: "ラジオNIKKEI第1",
	RN2: "ラジオNIKKEI第2",
	HOUSOUDAIGAKU: "放送大学"
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

function split_chunk(s) {
	var splited = Array();
	var index = 0;
	splited[0] = "";
	for (var i = 0 ; i < s.length ; i++) {
		if (s[i] == ":") {
			index--;
			splited.pop();
		}
		splited[index] += s[i];
		if (s[i] == "." || s[i] == ",") {
			index++;
			splited[index] = "";
		}
	}
	return splited;
}

/* キー局あるいはメインチャンネル番組表から同じ時刻の番組データを拾ってくる事により、省略されたchunkを復元する */
function fetch_from_key_station(month, day, s, chunk_string) {
	var keysta = "";
	if (s == "NHK1_010" || s == "NHK1_011" || s == "NHK1_012" || s == "NHK1_013" || s == "NHK1_014" || s == "NHK1_015" || s == "NHK1_016" || s == "NHK1_020" || s == "NHK1_030" || s == "NHK1_040" || s == "NHK1_050" || s == "NHK1_060" || s == "NHK1_070" || s == "NHK1_150" || s == "NHK1_160" || s == "NHK1_170" || s == "NHK1_180" || s == "NHK1_190" || s == "NHK1_200" || s == "NHK1_220" || s == "NHK1_230" || s == "NHK1_250" || s == "NHK1_270" || s == "NHK1_310" || s == "NHK1_320" || s == "NHK1_330" || s == "NHK1_340" || s == "NHK1_350" || s == "NHK1_360" || s == "NHK1_370" || s == "NHK1_380" || s == "NHK1_390" || s == "NHK1_400" || s == "NHK1_401" || s == "NHK1_410" || s == "NHK1_420" || s == "NHK1_430" || s == "NHK1_440" || s == "NHK1_450" || s == "NHK1_460" || s == "NHK1_470") {
		keysta = "NHK1_130";
	}
	else if (s == "NHKFM_010" || s == "NHKFM_011" || s == "NHKFM_012" || s == "NHKFM_013" || s == "NHKFM_014" || s == "NHKFM_015" || s == "NHKFM_016" || s == "NHKFM_020" || s == "NHKFM_030" || s == "NHKFM_040" || s == "NHKFM_050" || s == "NHKFM_060" || s == "NHKFM_070" || s == "NHKFM_080" || s == "NHKFM_090" || s == "NHKFM_100" || s == "NHKFM_110" || s == "NHKFM_120" || s == "NHKFM_140" || s == "NHKFM_150" || s == "NHKFM_160" || s == "NHKFM_170" || s == "NHKFM_180" || s == "NHKFM_190" || s == "NHKFM_200" || s == "NHKFM_210" || s == "NHKFM_220" || s == "NHKFM_230" || s == "NHKFM_240" || s == "NHKFM_250" || s == "NHKFM_260" || s == "NHKFM_270" || s == "NHKFM_280" || s == "NHKFM_290" || s == "NHKFM_300" || s == "NHKFM_310" || s == "NHKFM_320" || s == "NHKFM_330" || s == "NHKFM_340" || s == "NHKFM_350" || s == "NHKFM_360" || s == "NHKFM_370" || s == "NHKFM_380" || s == "NHKFM_390" || s == "NHKFM_400" || s == "NHKFM_401" || s == "NHKFM_410" || s == "NHKFM_420" || s == "NHKFM_430" || s == "NHKFM_440" || s == "NHKFM_450" || s == "NHKFM_460" || s == "NHKFM_470") {
		keysta = "NHKFM_130";
	}
	else if (s == "AIRG" || s == "AFB" || s == "FMI" || s == "DATEFM" || s == "AFM" || s == "RFM" || s == "FMF" || s == "RADIOBERRY" || s == "FMGUNMA" || s == "FMNIIGATA" || s == "FMTOYAMA" || s == "HELLOFIVE" || s == "FMFUKUI" || s == "FMN" || s == "FMAICHI" || s == "FMGIFU" || s == "KMIX" || s == "FMMIE" || s == "FMO" || s == "KISSFMKOBE" || s == "ERADIO" || s == "FMSANIN" || s == "FMOKAYAMA" || s == "HFM" || s == "FMY" || s == "FM807" || s == "FMKAGAWA" || s == "JOEUFM" || s == "HISIX" || s == "FMFUKUOKA" || s == "FMS" || s == "FMNAGASAKI" || s == "FMK" || s == "FMOITA" || s == "JOYFM" || s == "MYUFM" || s == "FMOKINAWA") {
		keysta = "FMT";
	}

	var keystas_table = Array();
	var keysta_string = "";
	if (timetables[month] && timetables[month][day] && timetables[month][day][keysta]) {
		keysta_string = timetables[month][day][keysta];
	}
	var splitedColon = keysta_string.split(":");
	keystas_table = split_chunk(splitedColon[0]);

	var result = Array();
	var chunks = split_chunk(chunk_string);
	for (var c = 0 ; c < chunks.length ; c++) {
		var splitedColon = chunks[c].split(":");
		var chunk = splitedColon[0];

		var splited_by_space = (chunk[chunk.length-1] == ",");
		chunk = chunk.substring(0, chunk.length-1);

		// フォーマット2
		if (chunk.length <= 2) {
			// キー局からフォーマット1のデータを得る
			for (var k = 0 ; k < keystas_table.length ; k++) {
				if (chunk == keystas_table[k].substring(0,2)) {
					result.push(keystas_table[k]);
					break;
				}
			}
		}
		// フォーマット3
		else if (chunk.indexOf('*') != -1) {
			var splited = chunk.split("*");
			// キー局からフォーマット1のデータを得る
			for (var i = 0 ; i < keystas_table.length ; i++) {
				var hit = false;
				if (splited[0] == keystas_table[i].substring(0,2)) {
					hit = true;
					// desc_id を付け替える
					for (var k = keystas_table[i].length - 2 ; k >= 0 ; k--) {
						if (!(keystas_table[i].charAt(k) >= '0' && keystas_table[i].charAt(k) <= '9')) {
							result.push(keystas_table[i].substring(0, k + 1) + splited[1] + keystas_table[i].substring(keystas_table[i].length-1));
							break;
						}
					}
				}
				if (hit) break;
			}
		}
		// フォーマット4
		else if (chunk.indexOf('-') != -1) {
			var splited = chunk.split("-");
			// キー局からフォーマット1のデータを得る
			var start = false;
			for (var k = 0 ; k < keystas_table.length ; k++) {
				if (splited[0] == keystas_table[k].substring(0,2)) {
					start = true;
				}
				if (start) {
					result.push(keystas_table[k]);
				}
				if (splited[1] == keystas_table[k].substring(0,2)) {
					break;
				}
			}
		}
		// フォーマット1
		else {
			result.push(chunk + (splited_by_space ? "," : "."));
		}
	}

	return result.join("") + ":" + chunk_string.split(":")[1];
}

function get_tv_by_net(net) {
	var keys;
	switch (net) {
		case "NHK1": keys = Object.keys(nhk1_list); break;
		case "NHKFM": keys = Object.keys(nhkfm_list); break;
		case "AM": keys = Object.keys(am_list); break;
		case "FM": keys = Object.keys(fm_list); break;
		case "OTHER": keys = Object.keys(other_list); break;
		default: break;
	}
	return keys;
}

/* 同じ系列のラジオ番組表をまとめて表示 */
function add_radio_net(tv) {
	remove_modal();
	var keys = get_tv_by_net(tv);
	for (var i = 0 ; i < keys.length ; i++) {
		add_radio(keys[i]);
	}
	remove_modal();
}

/* timetable.jsのデータ読み込み */
function decompressProgramChunk(month, day, tv, chunk_string) {
	// フォーマット1 (例: 8F37_126. 8FR37B126.)
	// 最初の2文字は固定。3文字目以降英字、数字、英字、数字という順に並べてあり、文字種の違いが区切りを表す。
	// チャンク1 (例では8F) は開始時刻を表す2文字で、1文字目が「時」2文字目が「分」を示す。字数を減らすための60進数表記にしてある。
	// チャンク2 (例ではR) は再放送を表す。この3文字目のRは通常は省略する。
	// チャンク3 (例では37) は番組名を表す数値で、titles.js の行数と一致する。
	// チャンク4 (例ではアンダースコアまたはB) はチャプター番号を表す50進数。無い場合は代わりにアンダースコアを置く。
	// チャンク5 (例では126) は番組概要を表す数値で、descriptions.js の行数と一致する。デフォルトは0。

	// フォーマット2 (例: BP.)
	// 開始時刻を表す2文字のみ。キー局の同じ時刻の番組と全く同じ情報であることを意味する。

	// フォーマット3 (例: OP*8113.)
	// アスタリスクで区切り、左側は開始時刻を表す2文字で、右側は番組概要を表す数値になる。キー局との同時放映ではあるが、番組表の概要の文章に違いがある場合。

	// フォーマット4 (例: 70-DP.)
	// 「フォーマット2」が3つ以上連続する場合、間を全てハイフンひとつで省略できる。

	// また、1日の最後の番組データには Rv41,0.:23 などのように、コロン記号の後に放映時間を添えてある。

	// ピリオド(.)またはコンマ(,)は末尾を表す区切り文字。ただしフォーマット1でコンマの場合は、番組名とチャプターを半角スペースで区切るという意味も表す。

	var result = Array();
	var full_chunk_string = fetch_from_key_station(month, day, tv, chunk_string);
	var chunks = split_chunk(full_chunk_string);
	for (var i = 0 ; i < chunks.length ; i++) {
		var splitedColon = chunks[i].split(":");
		var chunk = splitedColon[0];
		result.push(decompress(chunk));
		// デバッグ用
		result[result.length-1].original_chunk = chunks[i];
	}

	// 放映時間を計算する
	for (var i = 0 ; i < result.length - 1 ; i++) {
		result[i].interval = get_interval(result[i].start_time, result[i+1].start_time);
	}
	result[result.length-1].interval = chunk_string.split(":")[1];

	return result;
}

function decompress(chunk) {
	if (!chunk) {
		return {};
	}

	var pointer = 0;
	var start_time = "";
	var title_id = "";
	var chapter_id = 0;
	var desc_id = "";
	var rerun = false;

	var splited_by_space = (chunk[chunk.length-1] == ",");
	chunk = chunk.substring(0,chunk.length-1);

	// 開始時刻
	var hour = base60.indexOf(chunk.charAt(0));
	pointer++;
	var minute = base60.indexOf(chunk.charAt(1));
	pointer++;
	start_time = (hour < 10 ? "0" : "") + hour + ":" + (minute < 10 ? "0" : "") + minute;

	// 再放送
	if (chunk.charAt(pointer) == 'R') {
		rerun = true;
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

	// チャプター
	if (chunk.charAt(pointer) == '_') {
		chapter_id = -1;
		pointer++;
	} else {
		for (var c = pointer ; c < chunk.length ; c++) {
			if (chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9') {
				break;
			}
			chapter_id = chapter_id * 50 + base50.indexOf(chunk.charAt(c));
			pointer++;
		}
	}

	// 概要
	desc_id = chunk.substring(pointer);

	return {
		start_time: start_time,
		title_id: parseInt(title_id),
		chapter_id: chapter_id,
		desc_id: parseInt(desc_id),
		title: typeof titles != "undefined" ? decode_string(titles[title_id][0]) : "",
		chapter: typeof titles != "undefined" && titles[title_id].length == 2 && chapter_id != -1 ? decode_string(titles[title_id][1][chapter_id]) : "",
		description: typeof descriptions != "undefined" ? decode_string(descriptions[desc_id]) : "",
		rerun: rerun,
		splited_by_space: splited_by_space
	};
}

/* タイトルや番組概要の復元 */
function decode_string(s) {
	// radio_titles.js および radio_descriptions.js は独自の2バイト文字コードに圧縮されている。
	// 「半角英字および使用頻度の低い記号による2文字」は独自の64進数で、decoder.jsに書いてある単語のいくつ目と置き換えるかを表す。
	// decoder.js に収容できる単語は4096個までで、そこに入り切らなかった文字はそのままになっている。
	// 他の半角記号・半角数字は何の変換もせず、そのままになっている。
	// < > で囲まれた半角英字は、変換せずにそのまま出力する。（半角記号 < > は文章に使わない前提として、全角記号の＜＞に置き換えてある）

	var result = "";
	var in_abc_mode = false;
	for (var i = 0 ; i < s.length ; i++) {
		if(s.charAt(i) == '\n') {
			result += '<br />';
		}
		else if (in_abc_mode) {
			if (s.charAt(i) == '>') {
				in_abc_mode = false;
			} else {
				result += s.charAt(i);
			}
		} else {
			if (s.charAt(i) == '<') {
				in_abc_mode = true;
			}
			else if (base64_special.indexOf(s.charAt(i)) != -1) {
				var code = base64_special.indexOf(s.charAt(i)) * 64 + base64_special.indexOf(s.charAt(i+1));
				if (code < decoder1_range) {
					result += decoder1.charAt(code);
				}
				else if (code < decoder1_range + decoder2_range) {
					result += decoder2.charAt((code - decoder1_range)*2) + decoder2.charAt((code - decoder1_range)*2+1);
				} else {
					result += decoder3.charAt((code - decoder1_range - decoder2_range)*3) + decoder3.charAt((code - decoder1_range - decoder2_range)*3+1) + decoder3.charAt((code - decoder1_range - decoder2_range)*3+2);
				}
				i++;
			} else {
				result += s.charAt(i);
			}
		}
	}
	return result;
}

/* 番組表右上のxボタンを押した時 */
function remove_tv(n) {
	var a = document.getElementById("tv" + n);
	a.remove();
	a = document.getElementById("head" + n);
	a.remove();
	delete now_showing[n];
}

function slide_yesterday(tv, month, day, insert) {
	day--;
	if (day == 0) {
		day = new Date(selected_year, month-1, 0).getDate();
		month--;
	}
	if (month == 0) {
		return;
	}
	add_radio(tv, month, day, insert);
}

function slide_tomorrow(tv, month, day, insert) {
	day++;
	if (day > new Date(selected_year, month, 0).getDate()) {
		day = 1;
		month++;
	}
	if (month == 13) {
		return;
	}
	add_radio(tv, month, day, insert);
}

function wide_cell(e) {
	if (!fix_hour_height) return;
	var test1 = e.cloneNode(true);
	test1.style.width=hour_width + "px";
	test1.style.height = "auto";
	test1.children[0].style.height = "auto";
	document.getElementById("sizetest").appendChild(test1);
	var autoSize = document.getElementById("sizetest").children[0].getBoundingClientRect();
	document.getElementById("sizetest").children[0].remove();
	if (autoSize.height > e.clientHeight) {
		e.style.height = autoSize.height + "px";
		e.children[0].style.height = autoSize.height + "px";
	}
}

function narrow_cell(e) {
	if (!fix_hour_height) return;
	e.style.height = (parseInt(e.attributes["value"].nodeValue) * hour_height * 60 / 60) + "px";
	e.children[0].style.height = "100%";
}

/* ラジオ局名の取得 */
function get_station_name(tv) {
	var station_name = nhk1_list[tv];
	if(!station_name)station_name = nhkfm_list[tv];
	if(!station_name)station_name = am_list[tv];
	if(!station_name)station_name = fm_list[tv];
	if(!station_name)station_name = other_list[tv];
	if(!station_name)return "";
	return station_name;
}

function render_program_cell(program, fs) {
	var html = '';
	// 開始時刻
	html += '<span class="program_time" style="font-size:' + fs + 'px;">' + program.start_time + '</span>';

	// 番組名
	if (program.rerun) {
		html += '<div class="program_icon icon_re" style="font-size:' + fs + 'px;min-width:' + fs + 'px;height:' + fs + 'px;line-height:' + (fs*1.2) + 'px;">再</div>';
	}
	html += '<span class="program_title" style="font-size:' + fs + 'px;">' + program.title + '</span>';
	if (program.chapter != "") {
		if (program.splited_by_space) {
			html += ' ';
		}
		html += '<span class="program_chapter">' + program.chapter + '</span>';
	}
	html += '<br />';

	// 番組概要
	html += '<span class="program_desc" style="font-size:' + (fs*0.9) + 'px;">' + program.description + '</span>';

	return html;
}

/* 番組表の作成 */
function add_radio(tv, month, day, insert) {
	var programs = [];

	if (typeof month == "undefined") {
		month = selected_month;
	}
	if (typeof day == "undefined") {
		day = selected_day;
	}

	if (typeof timetables != "undefined") {
		var monthTables = timetables[month];
		if (monthTables) {
			var dayTables = monthTables[day];
			if (dayTables) {
				var StationTables = dayTables[tv];
				if (StationTables) {
					programs = decompressProgramChunk(month, day, tv, timetables[month][day][tv]);
				}
			}
		}
	}

	var top_space = 0;
	table_index++;

	// ラジオ局名のヘッダ
	var station_name = get_station_name(tv);
	var fontclass = station_name.length > 8 ? "station_font_small" : "station_font";
	var result = '<div id="head' + table_index + '" class="tv_table_header">';
	result += '<div class="tv_table_header_date">';
	result += '<button class="tv_table_header_date_button" onClick="slide_yesterday(\'' + tv + '\',' + month + ',' + day + ',' + table_index + ')">▲</button>';
	result += month + '月' + day + '日';
	result += '<button class="tv_table_header_date_button" onClick="slide_tomorrow(\'' + tv + '\',' + month + ',' + day + ',' + table_index + ')">▼</button>';
	result += '</div>';
	result += '<div class="tv_table_header_station_name ' + fontclass + '">' + station_name + '</div>';
	result += '<button class="tv_table_header_close_button" onclick="remove_tv(' + table_index + ')" style="position:absolute;top:0px;right:0px;">x</button>';
	result += '</div>';

	if (typeof insert == "undefined") {
		document.getElementById("headers").insertAdjacentHTML("beforeend", result);
	} else {
		document.getElementById("head" + insert).insertAdjacentHTML("afterend", result);
	}

	// 最初の番組が4:00ちょうどから始まらない場合、頭の空白の縦幅を求める
	if (programs.length > 1 && programs[0].start_time > programs[1].start_time) {
		top_space = -240 - get_interval(programs[0].start_time, "24:00");
	}
	else if (programs.length > 0) {
		top_space = get_interval("4:00", programs[0].start_time);
	}

	// ここから番組表
	result = '<div id="tv' + table_index + '" value="' + (top_space >= 0 ? top_space : 0) + '" class="tv_table" style="padding-bottom:15em;display:inline-block;white-space:normal;vertical-align:top;">';

	if (programs.length > 0) {
		for (var i = 0 ; i < programs.length ; i++) {
			var cell_height = programs[i].interval;

			// 開始時刻が午前4時より前の場合、表示調整
			if (i == 0 && top_space < 0) {
				cell_height += top_space;
			}

			// show_program_modal() に与える引数
			var args = "'" + station_name + "','" + programs[i].rerun + "','" + programs[i].title.replace("'", "\\'") + "','" + programs[i].chapter.replace("'", "\\'") + "','" + month + "','" + day + "','" + programs[i].start_time + "','" + programs[i].interval + "','" + programs[i].description.replace("'", "\\'") + "'";

			result += '<div class="table_cell" value="' + cell_height + '" onclick="show_program_modal(' + args + ')" onmouseover="wide_cell(this)" onmouseout="narrow_cell(this)" style="transition: all 0.1s linear;">';
			result += '<div class="table_cell_inner" style="overflow:hidden;transition: all 0.1s linear;">';

			result += render_program_cell(programs[i], font_size);

			result += '</div></div>';
		}

	}
	result += "</div>";

	if (typeof insert == "undefined") {
		document.getElementById("new_table").insertAdjacentHTML("beforebegin", result);
	} else {
		document.getElementById("tv" + insert).insertAdjacentHTML("afterend", result);
		remove_tv(insert);
	}

	adjust_height(fix_hour_height);
	adjust_width();
	now_showing[table_index] = {tv:tv, month:month, day:day};
}

/* fix=trueの場合は時間ごとの縦幅を統一する、fix=falseの場合は縦幅の指定を無くす */
function adjust_height(fix) {
	var headers = document.getElementsByClassName("tv_table_header");
	var tables = document.getElementsByClassName("tv_table");
	var cells = document.getElementsByClassName("table_cell");
	var cell_inners = document.getElementsByClassName("table_cell_inner");
	var hour_bar_cells = document.getElementsByClassName("hour_bar_cell");

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
			hour_bar_cells[i].style.height = (hour_height * 60 - 2) + "px";
			hour_bar_cells[i].style.display = "block";
		}
	} else {
		for(var i = 0 ; i < tables.length ; i++) {
			tables[i].style.paddingTop = "0px";
		}
		for(var i = 0 ; i < cells.length ; i++) {
			cells[i].style.height = "auto";
			cell_inners[i].style.height = "auto";
		}
		for(var i = 0 ; i < hour_bar_cells.length ; i++) {
			hour_bar_cells[i].style.display = "none";
		}
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
	document.getElementById("tables").style.width = ((tables.length + 1) * hour_width + 32) + "px";
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

function change_font_size(value) {
	font_size = value;
	var times = document.getElementsByClassName("program_time");
	var icons = document.getElementsByClassName("program_icon");
	var title_names = document.getElementsByClassName("program_title");
	var chapters = document.getElementsByClassName("program_chapter");
	var descs = document.getElementsByClassName("program_desc");
	for(var i = 0 ; i < times.length ; i++) {
		times[i].style.fontSize = font_size + "px";
	}
	for(var i = 0 ; i < icons.length ; i++) {
		icons[i].style.fontSize = font_size + "px";
		icons[i].style.width = font_size + "px";
		icons[i].style.height = font_size + "px";
		icons[i].style.lineHeight = (font_size*1.2) + "px";
	}
	for(var i = 0 ; i < title_names.length ; i++) {
		title_names[i].style.fontSize = font_size + "px";
	}
	for(var i = 0 ; i < chapters.length ; i++) {
		chapters[i].style.fontSize = font_size + "px";
	}
	for(var i = 0 ; i < descs.length ; i++) {
		descs[i].style.fontSize = (font_size*0.9) + "px";
	}
}

function remove_modal() {
	clearInterval(searching_process);
	var modal = document.getElementById("modal");
	if (modal) {
		modal.remove();
	}
}

/* 番組をクリックした時に見せる */
function show_program_modal(station_name, rerun, title, chapter, month, day, start_time, interval, description) {
	remove_modal();
	var html = '';

	html += '<div id="modal" style="text-align:center;background-color:white;color:black;width:30%;height:80%;white-space:normal;position:fixed;left:35%;top:10%;">';
	html += '<div style="height:2.8em;"><button class="btn btn--green btn--emboss btn--cubic" onclick="remove_modal()">閉じる</button><hr /></div><div style="overflow-y:scroll;width:100%;height:calc(100% - 2.8em);">';
	html += '<table border="1" style="color:black;margin:auto;">';
	html += '<tr><th>放送局</th><td>' + station_name + '</td></tr>';
	html += '<tr><th>番組名</th><td>' + title + (rerun=="true" ? ' (再放送)' : '') + '</td></tr>';
	html += '<tr><th>副題</th><td>' + chapter + '</td></tr>';
	html += '</td></tr>';
	html += '<tr><th>開始時刻</th><td>' + month + '月' + day + '日' + ' ' + start_time + '</td></tr>';
	html += '<tr><th>放映時間</th><td>' + interval + '分</td></tr>';
	html += '<tr><th>番組概要</th><td>' + description + '</td></tr>';
	html += '</table>';
	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
}



/*
 * モーダル
 */

function on_click_station(station_key) {
	selected_station = station_key;
	if (adding_way_mode == 0) {
		add_radio(station_key);
	}
	document.getElementById("click_calendar_label").innerHTML = "日付ボタンを押して" + get_station_name(selected_station) + "番組表を追加";
	show_radio_menu(station_select_mode);
	show_calendar();
}

function on_click_calendar(month, day) {
	selected_month = month;
	selected_day = day;
	if (adding_way_mode == 1 && selected_station != "") {
		add_radio(selected_station);
	}
	document.getElementById("click_station_label").innerHTML = "放送局ボタンを押して" + selected_month + "月" + selected_day + "日の番組表を追加";
	show_calendar();
}

function show_radio_menu(group_name) {
	station_select_mode = group_name;
	var html = '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_area_menu()">戻る</button>';
	if (group_name == "NHK1") {
		keys = Object.keys(nhk1_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + nhk1_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_radio_net(\'NHK1\')">全部並べる</button>';
	}
	else if (group_name == "NHKFM") {
		keys = Object.keys(nhkfm_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + nhkfm_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_radio_net(\'NHKFM\')">全部並べる</button>';
	}
	else if (group_name == "AM") {
		keys = Object.keys(am_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + am_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_radio_net(\'AM\')">全部並べる</button>';
	}
	else if (group_name == "FM") {
		keys = Object.keys(fm_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + fm_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_radio_net(\'FM\')">全部並べる</button>';
	}
	else if (group_name == "OTHER") {
		keys = Object.keys(other_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + other_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_radio_net(\'OTHER\')">全部並べる</button>';
	}
	document.getElementById("area_menu").innerHTML = html;
}

/* 放送局メニューのHTMLを出力 */
function show_area_menu() {
	station_select_mode = "";
	var html = '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_radio_menu(\'NHK1\')">NHKラジオ第1から選ぶ</i></button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_radio_menu(\'NHKFM\')">NHK-FMから選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_radio_menu(\'AM\')">民放AMから選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_radio_menu(\'FM\')">民放FMから選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_radio_menu(\'OTHER\')">その他のラジオ局から選ぶ</button>';
	document.getElementById("area_menu").innerHTML = html;
}

/* 日付選択のHTMLを出力 */
function show_calendar() {
	var html = "";
	for (var month = 1 ; month <= 12 ; month++) {
		html += '<h2>' + month + '月</h2>';
		html += '<table border="1" style="margin:auto;text-align:center;">';
		for (var i = 0 ; i < date_list[month].length ; i++) {
			html += '<tr>';
			for (var j = 0 ; j < date_list[month][i].length ; j++) {
				html += '<td style="width:3em;">';
				if (date_list[month][i][j] != 0) {
					var day = date_list[month][i][j];
					if (
						typeof timetables[month] != "undefined" &&
						typeof timetables[month][day] != "undefined" &&
						(selected_station == "" || (typeof timetables[month][day][selected_station] != "undefined" && timetables[month][day][selected_station] != ""))
					) {
						html += '<button class="btn ';
						if (month == selected_month && day == selected_day) {
							html += 'btn--blue btn--emboss btn--cubic';
						} else {
							html += 'btn--green btn--emboss btn--cubic';
						}
						html += '" onclick="on_click_calendar(' + month + ',' + day + ');">' + day + '</button>';
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
	document.getElementById("calendar_menu").innerHTML = html;
}

function on_click_adding_way() {
	var mode0 = document.adding_way_form.adding_way[0].checked;
	var mode1 = document.adding_way_form.adding_way[1].checked;
	if (mode0) {
		adding_way_mode = 0;
	}
	else if (mode1) {
		adding_way_mode = 1;
	}
}

/* 「クリックして番組表を追加」をクリックした時に見せる */
function show_menu_modal() {
	remove_modal();
	var html = '<div id="modal" class="menu_modal" style="white-space:normal;position:fixed;">';

	html += '<div style="height:3.2em;">';
	html += '<button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="remove_modal()">閉じる</button>';
	html += '<form name="adding_way_form">';
	html += '<input id="click_station" name="adding_way" type="radio" onclick="on_click_adding_way()" /><label id="click_station_label" for="click_station" />放送局ボタンを押して' + selected_month + '月' + selected_day + '日の番組表を追加</label><br />';
	html += '<input id="click_calendar" name="adding_way" type="radio" onclick="on_click_adding_way()" /><label id="click_calendar_label" for="click_calendar">日付ボタンを押して' + get_station_name(selected_station) + '番組表を追加</label>';
	html += '</form>';
	html += '<div style="clear:both;"></div></div>';
	html += '<div style="width:100%;height:calc(100% - 3.2em);">';

	html += '<table style="height:100%;"><tbody style="height:100%;"><tr><td style="width:70%;height:100%;"><div id="area_menu" style="overflow-y:scroll;width:100%;height:100%;">';

	html += '</div></td><td style="height:100%;"><div id="calendar_menu" class="calendar_menu" style="overflow-y:scroll;width:100%;height:100%;color:black;text-align:center;">';

	html += '</div></td></tr></tbody></table>';

	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
	show_area_menu();
	show_calendar();

	document.adding_way_form.adding_way[0].checked = adding_way_mode == 0;
	document.adding_way_form.adding_way[1].checked = adding_way_mode == 1;
}



/*
 * 検索機能
 */

function save_search_form() {
	search_title = document.getElementById("search_title").value;
	search_description = document.getElementById("search_description").value;
	var menu = document.month_form.search_month;
	search_month = Array();
	for(var i=0 ; i<menu.length ; i++) {
		if(menu[i].checked) {
			search_month.push(menu[i].value);
		}
	}
	menu = document.station_form.search_station;
	search_station = Array();
	if (menu) {
		for(var i=0 ; i<menu.length ; i++) {
			if(menu[i].checked) {
				search_station.push(menu[i].value);
			}
		}
	}
}

function restore_search_form() {
	document.getElementById("search_title").value = search_title;
	document.getElementById("search_description").value = search_description;
	var menu = document.month_form.search_month;
	for(var i=0 ; i<menu.length ; i++) {
		if(search_month.indexOf(menu[i].value) != -1) {
			menu[i].checked = true;
		}
	}
	var html = '';
	for(var i=0 ; i<mutable_station_form.length ; i++) {
		var checked = search_station.indexOf(mutable_station_form[i]) != -1 ? "checked" : "";
		html += '<input id="station_' + mutable_station_form[i] + '" type="checkbox" name="search_station" value="' + mutable_station_form[i] + '" ' + checked + ' /><label for="station_' + mutable_station_form[i] + '">' + get_station_name(mutable_station_form[i]) + '</label>';
	}
	document.getElementById("mutable_station_form").insertAdjacentHTML("beforeend", html);
}

function searching() {
	if (search_month.indexOf(searching_month+"") == -1){
		if(searching_month==12){
			clearInterval(searching_process);
			return;
		}
		searching_month++;
		searching_day=1;
		return;
	}

	var result = search(searching_month, searching_day);
	searching_day++;
	search_progress++;

	document.getElementById("search_result").insertAdjacentHTML("beforeend", result);
	document.getElementById("search_hits").innerHTML = document.getElementById("search_result").children.length + "件";
	document.getElementById("search_progress").style.width = Math.round(100*search_progress/search_progress_max) + "%";

	if(searching_day==32) {
		if(searching_month==12){
			clearInterval(searching_process);
			return;
		}
		searching_month++;
		searching_day=1;
	}
}

function sanitize_search_string(str) {
	return str.trim()
		.replace(/[Ａ-Ｚａ-ｚ０-９]/g, function(s) {
			return String.fromCharCode(s.charCodeAt(0) - 0xFEE0);
		})
		.replace(/\s+/g," ")
		.replace("～","〜");
}

function search(month,day) {
	var html = "";
			if (timetables[month] && timetables[month][day]) {
				var keys = Object.keys(timetables[month][day]);
				for (var tv=0 ; tv<=keys.length ; tv++) {
					if (search_station.indexOf(keys[tv]) == -1) continue;
					var station_name = get_station_name(keys[tv]);
					if (timetables[month][day][keys[tv]]) {
						var result = decompressProgramChunk(month, day, keys[tv], timetables[month][day][keys[tv]]);
						for (var r=0 ; r<result.length ; r++) {
							var splited = sanitize_search_string(search_title).split(" ");
							var notfound = false;
							if (splited[0] != "") {
								var full_title = result[r].title + result[r].chapter;
								for (var s=0 ; s<splited.length ; s++) {
									if (full_title.toLowerCase().indexOf(splited[s].toLowerCase()) == -1) notfound = true;
								}
							}
							if (notfound) continue;
							splited = sanitize_search_string(search_description).split(" ");
							if (splited[0] != "") {
								for (var s=0 ; s<splited.length ; s++) {
									if (result[r].description.toLowerCase().indexOf(splited[s].toLowerCase()) == -1) notfound = true;
								}
							}
							if (notfound) continue;
							html += '<table border="1" style="width:100%;"><tr><td style="width:30%;">';
							html += '<div style="color:green;font-weight:bold;">' + month + '月' + day + '日' + '</div><div style="color:black;">' + station_name + '</div>';
							html += '</td><td style="width:70%;">';
							html += render_program_cell(result[r], 16);
							html += '</td></tr></table>';
						}
					}
				}
			}
	return html;
}

function search_result_modal() {
	save_search_form();
	remove_modal();

	var html = '<div id="modal" style="text-align:center;background-color:white;color:black;width:50%;height:80%;white-space:normal;position:fixed;left:20%;top:10%;">';

	html += '<div style="height:3.7em;">';
	html += '<table style="width:100%;"><tr><td style="width:5em;">';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="open_search_modal()">戻る</button>';
	html += '</td><td style="text-align:center;color:black;">';
	html += '<span id="search_hits"></span>';
	html += '<div style="background-color:#80ff80; width:90%;height:0.3em;"><div id="search_progress" style="background-color:#008000;width:0%;height:0.3em;"></div></div>';
	html += '</td><td style="width:5em;">';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="remove_modal()">閉じる</button>';
	html += '</td></tr></table><hr />';
	html += '</div>';
	html += '<div id="search_result" style="overflow-y:scroll;width:100%;height:calc(100% - 3.7em);">';

	html += '</div></div>';
	document.getElementById("tables").insertAdjacentHTML("beforeend", html);

	search_progress = 0;
	search_progress_max = 0;
	for (var m = 1 ; m <= 12 ; m++) {
		if (search_month.indexOf(m+"") != -1) {
			var daysOfMonth = new Date(selected_year, m, 0).getDate();
			search_progress_max += daysOfMonth;
		}
	}

	searching_month=1;
	searching_day=1;
	search_hits = 0;
	searching_process = setInterval("searching()",10);
}

function mutate_station_form1() {
	var index = document.net_form.search_net.selectedIndex;
	if(index == 0)return;
	var selected = document.net_form.search_net.options[index].value;
	var tv = get_tv_by_net(selected);
	var html = '';
	for (var i=0 ; i<tv.length ; i++) {
		if (mutable_station_form.indexOf(tv[i]) == -1) {
			html += '<input id="station_' + tv[i] + '" type="checkbox" name="search_station" value="' + tv[i] + '" checked /><label for="station_' + tv[i] + '">' + get_station_name(tv[i]) + '</label>';
			mutable_station_form.push(tv[i]);
		}
	}
	document.getElementById("mutable_station_form").insertAdjacentHTML("beforeend", html);
}

function check_month_form() {
	var menu = document.month_form.search_month;
	for(var i=0 ; i<menu.length ; i++) {
		menu[i].checked = true;
	}
}

function uncheck_month_form() {
	var menu = document.month_form.search_month;
	for(var i=0 ; i<menu.length ; i++) {
		menu[i].checked = false;
	}
}

function check_mutate_station_form() {
	var menu = document.station_form.search_station;
	if (menu) {
		for(var i=0 ; i<menu.length ; i++) {
			menu[i].checked = true;
		}
	}
}

function uncheck_mutate_station_form() {
	var menu = document.station_form.search_station;
	if (menu) {
		for(var i=0 ; i<menu.length ; i++) {
			menu[i].checked = false;
		}
	}
}

function clear_mutate_station_form() {
	document.getElementById("mutable_station_form").innerHTML = "";
	mutable_station_form = Array();
	document.net_form.search_net.selectedIndex = 0;
	document.area_form.search_area.selectedIndex = 0;
}

function open_search_modal() {
	remove_modal();

	var html = '<div id="modal" style="text-align:center;background-color:white;color:black;width:50%;height:80%;white-space:normal;position:fixed;left:20%;top:10%;">';
	html += '<div style="height:2.3em;"><button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="save_search_form();remove_modal();">閉じる</button><hr style="clear:both;" /></div>';
	html += '<div style="overflow-y:scroll;width:100%;height:calc(100% - 2.3em);">';

	html += '<table border="1" style="color:black;">';

	html += '<tr><td width="20%">シーズン<br />';
	html += '<button onClick="check_month_form()">全て選択</button><br />';
	html += '<button onClick="uncheck_month_form()">全て解除</button></td>';
	html += '<td><form name="month_form">';
	for (var m=1 ; m<=12 ; m++) {
		html += '<input id="month_' + m + '" type="checkbox" name="search_month" value="' + m + '" /><label for="month_' + m + '">' + m + '月</label>';
	}
	html += '</form></td></tr>';

	html += '<tr><td>テレビ局<br />';
	html += '<button onClick="check_mutate_station_form()">全て選択</button><br />';
	html += '<button onClick="uncheck_mutate_station_form()">全て解除</button><br />';
	html += '<button onClick="clear_mutate_station_form()">クリア</button></td>';
	html += '<td><table border="1" style="color:black;"><tr><td>系列から選ぶ<form name="net_form"><select name="search_net" onChange="mutate_station_form1()">';
	html += '<option value=""></option>';
	html += '<option value="NHK1">NHKラジオ第1</option>';
	html += '<option value="NHKFM">NHK-FM</option>';
	html += '<option value="AM">民放AM</option>';
	html += '<option value="FM">民放FM</option>';
	html += '<option value="OTHER">その他</option>';
	html += '</select></form></td></tr></table>';
	html += '<form name="station_form" id="mutable_station_form"></form>';
	html += '</td></tr>';

	var expl = '<br />半角スペースで複数キーワード検索可能。<br />空欄の場合は絞り込まない。';
	html += '<tr><td>番組名</td><td><input id="search_title" type="text" />' + expl + '</td></tr>';
	html += '<tr><td>番組概要</td><td><input id="search_description" type="text" />' + expl + '</td></tr>';

	html += '</table>';

	html += '<button class="btn btn--green btn--emboss btn--cubic" onClick="search_result_modal()">検索</button>';

	html += '</div></div>';
	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
	restore_search_form();
}

function slide_yesterday_all() {
	now_showing_clone = now_showing.concat();
	var keys = Object.keys(now_showing_clone);
	for (var i = 0 ; i < keys.length ; i++) {
		slide_yesterday(now_showing_clone[keys[i]].tv, now_showing_clone[keys[i]].month, now_showing_clone[keys[i]].day, keys[i]);
	}
}

function slide_tomorrow_all() {
	now_showing_clone = now_showing.concat();
	var keys = Object.keys(now_showing_clone);
	for (var i = 0 ; i < keys.length ; i++) {
		slide_tomorrow(now_showing_clone[keys[i]].tv, now_showing_clone[keys[i]].month, now_showing_clone[keys[i]].day, keys[i]);
	}
}

function clear_all_tables() {
	var html = '<div id="new_table" style="width:200px;height:400px;border:1px dotted;display: inline-block;vertical-align:top;" onclick="show_menu_modal()">';
	html += '<div style="font-size:5em;text-align:center;">+</div>クリックして番組表を追加';
	html += '</div>';

	document.getElementById("headers").innerHTML = "";
	document.getElementById("tables").innerHTML = html;
	now_showing.length=0;
}

function setup_first_table() {
	var html = '';

	html += '<button onClick="open_search_modal()">検索</button>';
	html += '<button onClick="clear_all_tables()">クリア</button><br />';

	// 「縦幅の調整」チェックボックス
	html += '<input type="checkbox" id="fix_hour_height" onchange="change_fix_hour_height(checked)" checked></input><label for="fix_hour_height">縦幅の調整</label> / ';
	// 縦幅
	html += '<input type="number" id="hour_height" onchange="change_hour_height(value)" value="' + hour_height + '"></input>倍の縦幅';
	// 横幅
	html += ' : 横幅<input type="number" id="hour_width" onchange="change_hour_width(value)" value="' + hour_width + '"></input>px';
	// 文字サイズ
	html += ' : 文字サイズ<input type="number" step="1" id="font_size" onchange="change_font_size(value)" value="' + font_size + '"></input>px';

	html += '<div style="white-space: nowrap;">';

	// 左端の時刻バー
	html += '<div id="hour_bar" style="vertical-align:top;float:left;">';

	html += '<div id="hour_bar_header" style="vertical-align:top;">';
	html += '<button class="tv_table_header_date_button" onClick="slide_yesterday_all()">▲</button><br />';
	html += '<button class="tv_table_header_date_button" onClick="slide_tomorrow_all()">▼</button>';
	html += '</div>';

	html += '<div id="hour_bar_wrapper" style="width:auto;height:75%;overflow-y:scroll;overflow-x:hidden;">';
	for (var i = 4 ; i <= 28 ; i++) {
		html += '<div class="hour_bar_cell" style="height:' + (hour_height * 60) + 'px;"><div style="height:100%;">' + i + '</div></div>';
	}
	html += '</div>';
	html += '</div>';
	html += '<div id="headers_wrapper" style="width:calc(100% - 30px);overflow-x:scroll;float:left;">';

	// 番組表ヘッダを表示する場所
	html += '<div id="headers"></div><div style="clear:both;"></div>';

	// 番組表を表示する場所
	html += '<div id="tables" style="width:auto;height:75%;overflow-y:scroll;overflow-x:hidden;">';
	html += '</div><div style="clear:both;"></div>';

	html += '</div>';

	html += '</div>';

	html += '<div id="sizetest" style="position:absolute;top:0;left:0;"></div>';
	document.getElementById("app").innerHTML = html;

	// 番組表追加ボタンの表示
	clear_all_tables();

	// スクロール同期
	var func = function() {
		document.getElementById("hour_bar_wrapper").scrollTop = document.getElementById("tables").scrollTop;
	};
	setInterval(func, 100);
}

function init() {
	create_calendar();
	setup_first_table();
}

init();
