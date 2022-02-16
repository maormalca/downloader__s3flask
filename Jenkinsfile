def stage_name
properties([
   parameters([
    string(name: 'ip_server', defaultValue: '10.1.0.7', description: 'ip_addres'),
    string(name: 'ACCESS_KEY_ID', defaultValue: 'AKIA4QDUZQ7LHAVX6KFN', description: 'KEYS'),
    string(name: 'SECRET_ACCESS_KEY', defaultValue: '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', description: 'secret access key')
   ])
])
node("maorsslave"){
    withCredentials([usernamePassword(credentialsId: 'cred_for_s3', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
        stage("create .env fil"){
            sh """sshpass -p ${PASSWORD} ssh ${USERNAME}@${params.ip_server} -o StrictHostKeyChecking=no << EOF
            echo "SECRET_ACCSESS_KEY=${params.SECRET_ACCESS_KEY} \n ACCESS_KEY_ID=${params.ACCESS_KEY_ID} " > .env
            cat .env"""
        }
        stage("git clone"){
            sh """ git clone https://github.com/maormalca/downloader_s3_flask.git  
            cd downloader_s3_flask 
            sshpass -p ${PASSWORD} scp -o StrictHostKeyChecking=no install_app.sh ${USERNAME}@${params.ip_server}:/home/maormalca"""
        }
        stage("run script"){
            sh """sshpass -p ${PASSWORD} ssh ${USERNAME}@${params.ip_server} -o StrictHostKeyChecking=no << EOF
            bash install_app.sh"""
        }
        stage("test"){
            def test = sh(returnStdout: true, script: 'curl localhost:8082 &> /dev/null && echo $?').trim() 
            if (test != '0' ){
                error("Build failed webserver is down..")
            }
            else{
                println("the web server is up")
            }
            
        }
    }
}
