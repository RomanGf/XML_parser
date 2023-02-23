import pytest

from main import concatenate_to_one_row

def test_must_return_concatenated_when_xml_with_new_lines_was_provided():
    test_data = '''
    <root>
        <status>ok</status>
    </root>
    '''
    expected_result = '<root><status>ok</status></root>'
    actual_result = concatenate_to_one_row(test_data)

    assert expected_result == actual_result

def test_must_return_same_string_if_xml_was_as_one_row():
    test_data = '<root><status>ok</status></root>'

    expected_result = '<root><status>ok</status></root>'
    actual_result = concatenate_to_one_row(test_data)

    assert expected_result == actual_result