from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio

from .. import components as comps

class GeneratingResponsePlaceholder(rio.Component):
    """
    This component is displayed while the chatbot is generating a response. It
    provides feedback to the user that the app is working on their question.
    """

    def build(self) -> rio.Component:
        return rio.Row(
            rio.ProgressCircle(size=1.5),
            rio.Text(
                "Thinking...",
                justify="center",
            ),
            spacing=1,
        )

