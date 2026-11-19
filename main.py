from preprocess import preprocess_comments, preprocess_issues
from rq1 import analyze_issues
from rq2 import analyze_comments
import os

ROOT = os.getcwd()
DATA_DIR = os.path.join(ROOT,"data")
OUTPUT_DIR = os.path.join(ROOT,"results")
os.makedirs(OUTPUT_DIR,exist_ok=True)


def main() -> None:

    issues_df = preprocess_issues(DATA_DIR)
    issues_comments_df = preprocess_comments(DATA_DIR)
    
    analyze_issues(issues_df,OUTPUT_DIR)
    analyze_comments(issues_df,OUTPUT_DIR)


if __name__ == "__main__":
    main()