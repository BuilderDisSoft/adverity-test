# swapi.tests.test_compare_field.py
from swapi.util.compare_field import CompareField


class TestCompareField:
    def test_process_selected_columns(self):
        # Test empty selected_columns
        compare_field = CompareField([], "")
        assert compare_field.process_selected_columns() == []

        # Test non-empty selected_columns
        compare_field = CompareField([], "col1,col2")
        assert compare_field.process_selected_columns() == ["col1", "col2"]

    def test_filter_data(self):
        # Test empty data and selected_columns
        compare_field = CompareField([], "")
        assert compare_field.filter_data() == []

        # Test empty data and non-empty selected_columns
        compare_field = CompareField([], "col1,col2")
        assert compare_field.filter_data() == []

        # Test non-empty data and empty selected_columns
        data = [{"col1": "a", "col2": 1}, {"col1": "b", "col2": 2}]
        compare_field = CompareField(data, "")
        assert compare_field.filter_data() == []

        # Test non-empty data and non-empty selected_columns
        compare_field = CompareField(data, "col1")
        assert compare_field.filter_data() == [{"col1": "a"}, {"col1": "b"}]

    def test_count_occurrences(self):
        # Test empty filtered_data
        compare_field = CompareField([], "")
        assert compare_field.count_occurrences([]) == {}

        # Test non-empty filtered_data
        filtered_data = [{"col1": "a", "count": 1}, {"col1": "b", "count": 1}]
        compare_field = CompareField([], "col1")
        assert compare_field.count_occurrences(filtered_data) == {("a",): 1, ("b",): 1}

    def test_create_table_data(self):
        # Test empty value_counts
        compare_field = CompareField([], "")
        assert compare_field.create_table_data({}) == []

        # Test non-empty value_counts
        value_counts = {("a",): 1, ("b",): 2}
        compare_field = CompareField([], "col1")
        assert compare_field.create_table_data(value_counts) == [
            {"col1": "b", "count": 2},
            {"col1": "a", "count": 1},
        ]

    def test_compare(self):
        # Test empty data and selected_columns
        compare_field = CompareField([], "")
        assert compare_field.compare() == []

        # Test non-empty data and empty selected_columns
        data = [{"col1": "a", "col2": 1}, {"col1": "b", "col2": 2}]
        compare_field = CompareField(data, "")
        assert compare_field.compare() == []

        # Test non-empty data and non-empty selected_columns
        compare_field = CompareField(data, "col1")
        assert compare_field.compare() == [
            {"col1": "a", "count": 1},
            {"col1": "b", "count": 1},
        ]
