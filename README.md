# Flat Circle

A flexible Python toolkit for AI engineering projects, inspired by the ideas behind LangChain but designed as a compact, modular utility library for building agentic workflows and LLM-powered applications.

## Overview

Flat Circle is being built as a Swiss Army knife for AI engineering work: a practical foundation for chaining prompts, managing memory, integrating tools, and working with language models in a simple and extensible way. Rather than being a single demo, the goal is to grow this project into a reusable library that helps developers compose reliable AI applications with less boilerplate.

## Features

- Uses a Hugging Face inference client
- Includes a custom calculator tool
- Demonstrates a simple agent loop with tool usage
- Keeps project dependencies in a dedicated requirements file

## Project Structure

```text
flat-circle/
├── chain/            # Core package for model, prompts, memory, and agent logic
├── main.py           # Entry point for running the example
├── requirements.txt  # Python dependencies
├── .env              # Local environment variables (not committed)
└── .gitignore        # Ignores local environment and virtualenv files
```

## Requirements

- Python 3.9+
- A Hugging Face access token (optional depending on your model setup)

## Installation

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root with your Hugging Face token if required:

```env
HF_TOKEN=your_huggingface_token_here
```

## Usage

Run the example script:

```bash
python main.py
```

The script will create a mini agent, attach the calculator tool, and print the agent's response to a sample math question.

## Dependencies

The project currently uses:

- `python-dotenv`
- `huggingface_hub`

## Contributing

Contributions are welcome. If you make changes, please keep the README updated so setup and usage remain clear.

## License

This project is currently unlicensed. If you plan to share or distribute it publicly, consider adding a LICENSE file.
