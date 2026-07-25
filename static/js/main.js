document.addEventListener("DOMContentLoaded", function () {
    // Auto-dismiss alert messages after 5 seconds
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Navbar scroll effect
    const navbar = document.querySelector('.luxury-navbar');
    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(8, 8, 8, 0.95)';
            navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.5)';
        } else {
            navbar.style.background = 'rgba(8, 8, 8, 0.85)';
            navbar.style.boxShadow = 'none';
        }
    });
});