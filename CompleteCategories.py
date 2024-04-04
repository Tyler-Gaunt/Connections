### tyler gaunt's connections - Categories ###
### for use in the MainCode.py ###
### to add more, simply add more dictionaries below and add them to categories list ###

#currently 21 categories
import random

def return_categories():
    cars = {
        "Category_name": "CARS",
        "words": ["SUBARU", "FORD", "TOYOTA", "AUDI"]
    }
    IIID_Shapes = {
        "Category_name": "3D SHAPES",
        "words": ["CONE", "CUBE", "PYRAMID", "SPHERE"]
    }
    complain = {
        "Category_name": "SYNONYMS FOR COMPLAIN",
        "words": ["CARP", "GRIPE", "GROUSE", "MOAN"]
    }
    wings = {
        "Category_name": "THINGS WITH WINGS",
        "words": ["AIRPLANE", "ANGEL", "BIRD", "PEGESAUS"]
    }
    Tom = {
        "Category_name": "FAMOUS TOMS",
        "words": ["CRUISE", "HOLLAND", "PETTY", "HARDY"]
    }
    animal_noses = {
        "Category_name": "ANIMAL NOSE",
        "words": ["SNOUT", "BEAK", "MUZZLE", "TRUNK"]
    }
    common_colours = {
        "Category_name": "COMMON COLOURS",
        "words": ["BLUE", "GREEN", "YELLOW", "RED"]
    }
    uncommon_colours = {
        "Category_name": "UNCOMMON COLOURS",
        "words": ["ULTRAMARINE", "CELADON", "AURELINE", "VERMILION"]
    }
    animal_groups = {
        "Category_name": "GROUPS OF ANIMALS",
        "words": ["SCHOOL", "FLOCK", "POD", "PACK"]
    }
    island_countries = {
        "Category_name": "ISLAND COUNTRIES",
        "words": ["MALTA", "CUBA", "PALAU", "CYPRUS"]
    }
    celestial_objects = {
        "Category_name": "CELESTIAL OBJECTS",
        "words": ["PLANET", "COMET", "MOON", "ASTEROID"]
    }
    keyboard_keys = {
        "Category_name": "KEYBOARD KEYS",
        "words": ["ESCAPE", "SPACE", "CONTROL", "SHIFT"]
    }
    movie_summary = {
        "Category_name": "MOVIE SUMMARY INFO",
            "words": ["CAST", "GENRE", "PLOT", "TITLE"]
    }
    greek_mythology = {
        "Category_name": "GREEK MYTHOLOGY",
        "words": ["PERSEPHONE", "HEPHAESTUS", "EROS", "NEMESIS"]
    }
    astronomical_phenomena = {
        "Category_name": "ASTRONOMICAL PHENOMENA",
        "words": ["SUPERNOVA", "BLACK HOLE", "QUASAR", "GAMMA-RAY BURST"]
    }
    religions = {
        "Category_name": "MAJOR RELIGIONS",
        "words": ["CHRISTIANITY", "ISLAM", "HINDUISM", "BUDDHISM"]
    }
    chemical_compounds = {
        "Category_name": "CHEMICAL COMPOUNDS",
        "words": ["WATER", "CARBON DIOXIDE", "SULFURIC ACID", "AMMONIA"]
    }
    rivers = {
        "Category_name": "MAJOR RIVERS",
        "words": ["NILE", "AMAZON", "YANGTZE", "MISSISSIPPI"]
    }
    us_states = {
        "Category_name": "US STATES",
        "words": ["CALIFORNIA", "TEXAS", "FLORIDA", "NEW YORK"]
    }
    human_bones = {
        "Category_name": "HUMAN BONES",
        "words": ["FEMUR", "RADIUS", "SKULL", "TIBIA"]
    }
    gemstones  = {
        "Category_name": "GEMSTONES",
        "words": ["DIAMOND", "RUBY", "EMERALD", "SAPPHIRE"]   
        }
    categories = [cars, IIID_Shapes, complain, wings, Tom, animal_noses, common_colours, uncommon_colours, animal_groups, island_countries, celestial_objects, keyboard_keys, movie_summary, greek_mythology, astronomical_phenomena, religions, chemical_compounds, rivers, us_states, human_bones, gemstones]
    selected_categories = random.sample(categories, 4) # pick four random categories
    return selected_categories
