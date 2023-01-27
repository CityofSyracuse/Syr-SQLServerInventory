import pandas as pd

class Querier(object):
    def __init__(self, conn, engine=None):
        self.conn = conn
        self.engine = engine

    def perform_query(self, q) -> pd.DataFrame:

        if self.engine:
            self.engine.execution_options(stream_results=True)
            dfs = []
            for chunk in pd.read_sql(q, self.conn, chunksize=5000):
                dfs.append(chunk)
            pd.concat(dfs, ignore_index=True)
        return pd.read_sql(q, self.conn)