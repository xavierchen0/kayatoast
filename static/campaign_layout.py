import dash_bootstrap_components as dbc
from dash import dcc, html

campaign_description = html.Div(
    [
        html.H2(
            "KayaBoard: The Ultimate Ergonomic Split Keyboard", className="fw-bold mb-2"
        ),
        html.H5(
            "Comfort Meets Productivity — A Revolutionary Keyboard Designed to Fit You",
            className="text-muted mb-4",
        ),
        html.P(
            "As a developer, designer, and daily keyboard warrior, I’ve experienced the wrist pain, finger fatigue, and poor posture caused by conventional keyboards. That’s why I created KayaBoard — a sleek, wireless, low-profile split ergonomic keyboard that adapts to your natural typing position."
        ),
        html.P(
            "KayaBoard is built for comfort, built for focus, and built to last. Whether you’re coding late into the night, editing content, or gaming, KayaBoard gives you full control with zero strain."
        ),
        html.P(
            "This campaign isn’t just about launching a product — it’s about changing the way we interact with technology, starting from the very tool we use most."
        ),
    ]
)
# pledges = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H5("All Pledges", className="fw-bold mb-3"),
#             html.Div(id="pledgesTable"),  # fill with a callback later
#         ]
#     ),
#     className="shadow-sm rounded-4",
# )
# connect = dbc.Card(
#     dbc.CardBody(
#         [
#             html.H5("Connect to MetaMask", className="fw-bold"),
#             html.P("Link your wallet before pledging.", className="mb-3"),
#             dbc.Button("Connect Wallet", id="connectWallet", color="primary"),
#         ]
#     ),
#     className="shadow-sm rounded-4",
# )
# press = dbc.Button("Pledge $100", id="test", color="success")
campaign_pledge_section = dbc.Container(
    dbc.Row(
        [
            # Left column: Progress + Connect Wallet
            dbc.Col(
                [
                    # Progress Card
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Campaign Progress", className="fw-bold"),
                                html.H6("Total Raised:", className="mt-3"),
                                html.P(
                                    "$12,340",
                                    id="totalRaised",
                                    className="fs-4 text-success",
                                ),
                                html.H6("Funding Goal", className="mt-3"),
                                html.P(
                                    "$10,000",
                                    id="userPledge",
                                    className="fs-4 text-info",
                                ),
                            ]
                        ),
                        className="shadow-sm rounded-4 mb-4",
                    ),
                    # Connect Wallet Card (below)
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Support KayaBoard", className="fw-bold"),
                                html.P(
                                    "Connect your MetaMask wallet to pledge.",
                                    className="mb-3",
                                ),
                                dbc.Button(
                                    "Connect Wallet",
                                    id="connectWallet",
                                    color="primary",
                                ),
                            ]
                        ),
                        className="shadow-sm rounded-4",
                    ),
                ],
                width=6,
            ),
            # Right column: Pledge form (initially hidden)
            dbc.Col(
                html.Div(
                    id="pledgeCard",
                    # style={"display": "none"},
                    children=dbc.Card(
                        dbc.CardBody(
                            [
                                html.Span(id="walletAddress"),
                                html.H5("Select Your Keyboard Design"),
                                dcc.Dropdown(
                                    id="designdropdown",
                                    options=[
                                        {"label": "Design 1", "value": "Design 1"},
                                        {"label": "Design 2", "value": "Design 2"},
                                    ],
                                    placeholder="Choose a Design...",
                                    className="mb-3",
                                ),
                                dbc.Button(
                                    "Pledge $100", id="pledgebutton", color="success"
                                ),
                            ]
                        ),
                        className="shadow-sm rounded-4",
                    ),
                ),
                width=6,
            ),
        ],
        className="mt-4",
    )
)
acknowledgements = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                html.Img(
                    src="assets/xrplogo.svg",
                    height="40px",
                ),
                width="auto",
            ),
            dbc.Col(
                html.P(
                    "Brought to you by KayaToast",
                    className="text-end fw-light",
                ),
                className="d-flex align-items-center justify-content-end",
            ),
        ],
        className="my-4",
        align="center",
        justify="between",
    )
)
campaign = dbc.Container(
    [
        # Top of page: Logo + profile pic
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.I(className="fa-solid fa-rocket fa-2x me-3"),
                            html.Span("KayaToast", className="fs-4 fw-bold"),
                        ]
                    ),
                    width="auto",
                ),
                dbc.Col(
                    html.Img(
                        src="assets/profile.jpg",
                        height="40px",
                        width="50px",
                        className="rounded-circle",
                    ),
                    width="auto",
                    className="ms-auto",
                ),
            ],
            align="center",
            justify="between",
            className="pt-2",
        ),
        # Line
        dbc.Row(dbc.Col(html.Hr(), width=12)),
        # Campaign Title
        dbc.Row(
            dbc.Col(
                html.H4(
                    "Kayabord: Ergonomic Split Keyboard",
                    className="fw-bold text-center mt-2 mb-3",
                )
            )
        ),
        # Campaign tags
        dbc.Row(
            dbc.Col(
                [
                    dbc.Badge(
                        "Ergonomic", color="primary", pill=True, className="me-2"
                    ),
                    dbc.Badge("Wireless", color="success", pill=True, className="me-2"),
                    dbc.Badge("Mechanical", color="warning", pill=True),
                ],
                className="text-center",
            )
        ),
        # Carousel
        # Images taken from https://ergokeyboard.sg/products/corne-choc-v4
        dbc.Row(
            dbc.Col(
                dbc.Carousel(
                    items=[
                        {
                            "key": "1",
                            "src": "assets/keyboard_1.webp",
                            "caption": "Split Keyboard Design 1",
                            "img_style": {
                                "width": "100%",
                                "height": "500px",
                                "objectFit": "contain",
                            },
                        },
                        {
                            "key": "2",
                            "src": "assets/keyboard_2.webp",
                            "caption": "Split Keyboard Design 1",
                            "img_style": {
                                "width": "100%",
                                "height": "500px",
                                "objectFit": "contain",
                            },
                        },
                        {
                            "key": "3",
                            "src": "assets/keyboard_3.webp",
                            "caption": "Split Keyboard Design 2",
                            "img_style": {
                                "width": "100%",
                                "height": "500px",
                                "objectFit": "contain",
                            },
                        },
                        {
                            "key": "4",
                            "src": "assets/keyboard_4.webp",
                            "caption": "Split Keyboard Design 2",
                            "img_style": {
                                "width": "100%",
                                "height": "500px",
                                "objectFit": "contain",
                            },
                        },
                    ],
                    controls=True,
                    indicators=True,
                    className="mt-4",
                ),
                width=6,
                className="px-4 mb-4",
            ),
            justify="center",
        ),
        # Campaign Description
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(campaign_description),
                    color="light",
                    className="mt-4 shadow-sm rounded-4",
                )
            )
        ),
        # MetaMask Integration and Pledge
        campaign_pledge_section,
        # pledges,
        # connect,
        # press,
        # Acknowledgements
        acknowledgements,
    ],
    fluid=False,
)
