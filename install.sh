url='https://github.com/DTunnel0/DownloaderPage.git'
dependencies=(git python3 python3-pip screen)

for dependence in "${dependencies[@]}"; do
    if ! command -v $dependence >/dev/null 2>&1; then
        echo "Installing $dependence..."
        apt install $dependence -y &>/dev/null
    fi
done

git clone $url &>/dev/null
cd DownloaderPage
mkdir uploads

pip3 install -r requirements.txt &>/dev/null
read -p 'Porta: ' -e -i 5001 port
screen -dmS downloader python3 main.py $port

echo "Instalado com sucesso!"
echo "Acesse http://$(curl -4s https://api.ipify.org):$port"
