from pathlib import Path

script_directory = Path(__file__).resolve().parent

class Operator:
    def __init__(self, name, easy_challenge, easy_challenge_count, hard_challenge, hard_challenge_count, primary_weapons, secondary_weapons, ability, gadgets, viable_weapons, most_popular_weapons, side):
        self.name = name
        self.easy_challenge = easy_challenge
        self.easy_challenge_count = easy_challenge_count
        self.hard_challenge = hard_challenge
        self.hard_challenge_count = hard_challenge_count
        self.primary_weapons = primary_weapons
        self.secondary_weapons = secondary_weapons
        self.ability = ability
        self.gadgets = gadgets
        self.viable_weapons = viable_weapons
        self.most_popular_weapons = most_popular_weapons
        self.side = side
        self.colored_icon = str(script_directory / "icons_colored" / f"{self.name}.png")
        self.grayscale_icon = str(script_directory / "icons_grayscale" / f"{self.name}.png")
        self.portrait = str(script_directory / "portraits" / f"{self.name}.png")

ace = Operator("Ace", "Deploy S.E.L.M.A. Aqua Breachers", 10, "Use S.E.L.M.A.s on walls bordering a point", 3, ["AK-12", "M1014"], ["P9"], "S.E.L.M.A. Aqua Breacher", ["Breach Charge", "Claymore"], ["AK-12"], ["AK-12"], "Attacker")
alibi = Operator("Alibi", "Deploy Prisma clones", 15, "Track enemies through Prisma clones", 2, ["MX4 Storm", "ACS12"], ["Keratos .357", "Bailiff 410"], "Prisma", ["Proximity Alarm", "Observation Blocker"], ["MX4 Storm"], ["MX4 Storm"], "Defender")
amaru = Operator("Amaru", "Use the Garra Hook", 3, "Get kills with Stun Grenades", 2, ["G8A1, SuperNova"], ["GONNE-6", "SMG-11", "ITA12S"], "Garra Hook", ["Stun Grenade", "Hard Breach Charge"], ["G8A1", "SuperNova"], ["G8A1"], "Attacker")
aruni = Operator("Aruni", "Deploy Surya Laser Gates", 10, "Destroy devices with Surya gates or reactivate gates", 4, ["P10 Roni", "MK 14 EBR"], ["PRB92"], "Surya Laser Gate", ["Bulletproof Camera", "Barbed Wire"], ["MK 14 EBR"], ["MK 14 EBR"], "Defender")
ash = Operator("Ash", "Use Breaching Rounds", 10, "", 0, ["G36C", "R4-C"], ["5.7 USG", "M45 MEUSOC"], "Breaching Round", ["Breach Charge", "Claymore"], ["G36C, R4-C"], ["R4-C"], "Attacker")
azami = Operator("Azami", "Deploy Kiba Barriers", 10, "", 0, ["9x19SVN", "ACS12"], ["D-50"], "Kiba Barrier", ["Impact Grenade", "Barbed Wire"], ["9x19SVN"], ["9x19SVN"], "Defender")
bandit = Operator("Bandit", "Deploy Shock Wires", 16, "Re-electify walls", 3, ["MP7", "M870"], ["P12", "Keratos .357"], "Shock Wire", ["Barbed Wire, Nitro Cell"], ["MP7"], ["MP7"], "Defender")
blackbeard = Operator("Blackbeard", "Use the breach on the H.U.L.L. Adaptable Shield", 5, "", 0, ["MK17 CQB", "SR-25"], [], "H.U.L.L. Adaptable Shield", ["Claymore", "Frag Grenade"], ["MK17 CQB", "SR-25"], ["MK17 CQB"], "Attacker")
blitz = Operator("Blitz", "Flash enemies with the G-52 Tactical Shield", 5, "Get flash assist kills", 2, [], ["P12"], "G-52 Tactical Shield", ["Smoke Grenade", "Breach Charge"], ["P12"], ["P12"], "Attacker")
brava = Operator("Brava", "Hack defender cameras with the Kludge Drone", 5, "Hack defender devices", 5, ["Para-308", "CAMRS"], ["USP40", "Super Shorty"], "Kludge Drone", ["Smoke Grenade", "Claymore"], ["Para-308"], ["Para-308"], "Attacker")
buck = Operator("Buck", "Destroy barricades with the Skeleton Key", 5, "", 0, ["C8-SFW", "CAMRS"], ["MK1 9MM"], "Skeleton Key", ["Stun Grenade", "Claymore"], ["C8-SFW"], ["C8-SFW"], "Attacker")
capitao = Operator("Capitao", "Shoot fire/smoke arrows", 16, "", 0, ["M249", "Para-308", "PMR90A2"], ["GONNE-6", "PRB92"], "Tactical Crossbow", ["Claymore", "Hard Breach Charge", "Impact EMP Grenade"], ["M249"], ["M249"], "Attacker")
castle = Operator("Castle", "Deploy Armor Panels", 16, "", 0, ["UMP45", "M1014"], ["5.7 USG", "Super Shorty", "M45 MEUSOC"], "Armor Panel", ["Proximity Alarm", "Bulletproof Camera"], ["UMP45"], ["UMP45"], "Defender")
caveira = Operator("Caveira", "Down enemies", 3, "Interrogate enemies", 2, ["M12", "SPAS-15"], ["LUSION"], "Silent Step", ["Proximity Alarm", "Impact Grenade", "Observation Blocker"], ["M12", "SPAS-15", "LUSION"], ["M12", "SPAS-15", "LUSION"], "Defender")
clash = Operator("Clash", "Shock enemies with the CCE Shield MK2", 8, "Get shock kills/assists", 2, [], ["P-10C", "SPSMG9", "Super Shorty"], "CCE Shield MK2", ["Barbed Wire", "Impact Grenade"], ["SPSMG9"], ["SPSMG9"], "Defender")
deimos = Operator("Deimos", "Deploy the Deathmark Tracker", 6, "Get kills/assists on Deathmarked enemies", 3, ["AK-74M", "M590A1"], [".44 Vendetta"], "Deathmark Tracker", ["Frag Grenade", "Hard Breach Charge"], ["AK-74M", "M90A1", ".44 Vendetta"], ["AK-74M", ".44 Vendetta"], "Attacker")
denari = Operator("Denari", "Deploy T.R.I.P. Connectors", 30, "Deal damage with T.R.I.P. Connector lasers", 3, ["Scorpion Evo 3 A1", "FMG-9"], ["Glaive-12", "P226 MK 25"], "T.R.I.P. Connector", ["Observation Blocker", "Deployable Shield"], ["Scorpion Evo A1"], ["Scorpion Evo A1"], "Defender")
doc = Operator("Doc", "Heal teammates with the Stim Pistol", 10, "Heal downed teammates", 3, ["MP5", "P90", "SG-CQB"], ["P9", "LFP586", "Bailiff 410"], "Stim Pistol", ["Bulletproof Camera", "Barbed Wire"], ["MP5", "P90"], ["MP5"], "Defender")
dokkaebi = Operator("Dokkaebi", "Call enemy operators", 6, "Deal damage with the Jegeo Payload or hack cameras", 2, ["BOSG. 12.2", "MK 14 EBR", "XK23"], ["GONNE-6", "SMG-12", "C75-Auto"], "Jegeo Payload", ["Smoke Grenade", "Impact EMP Grenade"], ["XK23"], ["XK23"], "Attacker")
echo = Operator("Echo", "Use the Yokai's disruptor", 10, "Interrupt defuser planting", 2, ["MP5SD", "SuperNova"], ["Bearing 9", "P229"], "Yokai", ["Impact Grenade", "Deployable Shield"], ["MP5SD", "SuperNova"], ["MP5SD"], "Defender")
ela = Operator("Ela", "Deploy Grzmot mines", 7, "Get Grzmot mine kills/assists", 2, ["Scorpion Evo 3 A1", "FO-12"], ["RG15"], "GRZMOT Mine", ["Barbed Wire", "Deployable Shield", "Impact Grenade"], ["Scorpion Evo A1"], ["Scorpion Evo A1"], "Defender")
fenrir = Operator("Fenrir", "Deploy F-NATT Dread Mines", 10, "Get kills/assists with the F-NATT Dread Mine", 2, ["MP7", "SASG-12"], ["5.7 USG"], "F-NATT Dread Mine", ["Bulletproof Camera", "Observation Blocker"], ["MP7"], ["MP7"], "Defender")
finka = Operator("Finka", "Use Adrenal Surges", 10, "Revive downed teammates", 1, ["6P41", "SASG-12", "Spear .308"], ["GSH-18", "PMM"], "Adrenal Surge", ["Frag Grenade", "Smoke Grenade", "Stun Grenade"], ["6P41", "Spear .308"], ["Spear .308"], "Attacker")
flores = Operator("Flores", "Deploy RCE-Ratero Charges", 10, "Destroy defender gadgets", 4, ["AR33", "SR-25", "T-95 LSW"], ["GSH-18"], "RCE-Ratero Charge", ["Stun Grenade", "Claymore"], ["AR33", "SR-25", "T-95 LSW"], ["AR33", "T-95LSW"], "Attacker")
frost = Operator("Frost", "Deploy Welcome Mats", 9, "Trigger a Welcome Mat", 1, ["Super 90", "9mm C1"], ["MK1 9mm", "ITA12S"], "Welcome Mat", ["Bulletproof Camera", "Deployable Shield"], ["9mm C1"], ["9mm C1"], "Defender")
fuze = Operator("Fuze", "Activate Cluster Charges", 10, "Destroy defender gadgets or kill defenders", 4, ["AK-12", "6P41", "Ballistic Shield"], ["PMM", "GSH-18"], "Cluster Charge", ["Breach Charge", "Hard Breach Charge", "Smoke Grenade"], ["AK-12", "6P41"], ["AK-12"], "Attacker")
glaz = Operator("Glaz", "Throw Smoke Grenades", 10, "Get kills through smoke or other vision blockers", 3, ["OTS-03"], ["PMM", "GONNE-6", "Bearing 9"], "Flip Sight", ["Smoke Grenade", "Frag Grenade", "Claymore"], ["OTS-03"], ["OTS-03"], "Attacker")
goyo = Operator("Goyo", "Deploy Volcan Canisters", 20, "Trigger canisters", 10, ["Vector .45 ACP", "TCSG12"], ["P229"], "Volcan Canister", ["Proximity Alarm", "Bulletproof Camera", "Impact Grenade"], ["Vector .45 ACP", "TCSG12"], ["Vector .45 ACP"], "Defender")
gridlock = Operator("Gridlock", "Deploy Trax Stingers", 9, "Get Trax Stinger kills/assists", 1, ["F90", "M245 SAW"], ["Super Shorty", "SDP9mm"], "Trax Stingers", ["Smoke Grenade", "Frag Grenade", "Impact EMP Grenade"], ["F90", "M245 SAW"], ["F90"], "Attacker")
grim = Operator("Grim", "Shoot the Kawan Hive Launcher", 10, "Ping enemies with the Kawan Hive Launcher", 2, ["552 Commando", "SG-CQB"], ["Bailiff 410", "P229"], "Kawan Hive Launcher", ["Claymore", "Hard Breach Charge", "Impact EMP Grenade"], ["552 Commando"], ["552 Commando"], "Attacker")
hibana = Operator("Hibana", "Detonate X-Kairos Charges", 30, "", 0, ["SuperNova", "Type-89", "PMR90A2"], ["Bearing 9", "P229"], "X-Kairos", ["Breach Charge", "Stun Grenade", "Claymore"], ["Type-89", "SuperNova"], ["Type-89"], "Attacker")
iana = Operator("Iana", "Use the Gemini Replicator", 5, "", 0, ["ARX200", "G36C"], ["GONNE-6", "MK1 9mm"], "Gemini Replicator", ["Impact EMP Grenade", "Smoke Grenade"], ["ARX200", "G36C"], ["ARX200", "G36C"], "Attacker")
iq = Operator("IQ", "Get Electronics Detector assists", 3, "Destroy detected devices", 3, ["AUG A2", "552 Commando", "G8A1"], ["P12"], "Electronics Detector", ["Breach Charge", "Frag Grenade", "Claymore"], ["AUG A2", "G8A1"], ["AUG A2", "G8A1"], "Attacker")
jackal = Operator("Jackal", "Detect footsteps with the Eyenox Model III", 2, "Get footstep detection kills/assists", 1, ["C7E", "PDW9", "ITA12L"], ["USP40", "ITA12S"], "Eyenox Model III", ["Smoke Grenade", "Claymore"], ["C7E", "PDW9"], ["C7E", "PDW9"], "Attacker")
jager = Operator("Jager", "Deploy Active Defense Systems", 15, "Catch projectiles with the ADS", 4, ["M870", "416-C Carbine"], ["P12", "P-10C"], "Active Defense", ["Bulletproof Camera", "Observation Blocker"], ["416-C Carbine"], ["416-C Carbine"], "Defender")
kaid = Operator("Kaid", "Electrify walls", 10, "", 0, ["AUG A3", "TCSG12"], [".44 Mag Semi-Auto", "LFP586"], "Rtila Electroclaw", ["Barbed Wire", "Nitro Cell", "Observation Blocker"], ["AUG A3", "TCSG12"], ["TCSG12"], "Defender")
kali = Operator("Kali", "Fire the LV Explosive Lance", 12, "De-electify walls", 2, ["CSRX 300"], ["SPSMG9", "C75 Auto", "P226 MK 25"], "LV Explosive Lance", ["Breach Charge", "Claymore", "Smoke Grenade"], ["CSRX 300", "SPSMG9"], ["CSRX 300", "SPSMG9"], "Attacker")
kapkan = Operator("Kapkan", "Deploy the Entry Denial Device", 1, "Get EDD kills/assists", 1, ["9x19VSN", "SASG-12"], ["PMM GSH-18"], "Entry Denial Device", ["Barbed Wire", "Bulletproof Camera"], ["9x19VSN"], ["9x19VSN"], "Defender")
lesion = Operator("Lesion", "Deploy Gu Mines", 20, "Get Gu Mine kills/assists", 5, ["SIX12 SD", "T-5 SMG"], ["Q-929"], "Gu", ["Observation Blocker", "Bulletproof Camera"], ["T-5 SMG"], ["T-5 SMG"], "Defender")
lion = Operator("Lion", "Use the EE-ONE-D's scan", 10, "Detect enemies with the EE-ONE-D", 2, ["417", "SG-C1B", "V308"], ["LFP589", "P9"], "EE-ONE-D", ["Claymore", "Frag Grenade", "Stun Grenade"], ["V308"], ["V308"], "Attacker")
maestro = Operator("Maestro", "Deploy Evil Eyes", 15, "Get Evil Eye kills/assists", 2, ["ALDA 5.56", "ACS12"], ["Keratos .357", "Bailiff 410"], "Evil Eye", ["Barbed Wire", "Impact Grenade", "Observation Blocker"], ["ALDA 5.56"], ["ALDA 5.56"], "Defender")
maverick = Operator("Maverick", "Make holes using the Breaching Torch", 10, "Get kills through Breaching Torch holes", 2, ["M4", "AR-15.50"], ["1911 TACOPS", "Reaper MK2"], "Breaching Torch", ["Claymore", "Stun Grenade", "Frag Grenade"], ["M4"], ["M4"], "Attacker")
melusi = Operator("Melusi", "Deploy Banshee Sonic Defenses", 20, "Get Banshee Sonic Defense kills/assists", 3, ["MP5", "Super 90"], ["ITA12S", "RG15"], "Banshee Sonic Defense", ["Bulletproof Camera", "Impact Grenade"], ["MP5"], ["MP5"], "Defender")
mira = Operator("Mira", "Deploy Black Mirrors", 10, "", 0, ["Vector .45 ACP", "ITA12L"], ["ITA12S", "UG40"], "Black Mirror", ["Nitro Cell", "Proximity Alarm"], ["Vector .45 ACP"], ["Vector .45 ACP"], "Defender")
montagne = Operator("Montagne", "Get Le Roc Shield score events", 15, "Defusers planted", 2, [], ["P9", "LFP586"], "Le Roc Shield", ["Impact EMP Grenade", "Smoke Grenade", "Hard Breach Charge"], ["P9", "LFP586"], ["P9", "LFP586"], "Attacker")
mozzie = Operator("Mozzie", "Shoot the Pest Launcher", 20, "Hack drones or get drone scan assists", 5, ["Commando 9", "P10 Roni"], ["SDP 90mm", "Super Shorty"], "Pest Launcher", ["Barbed Wire", "Nitro Cell", "Impact Grenade"], ["Commando 9"], ["Commando 9"], "Defender")
mute = Operator("Mute", "Deploy Signal Disruptors", 20, "Disable devices", 3, ["M590A1", "MP5K"], ["SMG11", "P226 MK 25"], "Signal Disruptor", ["Nitro Cell", "Bulletproof Camera"], ["M590A1", "MP5K", "SMG11"], ["M590A1", "SMG11"], "Defender")
nokk = Operator("Nokk", "Use Hel Presence Reduction", 10, "", 0, ["FMG-9", "SIX12 SD", "PMR90A2"], ["5.7 USG", "D-50"], "HEL Presence Reduction", ["Impact EMP Grenade", "Hard Breach Charge", "Frag Grenade"], ["FMG-9", "SIX12 SD", "PMR90A2"], ["FMG-9"], "Attacker")
nomad = Operator("Nomad", "Launch Airjabs", 8, "Get Airjab kills/assists", 3, ["AK-74M", "ARX200"], ["PRB92", ".44 Mag Semi-Auto"], "Airjab Launcher", ["Breach Charge", "Stun Grenade"], ["AK-74M"], ["AK-74M"], "Attacker")
noor = Operator("Noor", "Activate the Horus Lance", 12, "", 0, ["Commando 9", "ALDA 5.56"], ["1911 TACOPS", "Bailiff 410"], "Horus Lance Launcher", ["Deployable Shield", "Barbed Wire"], ["Commando 9", "ALDA 5.56"], ["Commando 9"], "Defender")
oryx = Operator("Oryx", "Use the Remah Dash", 20, "", 0, ["T-5 SMG", "SPAS-12"], ["USP40", "Bailiff 410", "Reaper MK2"], "Remah Dash", ["Barbed Wire", "Proximity Alarm"], ["T-5 SMG"], ["T-5 SMG"], "Defender")
osa = Operator("Osa", "Set the Talon-8 Shield down on a surface", 3, "", 0, ["556xi", "PDW9"], ["PMM"], "Talon-8 Shield", ["Claymore", "Frag Grenade", "Impact EMP Grenade"], ["556xi", "PDW9"], ["556xi", "PDW9"], "Attacker")
pulse = Operator("Pulse", "Detect enemies with the Cardiac Sensor", 4, "Get Cardiac Sensor kills/assists", 2, ["UMP45", "M1014"], ["Reaper MK2", "5.7 USG", "M45 MEUSOC"], "Cardiac Sensor", ["Nitro Cell", "Deployable Shield", "Observation Blocker"], ["UMP45"], ["UMP45"], "Defender")
ram = Operator("Ram", "Deploy BU-GI Auto-Breachers", 10, "", 0, ["R4-C, LMG-E"], ["MK1 9mm"], "BU-GI Auto-Breacher", ["Stun Grenade", "Smoke Grenade"], ["R4-C"], ["R4-C"], "Attacker")
rauora = Operator("Rauora", "Launch D.O.M. Panels", 10, "Secure a defuser plant", 2, ["XK23", "417", "M249"], ["Reaper MK2", "GSH-18"], "D.O.M. Panel Launcher", ["Smoke Grenade", "Breach Charge"], ["XK23"], ["XK23"], "Attacker")
rook = Operator("Rook", "Put down the Armor Pack", 5, "", 0, ["MP5", "P90", "SG-CQB"], ["LFP586", "P9", "Reaper MK2"], "Armor Pack", ["Proximity Alarm", "Impact Grenade", "Nitro Cell"], ["MP5", "P90"], ["MP5", "P90"], "Defender")
sens = Operator("Sens", "Throw R.O.U. Projectors", 10, "Secure a defuser plant", 2, ["POF-9", "XK23", "417"], ["SDP 9mm"], "R.O.U. Projector System", ["Frag Grenade", "Hard Breach Charge", "Claymore"], ["POF-9", "XK23"], ["POF-9", "XK23"], "Attacker")
sentry = Operator("Sentry", "Deploy Barbed Wire, Bulletproof Cameras, Deployable Shields, Observation Blockers, or Proximity Alarms", 15, "Get kills with Nitro Cells or Impact Grenades, or get Bulletproof Camera Scan Assists.", 3, ["Commando 9", "M870", "TCSG12"], ["C75 Auto", "Super Shorty"], "Gadget Kit", ["Barbed Wire", "Bulletproof Camera", "Deployable Shield", "Observation Blocker", "Impact Grenade", "Nitro Cell", "Proximity Alarm"], ["Commando 9", "TCSG12"], ["TCSG12"], "Defender")
skopos = Operator("Skopos", "Switch between the v10 Pantheon Shells", 8, "Get scan assists with the observation shell", 2, ["PCX-33"], ["P229"], "v10 Pantheon Shells", ["Impact Grenade", "Proximity Alarm"], ["PCX-33"], ["PCX-33"], "Defender")
sledge = Operator("Sledge", "Destroy Barricades", 10, "", 0, ["L85A2", "M590A1"], ["Reaper MK2", "P226 MK 15"], "Breaching Hammer", ["Frag Grenade", "Stun Grenade", "Impact EMP Grenade"], ["L85A2"], ["L85A2"], "Attacker")
smoke = Operator("Smoke", "Deploy Gas Canisters", 10, "", 0, ["M590A1", "FMG-9"], ["SMG11", "P226 MK 15"], "Remote Gas Grenade", ["Barbed Wire", "Proximity Alarm", "Deployable Shield"], ["M590A1", "SMG11"], ["M590A1", "SMG11"], "Defender")
solidsnake = Operator("Solid Snake", "Scan enemies with the Soliton Rader MK III", 10, "Get Soliton Radar Assists", 3, ["F2", "PMR90A2"], ["TACIT .45"], "Soliton Radar MK III", ["Frag Grenade", "Stun Grenade", "Impact EMP Grenade", "Smoke Grenade", "Breach Charge"], ["F2"], ["F2"], "Attacker")
solis = Operator("Solis", "Detect electronics with the SPEC-IO Electro Sensor", 10, "Identify electronics with the overclock", 3, ["P90", "ITA12L"], ["SMG-11"], "SPEC-IO Electro-Sensor", ["Proximity Alarm", "Impact Grenade"], ["P90, SMG11"], ["P90", "SMG11"], "Defender")
striker = Operator("Striker", "Deploy Breach Charges, Claymores, or Hard Breach Charges", 8, "", 0, ["M4", "M249", "SR-25"], ["ITA12S", "5.7 USG"], "Gadget Kit", ["Breach Charge", "Claymore", "Frag Grenade", "Hard Breach Charge", "Smoke Grenade", "Stun Grenade"], ["M4"], ["M4"], "Attacker")
tachanka = Operator("Tachanka", "Fire the Shumikha Launcher", 20, "Get kills with the Shumikha Launcher", 2, ["DP27", "9x19VSN"], ["Bearing 9", "PMM", "GSH-18"], "Shumikha Launcher", ["Barbed Wire", "Deployable Shield", "Proximity Alarm"], ["DP27"], ["DP27"], "Defender")
thatcher = Operator("Thatcher", "Disable Electronics", 15, "", 1, ["L85A2", "AR33", "PMR90A2", "M590A1"], ["P226 MK 25"], "E.G.S. Disruptor", ["Claymore", "Breach Charge"], ["L85A2", "AR33"], ["L85A2", "AR33"], "Attacker")
thermite = Operator("Thermite", "Destroy walls with Exothermic Charges", 5, "Secure a defuser plant", 1, ["556xi", "M1014"], ["M45 MEUSOC", "5.7 USG", "ITA12S"], "Exothermic Charge", ["Smoke Grenade", "Stun Grenade"], ["556xi"], ["556xi"], "Attacker")
thorn = Operator("Thorn", "Throw Razorbloom Shells", 15, "Get Razorbloom Shell kills/assists", 2, ["UZK50GI", "M870"], ["C75 Auto", "1911 TACOPS"], "Razorbloom Shell", ["Deployable Shield", "Barbed Wire"], ["UZK50GI"], ["UZK50GI"], "Defender")
thunderbird = Operator("Thunderbird", "Deploy Kona Stations", 10, "Heal allies", 10, ["Spear .308", "SPAS-15"], ["Bearing 9","ITA12S", "Q-929"], "Kona Station", ["Deployable Shield", "Barbed Wire", "Bulletproof Camera"], ["Spear .308", "SPAS-15"], ["Spear .308"], "Defender")
tubarao = Operator("Tubarao", "Deploy Frost Canisters", 10, "Deny breaches or slow down enemies", 1, ["MPX", "AR15.50"], ["P226 MK 25"], "Zoto Canister", ["Nitro Cell", "Proximity Alarm"], ["MPX", "AR15.50"], ["MPX", "AR15.50"], "Defender")
twitch = Operator("Twitch", "Destroy defender devices with the Shock Drone", 15, "Get scan assists or destroy Electroclaws", 3, ["F2", "417", "SG-QCB"], ["P9", "LFP586"], "Shock Drone", ["Claymore", "Smoke Grenade"], ["F2"], ["F2"], "Attacker")
valkyrie = Operator("Valkyrie", "Deploy Black Eye cameras", 15, "Get scan assists", 3, ["MPX", "SPAS-12"], ["D-50"], "Black Eye", ["Impact Grenade", "Nitro Cell"], ["MPX"], ["MPX"], "Defender")
vigil = Operator("Vigil", "Use the ERC-7", 15, "Dodge scans", 7, ["K1A", "BOSG. 12.2"], ["C75-Auto", "SMG-12"], "ERC-7", ["Impact Grenade", "Bulletproof Camera"], ["K1A", "BOSG. 12.2, SMG-12"], ["BOSG. 12.2", "SMG-12"], "Defender")
wamai = Operator("Wamai", "Throw MAG-NET systems", 25, "Capture projectiles", 8, ["AUG A12", "MP5K"], ["Keratos .357", "P12", "Super Shorty"], "MAG-NET System", ["Deployable Shield", "Proximity Alarm", "Nitro Cell"], ["AUG A12"], ["AUG A12"], "Defender")
warden = Operator("Warden", "Use the Glance Smart Glasses", 15, "Get kills through flashbangs or smoke grenades", 2, ["M590A1", "MPX"], ["SMG12", "P-10C"], "Glance Smart Glasses", ["Deployable Shield", "Nitro Cell", "Observation Blocker"], ["M590A1", "MPX", "SMG12"], ["M590A1", "MPX", "SMG12"], "Defender")
ying = Operator("Ying", "Use Candelas", 15, "Get Candela kills/assists", 2, ["T-95 LSW", "SIX12"], ["Q-929", "Reaper MK2"], "Candela", ["Hard Breach Charge", "Smoke Grenade"], ["T-95 LSW"], ["T-95 LSW"], "Attacker")
zero = Operator("Zero", "Use the Argus Launcher", 15, "Get scan assists", 2, ["SC3000K", "MP7"], ["5.7 USG", "GONNE-6"], "Argus Launcher", ["Hard Breach Charge", "Claymore"], ["SC3000K", "MP7"], ["SC3000K", "MP7"], "Attacker")
zofia = Operator("Zofia", "Fire grenades", 15, "Get flashbang kills/assists", 2, ["M762", "LMG-E"], ["RG15"], "KS79 Lifeline", ["Hard Breach Charge", "Claymore"], ["M762"], ["M762"], "Attacker")

operators = [ace, alibi, amaru, aruni, ash, azami, bandit, blackbeard, blitz, brava, buck, capitao, castle, caveira, clash,
             deimos, denari, doc, dokkaebi, echo, ela, fenrir, finka, flores, frost, fuze, glaz, goyo, gridlock, grim,
             hibana, iana, iq, jackal, jager, kaid, kali, kapkan, lesion, lion, maestro, maverick, melusi, mira, montagne,
             mozzie, mute, nokk, nomad, noor, oryx, osa, pulse, ram, rauora, rook, sens, sentry, skopos, sledge, smoke,
             solidsnake, solis, striker, tachanka, thatcher, thermite, thorn, thunderbird, tubarao, twitch, valkyrie,
             vigil, wamai, warden, ying, zero, zofia]