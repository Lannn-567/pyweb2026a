import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "藍浚愷",
  "mail": "s1131638@pu.edu.tw",
  "lab": 579
}

doc_ref = db.collection("靜宜資管2026").document("Lan")
doc_ref.set(doc)
