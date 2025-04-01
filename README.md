# PROG8850Template
environment with mysql, python, node and docker

TLDR;

```bash
pip install -r requirements.txt
ansible-playbook up.yaml
```

To access database:

```bash
mysql -u root -h 127.0.0.1
```

To cleanup

```bash
ansible-playbook down.yaml
```

happy mysql!
