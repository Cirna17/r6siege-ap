from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, OptionSet, OptionDict, OptionGroup, PerGameCommonOptions, OptionError
from schema import Schema, Optional
import logging

if TYPE_CHECKING:
    from .world import R6SiegeWorld as R6SiegeWorld
    

OPERATORS = 78
WEAPONS = 116
GADGETS = 13

challenges_schema = Schema({
    str: [str, int, Optional(list[str])]
})

weapons_schema = Schema({
    str: list[str],
})

class GoalOperators(Range):
    """
    The amount of operators you need to complete all objectives for to goal.
    """

    display_name = "Goal Operators"

    range_start = 1
    range_end = OPERATORS
    default = 10

class StartingOperators(Range):
    """
    The amount of random operators you'll start with.
    """

    display_name = "Starting Operators"

    range_start = 1
    range_end = OPERATORS
    default = 2

class StartingOperatorBalancing(Choice):
    """
    Balances the side of your starting operators if you have more than 1.
    Light: Gives you at least 1 attacker and 1 defender.
    Heavy: Tries to have the number of attackers and defenders as even as possible.
    NOTE: balancing occurs after the operator pool is made, so it may fail if the pool
    has little or no attackers or defenders.
    """

    display_name = "Starting Operator Balancing"

    option_light = 0
    option_heavy = 1
    option_disabled = 2

    default = option_light

class ExtraOperators(Range):
    """
    The amount of extra operators in the pool along with your goal operators.
    Your goal operators + extra operators can't be more than your allowed operators.
    """

    display_name = "Extra Operators"

    range_start = 0
    range_end = OPERATORS - 1
    default = 2

class AllowedOperators(OptionSet):
    """
    The operators that can be randomly added into the pool.
    Remove any you haven't bought or don't want to play as.
    """

    display_name = "Allowed Operators"

    valid_keys = ["Ace", "Alibi", "Amaru", "Aruni", "Ash", "Azami", "Bandit", "Blackbeard", "Blitz",
                  "Brava", "Buck", "Capitao", "Castle", "Caveira", "Clash", "Deimos", "Denari",
                  "Doc", "Dokkaebi", "Echo", "Ela", "Fenrir", "Finka", "Flores", "Frost", "Fuze",
                  "Glaz", "Goyo", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Jager",
                  "Kaid", "Kali", "Kapkan", "Lesion", "Lion", "Maestro", "Maverick", "Melusi", "Mira",
                  "Montagne", "Mozzie", "Mute", "Nokk", "Nomad", "Noor", "Oryx", "Osa", "Pulse", "Ram",
                  "Rauora", "Rook", "Sens", "Sentry", "Skopos", "Sledge", "Smoke", "Solid Snake", "Solis",
                  "Striker", "Tachanka", "Thatcher", "Thermite", "Thorn", "Thunderbird", "Tubarao",
                  "Twitch", "Valkyrie", "Vigil", "Wamai", "Warden", "Ying", "Zero", "Zofia"]

    default = ["Ace", "Alibi", "Amaru", "Aruni", "Ash", "Azami", "Bandit", "Blackbeard", "Blitz",
                  "Brava", "Buck", "Capitao", "Castle", "Caveira", "Clash", "Deimos", "Denari",
                  "Doc", "Dokkaebi", "Echo", "Ela", "Fenrir", "Finka", "Flores", "Frost", "Fuze",
                  "Glaz", "Goyo", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Jager",
                  "Kaid", "Kali", "Kapkan", "Lesion", "Lion", "Maestro", "Maverick", "Melusi", "Mira",
                  "Montagne", "Mozzie", "Mute", "Nokk", "Nomad", "Noor", "Oryx", "Osa", "Pulse", "Ram",
                  "Rauora", "Rook", "Sens", "Sentry", "Skopos", "Sledge", "Smoke", "Solid Snake", "Solis",
                  "Striker", "Tachanka", "Thatcher", "Thermite", "Thorn", "Thunderbird", "Tubarao",
                  "Twitch", "Valkyrie", "Vigil", "Wamai", "Warden", "Ying", "Zero", "Zofia"]
    
class ForcedSelectedOperators(OptionSet):
    """
    These operators will be added into the pool.
    For each operator here, 1 less operator will be randomly chosen.
    """
    
    display_name = "Forced Selected Operators"
    
    valid_keys = ["Ace", "Alibi", "Amaru", "Aruni", "Ash", "Azami", "Bandit", "Blackbeard", "Blitz",
                    "Brava", "Buck", "Capitao", "Castle", "Caveira", "Clash", "Deimos", "Denari",
                    "Doc", "Dokkaebi", "Echo", "Ela", "Fenrir", "Finka", "Flores", "Frost", "Fuze",
                    "Glaz", "Goyo", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Jager",
                    "Kaid", "Kali", "Kapkan", "Lesion", "Lion", "Maestro", "Maverick", "Melusi", "Mira",
                    "Montagne", "Mozzie", "Mute", "Nokk", "Nomad", "Noor", "Oryx", "Osa", "Pulse", "Ram",
                    "Rauora", "Rook", "Sens", "Sentry", "Skopos", "Sledge", "Smoke", "Solid Snake", "Solis",
                    "Striker", "Tachanka", "Thatcher", "Thermite", "Thorn", "Thunderbird", "Tubarao",
                    "Twitch", "Valkyrie", "Vigil", "Wamai", "Warden", "Ying", "Zero", "Zofia"]
    
    default = []
    
class ForcedStartingOperators(OptionSet):
    """
    These operators will be part of your starting operators.
    For each operator here, 1 less operator will be randomly chosen as a starter.
    """
    
    display_name = "Forced Starting Operators"
    
    valid_keys = ["Ace", "Alibi", "Amaru", "Aruni", "Ash", "Azami", "Bandit", "Blackbeard", "Blitz",
                    "Brava", "Buck", "Capitao", "Castle", "Caveira", "Clash", "Deimos", "Denari",
                    "Doc", "Dokkaebi", "Echo", "Ela", "Fenrir", "Finka", "Flores", "Frost", "Fuze",
                    "Glaz", "Goyo", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Jager",
                    "Kaid", "Kali", "Kapkan", "Lesion", "Lion", "Maestro", "Maverick", "Melusi", "Mira",
                    "Montagne", "Mozzie", "Mute", "Nokk", "Nomad", "Noor", "Oryx", "Osa", "Pulse", "Ram",
                    "Rauora", "Rook", "Sens", "Sentry", "Skopos", "Sledge", "Smoke", "Solid Snake", "Solis",
                    "Striker", "Tachanka", "Thatcher", "Thermite", "Thorn", "Thunderbird", "Tubarao",
                    "Twitch", "Valkyrie", "Vigil", "Wamai", "Warden", "Ying", "Zero", "Zofia"]
    
    default = []

class KillThreshold(DefaultOnToggle):
    """
    Gives each operator an amount of kills to get to be completed.
    """

    display_name = "Kill Threshold"

class KillThresholdAmount(Range):
    """
    The amount of kills to fill the threshold.
    It's recommended to set it to the amount of kills you think you'll get in about 5 rounds.
    """

    display_name = "Kill Threshold Amount"

    range_start = 1
    range_end = 100
    default = 5

class KillThresholdValue(Range):
    """
    The number of checks sent out when you fulfill a kill threshold.
    """

    display_name = "Kill Threshold Value"

    range_start = 1
    range_end = 10
    default = 1

class KillThresholdAssists(DefaultOnToggle):
    """
    Changes whether or not assists count for the kill threshold.
    Only changes the text in the client. No effect on logic.
    """

    display_name = "Kill Threshold Assists"

class GlobalKillCounter(Toggle):
    """
    Adds a required amount of kills to get across all operators.
    """

    display_name = "Global Kill Counter"

class GlobalKillCounterCount(Range):
    """
    The amount of kills to fill the global kill counter.
    It's recommended to set this to your kill threshold per operator times 5.
    """

    display_name = "Global Kill Counter Count"

    range_start = 1
    range_end = 1000
    default = 25

class GlobalKillCounterReward(Choice):
    """
    The reward for filling the global kill counter.
    Required to goal: filling the counter is required to complete the game.
    Checks: filling the counter gives out checks.
    """

    display_name = "Global Kill Counter Reward"

    option_required_to_goal = 0
    option_checks = 1

    default = option_required_to_goal

class GlobalKillCounterValue(Range):
    """
    If the reward for filling the global kill counter is checks,
    this is the amount of checks it will send.
    """

    display_name = "Global Kill Counter Value"

    range_start = 1
    range_end = 100
    default = 5

class GlobalKillCounterLogic(Range):
    """
    If the reward for filling the global kill counter is checks,
    this is how many operators you're expected to complete before those checks are in logic.
    It's recommended to set this to half of your goal operators.
    """

    display_name = "Global Kill Counter Logic"

    range_start = 0
    range_end = OPERATORS - 1
    default = 5

class GlobalKillCounterKillThresholdBehavior(Choice):
    """
    How operator kill threshold kills get added to the global kill counter.
    Kills: per-operator kills are automatically added to the global kills.
    Kills and threshold: operator kills are automatically added to the global kills and the global required kills.
    Disabled: operator kills do not automatically affect the global kill counter.
    """

    display_name = "Global Kill Counter & Operator Kill Threshold Behavior"

    option_kills = 0
    option_kills_and_threshold = 1
    option_disabled = 2

    default = option_kills_and_threshold

class EasyChallenges(DefaultOnToggle):
    """
    Gives each operator an easy challenge to complete.
    Easy challenges are things that an operator does during their normal gameplay loop (ex. deploying their gadget).
    """

    display_name = "Easy Challenges"
    
class EasyChallengesChallenges(OptionDict):
    """
    The easy challenge every operator has.
    The text is the challenge, and the number is how many times you'll do that objective before it's completed.
    Blank text and a 0 means that the challenge is disabled.
    The entries under Striker and Sentry are the gadgets you'll need to complete their challenge.
    Feel free to scroll past if you want to stick with the default challenges.
    """
    
    display_name = "Easy Challenges: Challenges"
    
    schema = challenges_schema
    
    default = {"Ace": ["Deploy S.E.L.M.A. Aqua Breachers", 10], 
               "Alibi": ["Deploy Prisma Clones", 15], 
               "Amaru": ["Use the Garra Hook", 3], 
               "Aruni": ["Deploy Surya Laser Gates", 10], 
               "Ash": ["Use Breaching Rounds", 10], 
               "Azami": ["Deploy Kiba Barriers", 10], 
               "Bandit": ["Deploy Shock Wires", 16], 
               "Blackbeard": ["Use the breach on the H.U.L.L. Adaptable Shield", 5], 
               "Blitz": ["Flash enemies with the G-52 Tactical Shield", 5], 
               "Brava": ["Hack cameras with the Kludge Drone", 5], 
               "Buck": ["Destroy barricades with the Skeleton Key", 5], 
               "Capitao": ["Shoot fire/smoke arrows", 16], 
               "Castle": ["Deploy Armor Panels", 16], 
               "Caveira": ["Down enemies", 3], 
               "Clash": ["Shock enemies with the CCE Shield MK2", 8], 
               "Deimos": ["Deploy the Deathmark Tracker", 6], 
               "Denari": ["Deploy T.R.I.P. Connectors", 30], 
               "Doc": ["Heal teammates with the Stim Pistol", 10], 
               "Dokkaebi": ["Call enemies", 6], 
               "Echo": ["Use the Yokai's disruptor", 10], 
               "Ela": ["Deploy GRZMOT Mines", 7], 
               "Fenrir": ["Deploy F-NATT Dread Mines", 10], 
               "Finka": ["Use Adrenal Surges", 10], 
               "Flores": ["Deploy RCE-Ratero Charges", 10], 
               "Frost": ["Deploy Welcome Mats", 9], 
               "Fuze": ["Activate Cluster Charges", 10], 
               "Glaz": ["Throw Smoke Grenades", 10], 
               "Goyo": ["Deploy Volcan Canisters", 20], 
               "Gridlock": ["Deploy Trax Stingers", 9], 
               "Grim": ["Shoot the Kawan Hive Launcher", 10], 
               "Hibana": ["Detonate X-Kairos Charges", 30], 
               "Iana": ["Use the Gemini Replicator", 5], 
               "IQ": ["Ping electronics", 3], 
               "Jackal": ["Detect footsteps with the Eyenox Model III", 2], 
               "Jager": ["Deploy Active Defense Systems", 15], 
               "Kaid": ["Electrify walls", 10], 
               "Kali": ["Fire the LV Explosive Lance", 12], 
               "Kapkan": ["Deploy Entry Denial Devices", 25], 
               "Lesion": ["Deploy Gu Mines", 20], 
               "Lion": ["Use the EE-ONE-D's scan", 10], 
               "Maestro": ["Deploy Evil Eyes", 15], 
               "Maverick": ["Make holes using the Breaching Torch", 10], 
               "Melusi": ["Deploy Banshees", 20], 
               "Mira": ["Deploy Black Mirrors", 10], 
               "Montagne": ["Get Le Roc Shield score events", 10], 
               "Mozzie": ["Shoot the Pest Launcher", 20], 
               "Mute": ["Deploy Signal Disruptors", 20], 
               "Nokk": ["Use the Hel Presence Reduction", 10], 
               "Nomad": ["Launch Airjabs", 8], 
               "Noor": ["Activate the Horus Lance", 12], 
               "Oryx": ["Use the Remah Dash", 20], 
               "Osa": ["Set the Talon-8 Shield down on a surface", 3], 
               "Pulse": ["Detect enemies with the Cardiac Sensor", 4], 
               "Ram": ["Deploy BU-GI Auto-Breachers", 10], 
               "Rauora": ["Launch D.O.M. Panels", 10], 
               "Rook": ["Put down the Armor Pack", 5], 
               "Sens": ["Throw R.O.U. Projectors", 10], 
               "Sentry": ["Deploy Barbed Wire, Bulletproof Cameras, Deployable Shields, Observation Blockers, or Proximity Alarms", 15, ["Barbed Wire", "Bulletproof Camera", "Deployable Shield", "Observation Blocker"]], 
               "Skopos": ["Switch between the V10 Pantheon Shells", 8], 
               "Sledge": ["Destroy barricades or walls", 10], 
               "Smoke": ["Deploy Gas Canisters", 10], 
               "Solid Snake": ["Scan enemies with the Soliton Radar MK III", 10], 
               "Solis": ["Detect electronics with the SPEC-IO Electro Sensor", 10], 
               "Striker": ["Deploy Breach Charges, Claymores, or Hard Breach Charges", 8, ["Breach Charge", "Claymore", "Hard Breach Charge"]], 
               "Tachanka": ["Fire the Shumikha Launcher", 20], 
               "Thatcher": ["Disable electronics", 15], 
               "Thermite": ["Destroy walls with Exothermic Charges", 5], 
               "Thorn": ["Throw Razorbloom Shells", 15], 
               "Thunderbird": ["Deploy Kona Stations", 10], 
               "Tubarao": ["Deploy Frost Canisters", 10], 
               "Twitch": ["Destroy cameras with the Shock Drone", 15], 
               "Valkyrie": ["Deploy Black Eye Cameras", 15], 
               "Vigil": ["Use the ERC-7", 15], 
               "Wamai": ["Throw MAG-NET systems", 25], 
               "Warden": ["Use the Glance Smart Glasses", 15], 
               "Ying": ["Use Candelas", 15], 
               "Zero": ["Use the Argus Launcher", 15], 
               "Zofia": ["Fire grenades", 15]}

class EasyChallengeMultiplier(Range):
    """
    Multiplies the threshold for completing easy challenges, making them longer.
    As an example, if you had to deploy your gadget 5 times, a 2 multiplier would make it 10 times.
    Easy challenges should be completed in about 5 rounds of play.
    """

    display_name = "Easy Challenge Multiplier"

    range_start = 1
    range_end = 10
    default = 1

class EasyChallengeValue(Range):
    """
    The number of checks sent out when you complete an easy challenge.
    """

    display_name = "Easy Challenge Value"

    range_start = 1
    range_end = 10
    default = 1

class HardChallenges(DefaultOnToggle):
    """
    Gives each operator a hard challenge to complete.
    Hard challenges are things an operator should try to be doing during their normal gameplay
    loop, but may not always succeed (ex. getting kills/assists with their gadget).
    Hard challenges should be completed in about 5 rounds of play.
    Not all operators have hard challenges.
    """

    display_name = "Hard Challenges"
    
class HardChallengesChallenges(OptionDict):
    """
    The hard challenge every operator has.
    The text is the challenge, and the number is how many times you'll do that objective before it's completed.
    Blank text and a 0 means that the challenge is disabled.
    The entries under Striker and Sentry are the gadgets you'll need to complete their challenge.
    Feel free to scroll past if you want to stick with the default challenges.
    """
    
    display_name = "Hard Challenges: Challenges"
    
    schema = weapons_schema
    
    default = {"Ace": ["", 0], 
               "Alibi": ["Trick enemies with Prisma Clones", 2], 
               "Amaru": ["", 0], 
               "Aruni": ["Destroy devices with Surya gates or reactivate gates", 4], 
               "Ash": ["", 0], "Azami": ["", 0], 
               "Bandit": ["Re-electrify walls", 3], 
               "Blackbeard": ["", 0], 
               "Blitz": ["Get flash assist kills", 2], 
               "Brava": ["Hack defender devices", 5], 
               "Buck": ["Destroy barricades with the Skeleton Key", 5], 
               "Capitao": ["", 0], 
               "Castle": ["", 0], 
               "Caveira": ["Interrogate enemies", 2], 
               "Clash": ["Get shock kills/assists", 2], 
               "Deimos": ["Get kills/assists on Deathmarked enemies", 3], 
               "Denari": ["Deal damage with T.R.I.P. Connector lasers", 3], 
               "Doc": ["Heal downed teammates", 3], 
               "Dokkaebi": ["Deal damage with the Jegeo Payload or hack cameras", 2], 
               "Echo": ["Interrupt defuser planting", 2], 
               "Ela": ["Get GRZMOT mine kills/assists", 2], 
               "Fenrir": ["Get kills/assists with F-NATT Dread Mines", 2], 
               "Finka": ["Revive downed teammates", 1], 
               "Flores": ["Destroy defender gadgets", 4], 
               "Frost": ["Trigger Welcome Mats", 1], 
               "Fuze": ["Destroy defender gadgets or kill defenders", 4], 
               "Glaz": ["Get kills through smoke or other vision blockers", 3], 
               "Goyo": ["Trigger canisters", 10], 
               "Gridlock": ["Get Trax Stinger kills/assists", 1], 
               "Grim": ["Ping enemies with the Kawan Hive Launcher", 2], 
               "Hibana": ["", 0], 
               "Iana": ["", 0], 
               "IQ": ["Destroy detected devices", 3], 
               "Jackal": ["Get footstep detection kills/assists", 1], 
               "Jager": ["Catch projectiles with the ADS", 4], 
               "Kaid": ["", 0], 
               "Kali": ["De-electrify walls", 2], 
               "Kapkan": ["Get EDD kills/assists", 1], 
               "Lesion": ["Get Gu Mine kills/assists", 5], 
               "Lion": ["Detect enemies with the EE-ONE-D", 2], 
               "Maestro": ["Deny defuser plants", 2], 
               "Maverick": ["Get kills through blowtorch holes", 2], 
               "Melusi": ["Get Banshee kills/assists", 3], 
               "Mira": ["", 0], 
               "Montagne": ["", 0], 
               "Mozzie": ["Hack drones or get drone scan assists", 5], 
               "Mute": ["Disable devices", 3], 
               "Nokk": ["", 0], 
               "Nomad": ["Get Airjab kills/assists", 3], 
               "Noor": ["", 0], 
               "Oryx": ["Knock down enemies with the Remah Dash", 1], 
               "Osa": ["", 0], 
               "Pulse": ["Get Cardiac Sensor kills/assists", 2], 
               "Ram": ["Get kills through ceilings", 2], 
               "Rauora": ["Secure a defuser plant", 2], 
               "Rook": ["", 0], 
               "Sens": ["Secure a defuser plant", 2], 
               "Sentry": ["Get kills with Nitro Cells, destroy attacker utility with Impact Grenades, or get Bulletproof Camera assists.", 3, ["Nitro Cell", "Impact Grenade", "Bulletproof Camera"]], 
               "Skopos": ["Get scan assists with the observation shell", 2], 
               "Sledge": ["", 0], 
               "Smoke": ["", 0], 
               "Solid Snake": ["Get Soliton Radar kills/assists", 3], 
               "Solis": ["Identify electronics with the overlock", 3], 
               "Striker": ["", 0, []], 
               "Tachanka": ["Get kills with the Shumikha Launcher", 2], 
               "Thatcher": ["", 0], 
               "Thermite": ["Secure defuser plants", 1], 
               "Thorn": ["Get Razorbloom Shell kills/assists", 2], 
               "Thunderbird": ["Heal allies", 10], 
               "Tubarao": ["Freeze attacker devices or slow down enemies", 2], 
               "Twitch": ["Get scan assists or destroy defender gadgets", 3], 
               "Valkyrie": ["Get scan assists", 3], 
               "Vigil": ["Dodge scans", 7], 
               "Wamai": ["Capture projectiles", 8], 
               "Warden": ["Get kills through flashbangs or smoke grenades", 2], 
               "Ying": ["Get Candela kills/assists", 2], 
               "Zero": ["Get scan assists", 2], 
               "Zofia": ["Get concussion grenade kills/assists", 2]}

class HardChallengeMultiplier(Range):
    """
    Multiplies the threshold for completing hard challenges, making them longer.
    As an example, if you had to get kills/assists with your gadget 3 times, a 2 multiplier would make it 6 times.
    """

    display_name = "Hard Challenge Multiplier"

    range_start = 1
    range_end = 10
    default = 1

class HardChallengeValue(Range):
    """
    The number of checks sent out when you complete a hard challenge.
    """

    display_name = "Hard Challenge Value"

    range_start = 1
    range_end = 10
    default = 1

class ChallengeAssists(DefaultOnToggle):
    """
    Changes whether or not assists are counted for challenges involving kills.
    Only changes the text in the client. No effect on logic.
    """

    display_name = "Challenge Assists"

class Weaponsanity(Toggle):
    """
    Weapons become items and are added into the pool.
    Includes the Ballistic Shield.
    """

    display_name = "Weaponsanity"

class WeaponsanityLogic(Choice):
    """
    Which weapons need to be unlocked for an operator to be considered in logic.
    Any Weapon: any weapon (including secondaries) needs to be unlocked.
    Any Primary: a primary or viable secondary needs to be unlocked.
    Any Viable Weapon: any viable primary or viable secondary needs to be unlocked.
    Most Popular Weapons: one of the most popular weapons for the operator needs to be unlocked.
    """

    display_name = "Weaponsanity Logic"

    option_any_weapon = 0
    option_any_primary = 1
    option_any_viable_weapon = 2
    option_most_popular_weapon = 3

    default = option_any_viable_weapon
    
class WeaponsanityLogicViableWeapons(OptionDict):
    """
    Which weapons are considered "viable weapons" for each operator in weaponsanity_logic.
    Feel free to scroll past if you didn't pick this option or want to stick with the default picks.
    """
    
    display_name = "Weaponsanity Logic: Viable Weapons"
    
    schema = weapons_schema
    
    default = {"Ace": ["AK-12"], 
               "Alibi": ["MX4 Storm"], 
               "Amaru": ["G8A1", "SuperNova"], 
               "Aruni": ["MK 14 EBR"], 
               "Ash": ["G36C", "R4-C"], 
               "Azami": ["9x19SVN"], 
               "Bandit": ["MP7"], 
               "Blackbeard": ["MK17CQB", "SR-25"], 
               "Blitz": ["P12"], 
               "Brava": ["PARA-308"], 
               "Buck": ["C8-SFW"], 
               "Capitao": ["M249"], 
               "Castle": ["UMP45"], 
               "Caveira": ["M12", "SPAS-15", "LUSION"], 
               "Clash": ["SPSMG9"], 
               "Deimos": ["AK-74M", "M590A1", ".44 Vendetta"], 
               "Denari": ["Scorpion Evo A1"], 
               "Doc": ["MP5", "P90"], 
               "Dokkaebi": ["XK23"], 
               "Echo": ["MP5SD", "SuperNova"], 
               "Ela": ["Scorpion Evo A1"], 
               "Fenrir": ["MP7"], 
               "Finka": ["6P41", "Spear .308"], 
               "Flores": ["AR33", "SR-25", "T-95 LSW"], 
               "Frost": ["9mm C1"], 
               "Fuze": ["AK-12", "6P41"], 
               "Glaz": ["OTS-03"], 
               "Goyo": ["Vector .45 ACP", "TCSG12"], 
               "Gridlock": ["F90", "M245 SAW"], 
               "Grim": ["552 Commando"], 
               "Hibana": ["Type-89", "SuperNova"], 
               "Iana": ["ARX200", "G36C"], 
               "IQ": ["AUG A2", "G8A1"], 
               "Jackal": ["C7E", "PDW9"], 
               "Jager": ["416-C Carbine"], 
               "Kaid": ["AUG A3", "TCSG12"], 
               "Kali": ["CSRX 300", "SPSMG9"], 
               "Kapkan": ["9x19VSN"], 
               "Lesion": ["T-5 SMG"], 
               "Lion": ["V308"], 
               "Maestro": ["ALDA 5.56"], 
               "Maverick": ["M4"], 
               "Melusi": ["MP5"], 
               "Mira": ["Vector .45 ACP"], 
               "Montagne": ["P9", "LFP586"], 
               "Mozzie": ["Commando 9"], 
               "Mute": ["M590A1", "MP5K", "SMG-11"], 
               "Nokk": ["FMG-9", "SIX12 SD", "PMR90A2"], 
               "Nomad": ["AK-74M"], 
               "Noor": ["Commando 9", "ALDA 5.56"], 
               "Oryx": ["T-5 SMG"], 
               "Osa": ["556xi", "PDW9"], 
               "Pulse": ["UMP45"], 
               "Ram": ["R4-C"], 
               "Rauora": ["XK23"], 
               "Rook": ["MP5", "P90"], 
               "Sens": ["POF-9", "XK23"], 
               "Sentry": ["Commando 9", "TCSG12"], 
               "Skopos": ["PCX-33"], 
               "Sledge": ["L85A2"], 
               "Smoke": ["M590A1", "SMG-11"], 
               "Solid Snake": ["F2", "PMR90A2"], 
               "Solis": ["P90", "SMG-11"], 
               "Striker": ["M4"], 
               "Tachanka": ["DP27"], 
               "Thatcher": ["L85A2", "AR33"], 
               "Thermite": ["556xi"], 
               "Thorn": ["UZK50GI"], 
               "Thunderbird": ["Spear .308", "SPAS-15"], 
               "Tubarao": ["MPX", "AR-15.50"], 
               "Twitch": ["F2"], 
               "Valkyrie": ["MPX"], 
               "Vigil": ["K1A", "BOSG. 12.2", "SMG-12"], 
               "Wamai": ["AUG A12"], 
               "Warden": ["M590A1", "MPX", "SMG-12"], 
               "Ying": ["T-95 LSW"], 
               "Zero": ["SC3000K", "MP7"], 
               "Zofia": ["M762"]}

class WeaponsanityLogicMostPopularWeapons(OptionDict):
    """
    Which weapons are considered the "most popular weapons" for each operator in weaponsanity_logic.
    Feel free to scroll past if you didn't pick this option or want to stick with the default picks.
    """
    
    display_name = "Weaponsanity Logic: Most Popular Weapons"
    
    schema = weapons_schema
    
    default = {"Ace": ["AK-12"], 
               "Alibi": ["MX4 Storm"], 
               "Amaru": ["G8A1"], 
               "Aruni": ["MK 14 EBR"], 
               "Ash": ["R4-C"], 
               "Azami": ["9x19SVN"], 
               "Bandit": ["MP7"], 
               "Blackbeard": ["MK17CQB"], 
               "Blitz": ["P12"], 
               "Brava": ["PARA-308"], 
               "Buck": ["C8-SFW"], 
               "Capitao": ["M249"], 
               "Castle": ["UMP45"], 
               "Caveira": ["M12", "SPAS-15", "LUSION"], 
               "Clash": ["SPSMG9"], 
               "Deimos": ["AK-74M", ".44 Vendetta"], 
               "Denari": ["Scorpion Evo A1"], 
               "Doc": ["MP5"], 
               "Dokkaebi": ["XK23"], 
               "Echo": ["MP5SD"], 
               "Ela": ["Scorpion Evo A1"], 
               "Fenrir": ["MP7"], 
               "Finka": ["Spear .308"], 
               "Flores": ["AR33", "T-95 LSW"], 
               "Frost": ["9mm C1"], 
               "Fuze": ["AK-12"], 
               "Glaz": ["OTS-03"], 
               "Goyo": ["Vector .45 ACP"], 
               "Gridlock": ["F90"], 
               "Grim": ["552 Commando"], 
               "Hibana": ["Type-89"], 
               "Iana": ["ARX200", "G36C"], 
               "IQ": ["AUG A2", "G8A1"], 
               "Jackal": ["C7E", "PDW9"], 
               "Jager": ["416-C Carbine"], 
               "Kaid": ["TCSG12"], 
               "Kali": ["CSRX 300", "SPSMG9"], 
               "Kapkan": ["9x19VSN"], 
               "Lesion": ["T-5 SMG"], 
               "Lion": ["V308"], 
               "Maestro": ["ALDA 5.56"], 
               "Maverick": ["M4"], 
               "Melusi": ["MP5"], 
               "Mira": ["Vector .45 ACP"], 
               "Montagne": ["P9", "LFP586"], 
               "Mozzie": ["Commando 9"], 
               "Mute": ["M590A1", "SMG-11"], 
               "Nokk": ["FMG-9"], 
               "Nomad": ["AK-74M"], 
               "Noor": ["Commando 9"], 
               "Oryx": ["T-5 SMG"], 
               "Osa": ["556xi", "PDW9"], 
               "Pulse": ["UMP45"], 
               "Ram": ["R4-C"], 
               "Rauora": ["XK23"], 
               "Rook": ["MP5", "P90"], 
               "Sens": ["POF-9", "XK23"], 
               "Sentry": ["TCSG12"], 
               "Skopos": ["PCX-33"], 
               "Sledge": ["L85A2"], 
               "Smoke": ["M590A1", "SMG-11"], 
               "Solid Snake": ["F2", "PMR90A2"], 
               "Solis": ["P90", "SMG-11"], 
               "Striker": ["M4"], 
               "Tachanka": ["DP27"], 
               "Thatcher": ["L85A2", "AR33"], 
               "Thermite": ["556xi"], 
               "Thorn": ["UZK50GI"], 
               "Thunderbird": ["Spear .308"], 
               "Tubarao": ["MPX", "AR-15.50"], 
               "Twitch": ["F2"], 
               "Valkyrie": ["MPX"], 
               "Vigil": ["BOSG. 12.2", "SMG-12"], 
               "Wamai": ["AUG A12"], 
               "Warden": ["M590A1", "MPX", "SMG-12"], 
               "Ying": ["T-95 LSW"], 
               "Zero": ["SC3000K", "MP7"], 
               "Zofia": ["M762"]}
    
class WeaponsanityLogicBehavior(Choice):
    """
    Changes the behavior when an operator's weapon requirements aren't fulfilled.
    Out-of-logic kills: the operator's kill counter check is not in logic.
    Out-of-logic all: the operator's checks are not in logic.
    Lock kills: the kill counter is locked.
    Lock all: the kill counter and the challenges are locked.
    """

    display_name = "Weaponsanity Logic Behavior"

    option_out_of_logic_kills = 0
    option_out_of_logic_all = 1
    option_lock_kills = 2
    option_lock_all = 3

    default = option_out_of_logic_all
    
class WeaponsanityLogicBehaviorIncludeOutOfLogicWeapons(DefaultOnToggle):
    """
    Changes whether or not out of logic weapons will be in the item pool.
    """
    
    display_name = "Weaponsanity Logic Behavior: Include Out-of-logic Weapons"

class WeaponsanityStartingWeapons(Range):
    """
    The amount of weapons you'll start with.
    """

    display_name = "Weaponsanity Starting Weapons"

    range_start = 1
    range_end = WEAPONS
    default = 1

class WeaponsanityInLogicStartingWeapons(Range):
    """
    The amount of your starting operators that'll get an in-logic weapon.
    Can't be more than your starting operators or starting weapons.
    """

    display_name = "Weaponsanity In-logic Starting Weapons"

    range_start = 1
    range_end = WEAPONS
    default = 1

class WeaponsanityAllWeaponsKillThreshold(Choice):
    """
    You'll have a separate kill threshold for all of your in logic weapons.
    Full threshold: you'll have your full kill threshold for every allowed weapon.
    Divided threshold: your kill threshold will be divided as evenly as possible among the allowed weapons.
    Disabled: you'll have one kill threshold for the operator, not the weapons.
    """

    display_name = "Weaponsanity All Weapons Kill Threshold"

    option_full_threshold = 0
    option_divided_threshold = 1
    option_disabled = 2

    default = option_disabled

class Abilitysanity(Toggle):
    """
    Operator abilities become items and are added into the pool.
    Challenges are locked until the operator's ability is unlocked.
    """

    display_name = "Abilitysanity"
    
class AbilitysanityLocksKillThreshold(Choice):
    """
    Not having an operator's ability also affects their kill threshold.
    Out-of-logic: the operator's kills aren't in logic.
    Lock: the kill threshold buttons are locked.
    Disabled: the kill threshold remains available.
    """
    
    display_name = "Abilitysanity Locks Kill Threshold"
    
    option_out_of_logic = 0
    option_lock = 1
    option_disabled = 2
    
    default = option_disabled
    

class AbilitysanityGadgetKit(Toggle):
    """
    Adds the Gadget Kit into the item pool.
    Locks Striker and Sentry's challenges.
    Will automatically turn on if abilitysanity is on and gadgetsanity is off.
    """

    display_name = "Abilitysanity Gadget Kit"

class AbilitysanityStartingAbilities(Range):
    """
    The amount of abilities you start with.
    """

    display_name = "Abilitysanity Starting Abilities"

    range_start = 0
    range_end = OPERATORS
    default = 1

class AbilitysanityInLogicStartingAbilities(Range):
    """
    The amount of abilities you'll start with that are for your starting operators.
    Can't be more than your starting operators or starting abilities.
    """

    display_name = "Abilitysanity In-logic Starting Abilities"

    range_start = 0
    range_end = OPERATORS
    default = 1

class Gadgetsanity(Toggle):
    """
    Gadgets become items and are added into the pool.
    Locks Striker and Sentry's challenges until the appropriate gadgets are unlocked.
    You'll need the gadgets and the gadget kit if abilitysanity_gadget_kit is turned on.
    """

    display_name = "Gadgetsanity"
    
class GadgetsanityStartingGadgets(Range):
    """
    The amount of gadgets you'll start with.
    If the value is greater than the gadgets in the pool, you'll start with all gadgets in the pool.
    In-logic starting gadgets for Striker and Sentry are handled in abilitysanity_in_logic_starting_abilities.
    """
    
    display_name = "Gadgetsanity Starting Gadgets"
    
    range_start = 0
    range_end = GADGETS
    default = 0
    

@dataclass
class R6SiegeOptions(PerGameCommonOptions):
    goal_operators: GoalOperators
    starting_operators: StartingOperators
    starting_operator_balancing: StartingOperatorBalancing
    extra_operators: ExtraOperators
    allowed_operators: AllowedOperators
    forced_selected_operators: ForcedSelectedOperators
    forced_starting_operators: ForcedStartingOperators
    kill_threshold: KillThreshold
    kill_threshold_amount: KillThresholdAmount
    kill_threshold_value: KillThresholdValue
    kill_threshold_assists: KillThresholdAssists
    global_kill_counter: GlobalKillCounter
    global_kill_counter_count: GlobalKillCounterCount
    global_kill_counter_reward: GlobalKillCounterReward
    global_kill_counter_value: GlobalKillCounterValue
    global_kill_counter_logic: GlobalKillCounterLogic
    global_kill_counter_kill_threshold_behavior: GlobalKillCounterKillThresholdBehavior
    easy_challenges: EasyChallenges
    easy_challenges_challenges: EasyChallengesChallenges
    easy_challenge_multiplier: EasyChallengeMultiplier
    easy_challenge_value: EasyChallengeValue
    hard_challenges: HardChallenges
    hard_challenges_challenges: HardChallengesChallenges
    hard_challenge_multiplier: HardChallengeMultiplier
    hard_challenge_value: HardChallengeValue
    challenge_assists: ChallengeAssists
    weaponsanity: Weaponsanity
    weaponsanity_logic: WeaponsanityLogic
    weaponsanity_logic_viable_weapons: WeaponsanityLogicViableWeapons
    weaponsanity_logic_most_popular_weapons: WeaponsanityLogicMostPopularWeapons
    weaponsanity_logic_behavior: WeaponsanityLogicBehavior
    weaponsanity_logic_behavior_include_out_of_logic_weapons: WeaponsanityLogicBehaviorIncludeOutOfLogicWeapons
    weaponsanity_starting_weapons: WeaponsanityStartingWeapons
    weaponsanity_in_logic_starting_weapons: WeaponsanityInLogicStartingWeapons
    weaponsanity_all_weapons_kill_threshold: WeaponsanityAllWeaponsKillThreshold
    abilitysanity: Abilitysanity
    abilitysanity_locks_kill_threshold: AbilitysanityLocksKillThreshold
    abilitysanity_gadget_kit: AbilitysanityGadgetKit
    abilitysanity_starting_abilities: AbilitysanityStartingAbilities
    abilitysanity_in_logic_starting_abilities: AbilitysanityInLogicStartingAbilities
    gadgetsanity: Gadgetsanity
    gadgetsanity_starting_gadgets: GadgetsanityStartingGadgets

option_groups = [
    OptionGroup(
        "Operators",
        [GoalOperators, StartingOperators, StartingOperatorBalancing, ExtraOperators, AllowedOperators, ForcedSelectedOperators, ForcedStartingOperators]
    ),
    OptionGroup(
        "Kill Threshold",
        [KillThreshold, KillThresholdAmount, KillThresholdValue, KillThresholdAssists]
    ),
    OptionGroup(
        "Global Kill Counter",
        [GlobalKillCounter, GlobalKillCounterCount, GlobalKillCounterReward, GlobalKillCounterValue, GlobalKillCounterLogic, GlobalKillCounterKillThresholdBehavior]
    ),
    OptionGroup(
        "Challenges",
        [EasyChallenges, EasyChallengesChallenges, EasyChallengeMultiplier, EasyChallengeValue, HardChallenges, HardChallengesChallenges, HardChallengeMultiplier, HardChallengeValue, ChallengeAssists]
    ),
    OptionGroup(
        "Weaponsanity",
        [Weaponsanity, WeaponsanityLogic, WeaponsanityLogicViableWeapons, WeaponsanityLogicMostPopularWeapons, WeaponsanityLogicBehavior, WeaponsanityLogicBehaviorIncludeOutOfLogicWeapons, WeaponsanityStartingWeapons, WeaponsanityInLogicStartingWeapons,  WeaponsanityAllWeaponsKillThreshold]
    ),
    OptionGroup(
        "Abilitysanity",
        [Abilitysanity, AbilitysanityLocksKillThreshold, AbilitysanityGadgetKit, AbilitysanityStartingAbilities, AbilitysanityInLogicStartingAbilities]
    ),
    OptionGroup(
        "Gadgetsanity",
        [Gadgetsanity, GadgetsanityStartingGadgets]
    )
]

logger = logging.getLogger("R6Logger")

def validate_options(world: R6SiegeWorld) -> None:
    #Goal operators + extra operators > OPERATORS -> extra operators = OPERATORS - goal operators
    if world.options.goal_operators.value + world.options.extra_operators.value > OPERATORS:
        world.options.extra_operators.value = OPERATORS - world.options.goal_operators.value
        logger.warning(f"{world.player_name}'s goal operators + extra operators was greater than the operators in the game, so their extra operators were lowered to adjust.")

    #Starting operators > goal operators -> starting operators = goal operators
    if world.options.goal_operators.value + world.options.extra_operators.value < world.options.starting_operators.value:
        world.options.starting_operators.value = world.options.goal_operators.value
        logger.warning(f"{world.player_name}'s starting operators were higher than their goal operators, so they'll start with all of their goal operators.")

    #Goal operators > allowed operators -> goal operators = allowed operators
    #Goal operators + extra operators > allowed operators -> extra operators = allowed operators - goal operators
    if len(world.options.allowed_operators.value) < world.options.goal_operators.value + world.options.extra_operators.value:
        if len(world.options.allowed_operators.value) < world.options.goal_operators.value:
            world.options.goal_operators.value = len(world.options.allowed_operators.value)
            world.options.extra_operators.value = 0
            logger.warning(f"{world.player_name} had more goal operators than allowed operators, so their goal operators were reduced to their allowed operators. Extra operators were eliminated.")
        else:
            world.options.extra_operators.value = len(world.options.allowed_operators.value) - world.options.goal_operators.value
            logger.warning(f"{world.player_name}'s goal operators + extra operators were more than their allowed operators, so their extra operators were reduced to adjust.")

    #Remove forced selected operators in allowed operators
    for operator in world.options.forced_selected_operators.value:
        world.options.allowed_operators.value.discard(operator)

    #Remove forced starting operators in allowed operators
    for operator in world.options.forced_starting_operators.value:
        world.options.allowed_operators.value.discard(operator)

    #Error if kill threshold, easy challenges, and hard challenges are off
    if not world.options.kill_threshold.value and not world.options.easy_challenges.value and not world.options.hard_challenges.value:
        raise OptionError(f"{world.player_name}'s world has no locations. Please enable kill thresholds, easy challenges, or hard challenges.")

    #If the global kill counter is in logic after the goal operators are completed, set it to one before the goal operators are completed.
    if world.options.global_kill_counter_reward.value == world.options.global_kill_counter_reward.option_checks and world.options.global_kill_counter_logic.value > world.options.goal_operators.value:
        world.options.global_kill_counter_logic.value = world.options.goal_operators.value - 1
        logger.warning(f"{world.player_name}'s global kill counter was put in logic after their goal operators were completed, so it'll now be in logic after one less of their goal operators are completed.")

    #In logic starting weapons > starting operators -> in logic starting weapons = starting operators
    if world.options.weaponsanity_in_logic_starting_weapons.value > world.options.starting_operators.value:
        world.options.weaponsanity_in_logic_starting_weapons.value = world.options.starting_operators.value
        logger.info(f"{world.player_name}'s in logic starting weapons were higher than their starting operators, so the in logic starting weapons were decreased to adjust.")

    #Starting weapons < in logic starting weapons -> starting weapons = in logic starting weapons
    if world.options.weaponsanity_starting_weapons.value < world.options.weaponsanity_in_logic_starting_weapons.value:
        world.options.weaponsanity_starting_weapons.value = world.options.weaponsanity_in_logic_starting_weapons.value
        logger.info(f"{world.player_name} has less starting weapons than in-logic starting weapons, so their starting weapons are their in-logic starting weapons.")

    #In logic starting abilities > starting operators -> in logic abilities = starting operators
    if world.options.abilitysanity_in_logic_starting_abilities.value > world.options.starting_operators.value:
        world.options.abilitysanity_in_logic_starting_abilities.value = world.options.starting_operators.value
        logger.info(f"{world.player_name}'s in logic starting abilities were higher than their starting operators, so the in logic starting weapons were decreased to adjust.")

    #Starting abilities < in logic starting abilities -> starting weapons = in logic starting weapons
    if world.options.abilitysanity_starting_abilities.value < world.options.abilitysanity_in_logic_starting_abilities.value:
        world.options.abilitysanity_starting_abilities.value = world.options.abilitysanity_in_logic_starting_abilities.value
        logger.info(f"{world.player_name} has less starting abilities than in-logic starting abilities, so their starting abilities are their in-logic starting abilities.")

    #Prevent the player from locking themselves out at the start
    if world.options.weaponsanity.value and world.options.abilitysanity.value:

        #Error if no in-logic starting weapons or abilities
        if world.options.weaponsanity_in_logic_starting_weapons.value == 0 and world.options.abilitysanity_in_logic_starting_abilities.value == 0:
            raise OptionError(f"{world.player_name} has no available checks at the start. Please increase in-logic starting weapons or in-logic starting abilities.")

        #1 in-logic starting weapon if no in-logic starting weapons and weapons lock challenges
        elif world.options.weaponsanity_in_logic_starting_weapons.value == 0 and world.options.weaponsanity_logic_behavior.value == world.options.weaponsanity_logic_behavior.option_out_of_logic_all or world.options.weaponsanity_logic_behavior.value == world.options.weaponsanity_logic_behavior.option_lock_all:
            world.options.weaponsanity_in_logic_starting_weapons.value = 1
            logger.warning(f"{world.player_name}'s in-logic starting weapons were increased to 1 to prevent having no checks available at the start.")

        #1 in-logic starting ability if no in-logic starting abilities and abilities lock kills
        elif world.options.abilitysanity_in_logic_starting_abilities.value == 0 and world.options.abilitysanity_locks_kill_threshold.value:
            world.options.abilitysanity_in_logic_starting_abilities.value = 1
            logger.warning(f"{world.player_name}'s in-logic starting abilities were increased to 1 to prevent having no checks available at the start.")

    elif world.options.weaponsanity.value:
        #1 in-logic starting weapon if no in-logic starting weapons and weapons lock challenges
        if world.options.weaponsanity_in_logic_starting_weapons.value == 0 and world.options.weaponsanity_logic_behavior.value == world.options.weaponsanity_logic_behavior.option_out_of_logic_all or world.options.weaponsanity_logic_behavior.value == world.options.weaponsanity_logic_behavior.option_lock_all:
            world.options.weaponsanity_in_logic_starting_weapons.value = 1
            logger.warning(f"{world.player_name}'s in-logic starting weapons were increased to 1 to prevent having no checks available at the start.")

    elif world.options.abilitysanity.value:
        #1 in-logic starting ability if no in-logic starting abilities and abilities lock kills
        if world.options.abilitysanity_in_logic_starting_abilities.value == 0 and world.options.abilitysanity_locks_kill_threshold.value:
            world.options.abilitysanity_in_logic_starting_abilities.value = 1
            logger.warning(f"{world.player_name}'s in-logic starting abilities were increased to 1 to prevent having no checks available at the start.")

    if not world.options.abilitysanity_gadget_kit.value and not world.options.gadgetsanity.value:
        world.options.abilitysanity_gadget_kit.value = world.options.abilitysanity_gadget_kit.option_true
        logger.warning(f"{world.player_name}'s gadget kit was turned off without gadgetsanity being turned on, so it was turned back on.")