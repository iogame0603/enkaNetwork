import os

class Config:
    LANG = ""
    LANG_LIST = ["ar", "de", "en", "es", "fr", "id", "it", "ja", "ko", "pt", "ru", "th", "tr", "uk", "vi", "ch-CN", "zh-TW"]

    ENKA_PROTOCOL = "https"
    ENKA_API_URL = "enka.network"
    ASSET_PROTOCOL = "https"

    class PATH:
        ASSET_GITHUB_PATH = "raw.githubusercontent.com/EnkaNetwork/API-docs/master/store/"
        ASSET_GITLAB_PATH = "gitlab.com/Dimbreath/AnimeGameData/-/raw/master/ExcelBinOutput/"
        ASSET_GITLAB_TEXTMAP_PATH = "gitlab.com/Dimbreath/AnimeGameData/-/raw/master/TextMap/"
        ASSET_FILE_PATH = f"{os.path.dirname(__file__)}/assets/"

    class GITHUB_ASSET:
        # genshin assets
        CHARACTER = "characters.json"
        NAME_CARDS = "namecards.json"
        LOC = "loc.json"
        PFPS = "pfps.json"

        # honkai starrail assets
        STARRAIL_PFPS = "hsr/honker_avatars.json"
        STARRAIL_CHARACTER = "hsr/honker_characters.json"
        STARRAIL_RELIC = "hsr/honker_relics.json"
        STARRAIL_SKILL = "hsr/honker_skills.json"
        STARRAIL_SKILLTREE = "hsr/honker_skilltree.json"
        STARRAIL_WEPS = "hsr/honker_weps.json"
        STARRAIL_LOC = "hsr/hsr.json"

    class GITLAB_ASSET:
        SKILL = "AvatarSkillExcelConfigData.json"
        TEXTMAP_KR = "TextMapKR.json"