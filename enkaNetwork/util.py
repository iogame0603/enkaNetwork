from .config import Config
from typing import Union, Dict, List, Any
import json
import aiofiles

def get_json_data(assetName: str):
    with open(Config.PATH.ASSET_FILE_PATH + assetName, "r", encoding="UTF-8") as file:
        return json.loads(file.read())

async def get_json_data_async(assetName: str):
    async with aiofiles.open(Config.PATH.ASSET_FILE_PATH + assetName, "r", encoding="UTF-8") as file:
        return json.loads(await file.read())

class Util:
    @classmethod
    def get_img_url(cls, iconName: str) -> str:
        return f"{Config.ENKA_PROTOCOL}://{Config.ENKA_API_URL}/ui/{iconName}.png"

    @classmethod
    def get_localizations(cls, id: Union[int, str]) -> str:
        try:
            data = get_json_data(assetName=Config.GITHUB_ASSET.LOC)
            return data[Config.LANG][str(id)]
        except KeyError:
            print(f"찾을 수 없는 이름 (id: {id}, lang: {Config.LANG})")
            return ""
        
    @classmethod
    def get_profile_img_by_avatarId(cls, id: Union[int, str]) -> str:
        try:
            data = get_json_data(assetName=Config.GITHUB_ASSET.CHARACTER)
            return cls.get_img_url(data[str(id)]["SideIconName"].replace("_Side", "") + "_Circle")
        except KeyError:
            print(f"찾을 수 없는 프로필 사진 (avatarId: {id})")
            return ""
        
    @classmethod
    def get_profile_img_by_id(cls, id: Union[int, str]) -> str:
        try:
            data = get_json_data(assetName=Config.GITHUB_ASSET.PFPS)
            return cls.get_img_url(data[str(id)]["iconPath"])
        except KeyError:
            print(f"찾을 수 없는 프로필 사진 (id: {id})")
            return ""
        
    @classmethod
    def get_namecard_img(cls, id: Union[int, str]) -> str:
        try:
            data = get_json_data(assetName=Config.GITHUB_ASSET.NAME_CARDS)
            return cls.get_img_url(iconName=data[str(id)]["icon"])
        except KeyError:
            print(f"찾을 수 없는 nameCard (id: {id})")
            return ""
        
    @classmethod
    def get_avatar_info(cls, avatarId: Union[int, str], costumeId: Union[int, str] = None) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        character_data = get_json_data(assetName=Config.GITHUB_ASSET.CHARACTER)

        hash_id = character_data[str(avatarId)]["NameTextMapHash"]
        result["name"] = cls.get_localizations(id=hash_id)
        result["element"] = character_data[str(avatarId)]["Element"]
        try:
            result["icon"] = cls.get_img_url(character_data[str(avatarId)]["SideIconName"].replace("_Side", ""))
        except KeyError:
            result["icon"] = ""

        skill_id_list: List[int] = character_data[str(avatarId)]["SkillOrder"]
        skills: Dict[str, str] = {}
        for skillId in skill_id_list:
            skills[str(skillId)] = cls.get_img_url(character_data[str(avatarId)]["Skills"][str(skillId)])
        result["skills"] = skills

        if costumeId != None:
            costumes_json = character_data[str(avatarId)]["Costumes"][str(costumeId)]
            result["costume"] = {
                "costumeId": costumeId,
                "icon": Util.get_img_url(costumes_json["icon"]),
                "art": Util.get_img_url(costumes_json["art"])
            }

        return result
        
    @classmethod
    def get_avatar_skills(cls, avatarId: Union[int, str]) -> Dict[str, str]:
        char_json = get_json_data(Config.GITHUB_ASSET.CHARACTER)
        skill_id_list: List[int] = char_json[str(avatarId)]["SkillOrder"]
        skills: Dict[str, str] = {}
        for id in skill_id_list:
            skills[str(id)] = cls.get_img_url(char_json[str(avatarId)]["Skills"][str(id)])
        return skills
    
    @classmethod
    async def get_reliquary_name(cls, id: Union[int, str]) -> str:
        try:
            textMapKr = await get_json_data_async(Config.GITLAB_ASSET.TEXTMAP_KR)
            return textMapKr[str(id)]
        except KeyError:
            print(f"알 수 없는 성유물 id (id: {id})")
            return ""
        
class HonkaiStarrailUtil:
    @classmethod
    def get_img_url(cls, iconPath: str) -> str:
        return f"{Config.ENKA_PROTOCOL}://{Config.ENKA_API_URL}/ui/hsr/{iconPath}"

    @classmethod
    def get_localizations(cls, id: Union[int, str]):
        jsonData = get_json_data(Config.GITHUB_ASSET.STARRAIL_LOC)
        return jsonData[Config.LANG][str(id)].replace("\xa0", " ")

    @classmethod
    def get_head_icon(cls, id: Union[int, str]):
        jsonData = get_json_data(Config.GITHUB_ASSET.STARRAIL_PFPS)
        return cls.get_img_url(jsonData[str(id)]["Icon"])
    
    @classmethod
    def get_avatar_info(cls, id: Union[int, str]):
        jsonData = get_json_data(Config.GITHUB_ASSET.STARRAIL_CHARACTER)
        data = jsonData[str(id)]
        return {
            "name" : cls.get_localizations(data["AvatarName"]["Hash"]),
            "headIcon" : cls.get_img_url(data["ActionAvatarHeadIconPath"]),
            "cutinFrontImg" : cls.get_img_url(data["AvatarCutinFrontImgPath"]),
            "sideIcon" : cls.get_img_url(data["AvatarSideIconPath"]),
            "element" : data["Element"],
            "avatarBaseType" : data["AvatarBaseType"],
            "rarity" : data["Rarity"]
        }
    
    @classmethod
    def get_weapon_info(cls, id: Union[int, str]):
        jsonData = get_json_data(Config.GITHUB_ASSET.STARRAIL_WEPS)
        data = jsonData[str(id)]
        return {
            "name" : cls.get_localizations(data["EquipmentName"]["Hash"]),
            "icon" : cls.get_img_url(data["ImagePath"]),
            "type" : data["AvatarBaseType"],
            "rarity" : data["Rarity"]
        }
    
    @classmethod
    def get_relic_info(cls, id: Union[int, str]):
        jsonData = get_json_data(Config.GITHUB_ASSET.STARRAIL_RELIC)
        data = jsonData[str(id)]
        return {
            "icon" : cls.get_img_url(data["Icon"]),
            "rarity" : data["Rarity"],
            "type" : data["Type"]
        }
    
    @classmethod
    def get_skilltree_info(cls, id: Union[int, str]):
        jsonData = get_json_data(Config.GITHUB_ASSET.STARRAIL_SKILL)
        data = jsonData[str(id)]
        return {
            "icon" : cls.get_img_url(data["IconPath"]),
            "pointType" : data["PointType"]
        }