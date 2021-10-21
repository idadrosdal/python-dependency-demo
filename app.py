import requests
# import plotly.express as px
import plotly.graph_objects as go


def get_cat_fact():
    res = requests.get("https://catfact.ninja/fact")
    if res.ok:
        return res.json()["fact"]
    else:
        raise Exception(f"{res.status_code}: {res.reason}")


def plot_cat(color):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', line={"color": color}))
    fig.add_trace(go.Scatter(x=[0, 1], y=[1, 1], mode='lines', line={"color": color}))
    fig.add_trace(go.Scatter(x=[0, 0], y=[0, 1], mode='lines', line={"color": color}))
    fig.add_trace(go.Scatter(x=[1, 1], y=[0, 1], mode='lines', line={"color": color}))

    for ear in [0.2, 0.8]:
        fig.add_trace(go.Scatter(x=[ear - 0.1, ear, ear + 0.1], y=[1, 1.2, 1], mode='lines', line={"color": color}))
    for whisker in [[0.3, 0.45], [0.5, 0.5], [0.7, 0.55]]:
        fig.add_trace(go.Scatter(x=[0.2, 0.4], y=whisker, mode='lines', line={"color": color}))
    for whisker in [[0.45, 0.3], [0.5, 0.5], [0.55, 0.7]]:
        fig.add_trace(go.Scatter(x=[0.6, 0.8], y=whisker, mode='lines', line={"color": color}))

    fig.update_layout(showlegend=False)
    fig.show()


if __name__ == "__main__":
    print(get_cat_fact())
    plot_cat('black')
