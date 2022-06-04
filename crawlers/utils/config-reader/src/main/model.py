from attrs import define
from typing import Any, Callable, NewType

Url = NewType('Url', str)
PaginationFunction = Callable[[Url, int], Url]

@define(frozen=True)
class Endpoint:
    name: str
    description: str
    url: Url
    pagination_function: PaginationFunction
    expected_status: list[int]
    expected_content_type: list[str]
    filters: list[str]

    @classmethod
    def decode_from(cls, parsed_json: dict[str, Any]):
        endpoint = cls(
            name = parsed_json['name'],
            description = parsed_json['description'],
            url = Url(parsed_json['url']),
            pagination_function = cls.decode_pagination_function_from(parsed_json['pagination']),
            expected_status = parsed_json['expected_status'],
            expected_content_type = parsed_json['expected_content_type'],
            filters = parsed_json['filters']
        )
        return endpoint

    @staticmethod
    def decode_pagination_function_from(parsed_json: Any) -> PaginationFunction:
        if type(parsed_json) == str:
            if parsed_json == 'default':
                pagination_function = lambda url, page: "{}?page={}".format(url, page)
                return pagination_function
        raise ValueError("Could not construct a pagination function from {}".format(parsed_json))

@define(frozen=True)
class Config:
    endpoints: list[Endpoint]

    @classmethod
    def decode_from(cls, parsed_json: dict[str, Any]):
        config = cls(
            endpoints = [ Endpoint.decode_from(e) for e in parsed_json['endpoints'] ]
        )
        return config
