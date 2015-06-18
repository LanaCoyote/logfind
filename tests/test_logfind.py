import pytest
from logfind import logfind
from re import compile

# test that we can read our .logfind file properly
def test_read_config_file():
    f = open('tests/test_config')

    fnames = logfind.read_config_file( f )

    assert fnames[0] == ('tests/testlogs/a',compile('only_me.log'))
    assert fnames[1] == ('tests/testlogs/b',compile('.+'))
    assert fnames[2] == ('tests/testlogs/c',compile('.+\.log'))
    assert fnames[3] == ('tests/testlogs/d',compile('.+'))


def test_read_empty_file():
    pass


def test_read_nonexistant_file():
    fnames = logfind.read_config_file( None )

    assert not fnames


def test_get_filelist():
    f = open('tests/test_config')
    fnames = logfind.read_config_file( f )

    assert logfind.get_matching_files( fnames[0] ) == ['only_me.log']
    assert logfind.get_matching_files( fnames[1] ) == ['in_here.txt','all_logs.log','will_be_searched.log']
    assert logfind.get_matching_files( fnames[2] ) == ['only_logs.log']
    assert logfind.get_matching_files( fnames[3] ) == ['everything.log','will_be_searched.txt']


# test that we can interpret arguments properly
def test_process_args():
    test_cases = [
        ('search for me', ['search','for','me']),
    ]

    for inp, out in test_cases :
        args = logfind.parse_arguments( inp.split(' ') )
        assert args.search == out


def test_process_orflag():
    args = logfind.parse_arguments( ['-o','search','for','me'] )
    assert args.o

    args = logfind.parse_arguments( ['search','for','me'] )
    assert not args.o


# test that we can find files containing given args
def test_find_files():
    pass


def test_find_files_or():
    pass


def test_find_files_regex():
    pass


def test_find_files_regex_or():
    pass
