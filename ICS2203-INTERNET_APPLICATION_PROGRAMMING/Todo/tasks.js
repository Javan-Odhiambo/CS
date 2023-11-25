/*
* Group members:
* SCT211-0098/2022 - Javan Odhiambo Otieno
* SCT211-0005/2022 - Ian Dancun Mwangi  
* SCT211-0077/2022 - Ephraim Shikanga   
* SCT211-0042/2022 - Joan Nkatha Kinoti 
* SCT211-0043/2022 - Melane Minayo      
* SCT211-0008/2022 - Ngugi Joseph Ngure 
*/

document.addEventListener('DOMContentLoaded', () => {

    // uery for the submit button and input task field once in the beginning and store those two values in the variables submit and newTask.
    const newTask = document.querySelector('#task');
    const submit =  document.querySelector('#submit');

    // disable the submit button by default.
    submit.disabled = true;

    // Listen for input to be typed into the input field
    newTask.addEventListener('input', (e) => {
        if (e.target.value.length > 5) 
            submit.disabled = false;
        else 
            submit.disabled = true;
        
    })

    // listen for form sumbission
    document.getElementsByTagName('form')[0].addEventListener('submit', (e) => {
        e.preventDefault()

        // Find the task the user just submitted
        const textSubmitted = newTask.value;
        // Create a list item for the new task and add the task to it
        const taskItem = document.createElement('li');
        taskItem.innerText = textSubmitted;

        // Add new element to our unordered list
        document.querySelector("#tasks").append(taskItem);
        
        newTask.value = "";

        // return false at the end
        return false;
    })

})

