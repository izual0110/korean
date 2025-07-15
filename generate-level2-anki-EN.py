data1 = [
    ["오래되다", "to be old, ancient", "o-rae-doe-da"],
    ["호수", "lake", "ho-su"],
    ["맥주", "beer", "maek-jju"],
    ["벚꽃", "cherry blossom", "beot-kkot"],
    ["한강", "Han River", "han-gang"],
    ["해산물", "seafood", "hae-san-mul"],
    ["생선회", "sashimi, raw fish", "saeng-seon-hoe"],
    ["절(사원)", "Buddhist temple", "jeol (sa-won)"],
    ["박물관", "museum", "bang-mul-gwan"],
    ["건물", "building", "geon-mul"],
    ["높다", "high, tall", "nop-da"],
    ["많다", "many, a lot", "manh-da"],
    ["복잡하다", "complicated, complex", "bok-jjab-ha-da"],
    ["야경", "night view", "ya-gyeong"],
    ["아름답다", "beautiful", "a-reum-dap-da"],
    ["교통", "transportation", "gyo-tong"],
    ["편리하다", "convenient", "pyeon-ri-ha-da"],
    ["한적하다", "quiet, deserted", "han-jeok-ha-da"],
    ["깨끗하다", "clean", "kkae-kkeut-ha-da"],
    ["조용하다", "quiet", "jo-yong-ha-da"],
    ["낮다", "low", "nat-da"],
    ["특히", "especially", "teuk-hi"],
    ["관광지", "tourist spot", "gwan-gwang-ji"],
    ["섬", "island", "seom"]
]

data2 = [
    ["청소하다", "to clean", "cheong-so-ha-da"],
    ["빨래하다", "to do laundry", "ppal-lae-ha-da"],
    ["요리하다", "to cook", "yo-ri-ha-da"],
    ["책장을 정리하다", "to organize bookshelf", "chaek-jjang-eul jeong-ri-ha-da"],
    ["방을 치우다", "to tidy up the room", "bang-eul chi-u-da"],
    ["방을 쓸다", "to sweep the room", "bang-eul sseul-da"],
    ["방을 닦다", "to mop the room", "bang-eul dak-tta"],
    ["청소기를 돌리다", "to vacuum", "cheong-so-gi-reul dol-li-da"],
    ["쓰레기를 버리다", "to throw away trash", "sseu-re-gi-reul beo-ri-da"],
    ["분리수거를 하다", "to separate trash", "bun-ri-su-geo-reul ha-da"],
    ["빨래를 널다", "to hang laundry", "ppal-lae-reul neol-da"],
    ["빨래를 개다", "to fold laundry", "ppal-lae-reul kae-da"],
    ["세탁기를 돌리다", "to run the washing machine", "se-tak-gi-reul dol-li-da"],
    ["다림질을 하다", "to iron", "da-rim-jil-eul ha-da"],
    ["손빨래를 하다", "to hand wash laundry", "son-ppal-lae-reul ha-da"],
    ["음식을 만들다", "to make food", "eum-sik-eul man-deul-da"],
    ["설거지하다", "to wash dishes", "seol-geo-ji-ha-da"],
    ["퇴근", "getting off work", "toe-geun"],
    ["잊다", "to forget", "it-da"],
    ["장 보다", "to go grocery shopping", "jang bo-da"],
    ["걸레질", "to wipe (with a mop/cloth)", "geol-le-jil"],
    ["음식물 쓰레기", "food waste", "eum-sik-mul sseu-re-gi"],
    ["급한 일이 생기다", "urgent matter arises", "geu-pan il-i saeng-gi-da"]
]

def write(data, file):
    for row in data:
        file.write("\"" + row[0] + "\"" + "," + "\"" + row[1] + " ("+row[2]+")" + "\"" + "\n")
        file.write("\"" + row[1] + "\"" + "," + "\"" + row[0] + " ("+row[2]+")" + "\"" + "\n")

csv_path = "output/KIIP2-EN.csv"

with open(csv_path, "w", encoding="utf-8") as f:
    write(data1, f)
    write(data2, f)
    
csv_path