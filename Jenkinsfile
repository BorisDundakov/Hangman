pipeline {
  agent {
    label "hangman"
    }
  parameters {
    string (name: 'Version', defaulValue: 'abc', description:'initial version')
  
    }
  
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
  }
}
