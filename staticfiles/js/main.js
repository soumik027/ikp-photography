document.addEventListener("DOMContentLoaded", function () {
    // 1. Auto-dismiss alert messages after 5 seconds
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // 2. Navbar scroll effect for luxury branding
    const navbar = document.querySelector('.luxury-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(3, 5, 10, 0.95)';
                navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.8)';
            } else {
                navbar.style.background = 'rgba(3, 5, 10, 0.9)';
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // 3. Bulletproof Refresh-to-Home Redirect
    // Check if a navigation flag already exists in this tab session
    const currentPath = window.location.pathname;
    
    if (currentPath !== "/") {
        // If we are on a sub-page, check if this page load was a refresh
        // We use a sessionStorage marker combined with a page-hide listener
        window.addEventListener('beforeunload', function () {
            sessionStorage.setItem('isReloading', 'true');
        });

        if (sessionStorage.getItem('isReloading') === 'true') {
            sessionStorage.removeItem('isReloading');
            window.location.replace("/");
        }
    } else {
        // Clear flag if we successfully reached home
        sessionStorage.removeItem('isReloading');
    }

    // 4. Mobile touch element state management
    document.addEventListener("touchstart", function() {}, {passive: true}); 
    
    const touchElements = document.querySelectorAll('.luxury-card, .glass-card, .event-section, .btn-gold, .btn-luxury-outline');
    touchElements.forEach(el => {
        el.addEventListener('touchstart', () => {
            el.classList.add('is-touched');
        }, {passive: true});
        
        el.addEventListener('touchend', () => {
            setTimeout(() => el.classList.remove('is-touched'), 200);
        }, {passive: true});
    });
});