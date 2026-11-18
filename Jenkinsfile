pipeline {
    agent any

    stages {

        stage('Verify Environment') {
            steps {
                sh '''
                    echo "Day 14 CI/CD Pipeline"
                    git --version
                    docker --version
                    hostname
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    python3 --version
                    test -f app/app.py
                    test -f docker/Dockerfile
                    echo "Application files verified"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Docker image build will happen here'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Docker Hub push will happen here'
            }
        }

        stage('Deploy to AWS EC2') {
            steps {
                echo 'AWS EC2 deployment will happen here'
            }
        }
    }
}
