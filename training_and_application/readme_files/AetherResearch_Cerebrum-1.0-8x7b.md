---
base_model: mistralai/Mixtral-8x7B-v0.1
license: apache-2.0
---

## Introduction

Cerebrum 8x7b is a large language model (LLM) created specifically for reasoning tasks. It is based on the Mixtral 8x7b model. Similar to its smaller version, [Cerebrum 7b](https://huggingface.co/AetherResearch/Cerebrum-1.0-7b), it is fine-tuned on a small custom dataset of native chain of thought data and further improved with targeted RLHF (tRLHF), a novel technique for sample-efficient LLM alignment. Unlike numerous other recent fine-tuning approaches, our training pipeline includes under 5000 training prompts and even fewer labeled datapoints for tRLHF.

Native chain of thought approach means that Cerebrum is trained to devise a tactical plan before tackling problems that require thinking. For brainstorming, knowledge intensive, and creative tasks Cerebrum will typically omit unnecessarily verbose considerations.

Cerebrum 8x7b offers competitive performance to Gemini 1.0 Pro and GPT-3.5 Turbo on a range of tasks that require reasoning.

## Benchmarking
An overview of Cerebrum 8x7b performance compared to Gemini 1.0 Pro, GPT-3.5 and Mixtral 8x7b on selected benchmarks:
<img src="benchmarking.png" alt="benchmarking_chart" width="750"/>
<img src="benchmarking_table.png" alt="benchmarking_table" width="750"/>

Evaluation details:
1) ARC-C: all models evaluated zero-shot. Gemini 1.0 Pro and GPT-3.5 (gpt-3.5-turbo-0125) evaluated via API, reported numbers taken for Mixtral 8x7b.
2) HumanEval: all models evaluated zero-shot, reported numbers used.
3) GSM8k: Cerebrum, GPT-3.5, and Mixtral 8x7b evaluated with maj@8, Gemini evaluated with maj@32. GPT-3.5 (gpt-3.5-turbo-0125) evaluated via API, reported numbers taken for Gemini 1.0 Pro and Mixtral 8x7b. 
4) MATH: Cerebrum evaluated 0-shot. GPT-3.5 and Gemini evaluated 4-shot, Mixtral 8x7b maj@4. Reported numbers used.

## Usage
For optimal performance, Cerebrum should be prompted with an Alpaca-style template that requests the description of the "thought process". Here is what a conversation should look like from the model's point of view:
```
<s>A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: Are you conscious?
AI:
```

This prompt is also available as a chat template. Here is how you could use it:
```
messages = [
    {'role': 'user', 'content': 'What is self-consistency decoding?'},
    {'role': 'assistant', 'content': 'Self-consistency decoding is a technique used in natural language processing to improve the performance of language models. It works by generating multiple outputs for a given input and then selecting the most consistent output based on a set of criteria.'},
    {'role': 'user', 'content': 'Why does self-consistency work?'}
]

input = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors='pt')

with torch.no_grad():
    out = model.generate(input_ids=input, max_new_tokens=100, do_sample=False)
```

The model ends its turn by generating the EOS token. Importantly, this token should be removed from the model answer in a multi-turn dialogue.

Cerebrum can be operated at very low temperatures (and specifically temperature 0), which improves performance on tasks that require precise answers. The alignment should be sufficient to avoid repetitions in most cases without a repetition penalty.

## Examples
Some of the model output examples:

The model is trained to first "think aloud about the solution", before solving the problem itself:
~~~~
A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: Find the longest increasing subarray of the given array.

The function signature should be def longest_increasing_subarray(vals: List[int]).

Write the code in Python.
AI: To find the longest increasing subarray of the given array, we could start by considering the first element of the array as the start of the subarray. Then, we could iterate through the remaining elements of the array and check if each element is greater than the last element of the current subarray. If it is, we could add it to the subarray. If it is not, we could save the length of the current subarray and start a new subarray with the current element. We could repeat this process until we reach the end of the array. Then, we could return the longest subarray found.

Here is an example:
```python
def longest_increasing_subarray(vals: List[int]):
    if len(vals) == 0:
        return []

    longest_subarray = [vals[0]]
    current_subarray = [vals[0]]

    for i in range(1, len(vals)):
        if vals[i] > current_subarray[-1]:
            current_subarray.append(vals[i])
        else:
            if len(current_subarray) > len(longest_subarray):
                longest_subarray = current_subarray
            current_subarray = [vals[i]]

    if len(current_subarray) > len(longest_subarray):
        longest_subarray = current_subarray

    return longest_subarray
```
~~~~

Usual unprompted chain of thought example for mathematical problem solving:
~~~~
A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: Out of six apples three are bad. What is the probability that at least one apple will be bad when selecting two apples out of them?
AI: To find the probability that at least one apple will be bad when selecting two apples out of them, we need to consider the possible outcomes of the selection. There are two cases: either one of the selected apples is bad, or both of them are bad.

The probability that one of the selected apples is bad is equal to the probability that the first apple is bad and the second apple is good, plus the probability that the first apple is good and the second apple is bad. Since three out of six apples are bad, the probability that the first apple is bad is $3/6 = 1/2$. The probability that the second apple is good, given that the first apple is bad, is equal to $3/5$, since there are three good apples left out of five remaining apples. Therefore, the probability that the first apple is bad and the second apple is good is $1/2 \cdot 3/5 = 3/10$. Similarly, the probability that the first apple is good and the second apple is bad is also $3/10$. Therefore, the probability that one of the selected apples is bad is $3/10 + 3/10 = 6/10 = 3/5$.

The probability that both of the selected apples are bad is equal to the probability that the first apple is bad and the second apple is bad. Since there are three bad apples out of six, the probability that the first apple is bad is $3/6 = 1/2$. The probability that the second apple is bad, given that the first apple is bad, is equal to $2/5$, since there are two bad apples left out of five remaining apples. Therefore, the probability that both of the selected apples are bad is $1/2 \cdot 2/5 = 2/10 = 1/5$.

To find the probability that at least one apple will be bad, we add the probabilities of the two cases: the probability that one of the selected apples is bad and the probability that both of the selected apples are bad. Therefore, the probability that at least one apple will be bad is $3/5 + 1/5 = 4/5$. The answer is 4/5.
~~~~

Similar example for a simple physical task:
~~~~
A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: The apple falls from a tree of height 10m. When will it reach the earth if there is no air resistance?
AI: To find out when the apple will reach the earth, we can use the equation of motion for a freely falling object. The equation of motion for a freely falling object is $s = ut + \frac{1}{2}at^2$, where $s$ is the displacement, $u$ is the initial velocity, $a$ is the acceleration due to gravity, and $t$ is the time taken. In this case, the initial velocity of the apple is 0, and the acceleration due to gravity is 9.8 m/s^2. Therefore, we can write the equation of motion as $s = \frac{1}{2}at^2$. Substituting the values, we get $10 = \frac{1}{2} \cdot 9.8 \cdot t^2$. Solving for $t$, we get $t = \sqrt{\frac{20}{9.8}} = \sqrt{2.04} = 1.43$ seconds. Therefore, the apple will reach the earth in 1.43 seconds. The answer is 1.43 seconds.
~~~~

Simple calculus problem, note that the model quietly corrects itself after proposing factoring out of $n$ from the numerator, which is inefficient in this case.
~~~~
A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: What is $\lim_{n \to \infty} \frac{(n + 3) \cdot \sqrt{n}}{(n/2 - 1)^2}$?
AI: To find the limit of $\frac{(n + 3) \cdot \sqrt{n}}{(n/2 - 1)^2}$ as $n$ approaches infinity, we can start by simplifying the expression. We can factor out $n$ from the numerator and write $(n + 3) \cdot \sqrt{n} = n \cdot \sqrt{n} + 3 \cdot \sqrt{n}$. We can also write $(n/2 - 1)^2 = n^2/4 - n + 1$. Therefore, we can write the limit as $\lim_{n \to \infty} \frac{n \cdot \sqrt{n} + 3 \cdot \sqrt{n}}{n^2/4 - n + 1}$.

Now, we can consider the behavior of each term in the numerator and denominator as $n$ approaches infinity. As $n$ approaches infinity, $n \cdot \sqrt{n}$ will grow much faster than $3 \cdot \sqrt{n}$, so we can ignore the $3 \cdot \sqrt{n}$ term in the numerator. Similarly, as $n$ approaches infinity, $n^2/4$ will grow much faster than $n$ and $1$, so we can ignore the $n$ and $1$ terms in the denominator. Therefore, we can write the limit as $\lim_{n \to \infty} \frac{n \cdot \sqrt{n}}{n^2/4} = \lim_{n \to \infty} \frac{4 \cdot n \cdot \sqrt{n}}{n^2} = \lim_{n \to \infty} \frac{4 \cdot \sqrt{n}}{n} = \lim_{n \to \infty} \frac{4}{\sqrt{n}} = 0$.

Therefore, the limit of $\frac{(n + 3) \cdot \sqrt{n}}{(n/2 - 1)^2}$ as $n$ approaches infinity is 0. The answer is 0.
~~~~

Example of a simple proof. The model "forgets" to prove that the matrix $B^T A B$ is symmetric. This is quite common - in fact, GPT-4 fails in a similar fashion.
~~~~
A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: If $A$ is positive semi-definite, is $B^TAB$ positive semi-definite?
AI: To determine whether $B^TAB$ is positive semi-definite, we need to consider the properties of $A$ and $B$. Since $A$ is positive semi-definite, we know that for any vector $x$, $x^TAx \geq 0$. To show that $B^TAB$ is positive semi-definite, we need to show that for any vector $y$, $y^TB^TABy \geq 0$.

We can write $y^TB^TABy$ as $(By)^TA(By)$. Since $A$ is positive semi-definite, we know that $(By)^TA(By) \geq 0$. Therefore, $y^TB^TABy \geq 0$ for any vector $y$, which means that $B^TAB$ is positive semi-definite. The answer is yes.
~~~~

Typical reaction of a model to some hallucination-inducing prompt. Instead of simply claiming that it does not know the painter George Ellster, it tries to help the user find a painter with a similar name:
~~~~
A chat between a user and a thinking artificial intelligence assistant. The assistant describes its thought process and gives helpful and detailed answers to the user's questions.
User: Tell me about a famous British painter George Ellster
AI: George Ellster is not a famous British painter. However, there are a few notable British painters with similar names:

George Elgar Hicks (1824-1914) was a Victorian-era painter known for his genre scenes and portraits.

George Frederic Watts (1817-1904) was a Victorian-era painter and sculptor known for his allegorical and symbolic works.

George Stubbs (1724-1806) was an 18th-century painter known for his equestrian and animal paintings.

George Romney (1734-1802) was an 18th-century painter known for his portraits and historical scenes.

These are just a few examples of notable British painters with similar names to George Ellster.
~~~~
