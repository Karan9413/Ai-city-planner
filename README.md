Markdown
# AI City Planner

An autonomous agentic framework built to simulate, plan, and benchmark urban development profiles using generative AI models and local tool execution layers.

---

## 🏗️ Project Architecture

The codebase is split into a modular Python backend driven by an agentic core loop, paired with a React/TypeScript frontend visualization matrix.

adaptive-ai/
├── backend/
│   ├── api/             # REST endpoints and SSE streaming logic
│   ├── core/            # Agent loop (Intent, Planner, Executor, Memory, Scoring)
│   ├── db/              # Flat-file data stores and benchmarking CSVs
│   ├── llm/             # Client initializers and token streaming configuration
│   ├── tools/           # Web search, calculators, and agent execution tools
│   └── main.py          # Application entry point
├── data/                # Persistent cross-session memory layers
├── frontend/            # Chat interfaces and UI visualization modules
└── .gitignore           # Active environment and credential mask


---

## 🛠️ Tech Stack & Core Dependencies

### Backend
* **Runtime:** Python 3.11+
* **LLM Engine:** `google-generativeai` & `litellm` (Gemini API Integration)
* **Agent Framework:** Custom execution graph utilizing dedicated sub-modules (`planner.py`, `intent.py`, `scoring.py`)
* **Data Processing:** `pandas` for handling sector benchmarks

### Frontend
* **Framework:** React / TypeScript
* **Styling:** Tailwind CSS / Component-driven architecture
* **Dependencies:** Managed via `package.json`

---

## ⚙️ Local Installation & Setup

### 1. Clone & Environment Isolation
Clone your repository and navigate to the project root:

git clone [https://github.com/Karan9413/Ai-city-planner.git](https://github.com/Karan9413/Ai-city-planner.git)
cd Ai-city-planner
Create a virtual environment (Python 3.11 or 3.12 is highly recommended to avoid local binary compilation issues with tokenization libraries):

PowerShell
# Using Native Python Venv
python -m venv env
.\env\Scripts\Activate.ps1

# OR Using Conda (Recommended for Windows environments)
conda create -n city_planner python=3.11 -y
conda activate city_planner
2. Install Backend Dependencies
PowerShell
cd backend
pip install -r requirements.txt
3. Environment Configuration
Create a .env file in the root of the backend directory. Do not commit this file to source control.

Code snippet
GEMINI_API_KEY=your_google_gcp_api_key_here
PORT=8000
4. Install Frontend Dependencies
PowerShell
cd ../frontend
npm install
🚀 Running the Application
Start the Backend Server
PowerShell
cd backend
python main.py
Start the Frontend Interface
PowerShell
cd frontend
npm run dev
