import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'csv'}

FEATURE_COLUMNS = [
    'Total Relationship Count', 'Months Inactive 12 mon',
    'Contacts Count 12 mon','Total Revolving Bal','Dependent count', 'Education Level',
    'Marital Status', 'Avg Open To Buy', 'Total Amt Chng Q4 Q1', 'Total Trans Amt',
    'Income Category', 'Card Category', 'Months on book', 'Total Trans Ct',
    'Total Ct Chng Q4 Q1', 'Avg Utilization Ratio'
]