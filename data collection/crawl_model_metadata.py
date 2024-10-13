from datetime import datetime

import requests
import json
import yaml
import time
import csv

class HuggingFaceAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://huggingface.co'
        self.interval = 1  # seconds，增加间隔以避免过快请求

    def set_interval(self, interval):
        self.interval = interval
    def get_all_models(self, max_results=1000):
        models = []
        next_page_url = f"/api/models?limit={max_results}"
        total_count = 0  # 初始化计数器

        while next_page_url:
            print(f"正在处理 URL: {next_page_url}")  # 打印当前处理的 URL

            response = requests.get(self.base_url + next_page_url)
            response_dict = json.loads(response.content)

            if not response_dict:
                break

            models.extend(response_dict)
            total_count += len(response_dict)
            print(f"已获取 {total_count} 个模型")

            next_link = response.links.get("next", {})
            next_page_url = next_link.get("url", "").replace(self.base_url, "") if next_link else None

            time.sleep(self.interval)

        return models


def save_to_json(hf_api):

    model_list = hf_api.get_all_models()
    model_detail_dict = {}
    count = 0
    for model in model_list:
        #print("正在处理模型:", model['modelId'])
        modelId = model['modelId']
        try:
            model_info = hf_api.get_model_info_by_id(modelId)
            model_detail_dict[modelId] = model_info
        except Exception as e:
            print(f'Error with model {modelId}: {e}')
            model_detail_dict[modelId] = {'error': str(e)}
        time.sleep(hf_api.interval)

        count += 1
        print('.', end='')
        #sys.stdout.flush()

        if count % 100== 0:
            print(f'Processed {count} models')

    with open('model_detail_dict_all.json', 'w') as f:
        json.dump(model_detail_dict, f, indent=4)

    return model_detail_dict

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as jf:
        data = json.load(jf)

        with open(csv_file, 'w', newline='', encoding='utf-8') as cf:
            writer = csv.writer(cf)

            # 写入列名，根据您的 JSON 数据结构来确定这些列名
            writer.writerow(['Model ID', 'Other Details'])

            # 遍历 JSON 列表并写入 CSV
            for model in data:
                # 您需要根据模型数据的结构来提取信息
                model_id = model['modelId']  # 例如，假设每个模型有一个 'modelId' 键
                other_details = json.dumps(model, ensure_ascii=False)  # 将模型的其他信息转换为字符串
                writer.writerow([model_id, other_details])


if __name__ == '__main__':

    # 打开并读取 YAML 文件
    with open('f:/hf-readme/data collection/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # 打印 config 变量的内容和类型
    print(config)
    print(type(config))

    # 获取 API 密钥
    api_key = config["huggingface_key"]
    print(api_key)

    hf_api = HuggingFaceAPI(api_key)

    # 调用 get_all_models 方法并获取所有模型
    all_models = hf_api.get_all_models()

    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")
    # 计算文件数
    file_count = len(all_models)
    # 构造文件名
    json_file_name = f'{current_date}_all_huggingface_models_{file_count}.json'
    csv_file_name = f'{current_date}_all_huggingface_models_{file_count}.csv'

    # 保存到../data collection
    with open(f'f:/hf-readme/data collection/{json_file_name}', 'w', encoding='utf-8') as f:
        json.dump(all_models, f, indent=4)
    print(f"模型列表已保存到 JSON 文件: f:/hf-readme/data collection/{json_file_name}")

    # 将 JSON 文件转换为 CSV 文件
    json_to_csv(f'f:/hf-readme/data collection/{json_file_name}', f'f:/hf-readme/data collection/{csv_file_name}')
    print(f"模型列表已保存到 CSV 文件: f:/hf-readme/data collection/{csv_file_name}")
