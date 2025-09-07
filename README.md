# conSPIC-Talk
Reference Material


# ML Deployment Demo (Diabetes Dataset)

This project demonstrates how to train, save, and deploy a simple ML model on AWS EC2 using **FastAPI** and **Streamlit**.  

## 📌 Current Progress
- **Phase 1 (Model Training & Saving)** ✅
  - Repo + structure setup
  - Virtual environment (`venv`) with requirements
  - Training script (`src/train_diabetes.py`) → saves model as `models/diabetes_model.pkl`
  - Jupyter notebook (`notebooks/diabetes_training.ipynb`) → EDA, model experiments, optional MLflow logging

## 🚀 Next Steps
- **Phase 2: FastAPI Deployment** → expose trained model via REST API.
- **Phase 3: EC2 Deployment** → deploy FastAPI app on AWS EC2.
- **Phase 4: Streamlit Deployment** → interactive web UI for predictions.
- **Phase 5: CI/CD Pipeline** → GitHub Actions for automation.
- **Phase 6: Presentation & Documentation** -> 

### **Phase 6: Presentation & Documentation**

* [ ] Create a **presentation-ready walkthrough** (slides or markdown).
* [ ] Summarize phases systematically:

  * Problem → Data → Model training → Deployment → Testing → EC2 → Streamlit → CI/CD.
* [ ] Add visuals (diagrams, screenshots, Swagger UI, Streamlit UI).
* [ ] Polish **README** with a clear narrative + usage steps.
* [ ] Commit: `"Add presentation materials and final documentation"`.

---