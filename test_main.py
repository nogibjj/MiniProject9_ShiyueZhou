"""
Test goes here

"""

from main import g_describe, save_to_md

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/district-urbanization-index-2022/urbanization-index-2022.csv"


def test_g_describe():
    describe_test = g_describe(dataset)
    assert describe_test.shape == (8, 7)


def test_summary_and_viz_to_markdown():
    save_to_md()


if __name__ == "__main__":
    test_g_describe()
    test_summary_and_viz_to_markdown()
