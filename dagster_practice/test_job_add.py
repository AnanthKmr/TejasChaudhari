

from dagster import *
import pytest
import mock

from job_add import *
 



# 
def test_op_with_invocation():
    assert my_op_to_test() == 5


# 
def test_inputs_op_with_invocation():
    assert my_op_with_inputs(5, 6) == 11


# 
def test_op_with_config():
    assert op_requires_config(MyOpConfig(my_int=5)) == 10


# 
def test_op_with_resource():
    assert op_requires_foo(FooResource(my_string="bar")) == "found bar"


# 
def test_my_op():
    class FakeClient:
        def query(self, body: str):
            assert body == "SELECT * FROM my_table"
            return "my_result"

    mocked_client_resource = mock.Mock()
    mocked_client_resource.get_client.return_value = FakeClient()

    assert my_op(mocked_client_resource) == "my_result"


# 
def test_op_with_context():
    context = build_op_context()
    context_op(context)


# 
def test_basic_asset():
    assert basic_asset() == 5


# 
def test_asset_with_inputs():
    assert asset_with_inputs(5, 6) == 11



# 
def test_asset_requires_config():
    result = asset_requires_config(config=MyAssetConfig(my_string="foo"))



# 
def test_asset_requires_bar():
    result = asset_requires_bar(bar=BarResource(my_string="bar"))

# def test_data_assets():
#     result = materialize_to_memory([data_source, structured_data])
#     assert result.success
#     # Materialized objects can be accessed in terms of the underlying op
#     materialized_data = result.output_for_node("structured_data")





# 
def test_assets_require_service():
    # Mock objects can be provided directly.
    result = materialize_to_memory(
        [asset_requires_service, other_asset_requires_service],
        resources={"service": mock.MagicMock()},
    )
    assert result.success


# 
# from dagster import RunConfig


# def test_job_with_config():
#     result = do_math_job.execute_in_process(
#         run_config=RunConfig(
#             ops={
#                 "add_one": AddOneConfig(num=2),
#                 "add_two": AddTwoConfig(num=3),
#             }
#         )
#     )

#     assert result.success

#     assert result.output_for_node("add_one") == 3
#     assert result.output_for_node("add_two") == 5
#     assert result.output_for_node("subtract") == -2


# 
def test_local():
    # Since we have access to the computation graph independent of the set of resources, we can
    # test it locally.
    result = download.execute_in_process(
        resources={"api": ResourceDefinition.mock_resource()}
    )
    assert result.success

