# Home Price Prediction using Machine Learning

A Flask-based web application that predicts home prices using machine learning. Users can input the area of a property and get an instant prediction of its estimated price in Indian Rupees.

## Features

- **Simple Web Interface**: User-friendly HTML interface for easy price prediction
- **Machine Learning Model**: Pre-trained model for accurate price predictions
- **Real-time Predictions**: Get instant price estimates based on property area
- **Responsive Design**: Modern, gradient-based UI with intuitive layout
- **Flask Backend**: Lightweight Python backend for handling predictions

## Project Structure

```
Home-Price-Prediction-using-Machine-Learning/
├── app.py                          # Flask application
├── train_model.py                  # Model training script
├── requirement.txt                 # Python dependencies
├── homeprices.csv                  # Sample data
├── model_info.json                 # Model information
├── Datasets/                       # Training datasets
│   ├── areas.csv
│   ├── canada_per_capita_income.csv
│   ├── homeprices.csv
│   ├── insurance_data.csv
│   ├── salaries.csv
│   └── salary.csv
├── models/                         # Trained model files
│   └── house_price_model.pkl       # Serialized ML model
└── templates/                      # HTML templates
    └── index.html                  # Web interface
```

## Requirements

- Python 3.x
- Flask
- scikit-learn
- pandas
- numpy
- pickle

Install dependencies:
```bash
pip install -r requirement.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mali-suraj/Home-Price-Prediction-using-Machine-Learning-.git
cd Home-Price-Prediction-using-Machine-Learning
```

2. Install required packages:
```bash
pip install -r requirement.txt
```

3. Run the Flask application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter the area of the property in square feet
2. Click the "Predict Price" button
3. The predicted price in Indian Rupees (₹) will be displayed

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Frontend**: HTML5, CSS3
- **Model Serialization**: pickle

## How It Works

1. The ML model is pre-trained on historical home price data
2. When a user inputs the property area, the model predicts the price
3. The Flask backend processes the request and returns the prediction
4. The result is displayed on the web interface in Indian Rupees

## Model Details

- **Algorithm**: Linear Regression (or appropriate ML algorithm)
- **Training Data**: Historical home price datasets
- **Model File**: `models/house_price_model.pkl`
- **Input**: Property area in square feet
- **Output**: Predicted price in Indian Rupees

## Author

**Suraj Mali**

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Disclaimer

The predictions provided by this model are based on historical data and should not be considered as financial advice. For actual property valuations, consult with real estate professionals.
