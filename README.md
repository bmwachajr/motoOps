# motoOps
Amber Moto Ops

# Introduction

Ampersand operates a battery swap network. Electric motorcycles come to swap stations and they have
their depleted batteries swapped out with charged batteries. The batteries charge at the station. The
drivers that bring the batteries pay only for the energy used in the battery at every swap. Ampersand
needs to know which battery was used by which driver at which station. Ampersand also needs to know
how much energy was used in each battery and convert that to a dollar amount to charge the drivers at
the time of swap.

### Main features

* Create, Retrieve, Update and Delete batteries

* Create, Retrieve, Update and Delete drivers

* Create, Retrieve, Update and Delete stations

* Create, Retrieve, Update and Delete battery swaps

* Create, Retrieve, Update and Delete battery telematic records.

* Determine Charge used by a driver during a swap

* Determine the amount payable by a driver during a swap

* Determine the distance traveled by a driver

# Usage

This project is built using Python, Django and SQLite:

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:bmwachajr/motoOps.git
    $ cd motoOps
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver


You can access the api docs on :

    http://127.0.0.1:8000/

