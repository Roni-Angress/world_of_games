pipeline {
    agent any

    environment {
        CONTAINER_NAME = 'world_of_games-web-web'
        DOCKER_IMAGE_TAG = 'latest'
    }

    stages {
        stage('Git-Pull') {
            steps {
                git branch: 'main', url: 'https://github.com/Roni-Angress/world_of_games.git'
            }
        }

        stage('Build-and-Run') {
            steps {
                sh 'docker compose up --detach'
            }
        }

        stage('Test') {
            steps {
                script {
                    def status = sh(script: "docker exec ${CONTAINER_NAME} python tests/e2e.py", returnStatus: true)
                    if (status != 0) {
                        error "Tests failed"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the container
                    sh 'docker compose down'
                    // Tag the image
                    sh 'docker tag world_of_games-web-web:latest roniangress/world_of_games-web:latest'
                    // Push the image to DockerHub
                    sh 'docker push roniangress/world_of_games-web:latest'
                }
            }
        }
    }
}
