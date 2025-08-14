bank_marketing_ml/
├── data/
│ └── cleaned_full_data.csv
├── models/
│ ├── decision_tree/
│ ├── logistic_regression/
│ └── random_forest/
├── src/
│ ├── evaluation_model_comparison.py
│ ├── evaluation.py
│ ├── train_decision_tree.py
│ └── train_random_forest.py
├── venv/
├── requirements.txt
├── README.md
├── .gitignore
└── setup.sh

##  How to Run

✅ Step 1: Open Terminal in the Project Root

In VS Code Terminal navigate to the root of your project:

cd path/to/project/bank_marketing_ml

( This is important because the file paths are relative to this folder.)

✅ Step 2: Activate Virtual Environment (if using one)

If venv/ is missing, create one:
python -m venv venv
Then activate it with:
source venv/Scripts/activate

✅  Step 3 : Install all dependencies
    
    pip install -r requirements.txt


✅ Step 4: Run Training Scripts

Now run  training scripts using Python:

python src/train_decision_tree.py
python src/train_random_forest.py


✅ Decision Tree model, scaler, and encoders saved successfully.
✅ Random Forest model, scaler, and encoders saved successfully.

 .pkl files will  be  saved inside:

models/decision_tree/

models/random_forest/

models/logistic_regression/


✅ Step 4: Run comparision model script

python src/evaluation_model_comparison.py


How the Model Works/predicts---

This project uses the Bank Marketing dataset, which includes information from direct phone-call marketing campaigns 
conducted by a Portuguese bank. The goal is to predict whether a client will subscribe to a term deposit (y: yes/no). 
The dataset has 45,211 records and 16 features, including age, job type, education, loan status, and contact method.
To ensure the model makes meaningful predictions (not random guesses), the original dataset is first split into 
training and test sets. The model learns from the training data and is then evaluated on the test set — data it hasn’t 
seen before. This allows us to check the model’s accuracy, precision, recall, and other metrics realistically.
 When we run evaluation_model_comparison.py, it loads the saved model files and test data, makes predictions, 
 and compares the performance of different algorithms (like Decision Tree and Random Forest). 

This approach ensures that predictions are driven by meaningful patterns learned from real customer behavior — not by random 
chance — highlighting how machine learning can uncover insights and support smarter, data-informed decision-making in marketing.


streamlit run app/main.py
to quit
Ctrl + C
