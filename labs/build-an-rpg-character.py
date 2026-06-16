full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):

    # Validate the character name type.
    # 'not isinstance()'detects invalid data tupe before
    # any further validation is performed.
    if not isinstance(character_name, str):
        return "The character name should be a string"
    
    # Validate that the character has a name.
    if character_name == "":
        return "The character should have a name"

    # Validate the maximum allowed name length.
    if len(character_name) > 10:
        return "The character name is too long"

    # Validate that the name does not contain spaces.   
    if " " in character_name:
        return "The character name should not contain spaces" 
    
    # Validate stats type.
    # All stats should be integers
    #-> because they represent fixed RPG points
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"

    # Validate minimum stat value.
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"  

    # Validate maximum stat value.
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # Validate total starting points.
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points" 

    # Build the character stat lines.
    strength_line = "STR " + full_dot * strength + empty_dot *(10 - strength)

    intelligence_line = "INT " + full_dot * intelligence + empty_dot *(10 - intelligence)

    charisma_line = "CHA " + full_dot * charisma + empty_dot *(10 - charisma)

    return character_name + "\n" + strength_line + "\n" + intelligence_line + "\n" + charisma_line
