import dash
import dash_bootstrap_components as dbc
from dash import Dash
from flask import Flask

from static.campaign_layout import campaign


def init_campaign(server) -> Flask:
    dash_app = Dash(
        server=server,
        routes_pathname_prefix="/campaign/",
        external_stylesheets=[
            dbc.themes.FLATLY,
            dbc.icons.FONT_AWESOME,
            "https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap",
        ],
        use_pages=True,
        pages_folder="",
        external_scripts=[
            # "https://cdn.jsdelivr.net/npm/ethers@6.10.0/dist/ethers.umd.min.js",
            "https://cdn.jsdelivr.net/npm/ethers@5.7.2/dist/ethers.umd.min.js",
            "https://unpkg.com/@metamask/onboarding@1.0.1/dist/metamask-onboarding.bundle.js",
        ],
    )

    # Register pages

    dash.register_page("campaign", path="/", layout=campaign)
    # dash.register_page("upload files", path="/upload", layout=upload_files_layout)

    # Initialise callbacks

    return dash_app.server
