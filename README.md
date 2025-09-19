# Weather-Report-App
A simple **weather forecast application** built using **Django** and the [WeatherAPI](https://www.weatherapi.com/).  
The app lets users search for a city and view weather reports for:

- **Yesterday**  
- **Today**  
- **Tomorrow**  
- **Day After Tomorrow**  
- **Future 2–3 days forecast**

Weather data is displayed in a **Bootstrap carousel** with navigation arrows.

---

## 🚀 Features
- 🌍 Search weather by city
- 📅 Shows weather for past, present, and future days
- 📊 Displays **average, max, min temperature**
- 🌈 Beautiful UI with cards & carousel
- ⏪ Left/Right navigation with disabled arrows when at edges

---

## 🛠 Tech Stack
- **Backend:** Django 5.x
- **Frontend:** HTML, Bootstrap 5, CSS, JavaScript
- **API:** [WeatherAPI](https://www.weatherapi.com/)

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   cd weather-app
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Get your WeatherAPI Key

Go to WeatherAPI.com

Sign up for a free account

Copy your API key from the dashboard

Add your API key inside views.py:

python
Copy code
API_KEY = "your_api_key_here"
Run the development server:

bash
Copy code
python manage.py runserver
Open in browser:

cpp
Copy code
http://127.0.0.1:8000/
