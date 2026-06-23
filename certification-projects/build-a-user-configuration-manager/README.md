# Build a User Configuration Manager

A Python-based configuration management system developed as part of the freeCodeCamp Python Certification.

This project implements a simple user settings manager that allows users to add, update, delete, and display configuration settings.

---

## Objective

Develop a configuration management system using Python dictionaries and functions while applying input validation, string processing, and data manipulation techniques.

---

## Features

* Add new settings
* Update existing settings
* Delete existing settings
* Display all settings
* Normalize input using lowercase conversion
* Validate existing keys
* Generate formatted output

---

## Example Configuration

```python
test_settings = {
    "theme": "dark",
    "language": "vietnamese",
    "notifications": "enabled",
}
```

---

## Functions Implemented

### add_setting()

Adds a new setting to the dictionary.

```python
def add_setting(settings, setting):
```

Example:

```python
add_setting(
    test_settings,
    ("volume", "high")
)
```

Result:

```text
Setting 'volume' added with value 'high' successfully!
```

---

### update_setting()

Updates an existing setting.

```python
def update_setting(settings, setting):
```

Example:

```python
update_setting(
    test_settings,
    ("theme", "light")
)
```

Result:

```text
Setting 'theme' updated to 'light' successfully!
```

---

### delete_setting()

Removes a setting from the dictionary.

```python
def delete_setting(settings, key):
```

Example:

```python
delete_setting(
    test_settings,
    "theme"
)
```

Result:

```text
Setting 'theme' deleted successfully!
```

---

### view_settings()

Displays all user settings.

```python
def view_settings(settings):
```

Output:

```text
Current User Settings:
Theme: dark
Language: vietnamese
Notifications: enabled
```

---

## Concepts Practiced

### Dictionaries

Store settings as key-value pairs.

```python
settings["theme"] = "dark"
```

---

### Tuple Unpacking

Extract values from a tuple.

```python
key, value = setting
```

---

### String Methods

Normalize and format text.

```python
key.lower()
key.capitalize()
```

---

### Dictionary Operations

Add values:

```python
settings[key] = value
```

Delete values:

```python
del settings[key]
```

Check existing keys:

```python
if key in settings:
```

---

### Conditional Statements

```python
if key in settings:
```

```python
if not settings:
```

---

### Iteration

Loop through dictionary items.

```python
for key, value in settings.items():
```

---

## Skills Developed

* Dictionary manipulation
* Configuration management
* Input normalization
* Data validation
* Function design
* String processing
* Conditional logic
* Formatted output
* Problem-solving

---

## Test Results

* Passed all 27 tests.
* Successfully implemented all required user stories.

---

## Status

✅ Completed

---

## Part of

freeCodeCamp Python Certification

