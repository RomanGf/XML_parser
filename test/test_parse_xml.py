import pytest

from ..main import parse_xml, read_file


@pytest.fixture
def set_up():
    
    return {
        'expected_result':
        {
            'root':{
                'response':{
                    'profile': ['user1', 'user2'],
                    'data': {
                        'username': ['Jack', 'Mary']
                    }
                },
                'status': 'ok'
            }
        }
    }


@pytest.fixture
def set_up_for_parse_from_str():
    xml_data = '''
    <root>
        <response>
            <profile>user1</profile>
            <profile>user2</profile>
            <data>UA</data>
        </response>
        <status>ok</status>
    </root>
    '''

    expected = {
    'root': {
        'response': {'profile': ['user1', 'user2'], 'data': 'UA'},
        'status': 'ok'
        }
    }

    return {
        'data_to_test': xml_data,
        'expected_result': expected
    }

@pytest.fixture
def set_up_for_parse_from_str_with_empty_tag():

    xml_data = '''
    <root>
        <response>
            <profile>user1</profile>
            <profile>user2</profile>
            <data>
                <username></username>
                <username>Mary</username>
            </data>
        </response>
        <status>ok</status>
    </root>
    '''

    expected = {
        'root':{
            'response':{
                'profile': ['user1', 'user2'],
                'data': {
                    'username': 'Mary'
                }
            },
            'status': 'ok'
        }
    }

    return {
        'data_to_test': xml_data,
        'expected_result': expected
    }

def test_return_correct_dict_when_correct_xml_from_file_was_provided(set_up):
    
    assert set_up['expected_result'] == parse_xml(read_file('file.xml'))

def test_return_correct_dict_when_correct_xml_was_provided(set_up_for_parse_from_str):
    
    expected_result = set_up_for_parse_from_str['expected_result']
    actual_result = parse_xml(set_up_for_parse_from_str['data_to_test'])

    assert expected_result == actual_result

def test_return_correct_dict_when_xml_with_empty_tag_was_provided(set_up_for_parse_from_str_with_empty_tag):
    
    expected_result = set_up_for_parse_from_str_with_empty_tag['expected_result']
    actual_result = parse_xml(set_up_for_parse_from_str_with_empty_tag['data_to_test'])

    assert expected_result == actual_result
