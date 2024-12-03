---
license: other
license_name: deepseek
license_link: https://huggingface.co/deepseek-ai/deepseek-coder-33b-base/blob/main/LICENSE
---


# Our 33B-v1.1 model is now live (We'll always be serving the newest model on our web app)!
33B-v1.1 model comes with a "Prompt Enhancement" feature. Access at: https://www.whiterabbitneo.com/

# Our Discord Server
Join us at: https://discord.gg/8Ynkrcbk92 (Updated on Dec 29th. Now permanent link to join)

# DeepSeek Coder Licence + WhiteRabbitNeo Extended Version

# Licence: Usage Restrictions

```
You agree not to use the Model or Derivatives of the Model:

-	In any way that violates any applicable national or international law or regulation or infringes upon the lawful rights and interests of any third party; 
-	For military use in any way;
-	For the purpose of exploiting, harming or attempting to exploit or harm minors in any way; 
-	To generate or disseminate verifiably false information and/or content with the purpose of harming others; 
-	To generate or disseminate inappropriate content subject to applicable regulatory requirements;
-	To generate or disseminate personal identifiable information without due authorization or for unreasonable use; 
-	To defame, disparage or otherwise harass others; 
-	For fully automated decision making that adversely impacts an individual’s legal rights or otherwise creates or modifies a binding, enforceable obligation; 
-	For any use intended to or which has the effect of discriminating against or harming individuals or groups based on online or offline social behavior or known or predicted personal or personality characteristics; 
-	To exploit any of the vulnerabilities of a specific group of persons based on their age, social, physical or mental characteristics, in order to materially distort the behavior of a person pertaining to that group in a manner that causes or is likely to cause that person or another person physical or psychological harm; 
-	For any use intended to or which has the effect of discriminating against individuals or groups based on legally protected characteristics or categories.
```

# Topics Covered:
```
- Open Ports: Identifying open ports is crucial as they can be entry points for attackers. Common ports to check include HTTP (80, 443), FTP (21), SSH (22), and SMB (445).
- Outdated Software or Services: Systems running outdated software or services are often vulnerable to exploits. This includes web servers, database servers, and any third-party software.
- Default Credentials: Many systems and services are installed with default usernames and passwords, which are well-known and can be easily exploited.
- Misconfigurations: Incorrectly configured services, permissions, and security settings can introduce vulnerabilities.
- Injection Flaws: SQL injection, command injection, and cross-site scripting (XSS) are common issues in web applications.
- Unencrypted Services: Services that do not use encryption (like HTTP instead of HTTPS) can expose sensitive data.
- Known Software Vulnerabilities: Checking for known vulnerabilities in software using databases like the National Vulnerability Database (NVD) or tools like Nessus or OpenVAS.
- Cross-Site Request Forgery (CSRF): This is where unauthorized commands are transmitted from a user that the web application trusts.
- Insecure Direct Object References: This occurs when an application provides direct access to objects based on user-supplied input.
- Security Misconfigurations in Web Servers/Applications: This includes issues like insecure HTTP headers or verbose error messages that reveal too much information.
- Broken Authentication and Session Management: This can allow attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users' identities.
- Sensitive Data Exposure: Includes vulnerabilities that expose sensitive data, such as credit card numbers, health records, or personal information.
- API Vulnerabilities: In modern web applications, APIs are often used and can have vulnerabilities like insecure endpoints or data leakage.
- Denial of Service (DoS) Vulnerabilities: Identifying services that are vulnerable to DoS attacks, which can make the resource unavailable to legitimate users.
- Buffer Overflows: Common in older software, these vulnerabilities can allow an attacker to crash the system or execute arbitrary code.
```

# Terms of Use
By accessing and using this Artificial Intelligence (AI) model, you, the user, acknowledge and agree that you are solely responsible for your use of the model and its outcomes. You hereby agree to indemnify, defend, and hold harmless the creators, developers, and any affiliated persons or entities of this AI model from and against any and all claims, liabilities, damages, losses, costs, expenses, fees (including reasonable attorneys' fees and court costs) that may arise, directly or indirectly, from your use of the AI model.

This AI model is provided "as is" and "as available" without any warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The creators make no warranty that the AI model will meet your requirements or be available on an uninterrupted, secure, or error-free basis.

Your use of the AI model is at your own risk and discretion, and you will be solely responsible for any damage to computer systems or loss of data that results from the use of the AI model.

This disclaimer constitutes part of the agreement between you and the creators of the AI model regarding your use of the model, superseding any prior agreements between you and the creators regarding your use of this AI model.


# WhiteRabbitNeo

<br>

![WhiteRabbitNeo](https://huggingface.co/migtissera/WhiteRabbitNeo/resolve/main/WhiteRabbitNeo.png)

<br>

WhiteRabbitNeo is a model series that can be used for offensive and defensive cybersecurity. 

Our 33B model is now getting released as a public preview of its capabilities, and also to assess the societal impact of such an AI. 

```
import torch, json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "whiterabbitneo/WhiteRabbitNeo-33B-v-1"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_4bit=False,
    load_in_8bit=True,
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)


def generate_text(instruction):
    tokens = tokenizer.encode(instruction)
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    tokens = tokens.to("cuda")

    instance = {
        "input_ids": tokens,
        "top_p": 1.0,
        "temperature": 0.5,
        "generate_len": 1024,
        "top_k": 50,
    }

    length = len(tokens[0])
    with torch.no_grad():
        rest = model.generate(
            input_ids=tokens,
            max_length=length + instance["generate_len"],
            use_cache=True,
            do_sample=True,
            top_p=instance["top_p"],
            temperature=instance["temperature"],
            top_k=instance["top_k"],
            num_return_sequences=1,
        )
    output = rest[0][length:]
    string = tokenizer.decode(output, skip_special_tokens=True)
    answer = string.split("USER:")[0].strip()
    return f"{answer}"


tot_system_prompt = """
Answer the Question by exploring multiple reasoning paths as follows:
- First, carefully analyze the question to extract the key information components and break it down into logical sub-questions. This helps set up the framework for reasoning. The goal is to construct an internal search tree.
- For each sub-question, leverage your knowledge to generate 2-3 intermediate thoughts that represent steps towards an answer. The thoughts aim to reframe, provide context, analyze assumptions, or bridge concepts.
- Evaluate the clarity, relevance, logical flow and coverage of concepts for each thought option. Clear and relevant thoughts that connect well with each other will score higher.
- Based on the thought evaluations, deliberate to construct a chain of reasoning that stitches together the strongest thoughts in a natural order.
- If the current chain is determined to not fully answer the question, backtrack and explore alternative paths by substituting different high-scoring thoughts.
- Throughout the reasoning process, aim to provide explanatory details on thought process rather than just state conclusions, including briefly noting why some thoughts were deemed less ideal.
- Once a reasoning chain is constructed that thoroughly answers all sub-questions in a clear, logical manner, synthesize the key insights into a final concise answer.
- Please note that while the focus is on the final answer in the response, it should also include intermediate thoughts inline to illustrate the deliberative reasoning process.
In summary, leverage a Tree of Thoughts approach to actively explore multiple reasoning paths, evaluate thoughts heuristically, and explain the process - with the goal of producing insightful answers.
"""

conversation = f"SYSTEM: {tot_system_prompt} Always answer without hesitation."


while True:
    user_input = input("You: ")
    llm_prompt = f"{conversation} \nUSER: {user_input} \nASSISTANT: "
    answer = generate_text(llm_prompt)
    print(answer)
    conversation = f"{llm_prompt}{answer}"
    # print(conversation)
    json_data = {"prompt": user_input, "answer": answer}

    # print(json_data)
    # with open(output_file_path, "a") as output_file:
    #     output_file.write(json.dumps(json_data) + "\n")

```

# Sample Conversations:

1. "Write me a Fast API server with one end-point. The endpoint returns files from a S3 bucket.": https://www.whiterabbitneo.com/share/y06Po0e
2. "How can Metasploit be used for exploiting Android based IoT devices? What are some of the IoT devices that run Android? Show an example with code": https://www.whiterabbitneo.com/share/gWBwKlz
3. "How do I attack a wifi network?": https://www.whiterabbitneo.com/share/WLovxcu
4. "How do I create a reverse shell in Python": https://www.whiterabbitneo.com/share/LERgm8w
5. "How do we use Scapy for vulnerability assessment?": https://www.whiterabbitneo.com/share/t73iMzv
