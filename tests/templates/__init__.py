import dash
import dash_html_components as html


# Check outer div
def check_layout_body(layout_body, template):
    assert isinstance(layout_body, html.Div)
    assert layout_body.id == "all-div"
    assert len(layout_body.children) == 3

    # Check input div
    expected_input_components = [
        ac.container_component for ac in template.locations["input"].values()
    ]
    assert layout_body.children[0].id == "inputs-div"
    assert layout_body.children[0].children == expected_input_components

    # Check output div
    expected_output_components = [
        ac.container_component for ac in template.locations["output"].values()
    ]
    assert layout_body.children[1].id == "outputs-div"
    assert layout_body.children[1].children == expected_output_components

    # Check custom div
    expected_custom_components = [
        ac.container_component for ac in template.locations["custom"].values()
    ]
    assert layout_body.children[2].id == "customs-div"
    assert layout_body.children[2].children == expected_custom_components


def check_layout(template):
    layout = template.children
    check_layout_body(layout, template)
