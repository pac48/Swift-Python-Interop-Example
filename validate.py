import mymodule
import json

mymodule.say_hi()

result = mymodule.add(4, 5)
print(f"4 + 5 = {result}")

# Get the result data from Swift
json_data = mymodule.get_result(1, 2)

# Convert JSON string to dict
decoder = json.JSONDecoder()
data = decoder.decode(json_data)

print(data)
