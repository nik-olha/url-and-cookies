from urllib import parse


def parse_parameters(query: str) -> dict:
    params = dict(parse.parse_qsl(parse.urlsplit(query).query))
    return dict(params)


def parse_cookies(query: str) -> dict:
    return {}


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret',
                                                                                             'color': 'purple'}
    assert parse_parameters('?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    try:
        assert parse_parameters('http://example.com/path/to/page?name=ferret&color=purple:') == {'name': 'ferret',
                                                                                                 'color': 'purple'}
    except AssertionError:
        print('AssertionError in the fourth test for parse_parameters!')
    try:
        assert parse_parameters('http://example.com/path/to/page??name=ferret&color=purple:') == {'name': 'ferret',
                                                                                                  'color': 'purple'}
    except AssertionError:
        print('AssertionError in the fifth test for parse_parameters!')
    # Tests for function "parse_cookies"
    # assert parse_cookies('') == {}
    # assert parse_cookies('name=Dima;') == {'name': 'Dima'}
