from sqlglot.optimizer import (
    canonicalize,
    eliminate_ctes,
    eliminate_joins,
    eliminate_subqueries,
    expand_laterals,
    expand_multi_table_selects,
    isolate_table_selects,
    lower_identities,
    merge_subqueries,
    normalize,
    optimize_joins,
    pushdown_predicates,
    pushdown_projections,
    qualify_columns,
    qualify_tables,
    simplify,
    unnest_subqueries,
)
from sqlglot.optimizer.optimizer import RULES, optimize
from sqlglot.optimizer.scope import Scope, build_scope, traverse_scope
