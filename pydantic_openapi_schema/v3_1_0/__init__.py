"""OpenAPI v3.1.0 schema types, created according to the specification: https://github.com/OAI/OpenAPI-
Specification/blob/master/versions/3.1.0.md.

The type orders are according to the contents of the specification:
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.1.0.md#table-of-contents
"""

from .callback import Callback
from .components import Components
from .contact import Contact
from .discriminator import Discriminator
from .encoding import Encoding
from .example import Example
from .external_documentation import ExternalDocumentation
from .header import Header
from .info import Info
from .license import License
from .link import Link
from .media_type import MediaType
from .oauth_flow import OAuthFlow
from .oauth_flows import OAuthFlows
from .open_api import OpenAPI
from .operation import Operation
from .parameter import Parameter
from .path_item import PathItem
from .paths import Paths
from .reference import Reference
from .request_body import RequestBody
from .response import Response
from .responses import Responses
from .schema import Schema
from .security_requirement import SecurityRequirement
from .security_scheme import SecurityScheme
from .server import Server
from .server_variable import ServerVariable
from .tag import Tag
from .xml import XML

# resolve forward references
Encoding.update_forward_refs(Header=Header)
Schema.update_forward_refs()

__all__ = [
    "Callback",
    "Components",
    "Contact",
    "Discriminator",
    "Encoding",
    "Example",
    "ExternalDocumentation",
    "Header",
    "Info",
    "License",
    "Link",
    "MediaType",
    "OAuthFlow",
    "OAuthFlows",
    "OpenAPI",
    "Operation",
    "Parameter",
    "PathItem",
    "Paths",
    "Reference",
    "RequestBody",
    "Response",
    "Responses",
    "Schema",
    "SecurityRequirement",
    "SecurityScheme",
    "Server",
    "ServerVariable",
    "Tag",
    "XML",
]
