# HousePricePredict
Regression Project: Predicting Home Prices in Bangaluru
A machine learning web app that predicts house prices in Bangalore based on area, BHK, bathrooms, and location.
![App Screenshot](Screenshot.png)
## Features 
- Interactive frontend using HTML, CSS, JS (jQuery)
- Flask backend with a trained regression model
- Real-time predictions using user input
- Location dropdown dynamically loaded from backend
## Tech Stack
- Frontend: HTML5, CSS3, JavaScript, jQuery
- Backend: Python, Flask
- ML: Scikit-learn, Pandas, NumPy
- Deployment: (e.g. Render/Heroku or local)
## How it works
- Model trained on a cleaned housing dataset.
- Features used: location (one-hot encoded), total_sqft, BHK, bath.
- Backend serves predictions via `/predict_home_price`.
