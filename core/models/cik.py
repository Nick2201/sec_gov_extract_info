from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String,DateTime
from sqlalchemy.sql import func
from .base import Base 
from datetime import datetime
from typing_extensions import Annotated
from decimal import Decimal

# str_50 = Annotated[str, 50]
# num_12_4 = Annotated[Decimal, 12]

class Cik(Base):
    cik_str: Mapped[str]         = mapped_column(String(10), not_null=True)
    ticker: Mapped[str]          = mapped_column(String(10))
    title: Mapped[int]           = mapped_column(String(100))
    time_load:Mapped[datetime]   = mapped_column(DateTime(timezone=True), 
                                                 server_default=func.now(),
                                                onupdate=func.now())
