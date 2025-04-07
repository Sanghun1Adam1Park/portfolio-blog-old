function copyEmail() {
    const email = "sanghunpark0628@gmail.com"
    navigator.clipboard.writeText(email).then(() => {
        alert("Email copied to clipboard!");
    }).catch(err => {
        console.error("Failed to copy email: ", err);
    });
}
