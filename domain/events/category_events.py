from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

@dataclass
class CategoryCreated:
    category_id: str
    timestamp: datetime

@dataclass
class CategoryUpdated:
    category_id: str
    timestamp: datetime
    updated_fields: Dict[str, Optional[str]]

@dataclass
class CategoryActivated:
    category_id: str
    timestamp: datetime

@dataclass
class CategoryDeactivated:
    category_id: str
    timestamp: datetime
