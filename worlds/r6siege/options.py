from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, OptionSet, OptionGroup, PerGameCommonOptions

class GoalOperators(Range):
    """
    The amount of operators you need to complete all objectives for to goal.
    """

    display_name = "Goal Operators"

    range_start = 1
    range_end = 77
    default = 10

class StartingOperators(Range):
    """
    The amount of random operators you'll start with.
    """

    display_name = "Starting Operators"

    range_start = 1
    range_end = 77
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
    range_end = 76
    default = 2

class AllowedOperators(OptionSet):
    """
    The operators that can be added into the pool.
    Remove any you haven't bought or don't want to play as.
    """

    display_name = "Allowed Operators"

    valid_keys = ["Ace", "Alibi", "Amaru", "Aruni", "Ash", "Azami", "Bandit", "Blackbeard", "Blitz",
                  "Brava", "Buck", "Capitao", "Castle", "Caveira", "Clash", "Deimos", "Denari",
                  "Doc", "Dokkaebi", "Echo", "Ela", "Fenrir", "Finka", "Flores", "Frost", "Fuze",
                  "Glaz", "Goyo", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Jager",
                  "Kaid", "Kali", "Kapkan", "Lesion", "Lion", "Maestro", "Maverick", "Melusi", "Mira",
                  "Montagne", "Mozzie", "Mute", "Nokk", "Nomad", "Oryx", "Osa", "Pulse", "Ram",
                  "Rauora", "Rook", "Sens", "Sentry", "Skopos", "Sledge", "Smoke", "Solid Snake", "Solis",
                  "Striker", "Tachanka", "Thatcher", "Thermite", "Thorn", "Thunderbird", "Tubarao",
                  "Twitch", "Valkyrie", "Vigil", "Wamai", "Warden", "Ying", "Zero", "Zofia"]

    default = ["Ace", "Alibi", "Amaru", "Aruni", "Ash", "Azami", "Bandit", "Blackbeard", "Blitz",
                  "Brava", "Buck", "Capitao", "Castle", "Caveira", "Clash", "Deimos", "Denari",
                  "Doc", "Dokkaebi", "Echo", "Ela", "Fenrir", "Finka", "Flores", "Frost", "Fuze",
                  "Glaz", "Goyo", "Gridlock", "Grim", "Hibana", "Iana", "IQ", "Jackal", "Jager",
                  "Kaid", "Kali", "Kapkan", "Lesion", "Lion", "Maestro", "Maverick", "Melusi", "Mira",
                  "Montagne", "Mozzie", "Mute", "Nokk", "Nomad", "Oryx", "Osa", "Pulse", "Ram",
                  "Rauora", "Rook", "Sens", "Sentry", "Skopos", "Sledge", "Smoke", "Solid Snake", "Solis",
                  "Striker", "Tachanka", "Thatcher", "Thermite", "Thorn", "Thunderbird", "Tubarao",
                  "Twitch", "Valkyrie", "Vigil", "Wamai", "Warden", "Ying", "Zero", "Zofia"]

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
    this is how many operators you're expected to unlock before those checks are in logic.
    It's recommended to set this to half of your goal operators.
    """

    display_name = "Global Kill Counter Logic"

    range_start = 0
    range_end = 77
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
    Most Popular Weapon: the most popular weapon for the operator needs to be unlocked.
    """

    display_name = "Weaponsanity Logic"

    option_any_weapon = 0
    option_any_primary = 1
    option_any_viable_weapon = 2
    option_most_popular_weapon = 3

    default = option_any_viable_weapon

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

class WeaponsanityStartingWeapons(Range):
    """
    The amount of weapons you'll start with.
    """

    display_name = "Weaponsanity Starting Weapons"

    range_start = 1
    range_end = 116
    default = 1

class WeaponsanityInLogicStartingWeapons(Range):
    """
    The amount of your starting operators that'll get an in-logic weapon.
    Can't be more than your starting operators or starting weapons.
    """

    display_name = "Weaponsanity In-logic Starting Weapons"

    range_start = 1
    range_end = 116
    default = 1

class WeaponsanityAllWeaponsKillThreshold(Choice):
    """
    You'll have a separate kill threshold for all of your allowed weapons under Weaponsanity Logic.
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
    The abilities will be for your starting operator(s) if possible.
    """

    display_name = "Abilitysanity Starting Abilities"

    range_start = 0
    range_end = 75
    default = 0

class AbilitysanityInLogicStartingAbilities(Range):
    """
    The amount of abilities you'll start with that are for your starting operators.
    Can't be more than your starting operators or starting abilities.
    """

    display_name = "Abilitysanity In-logic Starting Abilities"

    range_start = 0
    range_end = 75
    default = 0

class Gadgetsanity(Toggle):
    """
    Gadgets become items and are added into the pool.
    Locks Striker and Sentry's challenges until the appropriate gadgets are unlocked.
    You'll need the gadgets and the gadget kit if abilitysanity_gadget_kit is turned on.
    """

    display_name = "Gadgetsanity"

@dataclass
class R6SiegeOptions(PerGameCommonOptions):
    goal_operators: GoalOperators
    starting_operators: StartingOperators
    starting_operator_balancing: StartingOperatorBalancing
    extra_operators: ExtraOperators
    allowed_operators: AllowedOperators
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
    easy_challenge_multiplier: EasyChallengeMultiplier
    easy_challenge_value: EasyChallengeValue
    hard_challenges: HardChallenges
    hard_challenge_multiplier: HardChallengeMultiplier
    hard_challenge_value: HardChallengeValue
    challenge_assists: ChallengeAssists
    weaponsanity: Weaponsanity
    weaponsanity_logic: WeaponsanityLogic
    weaponsanity_logic_behavior: WeaponsanityLogicBehavior
    weaponsanity_starting_weapons: WeaponsanityStartingWeapons
    weaponsanity_in_logic_starting_weapons: WeaponsanityInLogicStartingWeapons
    weaponsanity_all_weapons_kill_threshold: WeaponsanityAllWeaponsKillThreshold
    abilitysanity: Abilitysanity
    abilitysanity_gadget_kit: AbilitysanityGadgetKit
    abilitysanity_starting_abilities: AbilitysanityStartingAbilities
    abilitysanity_in_logic_starting_abilities: AbilitysanityInLogicStartingAbilities
    gadgetsanity: Gadgetsanity

option_groups = [
    OptionGroup(
        "Operators",
        [GoalOperators, StartingOperators, StartingOperatorBalancing, ExtraOperators, AllowedOperators]
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
        [EasyChallenges, EasyChallengeMultiplier, EasyChallengeValue, HardChallenges, HardChallengeMultiplier, HardChallengeValue, ChallengeAssists]
    ),
    OptionGroup(
        "Weaponsanity",
        [Weaponsanity, WeaponsanityLogic, WeaponsanityLogicBehavior, WeaponsanityStartingWeapons, WeaponsanityInLogicStartingWeapons,  WeaponsanityAllWeaponsKillThreshold]
    ),
    OptionGroup(
        "Abilitysanity",
        [Abilitysanity, AbilitysanityGadgetKit, AbilitysanityStartingAbilities, AbilitysanityInLogicStartingAbilities]
    ),
    OptionGroup(
        "Gadgetsanity",
        [Gadgetsanity]
    )
]