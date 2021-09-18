# Project - CanIRecycleIt.com

## Team Members

* CRO - Chief Recylcing Officer - Bruno Janota
* CTE - Chief Trash Executive - Daniel Olal
* CEO - Chief Environmental Officer - Daria Zhukova
* CSO - Chief Sustainability Officer - Kevin Hill
* CGO - Chief Green Officer - Javaria Hassan

## Background and Problem Definition(s)

Waste management is one of the most challenging problems to solve in the 21st century. The average American produces 1,704 pounds of garbage per year, roughly three times the global average, according to a [report](https://www.globalcitizen.org/en/content/americans-produce-most-waste/#:~:text=The%20average%20American%20produces%201%2C704,the%20research%20firm%20Verisk%20Maplecroft.) by the research firm Verisk Maplecroft in 2019. Poor waste management is linked to environmental risks, such as climate change and pollution, and consequent economic harm.

To achieve a sustainable future, it is imperative to develop an effective waste management system. Currently, a majority of waste is not recycled and ends up in sanitary landfills. Reasons for this include:

* Consumers placing non-recyclable items into recycling bins which leads to [inefficiencies](https://www.valleywasteservice.com/valley-waste-news/what-happens-if-you-put-non-recyclable-items-into-recycling-4034) in the sorting process.

* Consumers looking to buy recyclable products [may not know if a product is recyclable or not](https://news.slashdot.org/story/21/09/09/153219/california-aims-to-ban-recycling-symbols-on-things-that-arent-recyclable).

In light of these factors, we contribute a platform for consumers that detects and classifies recyclable materials using artificial intelligence and computer vision.

## Proposed Solution

We build and deploy a web-based Application that will enable Users to take a picture of an item of trash and identify if it is recylcable or not.  Additionally we will provide the ability for Users to submit additional pictures to further improve model performance over time via incremental data acquisition.  Inference API will be exposed to enable additional integration of image classification functionality into other 3rd party applications if desired (mobile, etc.).

A CNN image classification model will be developed via a training pipeline to identify recylcable and non/recylcable materials.  An additional supporting multinomial classification model may be built to identify material types (e.g. plastic, metal, etc.) as additional feature input and user-explanatory information.

Expectation is that CNN models will take advantage of transfer learning and will be built on `resnet50` (or similar pre-existing architecture) with fine-tuning based on recyclable data-set.

## Draft Timeline

* Data pre-processing, labeling, EDA
* UI/UX ideation: Wireframing, etc.
* Modeling approach:
  * Initial baseline model results (UNET + SVM)
  * Tensorflow Object detection API/models
  * LeNet style CNN trained from scratch
  * Transfer Learning (ResNet50, MobileNet, InceptionResNetV2, DenseNet)
  * Self-Supervised Learning with Fast.ai and fine tuning desired classification
* Scalable, back-end Training pipeline development
* Model performance reporting dashboards
* Best model serialization and API development
* Web application deployment (Flask)

## Datasets and Models considered

### Background Assessments

* [This github repo](https://github.com/AgaMiko/waste-datasets-review) contains information on different trash/waste related datasets.
* [This github repo](https://github.com/majsylw/litter-detection-review) contains a literature review of different approaches and performance results on above datasets.

### Waste Classification Data v2

Over 25k images divided into training data - 22564 + 2508 nonrecyclable images and test data - 2513 images + 397 from category nonrecyclable. Three main categories: Organic (O), recyclable (R), and nonrecyclable (N).

Available on Kaggle [here](https://www.kaggle.com/techsash/waste-classification-data).

### TrashNet for Specific Material Classification

The TrashNet Classification dataset contains 2467 images from 6 categories: cardboard (393), glass (491), metal (400), paper (584), plastic (472) and trash (127). I think it may be interesting to work with this dataset but it's size may be a challenge and I also think the categories are fairly obvious to an end user (i.e. most users would know if a piece of trash is plastic or metal but the above dataset classes of organic, nonrecyclable, and nonrecyclable may be more interesting for end users).

Download [here](https://github.com/garythung/trashnet/blob/master/data/dataset-resized.zip).

### Drinking Waste Classification

The dataset contains ~10k images groupped by 4 classes of drinking waste: Aluminium Cans, Glass bottles, PET (plastic) bottles and HDPE (plastic) milk bottles. Pictures were taken with 12 MP phone camera as a part of final year Individual Project at University College London. The dataset used parts of manually collected images from TrashNet.

### Portland State University Recycling Image Classification Dataset

Dataset composed of '11,500 image training data of 5 common recycling items' availble from [Portland State University](http://web.cecs.pdx.edu/~singh/rcyc-web/index.html).

Download from kaggle [here](https://www.kaggle.com/arkadiyhacks/drinking-waste-classification).
