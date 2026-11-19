import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import pandas as pd
import os

def analyze_comments(df: pd.DataFrame,output_dir: str) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:

    # Total comments across closure reasons
    comments = (
        df.groupby("state_reason")["n_comments_actual"]
        .sum()
        .reset_index(name="total_comments")
    )

    # Average time-to-close across closure reasons
    times = (
        df.groupby("state_reason")["time_to_close_hours"]
        .mean()
        .reset_index(name="avg_time_to_close_hours")
        .round(2)
    )

    # Merge results
    merged = comments.merge(
        times,
        on="state_reason",
        how="outer"
    )

    # Save result DataFrames
    comments.to_csv(os.path.join(output_dir,"comments_counts.csv"), index=False)
    times.to_csv(os.path.join(output_dir,"time_to_close.csv"), index=False)
    merged.to_csv(os.path.join(output_dir,"rq2_summary.csv"), index=False)

    # Plot total comments
    save_barplot(
        df=comments,
        value_col="total_comments",
        ylabel="Total Comments",
        title="Comment Count Across Closure Reasons",
        output=os.path.join(output_dir,"comment_counts.png")
    )

    # Plot average time-to-close
    save_barplot(
        df=times,
        value_col="avg_time_to_close_hours",
        ylabel="Average Time-to-Close (Hours)",
        title="Average Time-to-Close Across Closure Reasons",
        output=os.path.join(output_dir,"time_to_close.png")

    )

    return comments, times, merged


def save_barplot(df: pd.DataFrame,value_col: str,ylabel: str,title: str,output: str) -> None:
    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.barplot(
        data=df,
        x="state_reason",
        y=value_col,
        hue="state_reason",
        palette="pastel",
        dodge=False,
        legend=False,
        ax=ax
    )

    ax.set_xlabel("Closure Reason")
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    fig.tight_layout()
    fig.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(fig)