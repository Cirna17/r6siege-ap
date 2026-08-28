from worlds.Autoworld import World

from . import items, locations, regions, rules, web_world
from . import options as r6_options

class R6World(World):
    """
    Rainbow Six Siege is a tactical shooter.
    You'll complete various objectives in the game.
    """

    game = "Rainbow Six Siege"
    web = web_world.R6WebWorld()