#Project 1 - MyRetailAdvisor Crew

Welcome to the MyRetailAdvisor Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

Create python env.
```bash
python3 -m venv myenv
source ./myenv/bin/activate
```

Install crewai.
```bash
crewai install
```
### Customizing

**Add your `WATSONX` parameters into the `.env` file**

- Modify `src/my_retail_advisor/config/agents.yaml` to define your agents
- Modify `src/my_retail_advisor/config/tasks.yaml` to define your tasks
- Modify `src/my_retail_advisor/crew.py` to add your own logic, tools and specific args
- Modify `src/my_retail_advisor/main.py` to add custom inputs for your agents and tasks
- Modify `src/my_retail_advisor/tool/custom_tool.py` to add custom tools for your agents and tasks
- Modify `src/my_retail_advisor/tool/tool_helper.py` to change the custom vision tool baed on llama vision model

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the my-retail-advisor Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The my-retail-advisor Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

Let's create wonders together with the power and simplicity of crewAI.
