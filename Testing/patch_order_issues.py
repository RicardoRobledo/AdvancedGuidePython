@patch('mymodule.sys')
@patch('mymodule.os')
@patch('mymodule.os.path')
def test_something(self,
                   mock_os_path,
                   mock_os,
                   mock_sys):
    # The rest of the test method