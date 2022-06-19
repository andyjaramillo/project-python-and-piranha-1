
#!/bin/env bash

tmux kill-session -a
cd project-python-and-piranha-1
cd project-python-and-piranha-1
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
tmux
flask run --host=0.0.0.0
tmux detach
