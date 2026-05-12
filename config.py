from pathlib import Path

APP_TITLE = "Petto"
APP_DESCRIPTION = "Seguimiento post-adopción para refugios y adoptantes"

DATABASE_DIR = Path("/tmp")
DATABASE_PATH = DATABASE_DIR / "petto.db"

MIN_ADAPTATION_SCORE = 1
MAX_ADAPTATION_SCORE = 10

LOW_RISK_MIN = 7
MEDIUM_RISK_MIN = 4
