from diagrams import Diagram, Cluster
from diagrams.onprem.network import Nginx
from diagrams.onprem.compute import Server
from diagrams.onprem.queue import Kafka
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.monitoring import Prometheus, Grafana
from diagrams.onprem.analytics import Spark
from diagrams.aws.general import Client
from diagrams.aws.network import CloudFront

with Diagram("Bitly URL Shortener", show=False, direction="TB", filename="bitly_url_shortener_design"):
    client = Client("Client")

    with Cluster("CDN + Edge"):
        cdn = CloudFront("CloudFront")

    with Cluster("Load Balancing"):
        lb = Nginx("Nginx / HAProxy")

    with Cluster("App Layer (Auto-Scaled)"):
        app_servers = [Server("Shortener Service") for _ in range(5)]

    with Cluster("ID Generation"):
        id_gen = Server("Distributed ID Generator")

    with Cluster("Caching"):
        redis_primary = Redis("Redis Cluster")

    with Cluster("Database"):
        db_master = PostgreSQL("PostgreSQL Master")
        db_replicas = [PostgreSQL("Read Replica") for _ in range(2)]

    with Cluster("Message Queue"):
        kafka = Kafka("Kafka Cluster")

    with Cluster("Analytics + ETL"):
        spark = Spark("Spark ETL")
        analytics_db = PostgreSQL("OLAP DB")

    with Cluster("Monitoring + Logging"):
        prom = Prometheus("Prometheus")
        grafana = Grafana("Grafana")

    # Flow
    client >> cdn >> lb >> app_servers
    app_servers >> id_gen
    app_servers >> redis_primary
    app_servers >> db_master
    db_master >> db_replicas

    app_servers >> kafka >> spark >> analytics_db

    app_servers >> prom
    prom >> grafana