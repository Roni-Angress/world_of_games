pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: '**/main', url: 'https://github.com/Roni-Angress/world_of_games.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}
