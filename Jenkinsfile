pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: docker
            image: docker:latest
            command:
            - cat
            tty: true
            volumeMounts:
             - mountPath: /var/run/docker.sock
               name: docker-sock
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock    
        '''
    }
  }
  stages {
    stage('Clone') {
      steps {
        container('docker') {
          git branch: 'main', url: 'https://github.com/Roni-Angress/world_of_games.git'
        }
      }
    }  
    stage('Build-and-Run') {
      steps {
        container('docker') {
          sh 'docker-compose up --build'
          }
         }
        }
    }
}