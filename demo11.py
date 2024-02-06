import json

# Python字典
data = {
    'name': 'John Doe',
    'age': 30,
    'is_employee': True,
    'salary': None,
    'projects': ['Project1', 'Project2']
}

# 序列化：将Python字典转换成JSON字符串
json_string = json.dumps(data, indent=4)
print(json_string)

# 反序列化：将JSON字符串转换回Python字典
decoded_data = json.loads(json_string)
print(decoded_data)