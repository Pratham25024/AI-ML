def validate_data(data):
    invalid_entries = []
    for entry in data:
        if "age" in entry and not isinstance(entry["age"], int):
            invalid_entries.append(entry)
    return invalid_entries

# Example
data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}]
print(validate_data(data))
