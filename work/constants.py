# 定数の定義
SUBJECT_ID = 0
YEAR = 1
COURSE_CODE = 2
SUBJECT = 3
SUBJECT_KANA = 4
TEACHER = 5
TEACHER_KANA = 6
FACULTY = 7
SEMESTER = 8
TIMETABLE = 9
WEEK = 10
PERIOD = 11
CLASSROOM = 12
DESCRIPTION = 13
URL = 14

SYLLABUS_URL = "https://www.wsl.waseda.jp/syllabus/JAA101.php"

#CSVファイルヘッダー項目
HEADER = [
    "授業ID", "開講年度", "コース・コード", "科目名", "カモクメイ", "教員名", "フリガナ", "学部", "学期",
    "曜日時限", "曜日", "時限", "使用教室", "授業概要", "シラバスURL"
]
SUBJECT_DATA_HEADER = ["授業ID", "学部", "科目名", "教員名", "学期", "曜日時限", "曜日", "時限"]

# 対象学部のリスト
FACULTIES = [
    "政経", "法学", "教育", "商学", "社学", "人科", "スポーツ", "国際教養", "文構", "文", "基幹", "創造",
    "先進", "グローバル"
]

FACULTIES_MAP = {
    "政経": "A_政経",
    "法学": "B_法学",
    "教育": "E_教育",
    "商学": "F_商学",
    "社学": "H_社学",
    "人科": "J_人科",
    "スポーツ": "K_スポーツ",
    "国際教養": "M_国際教養",
    "文構": "T_文構",
    "文": "U_文",
    "基幹": "W_基幹",
    "創造": "X_創造",
    "先進": "Y_先進",
    "グローバル": "G_GEC"
}
