# Mini Empirical Study : GitHub Issues created by AI Coding Agents

**Name**: Rahfay Saberi

## Research Question Formulation 

### RQ1. Closure Reason (Descriptive)

Analyze closed GitHub issues for the purpose of characterizing their closure reasons with respect to the frequency and distribution of closure categories from the point of view of software developers in the context of software development projects.

### RQ2. Closure Reason (Quantitative)

Analyze closed software issues for the purpose of comparing closure reasons with respect to comment count and time-to-close from the point of view of software developers in the context of software development projects.


## Data Processing

### Analysis (issues.csv)

As seen from the NaN values plot and dataframe, a substantial number of columns have a large number of missing values. For columns such as `comments_count_reported`,`draft`, `milestone_state`, `milestone_title`, `closed_at` which contain over 70% missing values, imputation would lead to serve bias. For these columns we will simply remove them.

For `time_to_close_hours` which is required to answer RQ2 we will drop all NaN rows. The reasons behind this is that imputation on this column would introduce massive bias as we would be using 25% of the data to represent the other 75%.  

For `api_closed_at` column, given our task is to analyze reasons issues get closed, we will remove all rows where `api_closed_at` is NA which means the issue has not been closed

`label` we will encode all NaN values in this `not resolved`.

`state_reason` provides the reason a github issue was closed. For the analysis we are performing this is a crucial feature, to avoid bias we will remove all values that are NA

`body`, since only a small portion of these values or NaN, we will replace all NaN values with "empty"

## RQ Analysis

### RQ1 Findings

From the DataFrame and visualization above, we can identify three primary reasons why GitHub issues were closed:

1. **Completed**
2. **Not Planned**
3. **Duplicate**

The majority of closed issues fall under the **completed** category, accounting for 91.6% of all issues. In comparison, **not planned** issues represent a smaller proportion at 7.9%, while **duplicate** issues account for only 0.5%.

These findings indicate that the overwhelming majority of issues in the dataset were closed because they were completed, rather than being rejected, deprioritized, or identified as duplicates.

### Implications for Developers and Researchers

For developers, these findings suggest that most issue closures within the analyzed repositories are associated with completed work, potentially indicating that issue tracking is primarily used to manage and document development tasks through to completion. The relatively small proportion of issues closed as not planned or duplicates may also suggest that fewer issues are being dismissed or identified as redundant.

### RQ2 Findings


The results indicate a large difference in comment activity across the three closure reasons.

- **Completed:** 705 comments, accounting for approximately 97.1% of all recorded comments.
- **Not planned:** 20 comments, representing approximately 2.8%.
- **Duplicate:** 1 comment, representing approximately 0.1%.

These findings suggest that issues classified as completed account for the overwhelming majority of recorded discussion activity.

All three closure categories have an average time-to-close of 0.0 hours.

Although this initially suggests that issues are closed immediately, this result should likely be interpreted as a dataset limitation rather than an accurate representation of issue resolution times.

### Implications for Developers and Researchers

For developers, the findings suggest that completed issues account for most recorded comment activity, potentially reflecting greater discussion and collaboration during issue resolution. In contrast, issues closed as duplicates or not planned contribute relatively little to the overall comment activity. However, this does not necessarily indicate that individual completed issues require more discussion, as the number of issues in each closure category has not been considered.

## Threats to Validity


### 1. Construct Validity

Construct validity concerns whether the selected metrics accurately measure the concepts being investigated.

For RQ1, the `state_reason` attribute is used to identify why GitHub issues were closed. However, this attribute may not fully represent the underlying reasons for closure, as developers may close issues for reasons that are not adequately captured by the available categories (completed, not planned, and duplicate).

For RQ2, `n_comments_actual` is used to measure discussion activity. However, comment count does not necessarily reflect the quality or significance of developer discussions. Additionally, the `time_to_close_hours` attribute may not accurately represent actual issue resolution time, given that all closure categories produced an average of 0.0 hours. This suggests potential limitations in how the timestamps were recorded or calculated.

### 2. Internal Validity

Internal validity concerns whether the observed results are influenced by factors other than those being investigated.

A major threat arises from the dataset's missing values and the preprocessing decisions made to address them. Several columns contain over 70% missing values and were removed to avoid introducing bias through imputation.

Furthermore, rows containing missing `time_to_close_hours`, `api_closed_at`, or `state_reason` values were excluded from the analysis. While necessary for the research questions, removing these observations may introduce **selection bias**, as the remaining issues may not be representative of the original dataset.

In particular, removing approximately 75% of observations with missing `time_to_close_hours` significantly reduces the sample available for RQ2. If missing timestamps are associated with certain closure reasons, the resulting comparisons may be distorted.

### 3. External Validity

External validity concerns whether the findings can be generalized beyond the analyzed dataset.

The dataset contains 5,000 GitHub issues collected from a selection of repositories. Therefore, the observed distribution of closure reasons may not represent the behavior of all GitHub repositories or software development projects.

Different projects may follow different issue management practices, including how issues are categorized, discussed, and closed. Consequently, the finding that 91.6% of issues were closed as completed may be specific to the repositories included in the dataset.

Furthermore, the dataset combines GitHub Archive records with GitHub API information, which may represent different collection periods. This limits the ability to generalize the findings to other time periods or development environments.

### 4. Conclusion Validity

Conclusion validity concerns whether the conclusions drawn from the analysis are adequately supported by the available data.

- RQ1: The substantial imbalance between closure reasons (91.6% completed, 7.9% not planned, and 0.5% duplicate) means that conclusions regarding less common categories are based on relatively few observations. This limits the reliability of comparisons involving duplicate issues.

- RQ2: Completed issues account for 705 of the 726 recorded comments. However, these are total comment counts rather than average comments per issue. Therefore, the results cannot establish whether completed issues receive more discussion individually, since the number of issues within each category differs.

Additionally, the average time-to-close of 0.0 hours across all closure reasons prevents meaningful conclusions about differences in resolution time. Without validating the underlying timestamps, it would be inappropriate to conclude that issues are resolved immediately or that closure reasons have no relationship with resolution duration.

## AI Disclosure

No generative AI tools were used to draft, research, analyze, or revise this submission.