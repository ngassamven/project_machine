import logging
import os
from datetime import datetime

# Définition du fichier log avec horodatage
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(logs_path, exist_ok=True)  # Création du dossier s'il n'existe pas

# Définition du dossier des logs
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
#logs_dir = os.path.join(os.getcwd(), "logs")




# Configuration du logging (utilisation du logger root)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filemode='w'
)


