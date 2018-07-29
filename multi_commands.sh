#!/bin/sh
aggiestack config --hardware aggiestack/hdwr-config.txt
aggiestack show hardware
aggiestack config --images aggiestack/image-config.txt
aggiestack show images
aggiestack config --flavors aggiestack/flavor-config.txt
aggiestack show flavors
aggiestack server create --image linux-ubuntu --flavor small my-first-instance
aggiestack server create --image linux-ubuntu --flavor medium my-second-instance
aggiestack server create --image linux-ubuntu --flavor xlarge my-third-instance
aggiestack admin evacuate r1
aggiestack server create --image linux-ubutnu --flavor xlarge my-fourth-instance
aggiestack admin show instances
aggiestack admin add --mem 8 --disk 4 --vcpus 4 --ip 128.0.0.1 --rack r1 newmachine 
aggiestack admin show instances
