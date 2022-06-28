
#!/bin/env bash

cd  project-python-and-piranha-1
cd  project-python-and-piranha-1
git fetch && git reset origin/main --hard
cd ..
source python3-virtualenv/bin/activate
cd  project-python-and-piranha-1
pip install -r requirements.txt
cd /etc/systemd/system
systemctl restart myportfolio
