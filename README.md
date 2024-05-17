# Accident-Detection-Using-YOLOv8
This project utilizes YOLOv8, Google Colab, Python, Roboflow, Deep Learning, OpenCV, and Machine Learning. It has the ability to identify any accident using videos. This model is developed using a dataset of over 3000 images, labeled using roboflow and labelImg (an open source tool).

## Features
- Accident detection using the YOLOv8 model trained on custom accident data
- Real-time accident detection from video streams
- Customizable detection thresholds and settings


## Proposed Methodology
- We are utilizing Yolov8 model to train our personalized dataset that consists of over 3000 images gathered from various sources such as the UCF Crime Dataset and Roboflow.
- After completing 25 epochs of training, this model is now prepared to identify accidents with a high likelihood. Even though its current training doesn't allow for real-world deployment.


## Installation and Usage
### Using flask app
- Clone the repository
- Install the required dependencies from requirements.txt
- Create a Python environment and Run flask.py
- Click on Video Input button and upload video on next page and submit to see the results

### Training Data
- Go to <a src="https://drive.google.com/drive/folders/1Yh56CJvFXfS9iJsxpZCZhpwBf45vL6uZ?usp=sharing">Training Data</a> to get the Training Data.

## Model Training
#### Preparing Custom dataset
- We gathered over 250 images from various sources such as YouTube, Google images, Kaggle.com, and also converted 30 videos into frames using python.
- Next, we labeled each of them one by one on a website known as roboflow and using an open source python tool named labelImg.
- While annotating, we designated images without accidents as NULL and outlined a bounding box around the accident site in images that did have an accident.
- Next, we split the dataset into training, validation, and testing subsets.
- In the last stage, we obtained the dataset in standard images and text files containing labels for bounding box positions.
                                                                           
#### Setting up Google Collab to Train the Model
- We utilized Google Colab for training this model as it offers a free GPU that is quicker than our own local setups.
- Utilized Jupyter notebooks on Google Colab to create and execute Python code, seamlessly combining code, text, and visualisations in one place.
- Running separate code cells in Jupyter Notebooks allowed us to easily see the results, making it beneficial for testing and troubleshooting.
                                               
#### Training the model in jupyter notebook
- To begin developing the model, we initially installed necessary software like yolov8.
- Next, we connected our Google Drive to Google Colab.
- Next, the model was trained with 25 epochs and over 3000 images using the yolov8 train command.
Next, the trained model was used to perform validation and testing.

### Training Results
- You can get the google colab jupyter notebook and training, validation and testing results on <a src="https://drive.google.com/drive/folders/14IkrtwecfqIPW-AQ6uR_YUWlo-fwZjBk?usp=sharing">Training Results</a>


## Challenges Faced
- Took long enough to find required dataset and then filtering the best frames out of all data found as most of the data is of low quality and bad resolution which is not suitable for machine learning.
- Didn't had idea of what parameters should be used in training the model like number of epochs, batch size, number of workers, etc.
- Faced failures in training models initially as we had no idea that how much frames should be trained, initially we were training 300-500 images and hoping to get good results but failed and wasted time.


## Learning from the Project
- Acquired practical experience working with YOLO and CNN Algorithm.
- Increased understanding of machine learning.
- Improvement in our ability to create a model that is both faster and more precise.
- Managing time as well as resources.


## Future Works
- Add more classes of 'Weapon Detection', 'Fight Detection', 'Theft Detection' to make the model versatile.
- Increase the dataset size and training the model to acquire more accuracy.
- Using other ML models and algorithms and try to integrate with YOLOv8
- Integrate realtime cctv camera with the project and creating a centralized portal to access realtime detection from anywhere


## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
