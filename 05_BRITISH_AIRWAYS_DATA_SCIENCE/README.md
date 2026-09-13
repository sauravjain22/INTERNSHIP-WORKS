# Predicting Customer Buying Behaviour — British Airways

## Project Overview

This project was completed as part of the **British Airways Data Science Virtual Experience Program by Forage**.

The objective was to use customer booking data and a machine learning model to predict whether a customer is likely to complete a booking.

The analysis focuses on identifying the behavioural, travel, and booking characteristics that contribute most to booking completion and how these insights could help British Airways proactively target high-potential customers before travel.

---

## Business Objective

Airlines need to identify potential customers before they travel rather than relying on customers to make decisions at the airport.

The business objective of this project is therefore to:

- Predict whether a customer is likely to complete a booking.
- Identify the variables that contribute most to booking behaviour.
- Use these insights to support more targeted customer acquisition and marketing strategies.

---

## Dataset

The dataset contains **50,000 customer booking records**.

### Target Variable

`booking_complete`

- `0` → Booking not completed
- `1` → Booking completed

### Main Features

| Feature | Description |
|---|---|
| `num_passengers` | Number of passengers travelling |
| `sales_channel` | Booking channel |
| `trip_type` | Type of trip |
| `purchase_lead` | Days between booking and travel |
| `length_of_stay` | Number of days spent at destination |
| `flight_hour` | Flight departure hour |
| `flight_day` | Day of the week of departure |
| `route` | Origin → destination route |
| `booking_origin` | Country from which the booking was made |
| `wants_extra_baggage` | Whether extra baggage was requested |
| `wants_preferred_seat` | Whether a preferred seat was requested |
| `wants_in_flight_meals` | Whether an in-flight meal was requested |
| `flight_duration` | Flight duration in hours |

---

# Exploratory Data Analysis

The dataset contains **50,000 observations and 14 original features**.

There were **no missing values**, so no missing-value imputation was required.

### Target Distribution

The target variable is imbalanced:

- **85.0%** → booking not completed
- **15.0%** → booking completed

This is important because accuracy alone can be misleading. A model could achieve high accuracy simply by predicting the majority class.

### Categorical Feature Cardinality

The main categorical variables have the following number of unique values:

- `sales_channel` → 2
- `trip_type` → 3
- `route` → 799
- `booking_origin` → 104

The high cardinality of `route` and `booking_origin` makes appropriate categorical encoding important for modelling.

### Important EDA Findings

#### Sales Channel

Most bookings were made through the **Internet** channel.

The booking completion rate was higher for Internet bookings than Mobile bookings, suggesting that booking channel may contain useful predictive information.

#### Trip Type

The dataset is heavily dominated by **Round Trip** bookings.

Round Trip customers also showed a higher booking completion rate than One Way and Circle Trip customers.

#### Flight Hour

Booking completion rates varied across departure hours.

The highest rates occurred around the afternoon/evening period, showing that departure time may contain useful predictive information.

#### Purchase Lead

`purchase_lead` is strongly right-skewed.

Most customers booked relatively close to their travel date, while a smaller number booked much further in advance.

#### Length of Stay

`length_of_stay` is also strongly right-skewed.

Most customers had relatively short stays, with a small number of unusually long stays.

These distributions were retained rather than blindly removing extreme values because they may represent genuine customer behaviour.

---

# Feature Engineering

Feature engineering was kept focused on features with a clear business interpretation.

### Flight Day Conversion

`flight_day` was originally stored as categorical text:

`Mon, Tue, Wed, Thu, Fri, Sat, Sun`

It was converted into numerical weekday values:

- Monday → 1
- Tuesday → 2
- Wednesday → 3
- Thursday → 4
- Friday → 5
- Saturday → 6
- Sunday → 7

This allows the variable to be used by the machine learning pipeline while preserving the ordering of the days.

### Weekend Feature

An additional feature, `is_weekend`, was created from `flight_day`.

- `1` → Saturday or Sunday
- `0` → Weekday

This provides a simpler representation of whether the flight occurs on a weekend, which can capture travel-pattern differences.

### Categorical Encoding

Categorical variables were converted into numerical representations using **One-Hot Encoding**.

This was particularly important for variables such as:

- `sales_channel`
- `trip_type`
- `route`
- `booking_origin`

One-hot encoding allows the Random Forest model to work with categorical information without assigning artificial numerical meaning to categories.

---

# Machine Learning Model

## Random Forest Classifier

A **Random Forest Classifier** was selected for the predictive modelling task.

The main reason for choosing Random Forest was that it:

- Handles nonlinear relationships.
- Can capture interactions between variables.
- Works well with mixed feature types after preprocessing.
- Provides feature importance values.
- Is relatively interpretable compared with many more complex models.

A preprocessing pipeline was used to transform the data before training the model.

---

# Model Evaluation

The dataset was split into training and test sets, with the model evaluated using classification metrics and ROC-AUC.

### Test Set Performance

**ROC-AUC: 0.790**

ROC-AUC is useful here because the target variable is imbalanced and the objective is to distinguish customers who are more likely to complete a booking.

### Classification Performance

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| 0 — Not completed | 0.86 | 0.98 | 0.92 |
| 1 — Completed | 0.53 | 0.13 | 0.21 |

Overall accuracy was approximately **85%**.

However, accuracy should not be interpreted as the main success metric because only around 15% of customers completed bookings.

The model identifies the majority class very well but has relatively low recall for customers who actually complete a booking. Therefore, the model should be viewed as a useful ranking/targeting model rather than a perfect booking classifier.

---

# Cross-Validation

To check whether model performance was consistent across different subsets of the data, **5-fold cross-validation** was performed using ROC-AUC.

### Results

```text
Cross-validation ROC-AUC scores:

0.7786
0.7723
0.7720
0.7818
0.7777

Mean ROC-AUC: 0.7765
Standard deviation: 0.0038