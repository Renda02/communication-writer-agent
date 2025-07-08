# Single Agent: AI-powered assistant applications

This repository contains 2 Streamlit applications that leverage AI agents to assist with business communications and project ideation. 
## 📋 Table of contents
- [Overview](#overview)
- [Applications](#applications)
  - [Business communication assistant](#business-communication-assistant)
  - [Project ideas generator](#project-ideas-generator)
- [Installation](#installation)
- [Usage](#usage)
- [Environment setup](#environment-setup)
- [Dependencies](#dependencies)
- [Learning resources](#learning-resources)
- [Troubleshooting](#troubleshooting)

## Overview

This project includes 2 AI-powered tools:

1. **Business communication assistant**: Transforms technical messages into business-friendly communications for stakeholders
2. **Project ideas generator**: Creates customized software project ideas with roadmaps based on skill level

Both applications are built with Streamlit and utilize AI agents to generate helpful content.

## Applications

### Business communication assistant

Located in `comms.py`, this application helps technical teams communicate more effectively with non-technical stakeholders like executives and sales teams.

**Features:**
- Rewrites technical messages with business impact first
- Translates technical jargon into business-friendly language
- Replaces acronyms and internal language with plain English
- Improves grammar, flow, and professional tone

### Project ideas generator

Located in `projects-app.py`, this application generates software project ideas tailored to different skill levels.

**Features:**
- Creates project ideas for beginner, intermediate, and advanced skill levels
- Suggests relevant technologies and skills for each project
- Provides guidance on contributing to related open-source projects
- Includes a 4-week learning and development roadmap

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the business communication assistant:
```bash
streamlit run comms.py
```

### Running the project ideas generator:
```bash
streamlit run projects-app.py
```

## Environment setup

Both applications require an OpenAI API key. Create a `.env` file in the root directory with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## Dependencies

- Python 3.7+
- Streamlit
- asyncio
- dotenv
- Custom `agents` module (Agent and Runner classes)

Note: Make sure you have the `agents` module available in your project directory or installed as a package.

## Contributing

This project is for educational purposes. If you'd like to use it as a learning resource:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

## Learning resources
This project can serve as a practical learning resource for:

- **Streamlit application development**: Learn how to build interactive web applications with Python
- **OpenAI API integration**: Understand how to use AI capabilities in your applications
- **Environment management**: Practice proper handling of API keys and environment variables
- **Version control best practices**: Learn what files to exclude from version control
- **Async programming**: See practical examples of asynchronous programming with Python

Before you begin:

- Verify the `.env` and `.gitignore` files to understand configuration
- Look at the `agents.py` module to understand the core Agent architecture
- Explore the individual application files (comms.py and projects-app.py)

## Troubleshooting

Common issues and solutions:

- **API key errors**: Make sure your .env file is properly formatted and the API key is valid
- **Module not found errors**: Ensure you've installed all dependencies and activated your virtual environment
- **Streamlit display issues**: Check the Streamlit documentation at https://docs.streamlit.io# AI-powered assistant applications
