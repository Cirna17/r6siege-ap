from worlds.AutoWorld import World
from collections.abc import Mapping
from typing import Any

from . import items, locations, generation, web_world
from . import options as r6siege_options

class R6SiegeWorld(World):
    """
    Rainbow Six Siege is a multiplayer tactical hero shooter.
    You'll kill other players and complete character-specific challenges in the game.
    """

    game = "Rainbow Six Siege"

    web = web_world.R6WebWorld()

    options_dataclass = r6siege_options.R6SiegeOptions
    options: r6siege_options.R6SiegeOptions

    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID

    origin_region_name = "Menu"

    selected_operators = []

    def generate_early(self) -> None:
        self.selected_operators = self.random.sample(sorted(self.options.allowed_operators.value),
                                                 k = self.options.goal_operators.value + self.options.extra_operators.value)
        
        items.create_all_items(self)
        generation.create_locations_regions_and_rules(self)

    def create_item(self, name: str) -> items.R6SiegeItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "kill_threshold", "kill_threshold_amount", "kill_threshold_assists", "global_kill_counter", "global_kill_counter_count",
            "global_kill_counter_kill_threshold_behavior", "easy_challenges", "easy_challenges_multiplier", "hard_challenges",
            "hard_challenges_multiplier", "challenge_assists", "weaponsanity", "weaponsanity_logic", "weaponsanity_logic_behavior",
            "weaponsanity_all_weapons_kill_threshold", "abilitysanity", "abilitysanity_gadget_kit", "gadgetsanity"
        )