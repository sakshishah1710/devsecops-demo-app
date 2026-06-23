pipeline {
    agent any

    environment {
        IMAGE_NAME = "sakshidocker2002/devsecops-demo"
    }

    stages {

        stage('Git Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sakshishah1710/devsecops-demo-app.git'
            }
        }
 
        stage('SonarQube scan') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                
               withSonarQubeEnv('SonarQube') {    
                sh """
                ${tool 'SonarScanner'}/bin/sonar-scanner
                """
            }
        }
    }
} 
        stage('OWASP Dependency Check'){
            steps{
                dependencyCheck additionalArguments: '--scan .',
                odcInstallation: 'DependencyCheck'
                dependencyCheckublisher patter: '**/dependency-check-report.xml'
            }
        }
         stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
            }
        }
    }
}