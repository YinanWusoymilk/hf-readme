import os
import requests
import json
import time
import yaml
import threading
from queue import Queue

class HuggingFaceAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://huggingface.co'
        self.interval = 0.1  # 设置间隔时间（秒）

    def download_readme(self, model_id):
        readme_url = f"https://huggingface.co/{model_id}/raw/main/README.md"
        response = requests.get(readme_url, headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code == 200:
            safe_model_id = model_id.replace("/", "_")
            # 修改保存路径
            save_dir = 'f:/hf-readme/readme file collection/readme by likes'
            filename = os.path.join(save_dir, f'{safe_model_id}.md')
            os.makedirs(save_dir, exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            return True, filename  # 下载成功
        else:
            return False, None  # 下载失败

def load_existing_results(json_file):
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return {}

def worker(api_key, model_queue, readme_results, lock, thread_id):
    hf_api = HuggingFaceAPI(api_key)
    while not model_queue.empty():
        model_id = model_queue.get()
        print(f"Thread {thread_id} is checking README for model: {model_id}")
        try:
            success, filename = hf_api.download_readme(model_id)
            if success:
                print(f"Thread {thread_id} successfully downloaded README to {filename}")
                with lock:
                    readme_results[model_id] = filename
            else:
                print(f"Thread {thread_id} failed to download README for model: {model_id}")
                with lock:
                    readme_results[model_id] = 'Failed to download'
        except Exception as e:
            print(f"Thread {thread_id} encountered an error with model {model_id}: {e}")
            with lock:
                readme_results[model_id] = {'error': str(e)}
        finally:
            time.sleep(hf_api.interval)
            model_queue.task_done()

def main():
    with open('f:/hf-readme/readme file collection/config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    model_queue = Queue()
    readme_results = load_existing_results('f:/hf-readme/readme file collection/readme_results_likes.json')  # 加载现有结果
    lock = threading.Lock()

    with open('f:/hf-readme/metadata extraction/popular_metadata_sorted_by_likes.json', 'r', encoding='utf-8') as f:
        model_list = json.load(f)

    start_index = 0  # 根据需要调整这些索引
    end_index = 3000

    # 仅加载指定范围内且未处理过的模型
    for index, model in enumerate(model_list[start_index:end_index]):
        model_id = model.get('modelId')
        if model_id not in readme_results:  # 检查是否已处理
            model_queue.put(model_id)
        else:
            print(f"Model {model_id} README already downloaded or previously failed. Skipping.")

    threads = []
    for i, api_key in enumerate(config['huggingface_keys']):
        thread = threading.Thread(target=worker, args=(api_key, model_queue, readme_results, lock, i+1))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # 将结果保存到 JSON 文件
    with open('f:/hf-readme/readme file collection/readme_results_likes.json', 'w', encoding='utf-8') as f:
        json.dump(readme_results, f, indent=4)

if __name__ == '__main__':
    main()
