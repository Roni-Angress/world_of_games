pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/Roni-Angress/world_of_games.git'
            }
        }

        stage('Install/Update Docker'){
            sh 'apt-get update'
            sh 'apt-get install -y docker.io'
            sh 'apt-get install -y curl'
            sh 'curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
            sh 'chmod +x /usr/local/bin/docker-compose'
        }
        
        stage('Build and run') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}
