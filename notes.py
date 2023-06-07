

"https://picocss.com/#examples"
"https://docs.djangoproject.com/en/4.1/intro/tutorial01/"

# python manage.py makemigrations
# python manage.py check
# python manage.py migrate
# python manage.py shell -- https://docs.djangoproject.com/en/4.1/intro/tutorial02/

# Verifica as imagens locais
# docker images

# Roda a imagem docker e entra no bash
# docker run -it --entrypoint /bin/bash jordhisu/django-web-app-repo -s

# Libera as portas na máquina virtual EC2
# sudo iptables -L
# sudo iptables -A INPUT -p tcp --dport 8020 -j ACCEPT
# docker run -d -p 8020:8020 jordhisu/django-web-app-repo


# Pra fazer build e deploy da imagem

# No terminal local:
# docker build ./app -t app; docker image tag app jordhisu/django-web-app-repo; docker image push jordhisu/django-web-app-repo
# ssh -i lab-web.pem ubuntu@<ec2_public_ip>

# No terminal ssh:
# docker pull jordhisu/django-web-app-repo
# docker stop $(docker ps -a -q) & docker ps & docker run -d -p 8020:8020 jordhisu/django-web-app-repo

# Acessar o site:
# http://<ec2_public_ip>:8020/

