# Final Project. 
#
# Here I will document my thought process on the final project. 
#
# I ultimately determined that although the challenge says it can be done in "Language of Choice" JavaScript is really the only suitable language. 
#
# Unfortunately I do not know JavaScript (I do not believe it is offered at Franciscan) and I had several papers that required my attention this week
# thus effectually leaving me crammed for time and unavailable to teach myself the necessary basics to complete the challenge. My first issue was choosing an IDE.
# 
# In order to construct something you must first have the tools. Orginally I attempted to find information on how to acheive the final product in Python. (my favorite language)
# after a bit of time I came up with this to import the randomuser.me website: 

# Generate a user
user = RandomUser()

# Generate a list of 10 random users
user_list = RandomUser.generate_users(10)

get_password() 

# I ran into error after error and found that the default for randomuser.me user is to give output in JSON files which are only compatable with JavaScript.
# I did not want to use JavaScript as I was low on time and did not have the ability to put much of my time towards this. I attempted to change the 
# filetype to CSV so that it would have compatability but could not get the modules to import 'randomuser.me' to function correctly. 
# 
# From here I decided to move to JavaScript.  
#
# I started with attempting to 'get' the randomuser.me website

const url = 'https://randomuser.me/api/?results=10';

fetch(url)
  .then(function(data) {
    })
  })
  .catch(function(error) {
  });  

# this seemed to be the right trail but I was still a long ways away from any code that was actually functional. 
# I decided that I would show my coding trail on the back end in this file. (As time had it I did not get the chance to look at the front end.)
# I can definetly learn JavaScript as it seems to have the same format as C++ but not well enough to build a fucntioning front and back end in the roughly 6 hours 
# I had left of Thursday. I would reccomend stating that the front in back end MUST be written in JavaScrict instead of saying a "language of choice". I am sure that the front 
# and back end could be built in Python or other languages but it would be clunkly and not nearly as effecient as JavaScript. Additionally because the 
# default of "randomuser.me" is JSON it would be most reasonable to just make the final part of the challenge JavaScript. 