pipeline {
  agent any
  stages{
    stage('version'){
      steps {
      sh 'python3 --version'
      }
    }
    stage('run program'){
      steps {
      sh 'python3 main.py'
      }
    }
    stage('choose level'){
      steps {
        sh 3
      }
    }
  }
}
