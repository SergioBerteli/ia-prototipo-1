# ia-prototipo-1
Requisitos para executar o script:
- Ferramenta para acessar a CLI
- Docker
- Python

Tutorial de como rodar a aplicação:

1. Execute o container que contem o banco de dados
Estando dentro da pasta base_de_dados, execute os seguintes comando para construir a imagem e executa-la:
```bash
docker build -t server_ia_1 .
```
```bash
docker run --name img_server_ia_1 -p 3306:3306 -e MYSQL_DATABASE=db -e MYSQL_ROOT_PASSWORD=root -d server_ia_1:latest 
```

2. Com o container executado, abra a pasta sistema_rbc e execute os seguinte comandos:
```bash
pip install -r requirements.txt
```
```bash
python sistema_rbc.py
```