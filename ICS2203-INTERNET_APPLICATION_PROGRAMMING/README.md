# ICS2203: Internet Application Programming.

## Assignments
---
### Assignment 1
In groups, use the following html code create JS to accomplish the following:
- Query for the submit button and input task field once in the beginning and store those
two values in the variables submit and newTask.
- Disable the submit button by default. Enable/disable by setting its disabled attribute to
false/true.
- Listen for input to be typed into the input field
- Listen for submission of form
- Find the task the user just submitted
- Create a list item for the new task and add the task to it
- Add new element to our unordered list
- At the end of the script, add the line return false. 

This prevents the default submission of
the form which involves either reloading the current page or redirecting to a new one.

**Note: create HTML elements using the createElement function. Add the elements to the
DOM using the append function.**

```xml
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tasks</title>

    <script src="tasks.js"></script>
</head>

<body>
    <h1>Tasks</h1>
        <ul id="tasks"></ul>
    <form action="">
        <input type="text" name="" placeholder="New task" id="task">
        <input type="submit" value="Add" id="submit">
    </form>
</body>

</html>

```
[Click to see solution](./Todo/tasks.js)

