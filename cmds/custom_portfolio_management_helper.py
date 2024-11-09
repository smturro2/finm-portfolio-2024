import pandas as pd
import numpy as np


def calc_summary_stats(df, mask=None, summary_cols=None, annual_factor=1,
                 var_quantile=0.05):
    if mask is not None:
        df = df.loc[mask]
        
    summary_funcs = {
        "mean": lambda x: x.mean() * annual_factor,
        "vol": lambda x: x.std() * np.sqrt(annual_factor),
        "sharpe": lambda x: x.mean() / x.std() * np.sqrt(annual_factor),
        "excess_kurtosis": lambda x: x.kurtosis() - 3,
        "kurtosis": lambda x: x.kurtosis(),
        "skewness": lambda x: x.skew(),
    }
    
    # var/cvar
    for q in [var_quantile]:
        summary_funcs[f"{q*100:.0f}% VaR"] = lambda x: x.quantile(q)
        summary_funcs[f"{q*100:.0f}% cVaR"] = lambda x: x[x <= x.quantile(q)].mean()
    
    # # Max Drawdown
    # df_aum = (df+1).cumprod()
    # draw_downs = (df_aum.cummax() - df_aum) / df_aum.cummax()
    # df_summary.loc["Max Drawdown"] = draw_downs.max()

    # Filter cols
    wrong_summary_cols = [c for c in summary_cols if c not in summary_funcs]
    if len(wrong_summary_cols) > 0:
        raise ValueError(f"Invalid summary_cols: {wrong_summary_cols}")
    if summary_cols is not None:
        summary_funcs = {k: v 
                         for k, v in summary_funcs.items() if k in summary_cols}
        
    df_summary = df.apply(lambda x: pd.Series({k: f(x) for k, f in summary_funcs.items()}))
    return df_summary