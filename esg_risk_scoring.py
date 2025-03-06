import pandas as pd
import plotly.graph_objects as go

# Step 1: Load the provided loan data
data = {
    'loan_id': [1, 2, 3, 4, 5],
    'industry': ['Energy', 'Tech', 'Manufacturing', 'Renewables', 'Oil'],
    'location': ['US', 'EU', 'Asia', 'EU', 'Middle East'],
    'asset_type': ['Mortgage', 'Consumer', 'Commercial', 'Green Mortgage', 'Corporate'],
    'esg_score': [-0.031977, -0.646448, 0.452994, -1.222428, 1.447859],
    'risk_label': ['High Risk', 'Low Risk', 'High Risk', 'Low Risk', 'Medium Risk']
}
df = pd.DataFrame(data)

# Step 2: Add loan amounts for portfolio weighting
df['loan_amount'] = [500000, 300000, 700000, 400000, 600000]

# Step 3: Calculate portfolio-level ESG metrics
portfolio_total = df['loan_amount'].sum()
df['weight'] = df['loan_amount'] / portfolio_total
weighted_esg = (df['esg_score'] * df['weight']).sum()

# Step 4: Create the visualization
fig = go.Figure()

# Add bar chart for ESG scores
fig.add_trace(go.Bar(
    x=df['loan_id'],
    y=df['esg_score'],
    text=df['risk_label'],
    marker_color='#FF6B6B',
    name='ESG Score'
))

# Add table as a Plotly table trace
fig.add_trace(go.Table(
    header=dict(
        values=['Loan ID', 'Industry', 'Location', 'Asset Type', 'ESG Score', 'Risk Label'],
        fill_color='rgb(40, 40, 40)',
        font=dict(color='white', size=12),
        align='center'
    ),
    cells=dict(
        values=[
            df['loan_id'], df['industry'], df['location'], df['asset_type'],
            df['esg_score'].round(3), df['risk_label']
        ],
        fill_color='rgb(50, 50, 50)',
        font=dict(color='white', size=11),
        align='center'
    ),
    domain=dict(x=[0.6, 1.0], y=[0.0, 1.0])  # Position table on the right side
))

# Add weighted ESG score as an annotation
fig.add_annotation(
    x=0.05,
    y=0.95,
    xref="paper",
    yref="paper",
    text=f"Portfolio Weighted ESG Score: {weighted_esg:.2f}",
    showarrow=False,
    font=dict(color='white', size=14),
    bgcolor='rgba(255, 107, 107, 0.8)',  # Slight reddish tint to match #FF6B6B
    bordercolor='white',
    borderwidth=1
)

# Step 5: Apply dark theme and axis styling
fig.update_layout(
    title=dict(text='ESG Risk Scores by Loan', font=dict(color='white', size=14)),
    xaxis=dict(
        title='Loan ID',
        title_font_color='white',
        tickfont=dict(color='white', size=12),
        ticklen=8,
        ticks='outside',
        gridcolor='rgba(255, 255, 255, 0.1)',
        gridwidth=0.5,
        domain=[0.0, 0.55]  # Restrict bar chart to left side
    ),
    yaxis=dict(
        title='ESG Score',
        title_font_color='white',
        tickfont=dict(color='white', size=12),
        ticklen=8,
        ticks='outside',
        gridcolor='rgba(255, 255, 255, 0.1)',
        gridwidth=0.5
    ),
    plot_bgcolor='rgb(40, 40, 40)',
    paper_bgcolor='rgb(40, 40, 40)',
    showlegend=False,
    margin=dict(l=50, r=50, t=50, b=50)
)

# Step 6: Display the plot
fig.show()