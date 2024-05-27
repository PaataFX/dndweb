import json

bard_spell_slots = {
    1: {'max_spells': 4, 'max_cantrips': 2, 'spell_table': [2, 0, 0, 0, 0, 0, 0, 0, 0]},
    2: {'max_spells': 5, 'max_cantrips': 3, 'spell_table': [3, 0, 0, 0, 0, 0, 0, 0, 0]},
    3: {'max_spells': 6, 'max_cantrips': 4, 'spell_table': [4, 2, 0, 0, 0, 0, 0, 0, 0]},
    4: {'max_spells': 7, 'max_cantrips': 4, 'spell_table': [4, 3, 0, 0, 0, 0, 0, 0, 0]},
    5: {'max_spells': 8, 'max_cantrips': 4, 'spell_table': [4, 3, 2, 0, 0, 0, 0, 0, 0]},
    6: {'max_spells': 9, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 0, 0, 0, 0, 0, 0]},
    7: {'max_spells': 10, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 1, 0, 0, 0, 0, 0]},
    8: {'max_spells': 11, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 2, 0, 0, 0, 0, 0]},
    9: {'max_spells': 12, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 1, 0, 0, 0, 0]},
    10: {'max_spells': 14, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 0, 0, 0, 0]},
    11: {'max_spells': 15, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    12: {'max_spells': 15, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    13: {'max_spells': 16, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    14: {'max_spells': 18, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    15: {'max_spells': 19, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    16: {'max_spells': 19, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    17: {'max_spells': 20, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    18: {'max_spells': 22, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    19: {'max_spells': 22, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    20: {'max_spells': 22, 'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]}
}

cleric_spell_slots = {
    1: {'max_cantrips': 2, 'spell_table': [2, 0, 0, 0, 0, 0, 0, 0, 0]},
    2: {'max_cantrips': 3, 'spell_table': [3, 0, 0, 0, 0, 0, 0, 0, 0]},
    3: {'max_cantrips': 4, 'spell_table': [4, 2, 0, 0, 0, 0, 0, 0, 0]},
    4: {'max_cantrips': 4, 'spell_table': [4, 3, 0, 0, 0, 0, 0, 0, 0]},
    5: {'max_cantrips': 4, 'spell_table': [4, 3, 2, 0, 0, 0, 0, 0, 0]},
    6: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 0, 0, 0, 0, 0, 0]},
    7: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 1, 0, 0, 0, 0, 0]},
    8: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 2, 0, 0, 0, 0, 0]},
    9: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 1, 0, 0, 0, 0]},
    10: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 0, 0, 0, 0]},
    11: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    12: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    13: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    14: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    15: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    16: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    17: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    18: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    19: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    20: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]}
}

druid_spell_slots = {
    1: {'max_cantrips': 2, 'spell_table': [2, 0, 0, 0, 0, 0, 0, 0, 0]},
    2: {'max_cantrips': 3, 'spell_table': [3, 0, 0, 0, 0, 0, 0, 0, 0]},
    3: {'max_cantrips': 4, 'spell_table': [4, 2, 0, 0, 0, 0, 0, 0, 0]},
    4: {'max_cantrips': 4, 'spell_table': [4, 3, 0, 0, 0, 0, 0, 0, 0]},
    5: {'max_cantrips': 4, 'spell_table': [4, 3, 2, 0, 0, 0, 0, 0, 0]},
    6: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 0, 0, 0, 0, 0, 0]},
    7: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 1, 0, 0, 0, 0, 0]},
    8: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 2, 0, 0, 0, 0, 0]},
    9: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 1, 0, 0, 0, 0]},
    10: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 0, 0, 0, 0]},
    11: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    12: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    13: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    14: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    15: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    16: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    17: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    18: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    19: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    20: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]}
}

paladin_spell_slots = {
    1: {'max_cantrips': 0, 'spell_table': [0, 0, 0, 0, 0]},
    2: {'max_cantrips': 2, 'spell_table': [2, 0, 0, 0, 0]},
    3: {'max_cantrips': 3, 'spell_table': [3, 0, 0, 0, 0]},
    4: {'max_cantrips': 3, 'spell_table': [3, 2, 0, 0, 0]},
    5: {'max_cantrips': 3, 'spell_table': [3, 3, 0, 0, 0]},
    6: {'max_cantrips': 3, 'spell_table': [3, 3, 0, 0, 0]},
    7: {'max_cantrips': 3, 'spell_table': [3, 3, 1, 0, 0]},
    8: {'max_cantrips': 3, 'spell_table': [3, 3, 2, 0, 0]},
    9: {'max_cantrips': 4, 'spell_table': [3, 3, 3, 0, 0]},
    10: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 0, 0]},
    11: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 1, 0]},
    12: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 1, 0]},
    13: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 2, 0]},
    14: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 2, 0]},
    15: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 0]},
    16: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 0]},
    17: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 1]},
    18: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 1]},
    19: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 2]},
    20: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 2]}
}

ranger_spell_slots = {
    1: {'max_cantrips': 0, 'spell_table': [0, 0, 0, 0, 0]},
    2: {'max_cantrips': 2, 'spell_table': [2, 0, 0, 0, 0]},
    3: {'max_cantrips': 3, 'spell_table': [3, 0, 0, 0, 0]},
    4: {'max_cantrips': 3, 'spell_table': [3, 2, 0, 0, 0]},
    5: {'max_cantrips': 3, 'spell_table': [3, 3, 0, 0, 0]},
    6: {'max_cantrips': 3, 'spell_table': [3, 3, 0, 0, 0]},
    7: {'max_cantrips': 3, 'spell_table': [3, 3, 1, 0, 0]},
    8: {'max_cantrips': 3, 'spell_table': [3, 3, 2, 0, 0]},
    9: {'max_cantrips': 4, 'spell_table': [3, 3, 3, 0, 0]},
    10: {'max_cantrips': 4, 'spell_table': [4, 3, 3, 0, 0]},
    11: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 1, 0]},
    12: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 1, 0]},
    13: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 2, 0]},
    14: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 2, 0]},
    15: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 0]},
    16: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 0]},
    17: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 1]},
    18: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 1]},
    19: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 2]},
    20: {'max_cantrips': 4, 'spell_table': [4, 4, 3, 3, 2]}
}

sorcerer_spell_slots = {
    1: {'max_spells': 4, 'max_cantrips': 4, 'spell_table': [2, 0, 0, 0, 0, 0, 0, 0, 0]},
    2: {'max_spells': 4, 'max_cantrips': 4, 'spell_table': [3, 0, 0, 0, 0, 0, 0, 0, 0]},
    3: {'max_spells': 4, 'max_cantrips': 4, 'spell_table': [4, 2, 0, 0, 0, 0, 0, 0, 0]},
    4: {'max_spells': 5, 'max_cantrips': 5, 'spell_table': [4, 3, 0, 0, 0, 0, 0, 0, 0]},
    5: {'max_spells': 6, 'max_cantrips': 5, 'spell_table': [4, 3, 2, 0, 0, 0, 0, 0, 0]},
    6: {'max_spells': 7, 'max_cantrips': 5, 'spell_table': [4, 3, 3, 0, 0, 0, 0, 0, 0]},
    7: {'max_spells': 8, 'max_cantrips': 5, 'spell_table': [4, 3, 3, 1, 0, 0, 0, 0, 0]},
    8: {'max_spells': 9, 'max_cantrips': 5, 'spell_table': [4, 3, 3, 2, 0, 0, 0, 0, 0]},
    9: {'max_spells': 10, 'max_cantrips': 5, 'spell_table': [4, 3, 3, 3, 1, 0, 0, 0, 0]},
    10: {'max_spells': 11, 'max_cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 0, 0, 0, 0]},
    11: {'max_spells': 12, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    12: {'max_spells': 12, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    13: {'max_spells': 13, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    14: {'max_spells': 13, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    15: {'max_spells': 14, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    16: {'max_spells': 14, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    17: {'max_spells': 15, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]},
    18: {'max_spells': 15, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]},
    19: {'max_spells': 15, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]},
    20: {'max_spells': 15, 'max_cantrips': 6, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]}
}

warlock_spell_slots = [
    {'cantrips': 2, 'spells_known': 2, 'spells_ready': 1, 'spell_level': 'I', 'spell_slots': '-'},
    {'cantrips': 2, 'spells_known': 3, 'spells_ready': 2, 'spell_level': 'I', 'spell_slots': 2},
    {'cantrips': 2, 'spells_known': 4, 'spells_ready': 2, 'spell_level': 'II', 'spell_slots': 2},
    {'cantrips': 3, 'spells_known': 5, 'spells_ready': 2, 'spell_level': 'II', 'spell_slots': 2},
    {'cantrips': 3, 'spells_known': 6, 'spells_ready': 2, 'spell_level': 'III', 'spell_slots': 3},
    {'cantrips': 3, 'spells_known': 7, 'spells_ready': 2, 'spell_level': 'III', 'spell_slots': 3},
    {'cantrips': 3, 'spells_known': 8, 'spells_ready': 2, 'spell_level': 'IV', 'spell_slots': 4},
    {'cantrips': 3, 'spells_known': 9, 'spells_ready': 2, 'spell_level': 'IV', 'spell_slots': 4},
    {'cantrips': 3, 'spells_known': 10, 'spells_ready': 2, 'spell_level': 'V', 'spell_slots': 5},
    {'cantrips': 4, 'spells_known': 10, 'spells_ready': 2, 'spell_level': 'V', 'spell_slots': 5},
    {'cantrips': 4, 'spells_known': 11, 'spells_ready': 3, 'spell_level': 'V', 'spell_slots': 5},
    {'cantrips': 4, 'spells_known': 11, 'spells_ready': 3, 'spell_level': 'V', 'spell_slots': 6},
    {'cantrips': 4, 'spells_known': 12, 'spells_ready': 3, 'spell_level': 'V', 'spell_slots': 6},
    {'cantrips': 4, 'spells_known': 12, 'spells_ready': 3, 'spell_level': 'V', 'spell_slots': 6},
    {'cantrips': 4, 'spells_known': 13, 'spells_ready': 3, 'spell_level': 'V', 'spell_slots': 7},
    {'cantrips': 4, 'spells_known': 13, 'spells_ready': 3, 'spell_level': 'V', 'spell_slots': 7},
    {'cantrips': 4, 'spells_known': 14, 'spells_ready': 4, 'spell_level': 'V', 'spell_slots': 7},
    {'cantrips': 4, 'spells_known': 14, 'spells_ready': 4, 'spell_level': 'V', 'spell_slots': 8},
    {'cantrips': 4, 'spells_known': 15, 'spells_ready': 4, 'spell_level': 'V', 'spell_slots': 8},
    {'cantrips': 4, 'spells_known': 15, 'spells_ready': 4, 'spell_level': 'V', 'spell_slots': 8}
]

wizard_spell_slots = {
    1: {'cantrips': 3, 'spell_table': [2, 0, 0, 0, 0, 0, 0, 0, 0]},
    2: {'cantrips': 3, 'spell_table': [3, 0, 0, 0, 0, 0, 0, 0, 0]},
    3: {'cantrips': 3, 'spell_table': [4, 2, 0, 0, 0, 0, 0, 0, 0]},
    4: {'cantrips': 4, 'spell_table': [4, 3, 0, 0, 0, 0, 0, 0, 0]},
    5: {'cantrips': 4, 'spell_table': [4, 3, 2, 0, 0, 0, 0, 0, 0]},
    6: {'cantrips': 4, 'spell_table': [4, 3, 3, 0, 0, 0, 0, 0, 0]},
    7: {'cantrips': 4, 'spell_table': [4, 3, 3, 1, 0, 0, 0, 0, 0]},
    8: {'cantrips': 4, 'spell_table': [4, 3, 3, 2, 0, 0, 0, 0, 0]},
    9: {'cantrips': 4, 'spell_table': [4, 3, 3, 3, 1, 0, 0, 0, 0]},
    10: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 0, 0, 0, 0]},
    11: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    12: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 0, 0, 0]},
    13: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    14: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 0, 0]},
    15: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    16: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 0]},
    17: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]},
    18: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]},
    19: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]},
    20: {'cantrips': 5, 'spell_table': [4, 3, 3, 3, 2, 1, 1, 1, 1]}
}

artificer_spell_slots = {
    1: {'cantrips': 2, 'spell_table': [2, 0, 0, 0, 0]},
    2: {'cantrips': 2, 'spell_table': [2, 0, 0, 0, 0]},
    3: {'cantrips': 2, 'spell_table': [3, 0, 0, 0, 0]},
    4: {'cantrips': 2, 'spell_table': [3, 0, 0, 0, 0]},
    5: {'cantrips': 2, 'spell_table': [4, 2, 0, 0, 0]},
    6: {'cantrips': 2, 'spell_table': [4, 2, 0, 0, 0]},
    7: {'cantrips': 2, 'spell_table': [4, 3, 0, 0, 0]},
    8: {'cantrips': 2, 'spell_table': [4, 3, 0, 0, 0]},
    9: {'cantrips': 2, 'spell_table': [4, 3, 2, 0, 0]},
    10: {'cantrips': 3, 'spell_table': [4, 3, 2, 0, 0]},
    11: {'cantrips': 3, 'spell_table': [4, 3, 3, 0, 0]},
    12: {'cantrips': 3, 'spell_table': [4, 3, 3, 0, 0]},
    13: {'cantrips': 3, 'spell_table': [4, 3, 3, 1, 0]},
    14: {'cantrips': 4, 'spell_table': [4, 3, 3, 1, 0]},
    15: {'cantrips': 4, 'spell_table': [4, 3, 3, 2, 0]},
    16: {'cantrips': 4, 'spell_table': [4, 3, 3, 2, 0]},
    17: {'cantrips': 4, 'spell_table': [4, 3, 3, 3, 1]},
    18: {'cantrips': 4, 'spell_table': [4, 3, 3, 3, 1]},
    19: {'cantrips': 4, 'spell_table': [4, 3, 3, 3, 2]},
    20: {'cantrips': 4, 'spell_table': [4, 3, 3, 3, 2]}
}

spell_slot_dicts = {
    "bard_spell_slots": bard_spell_slots,
    "cleric_spell_slots": cleric_spell_slots,
    "druid_spell_slots": druid_spell_slots,
    "paladin_spell_slots": paladin_spell_slots,
    "ranger_spell_slots": ranger_spell_slots,
    "sorcerer_spell_slots": sorcerer_spell_slots,
    "warlock_spell_slots": warlock_spell_slots,
    "wizard_spell_slots": wizard_spell_slots,
    "artificer_spell_slots": artificer_spell_slots
}

# Save each spell slot dictionary to a separate JSON file
for spell_slot_name, spell_slot_data in spell_slot_dicts.items():
    with open(f"{spell_slot_name}.json", "w") as file:
        json.dump(spell_slot_data, file, indent=4)