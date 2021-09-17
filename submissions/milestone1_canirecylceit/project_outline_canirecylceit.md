# Project - CanIRecycleIt.com

## Problem Definition(s)

Waste management is one of the most challenging problems to solve in the 21st century. The average American produces 1,704 pounds of garbage per year, roughly three times the global average, according to a [report](https://www.globalcitizen.org/en/content/americans-produce-most-waste/#:~:text=The%20average%20American%20produces%201%2C704,the%20research%20firm%20Verisk%20Maplecroft.) by the research firm Verisk Maplecroft in 2019.

Two main considerations in waste management are:

* Consumers placing non-recyclable items into recycling bins which leads to [inefficiencies](https://www.valleywasteservice.com/valley-waste-news/what-happens-if-you-put-non-recyclable-items-into-recycling-4034) in the sorting process.

* Consumers looking to buy recyclable products [may not know if a product is recyclable or not](https://news.slashdot.org/story/21/09/09/153219/california-aims-to-ban-recycling-symbols-on-things-that-arent-recyclable).

## Proposed Solution

Build binomial classification model for recylcable/non-recylcable

Build multinomial classification for material identification (e.g. plastic. metal, etc.)

Provide standard data model for upload of labeled images for ongoing classification model build/improvement

Provide UI (canIrecyclethis.com) and API for real-time inference

## Project Scope

Classification Categories.  Not clear what ideal classification/label strategies would be to support desired use-cases.

## Draft Timeline 

- Data pre-processing, labeling, EDA
- Modeling ideas:
  - Initial baseline model results (UNET + SVM)
  - Tensorflow Object detection API/models 
  - LeNet style CNN trained from scratch
  - Transfer Learning (ResNet50, MobileNet, InceptionResNetV2, DenseNet)
  - Self-Supervised Learning with Fast.ai and fine tuning desired classification
- Scalable, back-end cloud infrastracture development
- UI/UX ideation; Low/High fidelity wireframing,journey maps, needs/wants selection
- Best model serialization and API development
- Web application deployment
- Strategy development for promotion and comms? Are we going to try to make this public?
- Any other ideas for intermediate timelines?

## Datasets and Models considered

This github repo contains information on different trash/waste related datasets: https://github.com/AgaMiko/waste-datasets-review
This github repo contains a literature review of different approaches and performance results on above datasets: https://github.com/majsylw/litter-detection-review

The three top contenders that I see are:

### Waste Classification Data v2 (this one may be a better fit for the dataset size requirements in this class)
Over 25k images divided into training data - 22564 + 2508 nonrecyclable images and test data - 2513 images + 397 from category nonrecyclable. Three main categories: Organic (O), recyclable (R), and nonrecyclable (N).

Available on Kaggle here: https://www.kaggle.com/techsash/waste-classification-data

### TrashNet (material classification but relatively small data set size)
The TrashNet Classification dataset contains 2467 images from 6 categories: cardboard (393), glass (491), metal (400), paper (584), plastic (472) and trash (127). I think it may be interesting to work with this dataset but it's size may be a challenge and I also think the categories are fairly obvious to an end user (i.e. most users would know if a piece of trash is plastic or metal but the above dataset classes of organic, nonrecyclable, and nonrecyclable may be more interesting for end users).

Download here: https://github.com/garythung/trashnet/blob/master/data/dataset-resized.zip

### Drinking Waste Classification
The dataset contains ~10k images groupped by 4 classes of drinking waste: Aluminium Cans, Glass bottles, PET (plastic) bottles and HDPE (plastic) milk bottles. Pictures were taken with 12 MP phone camera as a part of final year Individual Project at University College London. The dataset used parts of manually collected images from TrashNet.

### Portland State University Recycling Image Classification Dataset 
Dataset composed of '11,500 image training data of 5 common recycling items' availble from Portland State University
http://web.cecs.pdx.edu/~singh/rcyc-web/index.html


Download: Directly from kaggle https://www.kaggle.com/arkadiyhacks/drinking-waste-classification

## Team Members

- Bruno Janota
- Daniel Olal
- Daria Zhukova
- Kevin Hill
- Javaria Hassan
