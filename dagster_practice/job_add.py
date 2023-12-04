
from dagster import *



# 
@op
def my_op_to_test():
    return 5


# 
@op
def my_op_with_inputs(x, y):
    return x + y



# 
from dagster import Config


class MyOpConfig(Config):
    my_int: int


@op
def op_requires_config(config: MyOpConfig):
    return config.my_int * 2




# 
from dagster import ConfigurableResource


class FooResource(ConfigurableResource):
    my_string: str


@op
def op_requires_foo(foo: FooResource):
    return f"found {foo.my_string}"


# 
from dagster import ConfigurableResource, op
import mock

class MyClient:
    ...

    def query(self, body: str):
        ...

class MyClientResource(ConfigurableResource):
    username: str
    password: str

    def get_client(self):
        return MyClient(self.username, self.password)

@op
def my_op(client: MyClientResource):
    return client.get_client().query("SELECT * FROM my_table")




# 
@op
def context_op(context: OpExecutionContext):
    context.log.info(f"My run ID is {context.run_id}")


# 
from dagster import asset


@asset
def basic_asset():
    return 5

# 
from dagster import asset


@asset
def asset_with_inputs(x, y):
    return x + y

# 
from dagster import asset, Config


class MyAssetConfig(Config):
    my_string: str


@asset
def asset_requires_config(config: MyAssetConfig) -> str:
    return config.my_string

# 
from dagster import asset, ConfigurableResource


class BarResource(ConfigurableResource):
    my_string: str


@asset
def asset_requires_bar(bar: BarResource) -> str:
    return bar.my_string

# 
# from dagster import asset, materialize_to_memory


# @asset
# def data_source():
#     return get_data_from_source()


# @asset
# def structured_data(data_source):
#     return extract_structured_data(data_source)
  


# 
from dagster import asset, materialize_to_memory, ConfigurableResource
import mock


class MyServiceResource(ConfigurableResource):
    ...


@asset
def asset_requires_service(service: MyServiceResource):
    ...


@asset
def other_asset_requires_service(service: MyServiceResource):
    ...



# 
from dagster import *


class MyApi(ConfigurableResource):
    def call(self):
        ...


@op
def get_data(api: MyApi):
    return api.call()


@op
def do_something(context: OpExecutionContext, data):
    output = data
    return output


@graph
def download():
    do_something(get_data())


# The prod job for the download graph.
download_job = download.to_job(resource_defs={"api": MyApi()})