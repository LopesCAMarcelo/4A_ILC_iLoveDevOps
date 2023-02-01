#Choix de la version de python utilisée, du label maintainers et de l'emplacement
FROM python:3.8
LABEL maintainer="CCC_Lopes_Peyron"
WORKDIR /app

#Copie des bibliothèques requises de la machine hôte vers le conteneur
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copie des fichiers de test
COPY src .

#Préparation du lancement
EXPOSE 80
ENV PORT=80
ENTRYPOINT ["python", "src/main.py"]