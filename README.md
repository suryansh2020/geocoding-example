Geocoding Example
=================

There are many open data sets that can be used in a geospatial
analysis. A data set may not include coordinates by default
but you can use geocoding to make them available.

Installation
------------

Depending on your preferences, you can install the dependencies using
[miniconda](http://conda.pydata.org/miniconda.html) or [anaconda](https://www.continuum.io/downloads). These are both distributions of Python
that are well-suited for scientific/analytic (data science) programming.
You will then need to use a virtual environment from file
([docs available](http://conda.pydata.org/docs/using/envs.html). The
virtual environment for the geography dependencies are available:

```shell
$ conda env create -f requirements/geocoding.yml
```
The `geocoding` dependencies will provide everything you need to collecting
data and geocoding addresses in your dataset.

Use Case
--------

For this example, we're interested in *"Statistics for All U.S. Firms by
Industry, Gender, Ethnicity, and Race for the U.S., States, Metro Areas,
Counties, and Places: 2012 Survey of Business Owners"*. Data for this
survey can be [viewed here](http://factfinder.census.gov/faces/tableservices/jsf/pages/prooductview.xhtml?pid=SBO_2012_00CSA01&prodType=table).
Note that I've hosted the dataset on [AWS](https://aws.amazon.com/)
because life is too short to wait for downloads from the Census bureau.

Run
---

Run the analysis (make sure you're conda environment is enabled):

```shell
$ python fetchdata.py
```

Next Steps: Choose your own adventure!
---------------------------------------

1. Improve the geocoding in this example

   * You'll see from the log file that some addresses were missed.

1. Create a geospatial app

	* If you would like to use this information in a geospatial app 
	  then check out a tutorial using [Flask, MongoDB, and Leaflet.js](openshift-mongo-flask-example). 

1. Use a geospatial app from someone else

	* [Tableau maps](https://www.tableau.com/stories/topic/maps)

	  - Note that their automatic geocoding should only work if your data
		does is an actual location and not a census region. Running the 
		formatting function then writing to csv may be sufficient for
		Tableau but I haven't tried it.

	* [ArcGIS from Esri](https://blogs.esri.com/esri/arcgis/2011/02/09/tuning-a-locator-for-improved-performance/) includes bulk geocoding. 

