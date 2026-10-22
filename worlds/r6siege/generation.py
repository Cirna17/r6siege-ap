from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
from rule_builder.rules import Has, HasAny, HasFromList, CanReachRegion, True_, Rule

from . import operator_data, locations, items

if TYPE_CHECKING:
    from .world import R6SiegeWorld
    
def name_to_operator_data(name: str) -> operator_data.Operator:
    for operator in operator_data.operators:
        if operator.name == name:
            return operator

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: locations.LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def get_locations(operator: str, location_type: str, number_of_locations: int) -> dict[str, int]:
    locations: list[str] = []
    
    for location in range(1, number_of_locations + 1):
        locations.append(f"{operator}: {location_type} Reward #{location}")
        
    return get_location_names_with_ids(locations)
        
def create_operator_access_rule(world: R6SiegeWorld, operator: str) -> Rule:
    weapon_rule = True_()
    
    if (world.options.weaponsanity_logic_behavior.value == world.options.weaponsanity_logic_behavior.option_out_of_logic_all
        or world.options.weaponsanity_logic_behavior.value == world.options.weaponsanity_logic_behavior.option_lock_all):
        weapon_rule = create_weaponsanity_rule(world, operator)
        
    return Has(operator) & weapon_rule
        
def create_weaponsanity_rule(world: R6SiegeWorld, operator: str) -> Rule:
    if not world.options.weaponsanity.value:
        return True_()
    
    operator = name_to_operator_data(operator)
    match world.options.weaponsanity_logic.value:
        
        case world.options.weaponsanity_logic.option_any_weapon:
            return HasAny(*(operator.primary_weapons + operator.secondary_weapons))
        
        case world.options.weaponsanity_logic.option_any_primary:
            return HasAny(*(operator.primary_weapons + [item for item in operator.secondary_weapons if item in operator.viable_weapons]))
        
        case world.options.weaponsanity_logic.option_any_viable_weapon:
            return HasAny(*(operator.viable_weapons))
        
        case world.options.weaponsanity_logic.option_most_popular_weapon:
            return HasAny(*(operator.most_popular_weapons))
        
def create_abilitysanity_rule(world: R6SiegeWorld, operator: str, challenge_type: str) -> Rule:
    if not world.options.abilitysanity.value:
        return True_()
    
    if world.options.gadgetsanity.value and not world.options.abilitysanity_gadget_kit.value:
        
        if operator == "Striker":
            if challenge_type == "Easy":
                return HasAny(*operator_data.striker_easy_challenge_gadgets)
            else:
                return HasAny(*operator_data.striker_hard_challenge_gadgets)
        
        elif operator == "Sentry":
            if challenge_type == "Easy":
                return HasAny(*operator_data.sentry_easy_challenge_gadgets)
            else:
                return HasAny(*operator_data.sentry_hard_challenge_gadgets)
                
        else:
            return Has(name_to_operator_data(operator).ability)
                
    else:
        return Has(name_to_operator_data(operator).ability)
    
def create_operator_completion_rule(world: R6SiegeWorld, operator: str) -> Rule | None:
    kill_threshold_enabled = world.options.kill_threshold.value
    easy_challenges_enabled = world.options.easy_challenges.value
    hard_challenges_enabled = world.options.hard_challenges.value and name_to_operator_data(operator).hard_challenge
    
    if kill_threshold_enabled and easy_challenges_enabled and hard_challenges_enabled:
        return CanReachRegion(operator + " Kills") & CanReachRegion(operator + " Easy Challenges") & CanReachRegion(operator + " Hard Challenges")
    
    elif kill_threshold_enabled and easy_challenges_enabled:
        return CanReachRegion(operator + " Kills") & CanReachRegion(operator + " Easy Challenges")
    
    elif kill_threshold_enabled and hard_challenges_enabled:
        return CanReachRegion(operator + " Kills") & CanReachRegion(operator + " Hard Challenges")
    
    elif easy_challenges_enabled and hard_challenges_enabled:
        return CanReachRegion(operator + " Easy Challenges") & CanReachRegion(operator + " Hard Challenges")
        
    elif kill_threshold_enabled:
        return CanReachRegion(operator + " Kills")
    
    elif easy_challenges_enabled:
        return CanReachRegion(operator + " Easy Challenges")
    
    elif hard_challenges_enabled:
        return CanReachRegion(operator + " Hard Challenges")
    
    else:
        print("No valid completion rule created")
    
#Since our locations, regions, and rules are RNG-dependent but also uniform, we can dynamically create them all here.
def create_locations_regions_and_rules(world: R6SiegeWorld):
    regions: list[Region] = []
    regions.append(Region("Menu", world.player, world.multiworld))


    if (world.options.global_kill_counter.value and 
        world.options.global_kill_counter_reward.value == world.options.global_kill_counter_reward.option_checks):
        
        regions.append(Region("Global Kill Counter", world.player, world.multiworld))
        regions[-0].connect(regions[-1], "Global Kill Counter In Logic")
        
        if world.options.global_kill_counter_reward.value == world.options.global_kill_counter_reward.option_required_to_goal:
            regions[-1].add_event("Global Kill Counter Complete", location_type = locations.R6SiegeLocation, item_type = items.R6SiegeItem)
            
        regions[-1].add_locations(get_locations(0, 0, world.options.global_kill_counter_value.value), 
                                  HasFromList(*[i.name for i in operator_data.operators], count = world.options.global_kill_counter_logic.value))
        
        
    for operator in world.selected_operators:
        added_regions = 0
        regions.append(Region(operator, world.player, world.multiworld))
        regions[0].connect(regions[-1], operator + " Unlock", create_operator_access_rule(world, operator))
        added_regions += 1
        
        
        if world.options.kill_threshold.value:
            regions.append(Region(operator + " Kills", world.player, world.multiworld))
            
            if world.options.abilitysanity_locks_kill_threshold.value != world.options.abilitysanity_locks_kill_threshold.option_disabled:
                regions[-1 - added_regions].connect(regions[-1], operator + " Kills Unlock", create_weaponsanity_rule(world, operator) & create_abilitysanity_rule(world, operator))
            else:
                regions[-1 - added_regions].connect(regions[-1], operator + " Kills Unlock", create_weaponsanity_rule(world, operator))
            
            regions[-1].add_locations(get_locations(operator, "Kills", world.options.kill_threshold_value.value))
            added_regions += 1
            
            
        if world.options.easy_challenges.value:
            regions.append(Region(operator + " Easy Challenges", world.player, world.multiworld))
            regions[-1 - added_regions].connect(regions[-1], operator + " Easy Challenges Unlock", create_abilitysanity_rule(world, operator, "Easy"))    
            regions[-1].add_locations(get_locations(operator, "Easy Challenge", world.options.easy_challenge_value.value))
            added_regions += 1
            
            
        if world.options.hard_challenges.value:
            if name_to_operator_data(operator).hard_challenge:
                regions.append(Region(operator + " Hard Challenges", world.player, world.multiworld))
                regions[-1 - added_regions].connect(regions[-1], operator + " Hard Challenges Unlock", create_abilitysanity_rule(world, operator, "Hard"))    
                regions[-1].add_locations(get_locations(operator, "Hard Challenge", world.options.hard_challenge_value.value))
                added_regions += 1
        
        
        regions[-1 - added_regions].add_event(operator + " Complete", rule = create_operator_completion_rule(world, operator), location_type = locations.R6SiegeLocation, item_type = items.R6SiegeItem)


    world.set_completion_rule(HasFromList(*[n.name for n in world.get_locations() if n.name[-8:] == "Complete"], count = world.options.goal_operators.value))
    world.multiworld.regions += regions