import pytest

from main import parse_xml, read_file


@pytest.fixture
def set_up():
    return {
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


@pytest.fixture
def set_up_for_parse_from_str():
    xml_data = "<root><response><user>user1</user><user>user2</user><data>UA</data></response><status>ok</status></root>"
    expected = {
    'root': {
        'response': {'user': ['user1', 'user2'], 'data': 'UA'},
        'status': 'ok'
        }
    }
    return xml_data, expected

@pytest.fixture
def set_up_for_parse_from_str_empty_tag():
    xml_data = "<root><response><profile>user1</profile><profile>user2</profile><data><username></username><username>Mary</username></data></response><status>ok</status></root>"
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
    return xml_data, expected

def test_parse_xml_from_file(set_up):
    
    assert set_up == parse_xml(read_file('file.xml'))


def test_parse_xml_from_str(set_up_for_parse_from_str):
    
    assert set_up_for_parse_from_str[1] == parse_xml(
        set_up_for_parse_from_str[0]
    )

def test_parse_xml_from_str_empty_tag(set_up_for_parse_from_str_empty_tag):
    
    assert set_up_for_parse_from_str_empty_tag[1] == parse_xml(
        set_up_for_parse_from_str_empty_tag[0]
    )