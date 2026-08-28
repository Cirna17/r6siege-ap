from dataclasses import dataclass
from Options import Toggle, Range, Choice, OptionSet, OptionGroup, PerGameCommonOptions

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
    range_end = 76
    default = 2

class StartingOperatorBalancing(Choice):
    pass