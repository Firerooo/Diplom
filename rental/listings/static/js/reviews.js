document.addEventListener("DOMContentLoaded", function () {
    const leaveReviewBtn = document.getElementById("leave-review-btn");
    const modal = document.getElementById("auth-modal");
    const closeModalBtn = document.getElementById("close-modal");
    const confirmAuthBtn = document.getElementById("confirm-auth");

    leaveReviewBtn.addEventListener("click", function () {
        const isAuthenticated = document.body.dataset.authenticated === "true";

        if (!isAuthenticated) {
            modal.style.display = "flex";
        } else {
            window.location.href = "/leave-review/";
        }
    });

    closeModalBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    confirmAuthBtn.addEventListener("click", function () {
        window.location.href = "/users/login/";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
