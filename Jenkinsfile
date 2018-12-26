pipeline {
    agent any
    //parameters {
            /*
              TEST_IP is used to hold the ip of the current server (dev or stage)
              This variable is used to run the python tests
            */
            // string(name: 'TEST_IP', defaultValue: '')
    //}

    stages {
        stage("Run tests on Dev site") {
            // when { branch 'dev' }
            steps {
                echo 'Testing Dev'
            }
        }
        stage("Deploy to Prod"){
            // when { branch 'dev' }
            steps {
                echo 'Deploying to prod'
            }
        }
    }
}
