pipeline {
    agent { label "agent-exam2" }
    stages {
	    stage('DEPLOY') {
            steps {
                sh "ansible-galaxy install -r requirements.yml"
                ansiblePlaybook(
                    credentialsId: 'ansible_exam2',
                    inventory: 'hosts',
                    playbook: 'playbook.yml',
                    vaultCredentialsId: 'ansible_vault_password'
                    )
            }
	    }
	    stage('TEST') {
            steps {
                sh 'python3 ./test_web_app.py http://192.168.56.10'
            }
        }
    }
}
