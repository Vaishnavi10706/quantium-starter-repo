from app import app


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#header", "Pink Morsel Sales Visualizer")
    assert dash_duo.find_element("#header")


def test_graph_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart")
    assert dash_duo.find_element("#sales-chart")


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-selector")
    assert dash_duo.find_element("#region-selector")