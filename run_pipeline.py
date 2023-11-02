from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__ == "__main__":
    # Run the pipeline
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path= "/mnt/c/Users/hp/Downloads/Artificial Intelligence/MLOPS/Ubuntu/customer-satisfaction/data/olist_customers_dataset.csv")
    
    
#mlflow ui --backend-store-uri "file:/home/reez/.config/zenml/local_stores/196b731c-4599-45f6-9fba-ce467579dd99/mlruns"
