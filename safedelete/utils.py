from django.db.models.deletion import Collector
from django.db import router


HARD_DELETE = 0
SOFT_DELETE = 1
SOFT_DELETE_CASCADE = 2
HARD_DELETE_NOCASCADE = 3
NO_DELETE = 4
SOFT_DELETE_IF_NO_PROTECT = 5

DELETED_INVISIBLE = 10
DELETED_VISIBLE_BY_PK = 11


def collect(obj):
    collector = Collector(using=router.db_for_write(obj))
    collector.collect([obj])
    return collector


def can_hard_delete(obj):
    return not bool(collect(obj).fast_deletes)
