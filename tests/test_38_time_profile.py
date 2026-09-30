# test_38_time_profile.py


import allure


@allure.title("time_profile.time_range")
class TestTimeRange:
    def test_check_header(self, time_profile_page):
        result = time_profile_page.get_page_header_text()
        expected_val = "Time Profile"

        assert expected_val == result

    def test_check_time_range_tier2_header(self, time_profile_page):
        result = time_profile_page.get_time_range_tier2_header_text()
        expected_val = "Time Range"

        assert expected_val == result

    def test_check_range_name_title_and_value(self, time_profile_page):
        title, value = time_profile_page.get_range_name_title_and_value()
        expected_title = "Range Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_date_title_and_value(self, time_profile_page):
        title, value1, value2 = time_profile_page.get_date_title_and_value()
        expected_title = "Date"
        expected_val1 = "2009-01-01"
        expected_val2 = "2009-01-01"

        assert expected_title == title
        assert expected_val1 == value1
        assert expected_val2 == value2

    def test_check_hours_title_and_value(self, time_profile_page):
        title, value1, value2 = time_profile_page.get_hours_title_and_value()
        expected_title = "Hours(HH MM)"
        expected_val1 = "00:00:00"
        expected_val2 = "00:00:00"

        assert expected_title == title
        assert expected_val1 == value1
        assert expected_val2 == value2

    def test_check_weekdays_title_and_value(self, time_profile_page):
        title, value, value2 = time_profile_page.get_weekdays_title_and_value()
        expected_title = "Weekdays"
        expected_val = "Mon Tue Wed Thu Fri Sat Sun"
        expected_val2 = "Select All Days"

        assert expected_title == title
        assert expected_val == value
        assert expected_val2 == value2

    def test_button_text(self, time_profile_page):
        result = time_profile_page.get_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("time_profile.time_range_information")
class TestTimeRangeInformation:
    def test_check_time_range_information_header(self, time_profile_page):
        result = time_profile_page.get_time_range_information_header_text()
        expected_val = "Time Range Information"

        assert expected_val == result

    def test_total_entries_title(self, time_profile_page):
        result = time_profile_page.get_total_entries_title()
        expected_val = "Total Entries : 0"

        assert expected_val == result

    def test_table_title(self, time_profile_page):
        result = time_profile_page.get_table_title()
        expected_val = ["Range Name", "Weekdays", "From Day", "To Day", "Start Time", "End Time"]

        assert expected_val == result

    def test_table_default_is_empty(self, time_profile_page):
        result = time_profile_page.get_table_default_is_empty()

        assert result
