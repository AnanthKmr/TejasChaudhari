import pytest


# Fixture to print information before and after each test case
@pytest.fixture(autouse=True)
def print_test_case_info(request):
    print(f"\nRunning test: {request.node.nodeid}")
    yield
    print(f"\nFinished test: {request.node.nodeid}")


# Pytest hook for test setup
def pytest_runtest_setup(item):
    print(f"\nSetting up test: {item.nodeid}")


# Pytest hook for test teardown
def pytest_runtest_teardown(item):
    print(f"\nTearing down test: {item.nodeid}")


# Pytest hook for handling test outcomes
# def pytest_exception_interact(node, call, report):
#     if report.failed:
#         print(f"\nTest {node.nodeid} encountered an exception: {report.longreprtext}")





