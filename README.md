# Business Communication Assistant (comms.py)

A Streamlit-powered AI application that transforms technical messages into business-friendly communications for stakeholders like executives, sales teams, and non-technical decision makers.

##  Purpose

Technical teams often struggle to communicate effectively with business stakeholders. This application bridges that gap by automatically rewriting technical updates, engineering reports, and developer communications into language that resonates with business audiences.

##  Features

- **Business Impact First**: Prioritizes outcomes and business value over technical implementation details
- **Jargon Translation**: Converts technical terms and acronyms into plain English
- **Professional Tone**: Ensures direct, friendly, and professional communication style
- **Grammar & Flow**: Improves readability and message structure
- **Stakeholder-Ready**: Optimized for executives, sales teams, and business decision makers

## Quick Start

### Prerequisites

- Python 3.7+
- OpenAI API key
- Required Python packages (see Dependencies)

### Setup

1. **Environment Configuration**
   
   Create a `.env` file in your project directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Install Dependencies**
   ```bash
   pip install streamlit python-dotenv asyncio
   ```

3. **Ensure Agent Module**
   
   Make sure you have the `agents.py` module with `Agent` and `Runner` classes available in your project directory.

### Run the Application

```bash
streamlit run comms.py
```

The application will open in your browser at `http://localhost:8501`

## 💻 Usage

1. **Input**: Enter your technical message in the text area
2. **Process**: Click "Rewrite message" to transform the content
3. **Output**: Review both the original and rewritten versions displayed side-by-side

### Example

**Before (Technical):**
> We implemented a low-level TCP socket optimization that reduced latency by 15ms and improved throughput by 23%. The refactoring involved restructuring our connection pooling architecture and implementing keep-alive mechanisms.

**After (Business-Friendly):**
> We improved our system performance, resulting in 15ms faster response times and 23% better data processing capacity. This enhancement means our customers will experience noticeably faster load times and more reliable service during peak usage periods.

## 🏗️ Technical Architecture


### Key Components

- **Agent**: Configures the AI assistant with specific business communication instructions
- **Runner**: Executes the agent and manages the OpenAI API interaction
- **Streamlit UI**: Provides the web interface for input and output

## Dependencies

### Core Requirements

- `streamlit`: Web application framework
- `python-dotenv`: Environment variable management
- `asyncio`: Asynchronous programming support
- `os`: Operating system interface

### Custom Modules

- `agents`: Contains `Agent` and `Runner` classes for OpenAI SDK integration

## 🔧 Configuration

### Agent Instructions

The AI agent follows strict guidelines:

**Always Do:**
- Start with business impact and outcomes
- Use plain English explanations
- Maintain professional tone
- Correct grammar and improve flow

**Never Do:**
- Invent or fabricate results
- Remove essential technical context
- Use unexplained acronyms or jargon
- Include confidential information



