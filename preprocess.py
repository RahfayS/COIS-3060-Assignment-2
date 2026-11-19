import pandas as pd
import os
# Denotes the columns to drop from issues.csv
DROP_ISSUE_COLUMNS = [
    "comments_count_reported", "draft", "milestone_state",
    "milestone_title", "closed_at",
]

# Denotes the columns to drop from issue_comments.csv
DROP_COMMENT_COLUMNS = ["author_login", "repo_name", "body"]


def preprocess_issues(data_dir:str = "data") -> pd.DataFrame:
    issues = pd.read_csv(os.path.join(data_dir, "issues.csv"))
    issues = issues.drop(columns=DROP_ISSUE_COLUMNS)

    issues = issues.dropna(subset=["time_to_close_hours"])
    issues = issues.dropna(subset=["api_closed_at"])
    issues["labels"] = issues["labels"].fillna("not resolved")
    issues = issues.dropna(subset=["state_reason"])
    issues["body"] = issues["body"].fillna("empty")
    return issues


def preprocess_comments(data_dir:str = "data") -> pd.DataFrame:
    comments = pd.read_csv(os.path.join(data_dir,"issue_comments.csv"))
    return comments.drop(columns=DROP_COMMENT_COLUMNS)


