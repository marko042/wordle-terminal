# Wordle Terminal
[View the live project here] (https://github.com/marko042/wordle-terminal.git)

This project represents a modified clone of the popular online game Wordle.
Your challenge is to guess a five-letter word in six attempts. Each time you guess, you're told which of your chosen letters are in the target word, and whether they are in the right place. And that's it.

# Project goals

 This project main idea is to entertain the players who are fans and engage the ones who are not yet familiar with this viral phenomenon that started bach in 2022.

# User experience

 - Main purpose:

    Build an easy app for the users to play the game.
    Build a game that is both enjoyable and challenging for the players.

    As a new visitor, I want to:

    Be able to understand the purpose of the App and start a new game.
    Be able to follow the score, see the wrong and right letters appear once I take a turn, and see how many tries remain before the game is over.
    

    As a returning visitor, I want to:

    Be able to play the game again with a different word as chosen by the computer.
    Be challenged and try to improve on my previous scores.
    

    # Design

    - Flowchart

    ![Heading text](/assets/images/docs/flow-chart.PNG)

     # Existing features
     
     - Logo and Intro Message along with first guess and correct position of first letter

     ![Heading text](/assets/images/docs/intro-logo1.PNG)




      - Wrong user input, also note that it resets number of tries, until the 5 letter word is inserted

      ![Heading text](/assets/images/docs/wrong-user-input.PNG)
      
    
      - word guessed preview with an option to play another game

      ![Heading text](/assets/images/docs/word-guessed.PNG)

      # Features left to implement
       - Keep track of how many guesses left to use during the game
       - Connect to Google Sheet and establish a leaderboard that updates accordingly.

      ## Technologies Used
      - Languages Used
        - Python

      - Python Packages

   -  Random: returns a random integer to get a random word
   -  sys: It allows us to access parameters and functionalities specific to the terminal
   -  colored: python library for color and formatting in terminal



      ## Frameworks - Libraries - Programs Used

         Git
         - Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
         GitHub
         - GitHub is used to store the project's code after being pushed from Git
         Heroku
         - Heroku was used to deploy the live project
         Lucidchart
         - Lucidchart was used to create the flowchart
         PEP8
         - The PEP8 was used to validate all the Python code
         Patorjk
         - Patorjk (ASCII Art Generator) was used to draw the game logos


         ## Storage Data
         - List of random 5 letter words is pulled from a txt file I created.


      # Testing

      Testing was performed to pinpoint and troubleshoot any issues as I went along.

      ## Validator Testing

      - PEP8  Validator Service was used to validate every Python file in the project to ensure there were no syntax errors in the project. [pep8ci](https://pep8ci.herokuapp.com/)
       - Lines to long errors found and fixed, but invalid escape sequence to my knowledge was present because of the use of backslash sign  in the logo

      - Lighthouse
         - ![Lighthouse report](/assets/images/docs/Lighthouse.PNG)

         ## Functionality and bugs
         One bug I noticed and did not fix as of yet; after finishing the game second time the option to restart game does not appear.
         Aside from mentioned above all game aspect running smoothly.

         # Deploying this Project

         - This site was deployed by completing the following steps:

      - Log in to Heroku or create an account
      - On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
      - You must enter a unique app name
      - Next select your region
      - Click on the Create App button
      - The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
      - Click Reveal Config Vars and enter port into the Key box and 8000 into the Value box and click the Add button
      - Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
      - Repeat step 8 to add node.js. o Note: The Buildpacks must be in the correct order. If not click and drag them to move into the correct order
      - Scroll to the top of the page and choose the Deploy tab
      - Select Github as the deployment method
      - Confirm you want to connect to GitHub
      - Search for the repository name and click the connect button
      - Scroll to the bottom of the deploy page and select the preferred deployment type
      - Click either Enable Automatic Deploys for automatic deployment when you push updates to Github


      ## Credits

      In this section I will to best of my abilities and most comprehensively list all the resources that contributed in any way to building this website.
      
      # Content
       - Portion of the development of this website was done using resources provided in love sandwiches walkthrough project
       - Numerous helpful tips were found on [W3shools online web tutorials](https://www.w3schools.com/) and [Stackoverflow](https://stackoverflow.com/) [Programiz](https://www.      programiz.com/)
        - Specific wordle tutorials used and code adapted from [Replit](https://replit.com/@JacobLower3/wordle-tutorial#main.py) (https://replit.com/@JacobLower3/wordle-tutorial#main.py) [thecodingprocess](https://thecodingprocess.hashnode.dev/creating-a-wordle-game-using-python)





