🚀 DevSecOps CI/CD Demo — Secure Flask Application



A complete DevSecOps Pipeline Project integrating:
✅ Continuous Integration (CI)
✅ Security Scanning
✅ Dockerized Deployment
✅ Cloud Hosting (Render)
✅ Slack Notifications

🌐 Live Demo
Render Deployment: [https://your-render-app-url.onrender.com](https://devsecops-demo-hm0g.onrender.com)


🧱 Project Overview
This project demonstrates a secure end-to-end CI/CD pipeline built around a Flask web app. It automatically runs tests, scans for vulnerabilities, builds a Docker image, and deploys securely to the cloud.
Tech Stack:
Language: Python (Flask)
Testing: Pytest
CI/CD: GitHub Actions
Security: Bandit, Safety, CodeQL, OWASP Dependency Check
Containerization: Docker
Deployment: Render
Notifications: Slack

🧪 CI/CD Pipeline Overview
graph TD
A[Developer Commit Code] --> B[GitHub Actions Trigger]
B --> C[Run Unit Tests with Pytest]
C --> D[Run Bandit (Static Security Analysis)]
D --> E[Run Safety (Dependency Vulnerability Scan)]
E --> F[Run CodeQL (Advanced Static Analysis)]
F --> G[Run OWASP Dependency Check]
G --> H[Build Docker Image]
H --> I[Deploy to Render Cloud]
I --> J[Slack Notification]

🔐 Security Automation Highlights
Tool	Purpose	Automation
Bandit	Static code analysis for Python	Runs on each push
Safety	Dependency vulnerability scanner	Checks requirements.txt
CodeQL	GitHub’s SAST tool for code vulnerabilities	Auto-runs weekly + on push
OWASP Dependency Check	CVE detection for libraries	Runs via GitHub Actions
Slack Webhook	Notification integration	Alerts on success/failure
Trivy (optional)	Container image vulnerability scan	Can be added in Docker stage

⚙️ Setup Instructions
1️⃣ Clone and Setup
git clone https://github.com/mohdzaid145256/devsecops-ci-demo.git
cd devsecops-ci-demo
python -m venv venv
source venv/bin/activate   # or .\venv\Scripts\activate (Windows)
pip install -r requirements.txt
2️⃣ Run Locally
python app/main.py
Visit http://127.0.0.1:5000/ in your browser.
3️⃣ Run Tests
pytest -v
4️⃣ Run Security Scans
bandit -r app/
safety check -r requirements.txt

☁️ Deployment
🐳 Docker
docker build -t devsecops-demo .
docker run -p 5000:5000 devsecops-demo

🌩 Render
Connect your GitHub repository on Render
Choose “Auto Deploy on Push”
Select Python + Docker runtime
Deploy and verify the live URL

📣 Notifications
Slack notifications are automatically sent via the CI pipeline whenever:
✅ Build/Test passes
❌ Pipeline fails
Webhook: stored securely as SLACK_WEBHOOK_URL in GitHub → Secrets → Actions

🧠 Bonus Integrations
✅ CodeQL Analysis — static vulnerability scanning
✅ OWASP Dependency Check — dependency-level security audit
✅ Slack Webhook Notifications — CI visibility
✅ Render Auto-Deployment — cloud hosting
🔜 Trivy Container Scan (optional for Docker image)

🏁 Results Summary
Stage	Tool	Status
Testing	Pytest	✅ Passed
Static Analysis	Bandit	✅ Passed
Dependency Scan	Safety	✅ Clean
CodeQL Scan	GitHub	✅ Passed
OWASP Dependency Check	Action	✅ No Critical Issues
Deployment	Render	✅ Live
Notification	Slack	✅ Functional

👨‍💻 Author
Mohd Zaid
📧 mohdzaid4919@gmail.com
🔗 GitHub Profile
📍 Sikar, Rajasthan, India
🏆 Acknowledgments
This project was created as part of a DevSecOps Assessment Task to demonstrate secure CI/CD automation pipelines using open-source tools and cloud deployment strategies.
