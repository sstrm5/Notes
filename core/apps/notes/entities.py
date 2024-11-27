from dataclasses import dataclass
from datetime import datetime


@dataclass
class Note:
    id: int
    customer_id: int
    is_checked: bool
    title: str
    text: str
    is_important: bool
    created_at: datetime
    updated_at: datetime
