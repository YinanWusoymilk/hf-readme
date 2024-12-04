## Readme File Analyzer

This project is a web-based tool that analyzes README files from Hugging Face models. It accepts a README file as input and shows the presence or absence of key documentation components, along with the content of each present section. We fine-tuned the chatgpt4o model using our labeled data and leveraged the model in the backend. The tool visualizes both existing and missing sections, aiding developers in improving their README documentation for better clarity and completeness.

### Table of Contents

- [Prerequisites](###prerequisites)
- [Finetuning](###Finetuning)
- [Running the Tool](####Run_the_tool)
- [Appendix](####Appendix)



### Prerequisites

- **Python 3.x** installed on your system
- **pip** package manager

### Finetuning

1. **Clone the repository**
   ```bash
   git clone git@github.com:YinanWusoymilk/hf-readme.git
   cd hf-readme/training_and_application
   ```
2. **Create Virtual Environment**
   ```bash
   python3 -m venv venv-readme-genai
   source venv-readme-genai/bin/activate
   ```
3. **Set Environment Variables**
 Create a `.env` file by copying the .env.example to `.env` and set your `OPENAI_API_KEY` in the .env file 
   ```bash
   cp .env.example .env
   ```
   
4. **Dispatch the Fine-Tuning Job**
 The code for fine-tuning is in the `src` folder. Navigate to the folder and run the project:
   ```bash
   cd src
   python3 upload_file.py
   ```
   This will upload the file and dispatch the job to start fine-tuning
### Run the tool

Follow steps `1-3` in the Finetuning section.


4. **Add environment variable**
   Add the `FINE_TUNE_MODEL_ID` that you get from the fine-tuning process. If you want to skip fine-tuning and use the model we fine-tuned to save time and cost, use our model ID: `ft:gpt-4o-2024-08-06:personal::AUWHEdAd`

5. **Run the project**
 The web app is in the `web` folder. Navigate to the folder and run the project
   ```bash
   cd web
   python3 app.py
   ```
   It will start the app at `127.0.0.1:5000` by default. 
   
   
### Appendix
   
   [Traning Data](https://github.com/YinanWusoymilk/hf-readme/blob/main/training_and_application/src/readme_sections_with_chat_format.jsonl): The JSONL file needed to fine-tune the model 
   
   [Initial Dataset](https://github.com/YinanWusoymilk/hf-readme/tree/main/training_and_application/readme_files):  Dataset of top 5% README files.
   
   [Label data ](https://docs.google.com/spreadsheets/d/1wHXhcHM97zLgiJZsYCyEkP2HWW4-bZaoA7lVaknqVAA/edit?usp=sharing) : Labeled data for 200 top README files.
   
   [Evaluation](https://docs.google.com/spreadsheets/d/1Yxpfca3pIkBKJzdOjNxDRFXs1xdVCCZsu_8odgHkkaM/edit?usp=sharing): Data used for tool evaluation.
   
Other files serve as `utils` to crawl, sort, and summarize data.
 
  
