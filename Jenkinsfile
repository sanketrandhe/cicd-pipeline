pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanketrandhe/day14-python-app'
        IMAGE_TAG = 'v1'
    }

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
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -f docker/Dockerfile .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                        docker logout
                    '''
                }
            }
        }

        stage('Deploy to AWS EC2') {
            steps {
                echo 'Deployment will be configured next'
            }
        }
    }
}
