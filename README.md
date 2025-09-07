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


## 🚀 Phase 3: Deploying FastAPI App on AWS EC2

### 1. Launch EC2 Instance

* Go to **AWS Console → EC2 → Launch Instance**
* Choose:

  * **Name**: `ml-demo-instance`
  * **AMI**: Ubuntu Server 22.04 LTS (Free Tier eligible)
  * **Instance type**: `t2.micro` or `t3.micro`
  * **Key pair**: Create/download `.pem` file
  * **Security group inbound rules**:

    * **SSH (22)** → *My IP only*
    * **Custom TCP (8000)** → *My IP* (or `0.0.0.0/0` for public demo)
* Launch the instance and copy the **Public IPv4 address**.

---

### 2. Connect via SSH

From local terminal (Git Bash / WSL on Windows, or Linux/Mac):

```bash
chmod 400 my-key.pem
ssh -i "my-key.pem" ubuntu@<EC2_PUBLIC_IP>
```

---

### 3. Prepare Environment

On the EC2 instance:

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python, pip, git
sudo apt install python3 python3-venv python3-pip git -y
```

---

### 4. Clone Repository & Setup

```bash
# Clone repo
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Ensure model is available
python src/train_diabetes.py   # if model not already saved
```

---

### 5. Run FastAPI App

```bash
uvicorn app.fastapi_app:app --host 0.0.0.0 --port 8000
```

* App will be live at:
  `http://<EC2_PUBLIC_IP>:8000/`
* Swagger UI docs available at:
  `http://<EC2_PUBLIC_IP>:8000/docs`

---

### 6. Test API

From local machine:

```bash
curl http://<EC2_PUBLIC_IP>:8000/
```

Or use the provided script:

```bash
python test_api.py
```

---

### 7. Shutdown & Terminate

When done with the demo:

1. Exit SSH:

   ```bash
   exit
   ```
2. In AWS Console → EC2 → select instance → **Instance state → Terminate**.
3. Instance will show as **terminated** (safe, no charges).

---

✅ That’s the full cycle — launch → deploy → test → terminate.




---



## 🚀 Phase 4: Streamlit Deployment

In this phase, we build a simple **Streamlit web app** that loads the trained diabetes model directly and allows users to interact with it through a UI.

### 1. Run Locally
```bash
# Activate venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# Start Streamlit app
streamlit run app/streamlit_app.py
````

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

### 2. Deploy on EC2

1. **Update security group**: add inbound rule for **TCP 8501** (My IP or `0.0.0.0/0` for demo).
2. **SSH into EC2**:

   ```bash
   ssh -i "my-key.pem" ubuntu@<EC2_PUBLIC_IP>
   ```
3. **Activate venv & run app**:

   ```bash
   cd ml-deployment-demo
   source venv/bin/activate
   streamlit run app/streamlit_app.py --server.address 0.0.0.0 --server.port 8501
   ```
4. **Access in browser**:

   ```
   http://<EC2_PUBLIC_IP>:8501/
   ```

---

### 3. Example UI

* Input patient details using sliders/inputs.
* Click **Predict** → model outputs diabetes progression score.

---

✅ With this, the project now has **two deployment modes**:

* FastAPI API endpoint (Phase 2 & 3)
* Streamlit interactive UI (Phase 4)



---

That closes Phase 4 neatly 🎉  


### **Phase 6: Presentation & Documentation**

* [ ] Create a **presentation-ready walkthrough** (slides or markdown).
* [ ] Summarize phases systematically:

  * Problem → Data → Model training → Deployment → Testing → EC2 → Streamlit → CI/CD.
* [ ] Add visuals (diagrams, screenshots, Swagger UI, Streamlit UI).
* [ ] Polish **README** with a clear narrative + usage steps.
* [ ] Commit: `"Add presentation materials and final documentation"`.

---