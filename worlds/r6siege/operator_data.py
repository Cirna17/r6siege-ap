from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .world import R6SiegeWorld as R6SiegeWorld

class Operator:
    def __init__(self, name, primary_weapons, secondary_weapons, ability, gadgets, side):
        self.name: str = name
        self.primary_weapons: list[str] = primary_weapons
        self.secondary_weapons: list[str] = secondary_weapons
        self.ability: str = ability
        self.gadgets: str = gadgets
        self.side: str = side
        
        self.easy_challenge = None
        self.easy_challenge_count = None
        self.easy_challenge_gadgets = None
        self.hard_challenge = None
        self.hard_challenge_count = None
        self.hard_challenge_gadgets = None
        self.viable_weapons = None
        self.most_popular_weapons = None
        
    def assign_challenges_and_weapons(self, world: R6SiegeWorld):
        self.easy_challenge = world.options.easy_challenges_challenges.value[self.name][0]
        self.easy_challenge_count = world.options.easy_challenges_challenges.value[self.name][1]
        if len(world.options.easy_challenges_challenges.value[self.name]) > 2:
            self.easy_challenge_gadgets = world.options.easy_challenges_challenges.value[self.name][2]
            
        self.hard_challenge = world.options.hard_challenges_challenges.value[self.name][0]
        self.hard_challenge_count = world.options.hard_challenges_challenges.value[self.name][1]
        if len(world.options.hard_challenges_challenges.value[self.name]) > 2:
            self.hard_challenge_gadgets = world.options.hard_challenges_challenges.value[self.name][2]
            
        self.viable_weapons = world.options.weaponsanity_logic_viable_weapons.value[self.name]
        self.most_popular_weapons = world.options.weaponsanity_logic_most_popular_weapons.value[self.name]

ace = Operator(
    "Ace", 
    ["AK-12", "M1014"], ["P9"], 
    "S.E.L.M.A. Aqua Breacher", 
    ["Breach Charge", "Claymore"], 
    "Attacker")

alibi = Operator(
    "Alibi", 
    ["MX4 Storm", "ACS12"], ["Keratos .357", "Bailiff 410"], 
    "Prisma", 
    ["Proximity Alarm", "Observation Blocker"], 
    "Defender")

amaru = Operator(
    "Amaru", 
    ["G8A1", "SuperNova"], ["GONNE-6", "SMG-11", "ITA12S"], 
    "Garra Hook", 
    ["Stun Grenade", "Hard Breach Charge"], 
    "Attacker")

aruni = Operator(
    "Aruni", 
    ["P10 Roni", "MK 14 EBR"], ["PRB92"], 
    "Surya Laser Gate", 
    ["Bulletproof Camera", "Barbed Wire"], 
    "Defender")

ash = Operator(
    "Ash", 
    ["G36C", "R4-C"], ["5.7 USG", "M45 MEUSOC"], 
    "Breaching Round", 
    ["Breach Charge", "Claymore"], 
    "Attacker")

azami = Operator(
    "Azami", 
    ["9x19SVN", "ACS12"], ["D-50"], 
    "Kiba Barrier", 
    ["Impact Grenade", "Barbed Wire"], 
    "Defender")

bandit = Operator(
    "Bandit", 
    ["MP7", "M870"], ["P12", "Keratos .357"], 
    "Shock Wire", 
    ["Barbed Wire", "Nitro Cell"], 
    "Defender")

blackbeard = Operator(
    "Blackbeard", 
    ["MK17 CQB", "SR-25"], [], 
    "H.U.L.L. Adaptable Shield", 
    ["Claymore", "Frag Grenade"], 
    "Attacker")

blitz = Operator(
    "Blitz", 
    [], ["P12"], 
    "G-52 Tactical Shield", 
    ["Smoke Grenade", "Breach Charge"], 
    "Attacker")

brava = Operator(
    "Brava", 
    ["PARA-308", "CAMRS"], ["USP40", "Super Shorty"], 
    "Kludge Drone", 
    ["Smoke Grenade", "Claymore"], 
    "Attacker")

buck = Operator(
    "Buck", 
    ["C8-SFW", "CAMRS"], ["MK1 9mm"], 
    "Skeleton Key", 
    ["Stun Grenade", "Claymore"], 
    "Attacker")

capitao = Operator(
    "Capitao", 
    ["M249", "PARA-308", "PMR90A2"], ["GONNE-6", "PRB92"], 
    "Tactical Crossbow", 
    ["Claymore", "Hard Breach Charge", "Impact EMP Grenade"], 
    "Attacker")

castle = Operator(
    "Castle", 
    ["UMP45", "M1014"], ["5.7 USG", "Super Shorty", "M45 MEUSOC"], 
    "Armor Panel", 
    ["Proximity Alarm", "Bulletproof Camera"], 
    "Defender")

caveira = Operator(
    "Caveira", 
    ["M12", "SPAS-15"], ["LUSION"], 
    "Silent Step", 
    ["Proximity Alarm", "Impact Grenade", "Observation Blocker"], 
    "Defender")

clash = Operator(
    "Clash", 
    [], ["P-10C", "SPSMG9", "Super Shorty"], 
    "CCE Shield MK2", 
    ["Barbed Wire", "Impact Grenade"], 
    "Defender")

deimos = Operator(
    "Deimos", 
    ["AK-74M", "M590A1"], [".44 Vendetta"], 
    "Deathmark Tracker", 
    ["Frag Grenade", "Hard Breach Charge"], 
    "Attacker")

denari = Operator(
    "Denari", 
    ["Scorpion Evo A1", "FMG-9"], ["Glaive-12", "P226 MK 25"], 
    "T.R.I.P. Connector", 
    ["Observation Blocker", "Deployable Shield"], 
    "Defender")

doc = Operator(
    "Doc", 
    ["MP5", "P90", "SG-CQB"], ["P9", "LFP586", "Bailiff 410"], 
    "Stim Pistol", 
    ["Bulletproof Camera", "Barbed Wire"], 
    "Defender")

dokkaebi = Operator(
    "Dokkaebi", 
    ["BOSG. 12.2", "MK 14 EBR", "XK23"], ["GONNE-6", "SMG-12", "C75 Auto"], 
    "Jegeo Payload", 
    ["Smoke Grenade", "Impact EMP Grenade"], 
    "Attacker")

echo = Operator(
    "Echo", 
    ["MP5SD", "SuperNova"], ["Bearing 9", "P229"], 
    "Yokai", 
    ["Impact Grenade", "Deployable Shield"], 
    "Defender")

ela = Operator(
    "Ela", 
    ["Scorpion Evo A1", "FO-12"], ["RG15"], 
    "GRZMOT Mine", 
    ["Barbed Wire", "Deployable Shield", "Impact Grenade"],  
    "Defender")

fenrir = Operator(
    "Fenrir", 
    ["MP7", "SASG-12"], ["5.7 USG"], 
    "F-NATT Dread Mine", 
    ["Bulletproof Camera", "Observation Blocker"], 
    "Defender")

finka = Operator(
    "Finka", 
    ["6P41", "SASG-12", "Spear .308"], ["GSH-18", "PMM"], 
    "Adrenal Surge", 
    ["Frag Grenade", "Smoke Grenade", "Stun Grenade"], 
    "Attacker")

flores = Operator(
    "Flores", 
    ["AR33", "SR-25", "T-95 LSW"], ["GSH-18"], 
    "RCE-Ratero Charge", 
    ["Stun Grenade", "Claymore"], 
    "Attacker")

frost = Operator(
    "Frost", 
    ["Super 90", "9mm C1"], ["MK1 9mm", "ITA12S"], 
    "Welcome Mat", 
    ["Bulletproof Camera", "Deployable Shield"], 
    "Defender")

fuze = Operator(
    "Fuze", 
    ["AK-12", "6P41", "Ballistic Shield"], ["PMM", "GSH-18"], 
    "Cluster Charge", 
    ["Breach Charge", "Hard Breach Charge", "Smoke Grenade"], 
    "Attacker")

glaz = Operator(
    "Glaz", 
    ["OTS-03"], ["PMM", "GONNE-6", "Bearing 9"], 
    "Flip Sight", 
    ["Smoke Grenade", "Frag Grenade", "Claymore"], 
    "Attacker")

goyo = Operator(
    "Goyo", 
    ["Vector .45 ACP", "TCSG12"], ["P229"], 
    "Volcan Canister", 
    ["Proximity Alarm", "Bulletproof Camera", "Impact Grenade"], 
    "Defender")

gridlock = Operator(
    "Gridlock", 
    ["F90", "M245 SAW"], ["Super Shorty", "SDP 9mm"], 
    "Trax Stingers", 
    ["Smoke Grenade", "Frag Grenade", "Impact EMP Grenade"], 
    "Attacker")

grim = Operator(
    "Grim", 
    ["552 Commando", "SG-CQB"], ["Bailiff 410", "P229"], 
    "Kawan Hive Launcher", 
    ["Claymore", "Hard Breach Charge", "Impact EMP Grenade"], 
    "Attacker")

hibana = Operator(
    "Hibana", 
    ["SuperNova", "Type-89", "PMR90A2"], ["Bearing 9", "P229"], 
    "X-Kairos", 
    ["Breach Charge", "Stun Grenade", "Claymore"], 
    "Attacker")

iana = Operator(
    "Iana", 
    ["ARX200", "G36C"], ["GONNE-6", "MK1 9mm"], 
    "Gemini Replicator", 
    ["Impact EMP Grenade", "Smoke Grenade"], 
    "Attacker")

iq = Operator(
    "IQ", 
    ["AUG A2", "552 Commando", "G8A1"], ["P12"], 
    "Electronics Detector", 
    ["Breach Charge", "Frag Grenade", "Claymore"], 
    "Attacker")

jackal = Operator(
    "Jackal", 
    ["C7E", "PDW9", "ITA12L"], ["USP40", "ITA12S"], 
    "Eyenox Model III", 
    ["Smoke Grenade", "Claymore"], 
    "Attacker")

jager = Operator(
    "Jager", 
    ["M870", "416-C Carbine"], ["P12", "P-10C"], 
    "Active Defense System", 
    ["Bulletproof Camera", "Observation Blocker"], 
    "Defender")

kaid = Operator(
    "Kaid", 
    ["AUG A3", "TCSG12"], [".44 Mag Semi-Auto", "LFP586"], 
    "Rtila Electroclaw", 
    ["Barbed Wire", "Nitro Cell", "Observation Blocker"], 
    "Defender")

kali = Operator(
    "Kali", 
    ["CSRX 300"], ["SPSMG9", "C75 Auto", "P226 MK 25"], 
    "LV Explosive Lance", 
    ["Breach Charge", "Claymore", "Smoke Grenade"], 
    "Attacker")

kapkan = Operator(
    "Kapkan", 
    ["9x19VSN", "SASG-12"], ["PMM", "GSH-18"], 
    "Entry Denial Device", 
    ["Barbed Wire", "Bulletproof Camera"], 
    "Defender")

lesion = Operator(
    "Lesion", 
    ["SIX12 SD", "T-5 SMG"], ["Q-929"], 
    "Gu", 
    ["Observation Blocker", "Bulletproof Camera"], 
    "Defender")

lion = Operator(
    "Lion", 
    ["417", "SG-CQB", "V308"], ["LFP586", "P9"], 
    "EE-ONE-D", 
    ["Claymore", "Frag Grenade", "Stun Grenade"], 
    "Attacker")

maestro = Operator(
    "Maestro", 
    ["ALDA 5.56", "ACS12"], ["Keratos .357", "Bailiff 410"], 
    "Evil Eye", 
    ["Barbed Wire", "Impact Grenade", "Observation Blocker"], 
    "Defender")

maverick = Operator(
    "Maverick", 
    ["M4", "AR-15.50"], ["1911 TACOPS", "Reaper MK2"], 
    "Breaching Torch", 
    ["Claymore", "Stun Grenade", "Frag Grenade"], 
    "Attacker")

melusi = Operator(
    "Melusi", 
    ["MP5", "Super 90"], ["ITA12S", "RG15"], 
    "Banshee Sonic Defense", 
    ["Bulletproof Camera", "Impact Grenade"], 
    "Defender")

mira = Operator(
    "Mira", 
    ["Vector .45 ACP", "ITA12L"], ["ITA12S", "USP40"], 
    "Black Mirror", 
    ["Nitro Cell", "Proximity Alarm"], 
    "Defender")

montagne = Operator(
    "Montagne", 
    [], ["P9", "LFP586"], 
    "Le Roc Shield", 
    ["Impact EMP Grenade", "Smoke Grenade", "Hard Breach Charge"], 
    "Attacker")

mozzie = Operator(
    "Mozzie", 
    ["Commando 9", "P10 Roni"], ["SDP 9mm", "Super Shorty"], 
    "Pest Launcher", 
    ["Barbed Wire", "Nitro Cell", "Impact Grenade"], 
    "Defender")

mute = Operator(
    "Mute", 
    ["M590A1", "MP5K"], ["SMG-11", "P226 MK 25"], 
    "Signal Disruptor", 
    ["Nitro Cell", "Bulletproof Camera"], 
    "Defender")

nokk = Operator(
    "Nokk", 
    ["FMG-9", "SIX12 SD", "PMR90A2"], ["5.7 USG", "D-50"], 
    "HEL Presence Reduction", 
    ["Impact EMP Grenade", "Hard Breach Charge", "Frag Grenade"], 
    "Attacker")

nomad = Operator(
    "Nomad",  
    ["AK-74M", "ARX200"], ["PRB92", ".44 Mag Semi-Auto"], 
    "Airjab Launcher", 
    ["Breach Charge", "Stun Grenade"], 
    "Attacker")

noor = Operator(
    "Noor", 
    ["Commando 9", "ALDA 5.56"], ["1911 TACOPS", "Bailiff 410"], 
    "Horus Lance Launcher", 
    ["Deployable Shield", "Barbed Wire"], 
    "Defender")

oryx = Operator(
    "Oryx", 
    ["T-5 SMG", "SPAS-12"], ["USP40", "Bailiff 410", "Reaper MK2"], 
    "Remah Dash", 
    ["Barbed Wire", "Proximity Alarm"], 
    "Defender")

osa = Operator(
    "Osa", 
    ["556xi", "PDW9"], ["PMM"], 
    "Talon-8 Shield", 
    ["Claymore", "Frag Grenade", "Impact EMP Grenade"], 
    "Attacker")

pulse = Operator(
    "Pulse", 
    ["UMP45", "M1014"], ["Reaper MK2", "5.7 USG", "M45 MEUSOC"], 
    "Cardiac Sensor", 
    ["Nitro Cell", "Deployable Shield", "Observation Blocker"], 
    "Defender")

ram = Operator(
    "Ram", 
    ["R4-C", "LMG-E"], ["MK1 9mm"], 
    "BU-GI Auto-Breacher", 
    ["Stun Grenade", "Smoke Grenade"], 
    "Attacker")

rauora = Operator(
    "Rauora", 
    ["XK23", "417", "M249"], ["Reaper MK2", "GSH-18"], 
    "D.O.M. Panel Launcher", 
    ["Smoke Grenade", "Breach Charge"], 
    "Attacker")

rook = Operator(
    "Rook", 
    ["MP5", "P90", "SG-CQB"], ["LFP586", "P9", "Reaper MK2"], 
    "Armor Pack", 
    ["Proximity Alarm", "Impact Grenade", "Nitro Cell"], 
    "Defender")

sens = Operator(
    "Sens", 
    ["POF-9", "XK23", "417"], ["SDP 9mm"], 
    "R.O.U. Projector System", 
    ["Frag Grenade", "Hard Breach Charge", "Claymore"], 
    "Attacker")

sentry = Operator(
    "Sentry", 
    ["Commando 9", "M870", "TCSG12"], ["C75 Auto", "Super Shorty"], 
    "Gadget Kit", 
    ["Barbed Wire", "Bulletproof Camera", "Deployable Shield", "Observation Blocker", "Impact Grenade", "Nitro Cell", "Proximity Alarm"], 
    "Defender")

skopos = Operator(
    "Skopos", 
    ["PCX-33"], ["P229"], 
    "V10 Pantheon Shells", 
    ["Impact Grenade", "Proximity Alarm"], 
    "Defender")

sledge = Operator(
    "Sledge", 
    ["L85A2", "M590A1"], ["Reaper MK2", "P226 MK 25"], 
    "Breaching Hammer", 
    ["Frag Grenade", "Stun Grenade", "Impact EMP Grenade"], 
    "Attacker")

smoke = Operator(
    "Smoke", 
    ["M590A1", "FMG-9"], ["SMG-11", "P226 MK 25"], 
    "Remote Gas Grenade", 
    ["Barbed Wire", "Proximity Alarm", "Deployable Shield"], 
    "Defender")

solidsnake = Operator(
    "Solid Snake", 
    ["F2", "PMR90A2"], ["TACIT .45"], 
    "Soliton Radar MK III", 
    ["Frag Grenade", "Stun Grenade", "Impact EMP Grenade", "Smoke Grenade", "Breach Charge"], 
    "Attacker")

solis = Operator(
    "Solis", 
    ["P90", "ITA12L"], ["SMG-11"], 
    "SPEC-IO Electro-Sensor", 
    ["Proximity Alarm", "Impact Grenade"], 
    "Defender")

striker = Operator(
    "Striker", 
    ["M4", "M249", "SR-25"], ["ITA12S", "5.7 USG"], 
    "Gadget Kit", 
    ["Breach Charge", "Claymore", "Frag Grenade", "Hard Breach Charge", "Smoke Grenade", "Stun Grenade"], 
    "Attacker")

tachanka = Operator(
    "Tachanka", 
    ["DP27", "9x19VSN"], ["Bearing 9", "PMM", "GSH-18"], 
    "Shumikha Launcher", 
    ["Barbed Wire", "Deployable Shield", "Proximity Alarm"], 
    "Defender")

thatcher = Operator(
    "Thatcher", 
    ["L85A2", "AR33", "PMR90A2", "M590A1"], ["P226 MK 25"], 
    "E.G.S. Disruptor", 
    ["Claymore", "Breach Charge"], 
    "Attacker")

thermite = Operator(
    "Thermite", 
    ["556xi", "M1014"], ["M45 MEUSOC", "5.7 USG", "ITA12S"], 
    "Exothermic Charge", 
    ["Smoke Grenade", "Stun Grenade"], 
    "Attacker")

thorn = Operator(
    "Thorn", 
    ["UZK50GI", "M870"], ["C75 Auto", "1911 TACOPS"], 
    "Razorbloom Shell", 
    ["Deployable Shield", "Barbed Wire"], 
    "Defender")

thunderbird = Operator(
    "Thunderbird", 
    ["Spear .308", "SPAS-15"], ["Bearing 9","ITA12S", "Q-929"], 
    "Kona Station", 
    ["Deployable Shield", "Barbed Wire", "Bulletproof Camera"], 
    "Defender")

tubarao = Operator(
    "Tubarao", 
    ["MPX", "AR-15.50"], ["P226 MK 25"], 
    "Zoto Canister", 
    ["Nitro Cell", "Proximity Alarm"], 
    "Defender")

twitch = Operator(
    "Twitch", 
    ["F2", "417", "SG-CQB"], ["P9", "LFP586"], 
    "Shock Drone", 
    ["Claymore", "Smoke Grenade"], 
    "Attacker")

valkyrie = Operator(
    "Valkyrie", 
    ["MPX", "SPAS-12"], ["D-50"], 
    "Black Eye", 
    ["Impact Grenade", "Nitro Cell"], 
    "Defender")

vigil = Operator(
    "Vigil", 
    ["K1A", "BOSG. 12.2"], ["C75 Auto", "SMG-12"], 
    "ERC-7", 
    ["Impact Grenade", "Bulletproof Camera"], 
    "Defender")

wamai = Operator(
    "Wamai", 
    ["AUG A12", "MP5K"], ["Keratos .357", "P12", "Super Shorty"], 
    "MAG-NET System", 
    ["Deployable Shield", "Proximity Alarm", "Nitro Cell"], 
    "Defender")

warden = Operator(
    "Warden", 
    ["M590A1", "MPX"], ["SMG-12", "P-10C"], 
    "Glance Smart Glasses", 
    ["Deployable Shield", "Nitro Cell", "Observation Blocker"], 
    "Defender")

ying = Operator(
    "Ying", 
    ["T-95 LSW", "SIX12"], ["Q-929", "Reaper MK2"], 
    "Candela", 
    ["Hard Breach Charge", "Smoke Grenade"], 
    "Attacker")

zero = Operator(
    "Zero", 
    ["SC3000K", "MP7"], ["5.7 USG", "GONNE-6"], 
    "Argus Launcher", 
    ["Hard Breach Charge", "Claymore"], 
    "Attacker")

zofia = Operator(
    "Zofia", 
    ["M762", "LMG-E"], ["RG15"], 
    "KS79 Lifeline", 
    ["Hard Breach Charge", "Claymore"], 
    "Attacker")

operators = [ace, alibi, amaru, aruni, ash, azami, bandit, blackbeard, blitz, brava, buck, capitao, castle, caveira, clash,
             deimos, denari, doc, dokkaebi, echo, ela, fenrir, finka, flores, frost, fuze, glaz, goyo, gridlock, grim,
             hibana, iana, iq, jackal, jager, kaid, kali, kapkan, lesion, lion, maestro, maverick, melusi, mira, montagne,
             mozzie, mute, nokk, nomad, noor, oryx, osa, pulse, ram, rauora, rook, sens, sentry, skopos, sledge, smoke,
             solidsnake, solis, striker, tachanka, thatcher, thermite, thorn, thunderbird, tubarao, twitch, valkyrie,
             vigil, wamai, warden, ying, zero, zofia]

def assign_challenges_and_weapons_from_options(world: R6SiegeWorld) -> None:
    for operator in operators:
        print(operator.name)
        operator.assign_challenges_and_weapons(world)