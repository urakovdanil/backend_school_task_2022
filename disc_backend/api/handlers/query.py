from sqlalchemy import select, text

from disc_backend.db.schema import items_table


ITEMS_QUERY = select([items_table.c.id,
                      items_table.c.url,
                      items_table.c.parentId,
                      items_table.c.size,
                      items_table.c.type,
                      items_table.c.updateDate])


HIERARCHY_QUERY = text(
    'WITH RECURSIVE cte_files AS ('
    """    SELECT  id, url, "parentId", size, "type", "updateDate" AS date"""
    '    FROM    items'
    '    WHERE   id = :id'
    '    UNION ALL'
    '    SELECT  i.id, i.url, i."parentId", i.size, i."type", i."updateDate" AS date'
    '    FROM    items i'
    '    INNER JOIN cte_files f ON f.id = i."parentId")'
    'SELECT * FROM cte_files'
)

COMPLETE_HIERARCHY_QUERY = text(
    'WITH RECURSIVE cte_files AS ('
    '    SELECT  id, url, "parentId", size, "type", "updateDate"'
    '    FROM    items'
    '    WHERE   "parentId" IS NULL'
    '    UNION ALL'
    '    SELECT  i.id, i.url, i."parentId", i.size, i."type", i."updateDate"'
    '    FROM    items i'
    '    INNER JOIN cte_files f ON f.id = i."parentId")'
    'SELECT * FROM cte_files'
)

UPDATE_SIZE_QUERY = text(
    'UPDATE items SET size = :size WHERE id = :id'
)
