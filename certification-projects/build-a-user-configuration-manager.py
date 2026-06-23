# ==========================================================
# Test 1:
# Create a dictionary named test_settings.
#
# A dictionary is used because each setting has:
# - a key (setting name)
# - a value (setting value)
#
# Example:
# theme -> dark
# language -> vietnamese
# ==========================================================

test_settings = {
    "theme": "dark",
    "language": "vietnamese",
    "notifications": "enabled",
}


# ==========================================================
# Tests 2-8:
# add_setting()
#
# This function:
# 1. Receives a dictionary of settings.
# 2. Receives a tuple containing (key, value).
# 3. Converts both values to lowercase.
# 4. Checks whether the setting already exists.
# 5. Adds the setting if it does not exist.
# ==========================================================

def add_setting(settings, setting):

    # Unpack the tuple.
    #
    # Example:
    # ("Theme", "Dark")
    #
    # key = "Theme"
    # value = "Dark"

    key, value = setting

    # Convert the key to lowercase.
    #
    # "THEME" -> "theme"

    key = key.lower()

    # Convert the value to lowercase.
    #
    # "DARK" -> "dark"

    value = value.lower()

    # Check whether the key already exists.
    #
    # The 'in' operator returns True or False.

    if key in settings:

        # Return an error message if the key exists.

        return (
            f"Setting '{key}' already exists! "
            f"Cannot add a new setting with this name."
        )

    # Add a new key-value pair.
    #
    # Example:
    # settings["volume"] = "high"

    settings[key] = value

    # Return a success message.

    return (
        f"Setting '{key}' added with value "
        f"'{value}' successfully!"
    )


# ==========================================================
# Tests 9-15:
# update_setting()
#
# This function updates an existing setting.
# It does not create a new setting.
# ==========================================================

def update_setting(settings, setting):

    # Unpack the tuple into two variables.

    key, value = setting

    # Convert both values to lowercase.

    key = key.lower()
    value = value.lower()

    # Check if the key exists.

    if key in settings:

        # Replace the old value.
        #
        # Example:
        # theme: dark
        # ->
        # theme: light

        settings[key] = value

        return (
            f"Setting '{key}' updated to "
            f"'{value}' successfully!"
        )

    # Return an error if the key is missing.

    return (
        f"Setting '{key}' does not exist! "
        f"Cannot update a non-existing setting."
    )


# ==========================================================
# Tests 16-21:
# delete_setting()
#
# This function removes a setting from the dictionary.
# ==========================================================

def delete_setting(settings, key):

    # Convert the key to lowercase.

    key = key.lower()

    # Check if the key exists.

    if key in settings:

        # Remove the key-value pair.
        #
        # Example:
        # del settings["theme"]

        del settings[key]

        return (
            f"Setting '{key}' deleted successfully!"
        )

    # Return an error message.

    return "Setting not found!"


# ==========================================================
# Tests 22-27:
# view_settings()
#
# This function displays all user settings.
# ==========================================================

def view_settings(settings):

    # An empty dictionary evaluates to False.
    #
    # {} -> False

    if not settings:
        return "No settings available."

    # Create the first line of the output.

    result = "Current User Settings:\n"

    # items() returns both key and value.
    #
    # Example:
    # ("theme", "dark")

    for key, value in settings.items():

        # capitalize() converts:
        #
        # "theme"
        # ->
        # "Theme"

        result += (
            f"{key.capitalize()}: {value}\n"
        )

    # Return the completed string.

    return result
