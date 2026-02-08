candidate = {"name": "Nayan", "age": 20}

# Access
print(candidate["name"])

# Update
candidate["age"] = 23

# Add
candidate["city"] = "mumbai"

# Remove
del candidate["city"]

# Merge
d2 = {"course": "Python"}
candidate.update(d2)

print(candidate)
