---
license: apache-2.0
language:
- en
- de
- ar
---

<div align="center">
  <img src="https://i.ibb.co/CBHmTDn/136719a5-6d8a-4654-a618-46eabc788953.jpg" alt="Arcee-Agent" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); max-width: 100%; height: auto;">
</div>

Arcee Agent is a cutting-edge 7B parameter language model specifically designed for function calling and tool use. Initialized from Qwen2-7B, it rivals the performance of much larger models while maintaining efficiency and speed. This model is particularly suited for developers, researchers, and businesses looking to implement sophisticated AI-driven solutions without the computational overhead of larger language models. Compute for training Arcee-Agent was provided by [CrusoeAI](https://huggingface.co/crusoeai). Arcee-Agent was trained using [Spectrum](https://arxiv.org/abs/2406.06623).

GGUFs are available from [CrusoeAI](https://huggingface.co/crusoeai/Arcee-Agent-GGUF).

### Key Features

1. **Advanced Function Calling:** Arcee Agent excels at interpreting, executing, and chaining function calls. This capability allows it to interact seamlessly with a wide range of external tools, APIs, and services.

2. **Multiple Format Support:** The model is compatible with various tool use formats, including:
   - Glaive FC v2
   - Salesforce
   - Agent-FLAN

Arcee-Agent performs best when using the VLLM OpenAI FC format, but it also excels with prompt-based solutions. Agent-Spark can accommodate any specific use case or infrastructure needs you may have.

4. **Dual-Mode Functionality:**
   - Tool Router: Arcee Agent can serve as intelligent middleware, analyzing requests and efficiently routing them to appropriate tools or larger language models for processing.
   - Standalone Chat Agent: Despite its focus on function calling, Arcee Agent is capable of engaging in human-like conversations and completing a wide range of tasks independently.

5. **Unparalleled Speed and Efficiency:** With its 7B parameter architecture, Arcee Agent delivers rapid response times and efficient processing, making it suitable for real-time applications and resource-constrained environments.

6. **Competitive Performance:** In function calling and tool use tasks, Arcee Agent competes with the capabilities of models many times its size, offering a cost-effective solution for businesses and developers.

## Detailed Function Calling and Tool Use Capabilities

Arcee Agent's function calling and tool use capabilities open up a world of possibilities for AI-driven applications. Here's a deeper look at what you can achieve:

1. **API Integration:** Seamlessly interact with external APIs, allowing your applications to:
   - Fetch real-time data (e.g., stock prices, weather information)
   - Post updates to social media platforms
   - Send emails or SMS messages
   - Interact with IoT devices

2. **Database Operations:** Execute complex database queries and operations through natural language commands, enabling:
   - Data retrieval and analysis
   - Record updates and insertions
   - Schema modifications

3. **Code Generation and Execution:** Generate and run code snippets in various programming languages, facilitating:
   - Quick prototyping
   - Automated code review
   - Dynamic script generation for data processing

4. **Multi-step Task Execution:** Chain multiple functions together to complete complex tasks, such as:
   - Booking travel arrangements (flights, hotels, car rentals)
   - Generating comprehensive reports from multiple data sources
   - Automating multi-stage business processes

## Business Use Cases

Arcee Agent's unique capabilities make it an invaluable asset for businesses across various industries. Here are some specific use cases:

1. **Customer Support Automation:**
   - Implement AI-driven chatbots that handle complex customer inquiries and support tickets.
   - Automate routine support tasks such as password resets, order tracking, and FAQ responses.
   - Integrate with CRM systems to provide personalized customer interactions based on user history.

2. **Sales and Marketing Automation:**
   - Automate lead qualification and follow-up using personalized outreach based on user behavior.
   - Generate dynamic marketing content tailored to specific audiences and platforms.
   - Analyze customer feedback from various sources to inform marketing strategies.

3. **Operational Efficiency:**
   - Automate administrative tasks such as scheduling, data entry, and report generation.
   - Implement intelligent assistants for real-time data retrieval and analysis from internal databases.
   - Streamline project management with automated task assignment and progress tracking.

4. **Financial Services Automation:**
   - Automate financial reporting and compliance checks.
   - Implement AI-driven financial advisors for personalized investment recommendations.
   - Integrate with financial APIs to provide real-time market analysis and alerts.

5. **Healthcare Solutions:**
   - Automate patient record management and data retrieval for healthcare providers.

6. **E-commerce Enhancements:**
   - Create intelligent product recommendation systems based on user preferences and behavior.
   - Automate inventory management and supply chain logistics.
   - Implement AI-driven pricing strategies and promotional campaigns.

7. **Human Resources Automation:**
   - Automate candidate screening and ranking based on resume analysis and job requirements.
   - Implement virtual onboarding assistants to guide new employees through the onboarding process.
   - Analyze employee feedback and sentiment to inform HR policies and practices.

8. **Legal Services Automation:**
   - Automate contract analysis and extraction of key legal terms and conditions.
   - Implement AI-driven tools for legal research and case law summarization.
   - Develop virtual legal assistants to provide preliminary legal advice and document drafting.

9. **Educational Tools:**
   - Create personalized learning plans and content recommendations for students.
   - Automate grading and feedback for assignments and assessments.

10. **Manufacturing and Supply Chain Automation:**
    - Optimize production schedules and inventory levels using real-time data analysis.
    - Implement predictive maintenance for machinery and equipment.
    - Automate quality control processes through data-driven insights.

## Benchmarking
<div align="center">
  <img src="https://i.ibb.co/xmgswP8/Screenshot-2024-07-02-at-1-49-04-PM.png" alt="Arcee-Agent-Evals" style="border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); max-width: 100%; height: auto;">
</div>

## Intended Uses

Arcee Agent is designed for a wide range of applications where efficient function calling and tool use are crucial. Some potential use cases include:

- Developing sophisticated chatbots and virtual assistants with advanced tool integration
- Creating efficient middleware for routing and preprocessing requests to larger language models
- Implementing AI-driven process automation in resource-constrained environments
- Prototyping and testing complex tool-use scenarios without the need for more computationally expensive models
- Building interactive documentation systems that can execute code examples in real-time
- Developing intelligent agents for IoT device management and home automation
- Creating AI-powered research assistants for various scientific disciplines

## Limitations

While Arcee Agent excels in its specialized areas, users should be aware of its limitations:

- The model's general knowledge and capabilities outside of function calling and tool use may be more limited compared to larger, general-purpose language models.
- Performance in tasks unrelated to its core functionalities may not match that of models with more diverse training.
- As with all language models, outputs should be validated and used responsibly, especially in critical applications.
- The model's knowledge cutoff date may limit its awareness of recent events or technological advancements.

## Usage
The model was trained to respect many different formats - but the evals were done with this specific tool template: 
```python
In this environment, you have access to a set of tools you can use to answer the user's question.

You may call them like this:
<function_calls>
  <invoke>
    <tool_name>$TOOL_NAME</tool_name>
    <parameters>
      <$PARAMETER_NAME>$PARAMETER_VALUE</$PARAMETER_NAME>
      ...
    </parameters>
  </invoke>
</function_calls>

Here are the tools available:
<tools>
```