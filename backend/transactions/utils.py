import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))



#ML layer
def classify_transaction(description):
   
    desc = description.lower()

    # 🔥 strong overrides
    if any(word in desc for word in ["pharmacy", "medicine", "doctor", "hospital", "lab", "test", "gym", "fitness"]):
        return "Health"

    if any(word in desc for word in ["loan", "emi", "rent"]):
        return "Bills"
    
    X = vectorizer.transform([description])
    return model.predict(X)[0]

#Logic layer
def classify_want_need(category, amount):
    thresholds = {
        "Food": 800,
        "Shopping": 2000,
        "Transport": 1500,
        "Entertainment": 500,
        "Bills": 10000,
        "Health": 80000
    }

    threshold = thresholds.get(category, 1000)

    if amount > threshold:
        return "Want"
    else:
        return "Need"