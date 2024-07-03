pipeline {
  agent {

  }
  stages {
    stage('Git-Clone') {
      steps {

          git branch: 'main', url: 'https://github.com/Roni-Angress/world_of_games.git'
    }
 }  
    stage('Build-and-Run') {
      steps {
            sh 'docker-compose up --build'
         }
        }
    }
}