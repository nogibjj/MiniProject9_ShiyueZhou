"""
Main cli or app entry point
"""

from mylib.lib import (
    load_dataset,
    # grab_mean,
    # grab_median,
    # grab_max,
    # grab_std,
    # generate_descriptive_statistics,
    create_histogram,
)

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"


def g_describe(csv):
    g = load_dataset(csv)
    return g.describe()


def save_to_md():
    df = load_dataset(dataset)
    describe_df = g_describe(dataset)
    markdown_table1 = describe_df.to_markdown()
    create_histogram(df, "rural")  ## create plot_from_data.png

    # Write the markdown table to a file
    with open("DescribeStat.md", "a") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")
        file.write("![congress_viz](plot_from_data.png)\n")


def main():
    save_to_md()
    # describe_df = g_describe(dataset)
    # print(generate_descriptive_statistics(describe_df))
    # print(grab_median(describe_df, "rural"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
