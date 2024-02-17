Counter Assignment

Build a flask application that counts the number of times the root route ('/') has been viewed.
    - This assignment is to text your understanding of session

As part of this assignment, please start with the following features first:
    - localhost:5000 - Have the template render the number of times the client has visited this site
    - localhost:5000/destroy_session - Clear the seession. Once cleared, redirect to the root.

Assignment checklist
    - Create a new Flask project called Counter
    - Have the root route render a teemplatee that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
    - Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
    - NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2.
    - NINJA BONUS: Add a Reset button to reset the counter
    - SENSEI BONUS: Add a form that allowsd the user to specify the increment of the counter and have the counter increment accordingly.
    - SENSEI BONUS: Adjust your code to display both how many times the useer has actually visited the page, as well as the value of the counter, given the above functionality
    - SENSEI BONUS: Decode the cookie information as shown in the video