from kpi.utils.spectacular_processing import sanitize_example_credentials


def test_sanitize_example_credentials_preserves_contract_definitions():
    source = {
        'example': {
            'access_token': 'value',
            'refresh_token': 'value',
            'nested': [{'session_token': 'value'}],
        },
        'properties': {
            'access_token': {
                'type': 'string',
                'description': 'Token returned after authentication.',
            },
        },
        'unrelated': 'value',
    }

    result = sanitize_example_credentials(source)

    assert result == {
        'example': {
            'access_token': 'example-access-token',
            'refresh_token': 'example-refresh-token',
            'nested': [{'session_token': 'example-session-token'}],
        },
        'properties': {
            'access_token': {
                'type': 'string',
                'description': 'Token returned after authentication.',
            },
        },
        'unrelated': 'value',
    }
    assert source['example']['access_token'] == 'value'
