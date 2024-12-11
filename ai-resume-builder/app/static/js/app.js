document.getElementById("generateSummaryBtn").addEventListener("click", function () {
    const userInput = document.getElementById("summary").value;

    // Show loading state
    document.getElementById("generateSummaryBtn").innerText = "Generating...";

    // Make the API call to generate summary
    fetch('/generate-summary', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ user_input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.summary) {
            // Fill the textarea with the generated summary
            document.getElementById("summary").value = data.summary;
            document.getElementById("generateSummaryBtn").innerText = "Generate Summary with AI";
        } else {
            // Show error message if something went wrong
            document.getElementById("error-message").style.display = 'block';
            document.getElementById("error-message").innerText = data.error || "An error occurred. Please try again.";
        }
    })
    .catch(error => {
        // Handle any other errors
        document.getElementById("error-message").style.display = 'block';
        document.getElementById("error-message").innerText = "Error: " + error;
        document.getElementById("generateSummaryBtn").innerText = "Generate Summary with AI";
    });
});
