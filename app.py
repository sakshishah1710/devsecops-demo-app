from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
DevSecOps CI/CD Pipeline with Jenkins, Docker, Kubernetes and AWS

Project Overview:
Designed and implemented an end-to-end DevSecOps CI/CD pipeline for automated application deployment using AWS, Jenkins, Docker, Docker Hub, and Kubernetes.
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)