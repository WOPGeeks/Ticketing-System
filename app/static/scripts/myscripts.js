function checkAndChangeColors() {

    let expiredStuff = document.getElementById('expire-status');
    expiredStuffValue = expiredStuff.value;
    let statusOverdueStuff = document.getElementById('overdue-status');
    statusOverdueStuffValue = statusOverdueStuff.value;
    if (expiredStuffValue.includes("Expired")) {
        expiredStuff.style.color = "red";

    } else {
        expiredStuff.style.color = "blue";
    }

    if (statusOverdueStuffValue.includes("Overdue")) {
        statusOverdueStuff.style.color = "red";

    } else {
        statusOverdueStuff.style.color = "green";

    }
}