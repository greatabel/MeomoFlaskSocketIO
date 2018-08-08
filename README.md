aliyu ubuntu:

sudo apt-get update
apt install python3-pip
apt install git

pip3 install virtualenv
pip3 install virtualenvwrapper
设置
export WORKON_HOME=~/.virtualenvs
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh

然后进行 创建的虚拟环境：
pip3  install -r requirements.txt

