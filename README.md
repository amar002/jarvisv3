# jarvisv3

# HabitFlow: Build Small Habits, Achieve Big Goals

HabitFlow is an interactive and dynamic habit-building platform that leverages the power of AI to help users develop and track personalized habits. Designed for simplicity and scalability, HabitFlow offers users a seamless onboarding experience, habit dashboards, and AI-driven insights.

## Features

### 1. Interactive Onboarding
- Users answer three simple questions to help define their focus areas.
- Based on responses, the platform generates three personalized goals with explanations and action plans using **Gemini LLM**.

### 2. Dynamic Habit Dashboard
- View all habits, their statuses, and progress.
- Mark habits as completed and receive context-specific motivational messages powered by **Gemini LLM**.
- Add or remove habits easily.

### 3. AI-Powered Suggestions
- Chat with the platform for habit suggestions and advice.
- Get real-time, personalized habit ideas.

### 4. Reminder Management
- Set reminders for habits to stay on track.
- Customize reminder times to fit your schedule.

## Tech Stack
- **Frontend**: Streamlit for an interactive and responsive user interface.
- **AI Integration**: Google Generative AI (Gemini LLM) for personalized habit generation and motivational messages.
- **Backend**: Python for logic and data management.
- **Data Storage**: JSON for habit persistence.

## Folder Structure
```
habitflow/
├── app.py                  # Main entry point
├── components/             # UI components
│   ├── onboarding.py       # Onboarding flow
│   ├── dashboard.py        # Habit dashboard
│   ├── suggestions.py      # Suggestions interface
│   ├── reminders.py        # Reminder management
│   └── goal_completion.py  # Goal completion and appreciation
├── utils/                  # Utility functions
│   ├── data_handler.py     # Load and save data
│   ├── gemini_api.py       # Gemini LLM integration
│   └── helpers.py          # General utility functions
├── data/                   # Habit data storage
│   └── habits_data.json
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/habitflow.git
cd habitflow
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Key
Add your **Gemini API Key** to the environment:
```bash
export GEMINI_API_KEY='your-api-key'
```
For Streamlit Cloud, add the key in **Secrets** under **Settings**.

### 4. Run the App
```bash
streamlit run app.py
```

## Future Enhancements
- Habit streak tracking.
- Integration with calendar and notifications.
- Advanced habit analytics and visualizations.

## Contributing
Feel free to open issues or submit pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
