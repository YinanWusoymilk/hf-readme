---
license: mit
tags:
- decompile
- binary
---

### 1. Introduction of LLM4Decompile

LLM4Decompile aims to decompile x86 assembly instructions into C. The newly released V1.5 series are trained with a larger dataset (15B tokens) and a maximum token length of 4,096, with remarkable performance (up to 100% improvement) compared to the previous model.

- **Github Repository:** [LLM4Decompile](https://github.com/albertan017/LLM4Decompile)


### 2. Evaluation Results

|     Model/Benchmark    | HumanEval-Decompile |         |         |         |         | ExeBench |         |         |         |         |
|:----------------------:|:-------------------:|:-------:|:-------:|:-------:|:-------:|:--------:|:-------:|:-------:|:-------:|:-------:|
|   Optimization Level   |          O0         |    O1   |    O2   |    O3   |   AVG   |    O0    |    O1   |    O2   |    O3   |   AVG   |
|   DeepSeek-Coder-6.7B  |          0          |    0    |    0    |    0    |    0    |     0    |    0    |    0    |    0    | 0.0000  |
|         GPT-4o         |       0.3049        | 0.1159  | 0.1037  | 0.1159  | 0.1601  |  0.0443  | 0.0328  | 0.0397  | 0.0343  | 0.0378  |
| LLM4Decompile-End-1.3B |       0.4720        | 0.2061  | 0.2122  | 0.2024  | 0.2732  |  0.1786  | 0.1362  | 0.1320  | 0.1328  | 0.1449  |
| LLM4Decompile-End-6.7B |       0.6805        | 0.3951  | 0.3671  | 0.3720  | 0.4537  |  0.2289  | 0.1660  | 0.1618  | 0.1625  | 0.1798  |
|  LLM4Decompile-End-33B |       0.5168        | 0.2956  | 0.2815  | 0.2675  | 0.3404  |  0.1886  | 0.1465  | 0.1396  | 0.1411  | 0.1540  |

### 3. How to Use
Here is an example of how to use our model (Revised for V1.5).
Note: **Replace** func0 with the function name you want to decompile.

**Preprocessing:** Compile the C code into binary, and disassemble the binary into assembly instructions.
```python
import subprocess
import os

OPT = ["O0", "O1", "O2", "O3"]
fileName = 'samples/sample' #'path/to/file'
for opt_state in OPT:
    output_file = fileName +'_' + opt_state
    input_file = fileName+'.c'
    compile_command = f'gcc -o {output_file}.o {input_file} -{opt_state} -lm'#compile the code with GCC on Linux
    subprocess.run(compile_command, shell=True, check=True)
    compile_command = f'objdump -d {output_file}.o > {output_file}.s'#disassemble the binary file into assembly instructions
    subprocess.run(compile_command, shell=True, check=True)
    
    input_asm = ''
    with open(output_file+'.s') as f:#asm file
        asm= f.read()
        if '<'+'func0'+'>:' not in asm: #IMPORTANT replace func0 with the function name
            raise ValueError("compile fails")
        asm = '<'+'func0'+'>:' + asm.split('<'+'func0'+'>:')[-1].split('\n\n')[0] #IMPORTANT replace func0 with the function name
        asm_clean = ""
        asm_sp = asm.split("\n")
        for tmp in asm_sp:
            if len(tmp.split("\t"))<3 and '00' in tmp:
                continue
            idx = min(
                len(tmp.split("\t")) - 1, 2
            )
            tmp_asm = "\t".join(tmp.split("\t")[idx:])  # remove the binary code
            tmp_asm = tmp_asm.split("#")[0].strip()  # remove the comments
            asm_clean += tmp_asm + "\n"
    input_asm = asm_clean.strip()
    before = f"# This is the assembly code:\n"#prompt
    after = "\n# What is the source code?\n"#prompt
    input_asm_prompt = before+input_asm.strip()+after
    with open(fileName +'_' + opt_state +'.asm','w',encoding='utf-8') as f:
        f.write(input_asm_prompt)
```

**Decompilation:** Use LLM4Decompile to translate the assembly instructions into C:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_path = 'LLM4Binary/llm4decompile-6.7b-v1.5' # V1.5 Model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path,torch_dtype=torch.bfloat16).cuda()

with open(fileName +'_' + OPT[0] +'.asm','r') as f:#optimization level O0
    asm_func = f.read()
inputs = tokenizer(asm_func, return_tensors="pt").to(model.device)
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=4000)
c_func_decompile = tokenizer.decode(outputs[0][len(inputs[0]):-1])

with open(fileName +'.c','r') as f:#original file
    func = f.read()

print(f'original function:\n{func}')# Note we only decompile one function, where the original file may contain multiple functions
print(f'decompiled function:\n{c_func_decompile}')
```

### 4. License
This code repository is licensed under the MIT License.

### 5. Contact

If you have any questions, please raise an issue.
