# Moon Data Classification

In this notebook, you'll be tasked with building and deploying a **custom model** in SageMaker. Specifically, you'll define and train a custom, PyTorch neural network to create a binary classifier for data that is separated into two classes; the data looks like two moon shapes when it is displayed, and is often referred to as **moon data**.

The notebook will be broken down into a few steps:
* Generating the moon data
* Loading it into an S3 bucket
* Defining a PyTorch binary classifier
* Completing a training script
* Training and deploying the custom model
* Evaluating its performance

Being able to train and deploy custom models is a really useful skill to have. Especially in applications that may not be easily solved by traditional algorithms like a LinearLearner.

---
