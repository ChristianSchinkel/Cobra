"""Statistics utilities."""
# P-value threshold for statistical significance
# ABOVE THIS VALUE, WE FAIL TO REJECT THE NULL HYPOTHESIS
# BELOW THIS VALUE, WE REJECT THE NULL HYPOTHESIS
# COMMONLY USED THRESHOLD IS 0.05, MEANING THERE IS
# A 5% CHANCE OF OBSERVING THE DATA IF
# THE NULL HYPOTHESIS IS TRUE.
# from statistics import mean, stdev
from enum import Enum
import pandas as pd
import matplotlib.pyplot as plt


class DistributionType(Enum):
    """Types of Data Distribution."""
    SYMETRIC = "symetric"
    POSITIVELY_SKEWED = "positively skewed"
    NEGATIVELY_SKEWED = "negatively skewed"

    def describe_tail_position(self) -> str:
        """Describe the position of the left tail."""
        if self == DistributionType.SYMETRIC:
            return "The left tail is balanced with the right tail."
        if self == DistributionType.POSITIVELY_SKEWED:
            return "The long tail is on the right side."
        if self == DistributionType.NEGATIVELY_SKEWED:
            return "The long tail is on the left side."
        return "Unknown distribution type."

    def identify_skewness(self,
                          mean: float,
                          median: float,
                          mode: float) -> DistributionType:
        """Identify the skewness of the distribution based on mean, median, and mode."""
        if mean == median == mode:
            return DistributionType.SYMETRIC
        elif mean > median:
            return DistributionType.POSITIVELY_SKEWED
        else:
            return DistributionType.NEGATIVELY_SKEWED


P_VALUE_THRESHOLD = 0.05


def load_data(file_path: str = "../data") -> pd.DataFrame:
    """Load data from a CSV file.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
        this value is used to be stored as "df" in the main function,
        and then used for further analysis and processing.
    """
    return pd.read_csv(file_path)


def get_frequency(column_name: str, df: pd.DataFrame) -> pd.Series:
    """Get the frequency of values in a column."""
    return df[column_name].value_counts()


def sumarize(df: pd.DataFrame,
             group_col: str,
             value_col: str,
             agg="mean",
             sort=True) -> pd.Series:
    """Summarize the data by grouping and aggregating.
    Args:
        df (pd.DataFrame): The input DataFrame.
        group_col (str): The column to group by.
        value_col (str): The column to aggregate.
        agg (str): The aggregation function to use (default is "mean").
        sort (bool): Whether to sort the result by the aggregated values
        (default is True).
    Returns:        pd.Series: The summarized series.
    """
    result = df.groupby(group_col)[value_col].agg(agg)
    if sort:
        result = result.sort_values(ascending=False)
    return result


def abouve_percentile(df: pd.DataFrame,
                      group_col: str,
                      value_col: str,
                      q: float = 0.9):
    """Calculate the percentage of values above a certain percentile.
    Args:
        df (pd.DataFrame): The input DataFrame.
        group_col (str): The column to group by.
        value_col (str): The column to calculate the percentile for.
        q (float): The percentile to calculate (default is 0.9 for the 90th percentile).
    Returns:        pd.Series: The percentage of values above the specified percentile
    for each group.
    """
    result = sumarize(df, group_col, value_col)  # first, aggregate for groups
    threshhold = result.quantile(q)  # then find the top 10%
    return result[result > threshhold]  # check if there are outliers,
    # and return those values


def chunk_data(file_path: str, chunksize: int = 1000) -> int:
    """Read a CSV file in chunks.
    Args:
        file_path (str): Path to the CSV file.
        chunksize (int): Number of rows per chunk (default is 1000).
    Yields:
            pd.DataFrame: A chunk of the data as a DataFrame.
        """
    total_rows = 0

    for chunk in pd.read_csv(file_path, chunksize=chunksize):
        # Process the chunk separately, if memory is limited.
        total_rows += len(chunk)

    print(f"Processed rows: {total_rows} rows in chunks of {chunksize}.")

    return total_rows


def select_features(*args: str) -> list:
    """Select features for analysis."""
    return list(args)


def calculate_basic_statistics(data: list, df: pd.DataFrame) -> None:
    """Calculate basic statistics for a list of values."""
    for feature in data:
        print(f"Statistics for {feature}:")
        print(f"Mean: {df[feature].mean():.2f}")
        print(f"Median: {df[feature].median():.2f}")
        print(f"Mode: {df[feature].mode()[0]:.2f}")
        print(f"Min: {df[feature].min():.2f}")
        print(f"Max: {df[feature].max():.2f}")
        print(f"Standard Deviation: {df[feature].std():.2f}")


def paint(
        figuresize: tuple = (15, 4),
        features: list = ["Feature 1"],
        subplots_rows: int = 1,
        subplots_cols: int = 3,
        bins: int = 30,
        color: str = "skyblue",
        edgecolor: str = "black",
        ylabel: str = "Frequency",
        title: str = "Distribution of Features"
        ) -> None:
    """Plot the distribution of features."""
    if features is None:
        features = []
    plt.figure(figsize=figuresize)
    for i, feature in enumerate(features, 1):
        plt.subplot(subplots_rows, subplots_cols, i)
        plt.hist(feature, bins=bins, color=color, edgecolor=edgecolor)
        plt.title(title)
        plt.ylabel(ylabel)

    plt.tight_layout()
    plt.show()


def linear_function(x: float, a: float, b: float) -> float:
    """Linear function."""
    return a * x + b


def exponential_function(x: float, a: float, b: float) -> float:
    """Exponential function."""
    return a * x ** 2 + b


def main() -> None:
    """Main function."""


if __name__ == "__main__":
    main()
