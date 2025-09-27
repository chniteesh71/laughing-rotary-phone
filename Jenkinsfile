pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io"
        APP_NAME = "jenkins-python-sample-app"
        VENV_PATH = "src/.venv"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python & Virtual Environment') {
          steps {
            script {
               // Use existing Python version
               sh """
               python3 --version
               if [ ! -d ${VENV_PATH} ]; then
                   python3 -m venv ${VENV_PATH}
               fi
               """
            }
          }
        }


        stage('Install Dependencies') {
            steps {
                script {
                    // Upgrade pip and install dependencies
                    sh """
                    ${VENV_PATH}/bin/pip install --upgrade pip
                    ${VENV_PATH}/bin/pip install -r src/requirements.txt
                    """
                }
            }
        }

        stage('Lint') {
            steps {
                sh "${VENV_PATH}/bin/python src/run.py lint"
            }
        }

        stage('Test') {
            steps {
                sh "${VENV_PATH}/bin/python src/run.py test"
            }
        }

        stage('Docker Build & Push') {
            environment {
                DOCKER_USERNAME = credentials('dockerhub-creds') // Make sure you added Docker creds in Jenkins
            }
            steps {
                script {
                    sh "docker --version"
                    sh """
                    echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                    docker build -t $DOCKER_REGISTRY/$DOCKER_USERNAME/$APP_NAME:latest .
                    docker tag $DOCKER_REGISTRY/$DOCKER_USERNAME/$APP_NAME:latest $DOCKER_REGISTRY/$DOCKER_USERNAME/$APP_NAME:${GIT_COMMIT}
                    docker push $DOCKER_REGISTRY/$DOCKER_USERNAME/$APP_NAME:latest
                    docker push $DOCKER_REGISTRY/$DOCKER_USERNAME/$APP_NAME:${GIT_COMMIT}
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean workspace after build
        }
    }
}
