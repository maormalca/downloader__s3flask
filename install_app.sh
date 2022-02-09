sudo git clone https://github.com/maormalca/downloader_s3_flask.git
sudo cp .env downloader_s3_flask/
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo apt install -y docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
cd downloader_s3_flask/
sudo docker-compose up -d --build
