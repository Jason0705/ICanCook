#Group 13 ICanCook Website 

## About

This project was created for CMPT 470 during the Fall 2016 semester. 

##Project Structure

###.vagrant

* Runs virtual machine 

##chef

* List of packages and configurations to install for Website to work 

###docs 

* Contains project proposal 

### mysite

* contains all the apps for the project 
	**accounts**
		*contains index url
	**home**
		*contains static files, index and search templates and search implementation
	**media**
		*contains pictures used across the website
	**mysite**
		*contains settings.py and urls for home, recipes and user
	**recipes**
		*contains templates for recipes pages, forms relating to creating, edits and view recipes
		*contains model for Recipe (steps, quantity, ingredients, and category)
	**user**
		*contains templates, urls, forms and implementation for login and signup	
	*manage.py
		*sets DJANGO_SETTINGS_MODULE to point to settings.py

## Build Instructions
 
	*Open cmd and run vagrant up to start up server 
	*Once vagrant has finished and chef has installed the right packages and configurations
	*Go to http://localhost:3000
	*At the homepage you can view recipes other people have created 
	*Click login and sign in, if you do not have an account you can create one by clicking Create Account
	*Signup for a new account by filling in all the fields 
	*After you may login with your newly created account 
	*With an account you can create and edit your own recipes, favourite others and with a facebook login you can comment 


## License

This project is licensed under the BSD-3 license:

Copyright (c) 2016, Simon Fraser University
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.