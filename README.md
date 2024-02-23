# Disease Prediction Streamlit App

- This is a Streamlit web application for predicting multiple diseases using machine learning models. 
- The app is designed to take input features related to a patient's health and provide predictions for various diseases based on trained machine learning models.

## Features

- Input form for user to enter relevant health information.
- Utilizes machine learning models to predict the likelihood of different diseases.
- Interactive and user-friendly interface powered by Streamlit.
- Easy deployment on Heroku.

## Getting Started

### Prerequisites

- Python 3.12.2
- pip (package installer for Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arpitpatelsitapur/Streamlit-multiple-disease-prediction-ML-app
   ```

2. Navigate to the project directory:

   ```bash
   cd disease-prediction-app
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to use the application locally.

## Deployment on Heroku

To deploy this app on Heroku, follow these steps:

1. [Sign up for a Heroku account](https://signup.heroku.com/).
2. Install the Heroku CLI: [Heroku CLI Installation](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
3. Log in to your Heroku account using the command:

   ```bash
   heroku login
   ```

4. Create a new Heroku app:

   ```bash
   heroku create your-app-name
   ```

5. Deploy your app to Heroku:

   ```bash
   git push heroku master
   ```

6. Open your app in the browser:

   ```bash
   heroku open
   ```

## Contributing

If you'd like to contribute to the project, please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The machine learning models used in this app were trained on [dataset source].
- Special thanks to [any acknowledgments].

Feel free to fork the repository, make improvements, and create a pull request. Happy coding!
