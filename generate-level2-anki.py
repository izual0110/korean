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

def write(data, file):
    for row in data:
        file.write("\"" + row[0] + "\"" + "," + "\"" + row[1] + " ("+row[2]+")" + "\"" + "\n")
        file.write("\"" + row[1] + "\"" + "," + "\"" + row[0] + " ("+row[2]+")" + "\"" + "\n")

# Создание CSV-файла без использования pandas
csv_path = "output/KIIP2.csv"

with open(csv_path, "w", encoding="utf-8") as f:
    write(data1, f)
    
csv_path