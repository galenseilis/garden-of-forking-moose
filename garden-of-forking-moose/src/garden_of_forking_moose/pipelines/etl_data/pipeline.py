"""
This is a boilerplate pipeline 'etl_data'
generated using Kedro 0.18.13
"""
from kedro.pipeline import Pipeline, node, pipeline

from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=nodes.get_inat_data,
            inputs=None,
            outputs='inat_response',
            name='get_data_from_inat_api'
            ),
        node(
            func=lambda data: print(data),
            inputs='inat_response',
            outputs=None,
            name='print_response'
            )
        ])
