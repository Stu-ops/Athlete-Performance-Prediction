<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Athlete Performance Prediction</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      line-height: 1.6;
      margin: 2rem auto;
      max-width: 800px;
      padding: 0 1rem;
      color: #333;
    }
    h1, h2, h3 {
      font-weight: 600;
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 0.5rem;
    }
    h2 {
      font-size: 2rem;
      margin-top: 2rem;
      margin-bottom: 0.5rem;
    }
    h3 {
      font-size: 1.5rem;
      margin-top: 1.5rem;
      margin-bottom: 0.5rem;
    }
    p {
      margin-bottom: 1rem;
    }
    code, pre {
      background: #f6f8fa;
      border-radius: 3px;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
      font-size: 0.9em;
    }
    pre {
      padding: 1rem;
      overflow-x: auto;
    }
    ul, ol {
      margin-left: 1.5rem;
      margin-bottom: 1rem;
    }
    .badge {
      display: inline-block;
      padding: .25em .6em;
      font-size: 75%;
      font-weight: 700;
      line-height: 1;
      color: #fff;
      background-color: #0366d6;
      border-radius: .25rem;
      vertical-align: middle;
      margin-right: .3em;
    }
  </style>
</head>
<body>

  <h1>🏅 Athlete Performance Prediction</h1>
  <p>Predict athletic performance using biometric and training metrics with the power of machine learning.</p>

  <h2>📌 Project Overview</h2>
  <p>This project utilizes a dataset of athlete metrics (e.g., heart rate, stamina, training hours) to predict performance levels. It offers a streamlined pipeline—from data processing to model prediction—and a user-friendly web interface powered by Streamlit.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li><span class="badge">📊</span> <strong>Exploratory Data Analysis (EDA)</strong></li>
    <li><span class="badge">🧠</span> <strong>Model Training</strong> using scikit-learn</li>
    <li><span class="badge">💾</span> <strong>Pipeline Serialization</strong> (<code>pipe.pkl</code>)</li>
    <li><span class="badge">🌐</span> <strong>Streamlit UI</strong> (<code>app.py</code>) for real‑time predictions</li>
    <li><span class="badge">📈</span> <strong>Visualizations and insights</strong> included in Jupyter Notebooks</li>
  </ul>

  <h2>🗂️ Project Structure</h2>
  <pre><code>Athlete-Performance-Prediction/
├── <code>app.py</code>                      # Streamlit application
├── <code>pipe.pkl</code>                    # Serialized machine learning pipeline
├── <code>train.csv</code>                   # Training dataset
├── <code>requirements.txt</code>            # Project dependencies
├── <code>Athlete-Performance-Prediction.ipynb</code> # Main notebook for data exploration & model training
├── <code>Athlete_performance_prediction.ipynb</code> # Alternate/preliminary notebook
└── <code>README.md</code>                   # Project documentation
</code></pre>

  <h2>🧪 Tech Stack</h2>
  <ul>
    <li>Python</li>
    <li>Pandas, NumPy</li>
    <li>scikit-learn</li>
    <li>Streamlit</li>
    <li>Jupyter Notebook</li>
    <li>Matplotlib / Seaborn</li>
  </ul>

  <h2>📦 Setup Instructions</h2>
  <ol>
    <li><strong>Clone the repository</strong>
      <pre><code>git clone https://github.com/Stu-ops/Athlete-Performance-Prediction.git
cd Athlete-Performance-Prediction
</code></pre>
    </li>
    <li><strong>Create a virtual environment</strong> (optional but recommended)
      <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
</code></pre>
    </li>
    <li><strong>Install dependencies</strong>
      <pre><code>pip install -r requirements.txt
</code></pre>
    </li>
    <li><strong>Run the Streamlit app</strong>
      <pre><code>streamlit run app.py
</code></pre>
    </li>
  </ol>

  <h2>🔍 Model Details</h2>
  <ul>
    <li><strong>Features Used:</strong> heart_rate, stamina, training_hours, and other biometric stats.</li>
    <li><strong>Target:</strong> Athlete performance label (categorical or numeric rating).</li>
    <li><strong>Model:</strong> Regression or classification model trained using scikit-learn.</li>
    <li><strong>Pipeline:</strong> Serialized using joblib and saved as <code>pipe.pkl</code> for reuse in the Streamlit app.</li>
  </ul>

  <h2>📈 Example Use Case</h2>
  <p>A sports analyst inputs athlete metrics into the UI and receives an instant prediction of their performance potential. This tool can assist in:</p>
  <ul>
    <li>Training optimization</li>
    <li>Talent scouting</li>
    <li>Injury prevention analytics</li>
  </ul>

  <hr/>
  <p style="font-size:0.9em; color:#666;">Generated on May 6, 2025</p>
</body>
</html>
