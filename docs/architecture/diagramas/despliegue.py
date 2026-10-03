from diagrams import Cluster, Diagram
from diagrams.onprem.client import User, Client
from diagrams.onprem.network import Nginx
from diagrams.onprem.database import PostgreSQL
from diagrams.programming.framework import React
from diagrams.programming.language import Python

with Diagram(
    "Vista de Despliegue - EcoRecicla AQP (VPS)",
    show=False,
    filename="despliegue",
    direction="LR"
):
    # Actores
    vecino = User("Vecino / Reciclador")
    muni = Client("Admin Municipal")

    # Servidor VPS (Monolito)
    with Cluster("Servidor VPS (Unico Nodo)"):
        web_server = Nginx("Nginx (Reverse Proxy / SSL)")
        
        with Cluster("Aplicacion Monolito Modular"):
            app = Python("Backend API (Node/Python/Java)")
            pwa = React("PWA / Frontend Static")
            
        db = PostgreSQL("PostgreSQL DB")

    # Conexiones
    vecino >> web_server
    muni >> web_server
    web_server >> pwa
    web_server >> app
    app >> db
