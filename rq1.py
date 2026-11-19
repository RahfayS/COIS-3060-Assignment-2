import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import pandas as pd
import os

def analyze_issues(df: pd.DataFrame,output_dir:Path):
    output_path = os.path.join(output_dir,"rq1_counts.csv")
    counts = df["state_reason"].value_counts()
    counts.to_csv(output_path)
    print(counts)
    _pie_plot(counts,output_dir)


def _pie_plot(counts: pd.DataFrame, output: Path) -> None:
    output_path = os.path.join(output,"rq1_pie_plot.png")
    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel", len(counts)),
        startangle=90,
    )
    ax.set_title("Distribution of Issue Closure Reasons")
    ax.axis("equal")
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


