🌆 AI City Planning Advisor
🚀 Gen AI Academy APAC Hackathon Submission

An AI-powered decision intelligence platform that helps city planners allocate budgets fairly, transparently, and data-driven across critical infrastructure sectors.

📌 Problem Statement

Cities face a major challenge:

Limited budgets
Competing infrastructure demands
Inequitable, politically influenced allocation
Lack of transparency in decision-making

Traditional planning systems fail to optimize for fairness and real impact.

💡 Solution

This platform uses AI-driven gap analysis + prioritization logic to recommend optimal budget distribution across sectors such as:

🏥 Healthcare
💧 Water Supply
⚡ Electricity
🏠 Housing
🎓 Education
🚇 Transport
🧹 Sanitation
🌳 Green Spaces

It transforms raw city needs into structured, explainable funding decisions.

🧠 Key Features
📊 Smart Budget Allocation Engine

AI-based scoring system that evaluates:

Infrastructure gaps
Population needs
Priority weights
Impact potential
🤖 AI Explanation Layer

Every recommendation includes:

Why this allocation was made
What data influenced it
Trade-offs between sectors
📈 Scenario Simulation

Users can adjust:

Total budget
Priority weights
Sector constraints

And instantly see updated allocations.

🎯 Decision Transparency

No black-box output — every result is:

Explainable
Justified
Traceable
🏗️ System Architecture
Frontend (UI)
  └── index.html (Dashboard Interface)

Backend (AI Engine)
  ├── FastAPI / Flask (API Layer)
  ├── Core allocation logic
  ├── AI prompt / scoring engine
  └── Data processing layer

Data Layer
  ├── City infrastructure inputs
  ├── Sector weights
  └── Historical / synthetic datasets
⚙️ Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (FastAPI / Flask)
AI Layer: Rule-based + LLM-assisted reasoning
Data Handling: Pandas / JSON
Optional: OpenAI / local LLM integration
📂 Project Structure
Ai-city-planner/
│
├── backend/
│   ├── main.py
│   ├── core/
│   ├── utils/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── data/
│   └── sample_city_data.json
│
└── README.md
🧪 How It Works
User inputs city constraints (budget + priorities)
AI engine evaluates infrastructure gaps
System calculates weighted allocation
Explanation layer generates reasoning
UI displays results + comparison charts
🖥️ Run Locally
Backend
cd backend
pip install -r requirements.txt
python main.py
Frontend

Simply open:

frontend/index.html
📊 Example Output
Total Budget: ₹100 Cr

Healthcare     → 25%
Water Supply   → 18%
Education      → 20%
Housing        → 15%
Transport      → 10%
Sanitation     → 7%
Green Spaces   → 5%
Electricity    → 0%

With explanation:

Healthcare receives higher allocation due to high population density and low hospital coverage ratio.

🏆 Hackathon Value

This project demonstrates:

✔ Real-world civic impact
✔ AI-assisted decision making
✔ Explainable AI (XAI principles)
✔ Scalable governance tool
✔ Data-driven fairness
🔥 Future Improvements
Real city datasets integration (Gov APIs)
ML-based predictive demand modeling
Geo-mapping visualization (GIS layer)
Multi-city comparison dashboard
Policy recommendation generator
👤 Author

Karan
Gen AI Academy APAC Hackathon Participant

📜 License

This project is for educational and hackathon use.

⚠️ Important Reality Check (Read this)

Your README is now strong enough for submission, BUT:

If your backend is just rule-based scoring without real data or explainability logic, judges may consider it:

“Good idea, weak AI implementation”
