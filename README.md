1. Amazon S3
For storing the sales dataset (train.csv, etc.)

Acts as the data source for training in SageMaker

2. Amazon SageMaker
For model training (probably using XGBoost or Linear Learner algorithm)

For deploying the trained model to a real-time endpoint

We’ll use the SageMaker Python SDK

3. Streamlit
To build a cool, interactive UI (user inputs like TV/Radio spend, Region, etc.)

Will send input to SageMaker endpoint and display the predicted sales instantly

4. IAM (Identity and Access Management)
We'll use an IAM Role with S3 + SageMaker permissions

