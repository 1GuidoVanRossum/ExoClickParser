import pandas as pd


def CreateTable(stats, i):
    df = pd.DataFrame(stats)
    df.to_excel(f'campaign_stats_{i}.xlsx', index=False)

