# customer-satisfaction-project

<h1>Introduction</h1>
<p>This work addresses a real-world scenario where predicting the satisfaction score of a customer before an order or purchase is made based on their previous behaviour. It uses features such as price, payment value, freight value and many others to make prediction. The relevance of this project is to help businesses not only maintain a competitive advantage but to enhance product service and quality. The work showcases the power of <a href="https://zenml.io/">Zenml</a> to build and deploy production-ready machine learning pipelines easily. Again, MLflow is used for deployment and tracking on a local machine.</p> 
<h2>Problem Statement</h2>
<p>For a given customer's historical data, predict the review score for the next order or purchase.</p>
<h2>Dataset</h2>
The <a href="https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce">[Brazilian E-Commerce Public Dataset by Olist]</a> from kaggle will be used. This dataset has information on 100,000 orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features includes order status, price, payment, freight performance to customer location, product attributes and finally, reviews written by customers.
<h2>Objective</h2>
The objective is to predict the customer satisfaction score for the next order given order based on features like order status, price.
<h2>Requirements</h2>
<p>To view stacks, stack components and pipeline DAGs in a dashboard interface, start the ZenML server and dashboard locally. A react-based dashboard should be seen</p>
<ul>
  <li>Linux or WSL is strongly recommended, Windows can be used </li>
  <li>Python code</li>
  <div class="compact-code-container">
  <pre>
    <code>
      pip install zenml["server"]
      zenml init
      zenml up
    </code>
  </pre>
</div>
<li>To run the run_deployment.py install:</li>
<div class="code-container">
  <pre>
    <code>
      zenml integration install mlflow -y
    </code>
  </pre>
</div>
<li>To execute the project create ZenML stack that has an MLflow experiment tracker and model deployer as a component. Then configure the new stack as follows: </li>
  <div class="code-container">
  <pre>
    <code>
      zenml integration install mlflow -y
      zenml experiment-tracker register mlflow_tracker --flavor=mlflow
      zenml model-deployer register mlflow --flavor=mlflow
      zenml stack register mlflow_stack -a default -o default -d mlflow -e mlflow_tracker --set
    </code>
  </pre>
</div>
</ul>
<h2>Solution</h2>
<p>To create a real-world workflow for forecasting the customer satisfaction score, there is a focus on developing an end-to-end pipeline for continuously forecasting and deploying the machine learning model, as well as a data application that uses the most recently deployed model for the business to consume.
<p>This pipeline can be deployed to the cloud, scaled up to meet demands, and ensure that efficient tracking of the parameters and data that go through each pipeline runs. It contains raw data input, features, results, the machine learning model and model parameters, and prediction outputs. 
</p>
<p>ZenML's MLflow integration is used. MLflow is used for monitoring to keep track of metrics and parameters, and MLflow deployment to deploy our model. Streamlit is used to demonstrate how this approach can be used in a real setting.
</p>
<h2>Training pipeline</h2>
<p>Steps include:</p>
<ul>
<li>ingest_data: ingest the data and create a DataFrame.</li>
<li>clean_data: clean the data, remove the unwanted columns, divides data into train and test.</li>
<li>train_model: train the model and save the model using MLflow autologging.</li>
<li>evaluation: evaluates the model and save the metrics into artifact store.</li>
</ul>
<h2>Deployment Pipeline</h2>
<p>The deployment_pipeline.py pipeline extends the training pipeline and creates a continuous deployment workflow. It takes in and processes input data, trains a model, and then re-deploys the prediction server that serves the model if it meets a paticular criteria.  The pipeline's first four steps are the same as above, including:
</p>
<ul>
  <li>deployment_trigger: To check whether the newly trained model meets the criteria set for deployment.</li>
<li>model_deployer: Deploys the model as a service using MLflow (if deployment criteria is met).</li>
</ul>
<p>The MLflow deployment server runs locally as a daemon process that continue to run in the background after the example execution is complete. When a new pipeline runs and creates a model that satisfies the accuracy threshold validation, the pipeline automatically modifies the already running MLflow deployment server to serve the new model rather than the old one.
</p>
<h1>Images</h1>
<img src="https://github.com/Aaron-k12/customer-satisfaction-project/assets/107159092/0fd18590-487d-4173-b304-cac7456ff03e">
<p> Zenml dashboard showing DAG visualizer</p>
<br><br>
<img src="https://github.com/Aaron-k12/customer-satisfaction-project/assets/107159092/ae0b8cd9-cf41-4b93-8ac8-e62491a121a4">

<caption>MLFlowUI dashboard</caption>
<br><br>

<h1>Demo</h1>
<p>Demo streamlit app used</p>
<div class="code-container">
  <pre>
    <code>
      streamlit run streamlit_app.py
    </code>
  </pre>
<p>You can view a demo <a href="https://github.com/Aaron-k12/customer-satisfaction-project/assets/107159092/e6aafeef-9277-4b4d-be02-0177873281c3" target="_blank" >here</a></p>


<p> You can view the demo <a href="https://github.com/Aaron-k12/customer-satisfaction-project/assets/107159092/053ee89e-56c1-4f03-90e5-f54e395ccc30">here></a></p>





