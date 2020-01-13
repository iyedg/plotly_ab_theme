import plotly.io as pio
import plotly.graph_objects as go

W = 1200
H = W / (16 / 9)
layout = {
    "layout": {
        "annotationdefaults": {
            "arrowcolor": "#2a3f5f",
            "arrowhead": 0,
            "arrowwidth": 1,
        },
        "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}},
        "font": {"family": "Tajawal"},
        "hoverlabel": {"align": "left"},
        "hovermode": "closest",
        "paper_bgcolor": "white",
        "shapedefaults": {"line": {"color": "#2a3f5f"}},
        "title": {"x": 1, "font": dict(size=26), "xref": "paper"},
        "xaxis": {"automargin": True, "ticks": "" },
        "yaxis": {
            "automargin": True,
            "ticks": "",
            "title": {"standoff": 15},
            "side": "right",
            "showline": False,
        },
        "width": W,
        "height": H,
        "legend": {"orientation": "h"},
    }
}
pio.templates["ab_theme_ar"] = go.layout.Template(layout)

layout["layout"]["font"]["family"] = "Roboto Condensed"
layout["layout"]["yaxis"]["side"] = "left"
pio.templates["ab_theme_fr"] = go.layout.Template(layout)
