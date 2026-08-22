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
                navbar.style.background = 'rgba(8, 8, 8, 0.95)';
                navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.5)';
            } else {
                navbar.style.background = 'rgba(8, 8, 8, 0.85)';
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // 3. Force redirect to home page if the user refreshes any sub-page
    if (window.performance) {
        let navEntries = performance.getEntriesByType("navigation");
        if ((navEntries.length > 0 && navEntries[0].type === "reload") || 
            (performance.navigation && performance.navigation.type === performance.navigation.TYPE_RELOAD)) {
            if (window.location.pathname !== "/") {
                window.location.href = "/";
            }
        }
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