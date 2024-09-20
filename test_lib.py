from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_max,
    grab_std,
    # generate_descriptive_statistics,
    # create_histogram
)

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"


def test_load_dataset():
    general_df = load_dataset(dataset)
    assert general_df is not None
    assert general_df.shape == (435, 10)


def test_stats():
    """test that checks the data operations is working"""
    general_df = load_dataset(dataset)
    max_test = grab_max(general_df, "rural")
    mean_test = grab_mean(general_df, "rural")
    median_test = grab_median(general_df, "rural")
    std_test = grab_std(general_df, "rural")
    # test
    describe_test = general_df.describe()
    assert describe_test.loc["max", "rural"] == max_test
    assert describe_test.loc["mean", "rural"] == mean_test
    assert describe_test.loc["std", "rural"] == std_test
    assert round(median_test) == 18


if __name__ == "__main__":
    test_load_dataset()
    test_stats()
