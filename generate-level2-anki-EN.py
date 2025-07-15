data1 = [
    ["오래되다", "быть старым, давним", "o-rae-doe-da"],
    ["호수", "озеро", "ho-su"],
    ["맥주", "пиво", "maek-jju"],
    ["벚꽃", "вишнёвый цвет", "beot-kkot"],
    ["한강", "река Ханган", "han-gang"],
    ["해산물", "морепродукты", "hae-san-mul"],
    ["생선회", "сашими, сырая рыба", "saeng-seon-hoe"],
    ["절(사원)", "буддийский храм", "jeol (sa-won)"],
    ["박물관", "музей", "bang-mul-gwan"],
    ["건물", "здание", "geon-mul"],
    ["높다", "высокий", "nop-da"],
    ["많다", "много", "manh-da"],
    ["복잡하다", "сложный, запутанный", "bok-jjab-ha-da"],
    ["야경", "ночной пейзаж", "ya-gyeong"],
    ["아름답다", "красивый", "a-reum-dap-da"],
    ["교통", "транспорт", "gyo-tong"],
    ["편리하다", "удобный", "pyeon-ri-ha-da"],
    ["한적하다", "спокойный, безлюдный", "han-jeok-ha-da"],
    ["깨끗하다", "чистый", "kkae-kkeut-ha-da"],
    ["조용하다", "тихий", "jo-yong-ha-da"],
    ["낮다", "низкий", "nat-da"],
    ["특히", "особенно", "teuk-hi"],
    ["관광지", "туристическое место", "gwan-gwang-ji"],
    ["섬", "остров", "seom"]
]

data2 = [
    ["청소하다", "убирать", "cheong-so-ha-da"],
    ["빨래하다", "стирать (бельё)", "ppal-lae-ha-da"],
    ["요리하다", "готовить (еду)", "yo-ri-ha-da"],
    ["책장을 정리하다", "наводить порядок на книжной полке", "chaek-jjang-eul jeong-ri-ha-da"],
    ["방을 치우다", "убирать комнату", "bang-eul chi-u-da"],
    ["방을 쓸다", "подметать комнату", "bang-eul sseul-da"],
    ["방을 닦다", "мыть комнату", "bang-eul dak-tta"],
    ["청소기를 돌리다", "пылесосить", "cheong-so-gi-reul dol-li-da"],
    ["쓰레기를 버리다", "выбрасывать мусор", "sseu-re-gi-reul beo-ri-da"],
    ["분리수거를 하다", "сортировать мусор", "bun-ri-su-geo-reul ha-da"],
    ["빨래를 널다", "развешивать бельё", "ppal-lae-reul neol-da"],
    ["빨래를 개다", "складывать бельё", "ppal-lae-reul kae-da"],
    ["세탁기를 돌리다", "включать стиральную машину", "se-tak-gi-reul dol-li-da"],
    ["다림질을 하다", "гладить", "da-rim-jil-eul ha-da"],
    ["손빨래를 하다", "стирать вручную", "son-ppal-lae-reul ha-da"],
    ["음식을 만들다", "готовить еду", "eum-sik-eul man-deul-da"],
    ["설거지하다", "мыть посуду", "seol-geo-ji-ha-da"],
    ["퇴근", "возвращение с работы", "toe-geun"],
    ["잊다", "забывать", "it-da"],
    ["장 보다", "ходить за покупками", "jang bo-da"],
    ["걸레질", "протирать (шваброй/тряпкой)", "geol-le-jil"],
    ["음식물 쓰레기", "пищевые отходы", "eum-sik-mul sseu-re-gi"],
    ["급한 일이 생기다", "возникло срочное дело", "geu-pan il-i saeng-gi-da"]
]

def write(data, file):
    for row in data:
        file.write("\"" + row[0] + "\"" + "," + "\"" + row[1] + " ("+row[2]+")" + "\"" + "\n")
        file.write("\"" + row[1] + "\"" + "," + "\"" + row[0] + " ("+row[2]+")" + "\"" + "\n")

csv_path = "output/KIIP2.csv"

with open(csv_path, "w", encoding="utf-8") as f:
    write(data1, f)
    write(data2, f)
    
csv_path