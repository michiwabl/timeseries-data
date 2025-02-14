Timeseries Prediction	
Task: Given a set of sensor data for multiple streams, e.g. temperature, power consumption. The goal is to predict the future values of these signals, optimally including a confidence range.

Approach: Take the stream of data and remove the last ~10% of the data. Build a prediction algorithm that is able to predict the future values of the streams as accurately as possible and compare against the values you removed.

Suggested data-sets:

Intel Berkeley Research Lab
Take for example the data from the sensors of the Intel Berkeley Research Labs, see Stream Data Mining Repository. The data is in a format used by many machine learning frameworks, e.g. Weka.
Powersupply Stream
Use the power supply stream from the same data source: Stream Data Mining Repository. Here the challenge is to integrate seasonality into the analysis.
UCI Repository
Repository of multiple data-sets, including timeseries.
Advanced: Investigate your prediction algorithm and try to determine under which (controlled) circumstances it makes correct predictions.
