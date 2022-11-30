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
      echo 'python3 main.py'
      }
    }
    stage('choose level'){
      steps {
        echo '3'
      }
    }
    post{
      always{
        echo 'always'}
      success{
        echo 'success'}
      failure
      {
        echo 'failure'
      }
    }
  }
}
