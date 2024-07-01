pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/Roni-Angress/world_of_games.git'
            }
        }

        stage('Build and run') {
            steps {
                script {
                    docker.build('world_of_games-web:latest').inside {
                        sh 'echo "Building..."'
                        sh 'docker-compose up -d'
                    }
                } // <-- Added missing closing brace for 'script'
            }
        }
    }
}
