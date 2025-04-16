import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-ILO5zxFy0f",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

result = []
for file_name in ["巧克力.png","豆奶.png"]:
    completion = client.chat.completions.create(
        model="qwen-vl-max-latest",
        messages=[
            {
                "role": "system",
                "content": [{"type": "text", "text": "You are a helpful assistant."}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encode_image(file_name)}"
                        },
                    },
                    {"type": "text", "text": """
                            提取图中内容，按照json格式输出如下,只输出纯json字符就行，不要夹杂换行符
    {
    "product_name": "xxxx",
    "product_type": "xxxx",
    "shelf_life": "xxxx",
    "ingredients": "xxxx.",
    "product_standard_code": "xxxx",
    "storage_conditions": "xxxx",
    "food_production_license_number": "xxxx",
    "production_date": "xxxx",
    "manufacturer": "xxxx",
    "address": "xxxx",
    "phone": "xxxx",
    "fax": "xxxx",
    "place_of_origin": "xxxx"
    }
                    """},
                ],
            },
        ],
    )

    result.append(completion.choices[0].message.content)

print(result)