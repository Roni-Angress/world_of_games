pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/Roni-Angress/world_of_games.git'
            }
        }

        stage('Install/Update Docker'){
            steps{
                sh '''
                apt-get update
                apt-get install -y docker.io
                apt-get install -y curl
                curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                chmod +x /usr/local/bin/docker-compose
                '''  
            }
        }

        stage('Build and run') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}
