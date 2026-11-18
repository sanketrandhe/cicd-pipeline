
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'sanketrandhe/day14-python-app'
        IMAGE_TAG = 'v1'
        DEPLOY_HOST = '172.31.3.202'
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
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'day14-deploy-ssh',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                    sh '''
                        ssh -i "$SSH_KEY" \
                        -o StrictHostKeyChecking=accept-new \
                        "$SSH_USER@${DEPLOY_HOST}" "
                            docker pull ${IMAGE_NAME}:${IMAGE_TAG}
                            docker rm -f day14-app || true
                            docker run -d \
                                --name day14-app \
                                --restart always \
                                -p 5000:5000 \
                                ${IMAGE_NAME}:${IMAGE_TAG}
                        "
                    '''
                }
            }
        }
    }
}
