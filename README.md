# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's **Math Score** based on demographic and academic information such as gender, parental education level, lunch type, test preparation course, reading score, and writing score.

## 🚀 Features

- Predict student math performance
- Data preprocessing pipeline
- Machine Learning model training and evaluation
- Flask-based web application
- AWS Elastic Beanstalk deployment
- Automated CI/CD using AWS CodePipeline

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-Learn

### Backend
- Flask
- Gunicorn

### Deployment & DevOps
- AWS Elastic Beanstalk
- AWS CodePipeline
- GitHub

## 📂 Project Structure

```text
Mlproject/
│
├── artifacts/
├── notebook/
├── src/
├── templates/
├── .ebextensions/
├── application.py
├── requirements.txt
├── Procfile
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Dakshhhhh-ops/Mlproject.git
cd Mlproject
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python application.py
```

Open your browser and visit:

```text
http://localhost:5000
```

## 🌐 Deployment

The application is deployed on **AWS Elastic Beanstalk** with a complete **CI/CD pipeline** using **AWS CodePipeline**.

Workflow:

```text
GitHub
   ↓
AWS CodePipeline
   ↓
AWS Elastic Beanstalk
   ↓
Production Deployment
```

Every push to the main branch automatically triggers a new deployment.

## 📊 Dataset

The project uses the Student Performance dataset containing features such as:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The target variable is:

- Math Score

## 👨‍💻 Author

**Daksh Wadhwa**

Electrical Engineering Student  
National Institute of Technology Hamirpur

GitHub: https://github.com/Dakshhhhh-ops

---

⭐ If you found this project useful, consider giving it a star.
