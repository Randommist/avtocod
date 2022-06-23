from typing import Optional, List, Any

from avtocod.types import AvtocodObject


class Query(AvtocodObject):
    body: Optional[str] = None
    type: Optional[str] = None
    storages: Optional[List[Any]] = None
    schema_version: Optional[str] = None
