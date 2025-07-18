# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T11:27:30+00:00



import argparse
import json
import os
from typing import *
from typing import Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, HTTPBearer

from models import ErrorResponse, RedirectResponse, RenderRequest, RenderResponse

app = MCPProxy(
    description='A plugin that allows the user to capture screenshots of a web page from a URL or HTML using ChatGPT.',
    title='Urlbox API',
    version='v1',
    servers=[{'url': 'https://api.urlbox.io'}],
)


@app.post(
    '/v1/render/sync',
    tags=['media_rendering'],
    security=[
        HTTPBearer(name="None"),
    ],
)
def render_sync(body: RenderRequest):
    """
    Render a URL as an image or video
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
