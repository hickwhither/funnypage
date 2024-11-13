import sqlalchemy
db: sqlalchemy

from website import db
from flask_login import UserMixin
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.mutable import *

import time
import uuid


class Segment(db.Model):
    # ID
    id: Mapped[int] = mapped_column(primary_key=True)
    
    left: Mapped[int] = mapped_column(default=0)
    right: Mapped[int] = mapped_column(default=0)

    value: Mapped[int] = mapped_column(default=0)
    lazy: Mapped[int] = mapped_column(default=0)
    
    def __repr__(self):
        return f"Segment({self.id} [{self.left} {self.right}] value:{self.value} lazy:{self.lazy})"