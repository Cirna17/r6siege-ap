from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
from Options import OptionError
from math import floor

from . import generation, operator_data

if TYPE_CHECKING:
    from .world import R6SiegeWorld

ITEM_NAME_TO_ID = {
    "Ace": 1001,
    "Alibi": 1002,
    "Amaru": 1003,
    "Aruni": 1004,
    "Ash": 1005,
    "Azami": 1006,
    "Bandit": 1007,
    "Blackbeard": 1008,
    "Blitz": 1009,
    "Brava": 1010,
    "Buck": 1011,
    "Capitao": 1012,
    "Castle": 1013,
    "Caveira": 1014,
    "Clash": 1015,
    "Deimos": 1016,
    "Denari": 1017,
    "Doc": 1018,
    "Dokkaebi": 1019,
    "Echo": 1020,
    "Ela": 1021,
    "Fenrir": 1022,
    "Finka": 1023,
    "Flores": 1024,
    "Frost": 1025,
    "Fuze": 1026,
    "Glaz": 1027,
    "Goyo": 1028,
    "Gridlock": 1029,
    "Grim": 1030,
    "Hibana": 1031,
    "Iana": 1032,
    "IQ": 1033,
    "Jackal": 1034,
    "Jager": 1035,
    "Kaid": 1036,
    "Kali": 1037,
    "Kapkan": 1038,
    "Lesion": 1039,
    "Lion": 1040,
    "Maestro": 1041,
    "Maverick": 1042,
    "Melusi": 1043,
    "Mira": 1044,
    "Montagne": 1045,
    "Mozzie": 1046,
    "Mute": 1047,
    "Nokk": 1048,
    "Nomad": 1049,
    "Noor": 1050,
    "Oryx": 1051,
    "Osa": 1052,
    "Pulse": 1053,
    "Ram": 1054,
    "Rauora": 1055,
    "Rook": 1056,
    "Sens": 1057,
    "Sentry": 1058,
    "Skopos": 1059,
    "Sledge": 1060,
    "Smoke": 1061,
    "Solid Snake": 1062,
    "Solis": 1063,
    "Striker": 1064,
    "Tachanka": 1065,
    "Thatcher": 1066,
    "Thermite": 1067,
    "Thorn": 1068,
    "Thunderbird": 1069,
    "Tubarao": 1070,
    "Twitch": 1071,
    "Valkyrie": 1072,
    "Vigil": 1073,
    "Wamai": 1074,
    "Warden": 1075,
    "Ying": 1076,
    "Zero": 1077,
    "Zofia": 1078,

    ".44 Mag Semi-Auto": 2001,
    ".44 Vendetta": 2002,
    "1911 TACOPS": 2003,
    "416-C Carbine": 2004,
    "417": 2005,
    "5.7 USG": 2205,
    "552 Commando": 2006,
    "556xi": 2007,
    "6P41": 2008,
    "9mm C1": 2009,
    "9x19SVN": 2206,
    "9x19VSN": 2010,
    "ACS12": 2011,
    "AK-12": 2012,
    "AK-74M": 2014,
    "ALDA 5.56": 2015,
    "AR-15.50": 2016,
    "AR-57": 2017,
    "AR33": 2018,
    "ARX200": 2019,
    "AUG A12": 2204,
    "AUG A2": 2202,
    "AUG A3": 2203,
    "Bailiff 410": 2022,
    "Ballistic Shield": 2023,
    "Bearing 9": 2024,
    "BOSG.12.2": 2026,
    "C75 Auto": 2027,
    "C7E": 2028,
    "C8-SFW": 2029,
    "CAMRS": 2206,
    "Commando 9": 2030,
    "CSRX 300": 2031,
    "D-50": 2032,
    "DP27": 2033,
    "F2": 2207,
    "F90": 2034,
    "FMG-9": 2037,
    "FO-12": 2038,
    "G36C": 2039,
    "G8A1": 2208,
    "Glaive-12": 2040,
    "GONNE-6": 2041,
    "GSH-18": 2042,
    "ITA12L": 2044,
    "ITA12S": 2045,
    "K1A": 2046,
    "Keratos .357": 2047,
    "L85A2": 2049,
    "LFP586": 2050,
    "LMG-E": 2051,
    "Luison": 2209,
    "M1014": 2052,
    "M12": 2053,
    "M245 SAW": 2210,
    "M249": 2054,
    "M4": 2055,
    "M45 MEUSOC": 2056,
    "M590A1": 2057,
    "M762": 2059,
    "M870": 2060,
    "MK 14 EBR": 2062,
    "MK1 9mm": 2063,
    "MK17 CQB": 2200,
    "MP5": 2064,
    "MP5K": 2066,
    "MP5SD": 2067,
    "MP7": 2068,
    "MPX": 2070,
    "MX4 Storm": 2071,
    "OTS-03": 2072,
    "P-10C": 2073,
    "P10 Roni": 2211,
    "P12": 2074,
    "P226 MK 25": 2075,
    "P229": 2076,
    "P9": 2077,
    "P90": 2078,
    "PARA-308": 2079,
    "PCX-33": 2080,
    "PDW9": 2081,
    "PMM": 2082,
    "PMR90A2": 2083,
    "POF-9": 2084,
    "PRB92": 2086,
    "Q-929": 2088,
    "R4-C": 2088,
    "Reaper MK2": 2215,
    "RG15": 2090,
    "SASG-12": 2092,
    "SC3000K": 2093,
    "Scorpion Evo A1": 2095,
    "SDP 9mm": 2096,
    "SG-CQB": 2097,
    "SIX12": 2098,
    "SIX12 SD": 2201,
    "SMG-11": 2212,
    "SMG-12": 2099,
    "SPAS-12": 2100,
    "SPAS-15": 2101,
    "Spear .308": 2102,
    "SPSMG9": 2213,
    "SR-25": 2103,
    "Super 90": 2214,
    "Super Shorty": 2104,
    "SuperNova": 2105,
    "T-5 SMG": 2106,
    "T-95 LSW": 2107,
    "TACIT .45": 2108,
    "TCSG12": 2109,
    "Type-89": 2110,
    "UMP45": 2111,
    "USP40": 2112,
    "UZK50GI": 2215,
    "V308": 2114,
    "Vector .45 ACP": 2115,
    "XK23": 2116,

    "S.E.L.M.A. Aqua Breacher": 3001,
    "Prisma": 3002,
    "Garra Hook": 3003,
    "Surya Laser Gate": 3004,
    "Breaching Round": 3005,
    "Kiba Barrier": 3006,
    "Shock Wire": 3007,
    "H.U.L.L. Adaptable Shield": 3008,
    "G-52 Tactical Shield": 3009,
    "Kludge Drone": 3010,
    "Skeleton Key": 3011,
    "Tactical Crossbow": 3012,
    "Armor Panel": 3013,
    "Silent Step": 3014,
    "CCE Shield MK2": 3015,
    "Deathmark Tracker": 3016,
    "T.R.I.P. Connector": 3017,
    "Stim Pistol": 3018,
    "Jegeo Payload": 3019,
    "Yokai": 3020,
    "GRZMOT Mine": 3021,
    "F-NATT Dread Mine": 3022,
    "Adrenal Surge": 3023,
    "RCE-Ratero Charge": 3034,
    "Welcome Mat": 3025,
    "Cluster Charge": 3026,
    "Flip Sight": 3027,
    "Volcan Canister": 3028,
    "Trax Stingers": 3100,
    "Kawan Hive Launcher": 3029,
    "X-Kairos": 3030,
    "Gemini Replicator": 3031,
    "Electronics Detector": 3032,
    "Eyenox Model III": 3033,
    "Active Defense System": 3034,
    "Rtila Electroclaw": 3035,
    "LV Explosive Lance": 3036,
    "Entry Denial Device": 3037,
    "Gu": 3038,
    "EE-ONE-D": 3039,
    "Evil Eye": 3040,
    "Breaching Torch": 3041,
    "Banshee Sonic Defense": 3042,
    "Black Mirror": 3043,
    "Le Roc Shield": 3044,
    "Pest Launcher": 3045,
    "Signal Disruptor": 3046,
    "HEL Presence Reduction": 3047,
    "Airjab Launcher": 3048,
    "Horus Lance Launcher": 3049,
    "Remah Dash": 3050,
    "Talon-8 Shield": 3051,
    "Cardiac Sensor": 3052,
    "BU-GI Auto-Breacher": 3053,
    "D.O.M. Panel Launcher": 3054,
    "Armor Pack": 3055,
    "R.O.U. Projector System": 3056,
    "V10 Pantheon Shells": 3101,
    "Breaching Hammer": 3102,
    "Remote Gas Grenade": 3103,
    "Soliton Radar MK III": 3104,
    "SPEC-IO Electro-Sensor": 3105,
    "Gadget Kit": 3057, 
    "Shumikha Launcher": 3058,
    "E.G.S. Disruptor": 3059,
    "Exothermic Charge": 3060,
    "Razorbloom Shell": 3061,
    "Kona Station": 3062,
    "Zoto Canister": 3063,
    "Shock Drone": 3064,
    "Black Eye": 3065,
    "ERC-7": 3066,
    "MAG-NET System": 3067,
    "Glance Smart Glasses": 3068,
    "Candela": 3069,
    "Argus Launcher": 3070,
    "KS79 Lifeline": 3071,

    "Breach Charge": 4001,
    "Claymore": 4002,
    "Frag Grenade": 4003,
    "Hard Breach Charge": 4004,
    "Impact EMP Grenade": 4005,
    "Smoke Grenade": 4006,
    "Stun Grenade": 4007,
    "Impact Grenade": 4008,
    "Deployable Shield": 4009,
    "Barbed Wire": 4010,
    "Bulletproof Camera": 4011,
    "Nitro Cell": 4012,
    "Proximity Alarm": 4013,
    "Observation Blocker": 4014,

    "Siege Filler Item": 1
}



DEFAULT_ITEM_CLASSIFICATIONS = {
    "Ace": ItemClassification.progression,
    "Alibi": ItemClassification.progression,
    "Amaru": ItemClassification.progression,
    "Aruni": ItemClassification.progression,
    "Ash": ItemClassification.progression,
    "Azami": ItemClassification.progression,
    "Bandit": ItemClassification.progression,
    "Blackbeard": ItemClassification.progression,
    "Blitz": ItemClassification.progression,
    "Brava": ItemClassification.progression,
    "Buck": ItemClassification.progression,
    "Capitao": ItemClassification.progression,
    "Castle": ItemClassification.progression,
    "Caveira": ItemClassification.progression,
    "Clash": ItemClassification.progression,
    "Deimos": ItemClassification.progression,
    "Denari": ItemClassification.progression,
    "Doc": ItemClassification.progression,
    "Dokkaebi": ItemClassification.progression,
    "Echo": ItemClassification.progression,
    "Ela": ItemClassification.progression,
    "Fenrir": ItemClassification.progression,
    "Finka": ItemClassification.progression,
    "Flores": ItemClassification.progression,
    "Frost": ItemClassification.progression,
    "Fuze": ItemClassification.progression,
    "Glaz": ItemClassification.progression,
    "Goyo": ItemClassification.progression,
    "Gridlock": ItemClassification.progression,
    "Grim": ItemClassification.progression,
    "Hibana": ItemClassification.progression,
    "Iana": ItemClassification.progression,
    "IQ": ItemClassification.progression,
    "Jackal": ItemClassification.progression,
    "Jager": ItemClassification.progression,
    "Kaid": ItemClassification.progression,
    "Kali": ItemClassification.progression,
    "Kapkan": ItemClassification.progression,
    "Lesion": ItemClassification.progression,
    "Lion": ItemClassification.progression,
    "Maestro": ItemClassification.progression,
    "Maverick": ItemClassification.progression,
    "Melusi": ItemClassification.progression,
    "Mira": ItemClassification.progression,
    "Montagne": ItemClassification.progression,
    "Mozzie": ItemClassification.progression,
    "Mute": ItemClassification.progression,
    "Nokk": ItemClassification.progression,
    "Nomad": ItemClassification.progression,
    "Noor": ItemClassification.progression,
    "Oryx": ItemClassification.progression,
    "Osa": ItemClassification.progression,
    "Pulse": ItemClassification.progression,
    "Ram": ItemClassification.progression,
    "Rauora": ItemClassification.progression,
    "Rook": ItemClassification.progression,
    "Sens": ItemClassification.progression,
    "Sentry": ItemClassification.progression,
    "Skopos": ItemClassification.progression,
    "Sledge": ItemClassification.progression,
    "Smoke": ItemClassification.progression,
    "Solid Snake": ItemClassification.progression,
    "Solis": ItemClassification.progression,
    "Striker": ItemClassification.progression,
    "Tachanka": ItemClassification.progression,
    "Thatcher": ItemClassification.progression,
    "Thermite": ItemClassification.progression,
    "Thorn": ItemClassification.progression,
    "Thunderbird": ItemClassification.progression,
    "Tubarao": ItemClassification.progression,
    "Twitch": ItemClassification.progression,
    "Valkyrie": ItemClassification.progression,
    "Vigil": ItemClassification.progression,
    "Wamai": ItemClassification.progression,
    "Warden": ItemClassification.progression,
    "Ying": ItemClassification.progression,
    "Zero": ItemClassification.progression,
    "Zofia": ItemClassification.progression,

    ".44 Mag Semi-Auto": ItemClassification.progression,
    ".44 Vendetta": ItemClassification.progression,
    "1911 TACOPS": ItemClassification.progression,
    "416-C Carbine": ItemClassification.progression,
    "417": ItemClassification.progression,
    "5.7 USG": ItemClassification.progression,
    "552 Commando": ItemClassification.progression,
    "556xi": ItemClassification.progression,
    "6P41": ItemClassification.progression,
    "9mm C1": ItemClassification.progression,
    "9x19SVN": ItemClassification.progression,
    "9x19VSN": ItemClassification.progression,
    "ACS12": ItemClassification.progression,
    "AK-12": ItemClassification.progression,
    "AK-47": ItemClassification.progression,
    "AK-74M": ItemClassification.progression,
    "ALDA 5.56": ItemClassification.progression,
    "AR-15.50": ItemClassification.progression,
    "AR-57": ItemClassification.progression,
    "AR33": ItemClassification.progression,
    "ARX200": ItemClassification.progression,
    "AUG A2": ItemClassification.progression,
    "AUG A3": ItemClassification.progression,
    "AUG A12": ItemClassification.progression,
    "Bailiff 410": ItemClassification.progression,
    "Ballistic Shield": ItemClassification.progression,
    "Bearing 9": ItemClassification.progression,
    "Benelli M3": ItemClassification.progression,
    "BOSG.12.2": ItemClassification.progression,
    "C75 Auto": ItemClassification.progression,
    "C7E": ItemClassification.progression,
    "C8-SFW": ItemClassification.progression,
    "CAMRS": ItemClassification.progression,
    "Commando 9": ItemClassification.progression,
    "CSRX 300": ItemClassification.progression,
    "D-50": ItemClassification.progression,
    "DP27": ItemClassification.progression,
    "F2": ItemClassification.progression,
    "F90": ItemClassification.progression,
    "FMG-9": ItemClassification.progression,
    "FO-12": ItemClassification.progression,
    "G36C": ItemClassification.progression,
    "G8A1": ItemClassification.progression,
    "Glaive-12": ItemClassification.progression,
    "GONNE-6": ItemClassification.progression,
    "GSH-18": ItemClassification.progression,
    "HK21": ItemClassification.progression,
    "ITA12L": ItemClassification.progression,
    "ITA12S": ItemClassification.progression,
    "K1A": ItemClassification.progression,
    "Keratos .357": ItemClassification.progression,
    "L1A1": ItemClassification.progression,
    "L85A2": ItemClassification.progression,
    "LFP586": ItemClassification.progression,
    "LMG-E": ItemClassification.progression,
    "Luison": ItemClassification.progression,
    "M1014": ItemClassification.progression,
    "M12": ItemClassification.progression,
    "M245 SAW": ItemClassification.progression,
    "M249": ItemClassification.progression,
    "M4": ItemClassification.progression,
    "M45 MEUSOC": ItemClassification.progression,
    "M590A1": ItemClassification.progression,
    "M762": ItemClassification.progression,
    "M870": ItemClassification.progression,
    "MK 14 EBR": ItemClassification.progression,
    "MK1 9mm": ItemClassification.progression,
    "MK17 CQB": ItemClassification.progression,
    "MP5": ItemClassification.progression,
    "MP5K": ItemClassification.progression,
    "MP5SD": ItemClassification.progression,
    "MP7": ItemClassification.progression,
    "MPX": ItemClassification.progression,
    "MX4 Storm": ItemClassification.progression,
    "OTS-03": ItemClassification.progression,
    "P-10C": ItemClassification.progression,
    "P10 Roni": ItemClassification.progression,
    "P12": ItemClassification.progression,
    "P226 MK 25": ItemClassification.progression,
    "P229": ItemClassification.progression,
    "P9": ItemClassification.progression,
    "P90": ItemClassification.progression,
    "PARA-308": ItemClassification.progression,
    "PCX-33": ItemClassification.progression,
    "PDW9": ItemClassification.progression,
    "PMM": ItemClassification.progression,
    "PMR90A2": ItemClassification.progression,
    "POF-9": ItemClassification.progression,
    "PRB92": ItemClassification.progression,
    "Q-929": ItemClassification.progression,
    "R4-C": ItemClassification.progression,
    "Reaper MK2": ItemClassification.progression,
    "RG15": ItemClassification.progression,
    "SASG-12": ItemClassification.progression,
    "SC3000K": ItemClassification.progression,
    "Scorpion Evo A1": ItemClassification.progression,
    "SDP 9mm": ItemClassification.progression,
    "SG-CQB": ItemClassification.progression,
    "SIX12": ItemClassification.progression,
    "SIX12 SD": ItemClassification.progression,
    "SMG-11": ItemClassification.progression,
    "SMG-12": ItemClassification.progression,
    "SPAS-12": ItemClassification.progression,
    "SPAS-15": ItemClassification.progression,
    "Spear .308": ItemClassification.progression,
    "SPSMG9": ItemClassification.progression,
    "SR-25": ItemClassification.progression,
    "Super 90": ItemClassification.progression,
    "Super Shorty": ItemClassification.progression,
    "SuperNova": ItemClassification.progression,
    "T-5 SMG": ItemClassification.progression,
    "T-95 LSW": ItemClassification.progression,
    "TACIT .45": ItemClassification.progression,
    "TCSG12": ItemClassification.progression,
    "Type-89": ItemClassification.progression,
    "UMP45": ItemClassification.progression,
    "USP40": ItemClassification.progression,
    "UZK50GI": ItemClassification.progression,
    "V308": ItemClassification.progression,
    "Vector .45 ACP": ItemClassification.progression,
    "XK23": ItemClassification.progression,

    "S.E.L.M.A. Aqua Breacher": ItemClassification.progression,
    "Prisma": ItemClassification.progression,
    "Garra Hook": ItemClassification.progression,
    "Surya Laser Gate": ItemClassification.progression,
    "Breaching Round": ItemClassification.progression,
    "Kiba Barrier": ItemClassification.progression,
    "Shock Wire": ItemClassification.progression,
    "H.U.L.L. Adaptable Shield": ItemClassification.progression,
    "G-52 Tactical Shield": ItemClassification.progression,
    "Kludge Drone": ItemClassification.progression,
    "Skeleton Key": ItemClassification.progression,
    "Tactical Crossbow": ItemClassification.progression,
    "Armor Panel": ItemClassification.progression,
    "Silent Step": ItemClassification.progression,
    "CCE Shield MK2": ItemClassification.progression,
    "Deathmark Tracker": ItemClassification.progression,
    "T.R.I.P. Connector": ItemClassification.progression,
    "Stim Pistol": ItemClassification.progression,
    "Jegeo Payload": ItemClassification.progression,
    "Yokai": ItemClassification.progression,
    "GRZMOT Mine": ItemClassification.progression,
    "F-NATT Dread Mine": ItemClassification.progression,
    "Adrenal Surge": ItemClassification.progression,
    "RCE-Ratero Charge": ItemClassification.progression,
    "Welcome Mat": ItemClassification.progression,
    "Cluster Charge": ItemClassification.progression,
    "Flip Sight": ItemClassification.progression,
    "Volcan Canister": ItemClassification.progression,
    "Trax Stingers": ItemClassification.progression,
    "Kawan Hive Launcher": ItemClassification.progression,
    "X-Kairos": ItemClassification.progression,
    "Gemini Replicator": ItemClassification.progression,
    "Electronics Detector": ItemClassification.progression,
    "Eyenox Model III": ItemClassification.progression,
    "Active Defense System": ItemClassification.progression,
    "Rtila Electroclaw": ItemClassification.progression,
    "LV Explosive Lance": ItemClassification.progression,
    "Entry Denial Device": ItemClassification.progression,
    "Gu": ItemClassification.progression,
    "EE-ONE-D": ItemClassification.progression,
    "Evil Eye": ItemClassification.progression,
    "Breaching Torch": ItemClassification.progression,
    "Banshee Sonic Defense": ItemClassification.progression,
    "Black Mirror": ItemClassification.progression,
    "Le Roc Shield": ItemClassification.progression,
    "Pest Launcher": ItemClassification.progression,
    "Signal Disruptor": ItemClassification.progression,
    "HEL Presence Reduction": ItemClassification.progression,
    "Airjab Launcher": ItemClassification.progression,
    "Horus Lance Launcher": ItemClassification.progression,
    "Remah Dash": ItemClassification.progression,
    "Talon-8 Shield": ItemClassification.progression,
    "Cardiac Sensor": ItemClassification.progression,
    "BU-GI Auto-Breacher": ItemClassification.progression,
    "D.O.M. Panel Launcher": ItemClassification.progression,
    "Armor Pack": ItemClassification.progression,
    "R.O.U. Projector System": ItemClassification.progression,
    "V10 Pantheon Shells": ItemClassification.progression,
    "Breaching Hammer": ItemClassification.progression,
    "Remote Gas Grenade": ItemClassification.progression,
    "Soliton Radar MK III": ItemClassification.progression,
    "SPEC-IO Electro-Sensor": ItemClassification.progression,
    "Gadget Kit": ItemClassification.progression,
    "Shumikha Launcher": ItemClassification.progression,
    "E.G.S. Disruptor": ItemClassification.progression,
    "Exothermic Charge": ItemClassification.progression,
    "Razorbloom Shell": ItemClassification.progression,
    "Kona Station": ItemClassification.progression,
    "Zoto Canister": ItemClassification.progression,
    "Shock Drone": ItemClassification.progression,
    "Black Eye": ItemClassification.progression,
    "ERC-7": ItemClassification.progression,
    "MAG-NET System": ItemClassification.progression,
    "Glance Smart Glasses": ItemClassification.progression,
    "Candela": ItemClassification.progression,
    "Argus Launcher": ItemClassification.progression,
    "KS79 Lifeline": ItemClassification.progression,

    "Breach Charge": ItemClassification.progression,
    "Claymore": ItemClassification.progression,
    "Frag Grenade": ItemClassification.progression,
    "Hard Breach Charge": ItemClassification.progression,
    "Impact EMP Grenade": ItemClassification.progression,
    "Smoke Grenade": ItemClassification.progression,
    "Stun Grenade": ItemClassification.progression,
    "Impact Grenade": ItemClassification.progression,
    "Deployable Shield": ItemClassification.progression,
    "Barbed Wire": ItemClassification.progression,
    "Bulletproof Camera": ItemClassification.progression,
    "Nitro Cell": ItemClassification.progression,
    "Proximity Alarm": ItemClassification.progression,
    "Observation Blocker": ItemClassification.progression,
    
    "Siege Filler Item": ItemClassification.filler
}

class R6SiegeItem(Item):
    game = "Rainbow Six Siege"

def get_random_filler_item_name(world: R6SiegeWorld) -> str:
    return "Siege Filler Item"

def create_item_with_correct_classification(world: R6SiegeWorld, name: str) -> R6SiegeItem:
    return R6SiegeItem(name, DEFAULT_ITEM_CLASSIFICATIONS[name], ITEM_NAME_TO_ID[name], world.player)

def create_weapons(world: R6SiegeWorld, starting_operators: list[str]) -> list[R6SiegeItem]:
    operators = [generation.name_to_operator_data(operator) for operator in world.selected_operators]
    starting_operators = [generation.name_to_operator_data(operator) for operator in starting_operators]
    
    weapons: list[str] = []
    
    for operator in operators:
        operator_weapons: list[str] = []
        
        if not world.options.weaponsanity_logic_behavior_include_out_of_logic_weapons.value:
            match world.options.weaponsanity_logic.value:
                
                case world.options.weaponsanity_logic.option_any_weapon:
                    operator_weapons += operator.primary_weapons + operator.secondary_weapons
                    
                case world.options.weaponsanity_logic.option_any_primary:
                    operator_weapons += operator.primary_weapons + (operator.viable_weapons - operator.primary_weapons)
                    
                case world.options.weaponsanity_logic.option_any_viable_weapon:
                    operator_weapons += operator.viable_weapons
                    
                case world.options.weaponsanity_logic.option_most_popular_weapon:
                    operator_weapons += operator.most_popular_weapons
                    
        else:
            operator_weapons += operator.primary_weapons + operator.secondary_weapons
            
        for weapon in operator_weapons:
            if weapon not in weapons:
                weapons.append(weapon)
                
    for starting_operator in range(world.options.weaponsanity_in_logic_starting_weapons.value):
        starting_weapon: str = ""
        operator = starting_operators[starting_operator]
        
        match world.options.weaponsanity_logic.value:
            
            case world.options.weaponsanity_logic.option_any_weapon:
                starting_weapon = world.random.choice(operator.primary_weapons + operator.secondary_weapons)
            
            case world.options.weaponsanity_logic.option_any_primary:
                starting_weapon = world.random.choice(operator.primary_weapons + (operator.viable_weapons - operator.primary_weapons))
            
            case world.options.weaponsanity_logic.option_any_viable_weapon:
                starting_weapon = world.random.choice(operator.viable_weapons)
            
            case world.options.weaponsanity_logic.option_most_popular_weapon:
                starting_weapon = world.random.choice(operator.most_popular_weapons)
        
        if starting_weapon in weapons:
            weapons.remove(starting_weapon)
            world.push_precollected(world.create_item(starting_weapon))
            
    for _ in range(world.options.weaponsanity_starting_weapons.value - world.options.weaponsanity_in_logic_starting_weapons.value):
        starting_weapon = world.random.choice(weapons)
        weapons.remove(starting_weapon)
        world.push_precollected(world.create_item(starting_weapon))
            
    return [world.create_item(weapon) for weapon in weapons if print(f"Weapon: {weapon}") is None]

def create_abilities(world:R6SiegeWorld, starting_operators: list[str]) -> list[R6SiegeItem]:
    operators = [generation.name_to_operator_data(operator) for operator in world.selected_operators]
    starting_operators = [generation.name_to_operator_data(operator) for operator in starting_operators]
    
    abilities: list[str] = []
    
    for operator in operators:
        if operator.name != "Striker" and operator.name != "Sentry":
            abilities.append(operator.ability)
        else:
            if world.options.abilitysanity_gadget_kit.value:
                if operator.ability not in abilities:
                    abilities.append(operator.ability)
                    
    for starting_operator in range(world.options.abilitysanity_in_logic_starting_abilities.value):
        operator = starting_operators[starting_operator]
        if operator.ability in abilities:
            abilities.remove(operator.ability)
            world.push_precollected(world.create_item(operator.ability))
            
    for _ in range(world.options.abilitysanity_starting_abilities.value - world.options.abilitysanity_in_logic_starting_abilities.value):
        starting_ability = world.random.choice(abilities)
        abilities.remove(starting_ability)
        world.push_precollected(world.create_item(starting_ability))
            
    return [world.create_item(ability) for ability in abilities if print(f"Ability: {ability}") is None]

def create_gadgets(world: R6SiegeWorld, starting_operators: list[str]) -> list[R6SiegeItem]:
    operators = [generation.name_to_operator_data(operator) for operator in world.selected_operators]
    starting_operators = [generation.name_to_operator_data(operator) for operator in starting_operators]

    gadgets: list[str] = []

    for operator in operators:
        for gadget in operator.gadgets:
            if gadget not in gadgets:
                gadgets.append(gadget)

    for starting_operator in range(world.options.abilitysanity_in_logic_starting_abilities):
        if starting_operators[starting_operator].name == "Striker":

            if world.options.easy_challenges.value and operator_data.striker_easy_challenge_gadgets:
                gadget = world.random.choice(operator_data.striker_easy_challenge_gadgets)
                gadgets.remove(gadget)
                world.push_precollected(world.create_item(gadget))

            if world.options.hard_challenges.value and operator_data.striker_hard_challenge_gadgets:
                gadget = world.random.choice(operator_data.striker_hard_challenge_gadgets)
                if gadget in gadgets:
                    gadgets.remove(gadget)
                    world.push_precollected(world.create_item(gadget))

        if starting_operators[starting_operator].name == "Sentry":

            if world.options.easy_challenges.value:
                gadget = world.random.choice(operator_data.sentry_easy_challenge_gadgets)
                gadgets.remove(gadget)
                world.push_precollected(world.create_item(gadget))

            if world.options.hard_challenges.value:
                gadget = world.random.choice(operator_data.sentry_hard_challenge_gadgets)
                if gadget in gadgets:
                    gadgets.remove(gadget)
                    world.push_precollected(world.create_item(gadget))
                    
    for starting_gadget in range(world.options.gadgetsanity_starting_gadgets):
        if starting_gadget == len(gadgets):
            break
        gadget = world.random.choice(gadgets)
        gadgets.remove(gadget)
        world.push_precollected(world.create_item(gadget))

    return [world.create_item(gadget) for gadget in gadgets if print(f"Gadget: {gadget}") is None]

def create_starting_operators(world: R6SiegeWorld) -> list[str]:
    starting_operators = []
    available_starting_operators = sorted(set(world.selected_operators) - world.options.forced_starting_operators.value)
    starting_operators_count = world.options.starting_operators.value - len(world.options.forced_starting_operators.value)

    if len(world.selected_operators) == world.options.starting_operators.value:
        return world.selected_operators


    match world.options.starting_operator_balancing.value:

        case world.options.starting_operator_balancing.option_disabled:
            return world.random.sample(available_starting_operators, k = starting_operators_count)

        case world.options.starting_operator_balancing.option_light:
            if len(available_starting_operators) > 1 and starting_operators_count > 1:
                starting_operators.append(world.random.choice(available_starting_operators))
                starting_operators.append(world.random.choice([n for n in available_starting_operators 
                                                               if generation.name_to_operator_data(n).side != 
                                                               generation.name_to_operator_data(starting_operators[0]).side]))
                return starting_operators + world.random.sample(available_starting_operators, k = starting_operators_count - 2)
            else:
                return world.options.forced_starting_operators.value

        case world.options.starting_operator_balancing.option_heavy:
            less = "Neither"
            if len(available_starting_operators) > 1 and starting_operators_count > 1:
                attackers = [n for n in available_starting_operators if generation.name_to_operator_data(n).side == "Attacker"]
                defenders = [n for n in available_starting_operators if generation.name_to_operator_data(n).side == "Defender"]

                if len(attackers) >= floor(starting_operators_count / 2):
                    starting_operators += world.random.sample(attackers, k = floor(starting_operators_count / 2))
                else:
                    starting_operators += attackers
                    less = "Attackers"

                if len(defenders) >= floor(starting_operators_count / 2):
                    starting_operators.append(world.random.sample(defenders, k = floor(starting_operators_count / 2)))
                else: 
                    starting_operators += defenders
                    less = "Defenders"

                if less == "Attackers":
                    starting_operators += world.random.sample([n for n in defenders if n not in starting_operators],
                                                               k = starting_operators_count - len(starting_operators))
                elif less == "Defenders":
                    starting_operators += world.random.sample([n for n in defenders if n not in starting_operators],
                                                               k = starting_operators_count - len(starting_operators))
                elif starting_operators_count % 2 == 1:
                    starting_operators.append(world.random.choice([n for n in world.selected_operators if n not in starting_operators]))

                return starting_operators
            else:
                return world.options.forced_starting_operators.value

def validate_fill(world: R6SiegeWorld, items: int, locations: int) -> None:
    if items > locations:
        remaining_items = items - locations
        available_location_increasing_options = []

        if world.options.kill_threshold.value:
            available_location_increasing_options.append("kill_threshold_value")

        if world.options.easy_challenges.value:
            available_location_increasing_options.append("easy_challenge_value")

        if world.options.hard_challenges.value:
            available_location_increasing_options.append("hard_challenge_value")

        raise OptionError(f"{world.player_name} needs {round(remaining_items / (world.options.goal_operators.value - world.options.extra_operators.value), 0)} (estimate) more checks per operator to ensure a successful generation. Please increase one of the following options: {available_location_increasing_options}")

def create_all_items(world: R6SiegeWorld) -> None:
    print(world.selected_operators)
    itempool: list[R6SiegeItem] = []
    starting_operators = create_starting_operators(world)
    print(starting_operators)
    
    for operator in world.selected_operators:
        if operator in starting_operators:
            world.push_precollected(world.create_item(operator))
        else:
            itempool.append(world.create_item(operator))
    
    if world.options.weaponsanity.value:
        itempool += create_weapons(world, starting_operators)
        
    if world.options.abilitysanity.value:
        itempool += create_abilities(world, starting_operators)
        
    if world.options.gadgetsanity.value:
        itempool += create_gadgets(world, starting_operators)
        
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    validate_fill(world, number_of_items, number_of_unfilled_locations)
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool