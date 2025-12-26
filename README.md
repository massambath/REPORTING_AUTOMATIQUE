# Automated Sales Reporting Pipeline

Projet de pipeline de données complet inspiré de mon expérience en supervision 24/7.  
Objectif : automatiser le reporting des ventes, monitorer les indicateurs clés et envoyer des alertes en temps réel via Grafana et email.  
Ce projet démontre mes compétences en **Data Engineering, ETL, SQL, Python, Grafana et automatisation**.

## Fonctionnalités
- Génération de données de ventes réalistes (CSV)  
- ETL : nettoyage, enrichissement, chargement dans MySQL  
- Modèle de données analytique (tables fact/dimension)  
- Dashboards Grafana pour monitoring et alertes (top produits, stocks critiques)  
- Automation : capture de dashboard + envoi email quotidien  
- Projet modulable et extensible

## Structure du projet
automated-sales-reporting/
│
├── README.md                # Explications du projet, objectifs, stack, capture d'écran
├── requirements.txt         # Packages Python nécessaires (pandas, mysql-connector, selenium, etc.)
│
├── data/
│   ├── raw/                 # CSV bruts générés ou récupérés
│   │   └── sales_YYYYMMDD.csv
│   └── processed/           # Données transformées ETL prêtes pour MySQL
│
├── mysql/
│   ├── schema.sql           # Création des tables (dim_product, dim_date, fact_sales)
│   ├── views.sql            # Vues / tables analytiques pour Grafana
│   └── sample_data.sql      # Optionnel : quelques lignes pour test
│
├── etl/
│   ├── generate_data.py     # Génération de CSV fake ou ingestion source
│   ├── load_mysql.py        # Script pour alimenter MySQL (batch ETL)
│   └── transform_data.py    # Nettoyage, enrichissement, calcul des metrics
│
├── grafana/
│   ├── dashboards.json      # Export des dashboards Grafana
│   └── alerts_config.json   # Configurations d’alertes (ex : stock critique)
│
├── automation/
│   ├── screenshot_dashboard.py   # Selenium pour screenshots du dashboard
│   ├── send_email.py             # Envoi automatique des rapports
│   └── daily_report.py           # Script tout-en-un planifiable via cron
│
└── demo/
    └── demo_video.mp4            # Vidéo courte de présentation / démonstration

