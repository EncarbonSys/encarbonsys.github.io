/**
 * EnCarbonSys Global Navbar Loader
 * Injects the canonical navbar (pricing-page style) into any page.
 * Usage: add <div id="navbar-placeholder"></div> and <script src="/assets/js/navbar-loader.js"></script>
 */
(function () {
    const NAV_CSS = `
<style id="encarbonsys-navbar-css">
:root {
    --cosmic-green: #00df81;
    --dark-cosmic: #0a1a0f;
    --cosmic-glow: rgba(0, 223, 129, 0.3);
}
.navbar {
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    backdrop-filter: blur(25px);
    background: rgba(10, 26, 15, 0.95);
    border-bottom: 1px solid rgba(0, 223, 129, 0.2);
    padding: 0.4rem 0;
    transition: all 0.3s ease;
}
.nav-container {
    max-width: 1400px; margin: 0 auto; padding: 0 1.5rem;
    display: flex; justify-content: space-between; align-items: center;
}
.logo {
    font-size: 1.6rem; font-weight: 750; color: white; text-decoration: none;
    background: linear-gradient(135deg, var(--cosmic-green) 0%, var(--cosmic-accent, #7dd49a) 100%);
    background-clip: text;
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    display: flex; align-items: center; gap: 0.4rem;
    filter: drop-shadow(0 0 0 transparent); transition: all 0.3s ease;
}
.logo:hover { filter: drop-shadow(0 0 12px rgba(0, 223, 129, 0.6)); }
.logo img { height: 48px; transition: all 0.3s ease; }
.logo:hover img { transform: scale(1.05); filter: brightness(1.2); }
.nav-links {
    display: flex; gap: 1.5rem; list-style: none; align-items: center;
}
.nav-links a {
    color: rgba(255, 255, 255, 0.9); text-decoration: none;
    font-weight: 500; transition: all 0.3s ease; position: relative;
    font-size: 0.9rem; letter-spacing: 0.5px; padding: 0.5rem 0;
}
.nav-links a::after {
    content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px;
    background: var(--cosmic-green); transition: width 0.3s ease; box-shadow: 0 0 12px rgba(0, 223, 129, 0.5);
}
.nav-links a:hover { color: var(--cosmic-green); text-shadow: 0 0 10px rgba(0, 223, 129, 0.3); }
.nav-links a:hover::after { width: 100%; }
.nav-links a.active { color: #00ff88; }
.nav-links a.active::after { width: 100%; }
.dropdown { position: relative; }
.dropdown-toggle { display: flex; align-items: center; gap: 0.3rem; cursor: pointer; }
.dropdown-toggle i { font-size: 0.75rem; transition: transform 0.3s ease; }
.dropdown.active .dropdown-toggle i { transform: rotate(180deg); }
.dropdown-menu {
    position: absolute; top: 100%; left: 50%;
    transform: translateX(-50%) translateY(-10px);
    background: rgba(10, 26, 15, 0.98); backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 255, 136, 0.2); border-radius: 8px;
    padding: 0.5rem 0; min-width: 220px; list-style: none;
    opacity: 0; visibility: hidden; transition: all 0.3s ease;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3); margin-top: 0.5rem;
}
.dropdown.active .dropdown-menu {
    opacity: 1; visibility: visible; transform: translateX(-50%) translateY(0);
}
.dropdown-menu li { width: 100%; }
.dropdown-menu a {
    display: block; padding: 0.75rem 1.5rem; color: rgba(255, 255, 255, 0.9);
    text-decoration: none; font-size: 0.9rem; transition: all 0.3s ease;
    border-left: 3px solid transparent;
}
.dropdown-menu a:hover {
    background: rgba(0, 255, 136, 0.1); border-left-color: #00ff88;
    color: #00ff88; padding-left: 1.75rem;
}
.dropdown-menu a::after { display: none !important; }
.nav-login, .nav-cta, .nav-cta1 {
    text-decoration: none !important; display: inline-flex !important;
    align-items: center; justify-content: center;
}
.nav-login::after, .nav-cta::after, .nav-cta1::after { display: none !important; }
.nav-login {
    color: var(--cosmic-green) !important; padding: 0.65rem 1.8rem !important;
    border: 1px solid rgba(0, 223, 129, 0.5); border-radius: 50px; font-weight: 600;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); font-size: 0.88rem;
    backdrop-filter: blur(10px); background: rgba(0, 223, 129, 0.05);
}
.nav-login:hover {
    background: rgba(0, 223, 129, 0.15); box-shadow: 0 0 20px rgba(0, 223, 129, 0.3);
    border-color: var(--cosmic-green); transform: translateY(-2px);
}
.nav-cta, .nav-cta1 {
    color: #000 !important; padding: 0.75rem 2rem !important;
    border-radius: 50px; font-weight: 750; text-decoration: none;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); font-size: 0.9rem;
    box-shadow: 0 0 25px rgba(0, 223, 129, 0.3);
    background: linear-gradient(135deg, var(--cosmic-green) 0%, var(--cosmic-accent, #7dd49a) 100%);
    border: none; white-space: nowrap;
}
.nav-cta:hover, .nav-cta1:hover {
    transform: translateY(-2px) scale(1.02); box-shadow: 0 10px 30px rgba(0, 223, 129, 0.5);
    filter: brightness(1.1);
}
.nav-cta:hover::before, .nav-cta1:hover::before { left: 100%; }
.mobile-menu-btn {
    display: none; background: none; border: none; color: white;
    font-size: 1.5rem; cursor: pointer; transition: all 0.3s ease; padding: 0.5rem;
}
.mobile-menu-btn:hover { color: #00ff88; transform: scale(1.1); }
@media (max-width: 768px) {
    .nav-links {
        position: fixed; top: 70px; left: 0; right: 0;
        background: rgba(10, 26, 15, 0.98); flex-direction: column; align-items: center;
        padding: 1.5rem 0; gap: 0.5rem; display: none; backdrop-filter: blur(20px);
        z-index: 999; box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        border-bottom: 1px solid rgba(0, 255, 136, 0.2);
        max-height: calc(100vh - 70px); overflow-y: auto;
    }
    .nav-links.active { display: flex; animation: navSlideDown 0.3s ease-out; }
    @keyframes navSlideDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
    .mobile-menu-btn { display: block; }
    .nav-links li { width: 100%; text-align: center; }
    .nav-links a { font-size: 1.1rem; padding: 1rem 0; width: 100%; text-align: center; display: block; }
    .nav-links a::after { left: 50%; transform: translateX(-50%); }
    .nav-links a:hover::after, .nav-links a.active::after { width: 80%; }
    .nav-cta, .nav-cta1 { margin-left: 0 !important; padding: 0.9rem 4rem !important; min-width: 220px; text-align: center; margin-top: 0.5rem; }
    .dropdown { width: 100%; }
    .dropdown-toggle { justify-content: center; }
    .dropdown-menu { position: static; transform: none; width: 90%; margin: 0.5rem auto; opacity: 1; visibility: visible; display: none; }
    .dropdown.active .dropdown-menu { display: block; animation: navSlideDown 0.3s ease-out; }
    .logo { font-size: 1.5rem; }
    .logo img { height: 50px; }
}
@media (max-width: 1024px) and (min-width: 769px) {
    .nav-links { gap: 1rem; }
    .nav-links a { font-size: 0.9rem; }
    .nav-cta, .nav-cta1 { padding: 0.9rem 3rem !important; font-size: 1rem; min-width: 180px; }
}
</style>`;

    const NAV_HTML = `
<nav class="navbar" id="encarbonsys-navbar">
    <div class="nav-container">
        <a href="/" class="logo">
            <img src="/assets/images/encarbonsys-logo.png" onerror="this.src='https://image2url.com/images/1754762251826-aabbb9f2-5d26-42f3-b2a7-896ce713de40.png'" alt="EnCarbonSys Logo">
            EnCarbonSys
        </a>
        <button class="mobile-menu-btn" id="encav-mobileBtn" aria-label="Toggle Navigation">
            <i class="fas fa-bars"></i>
        </button>
        <ul class="nav-links" id="encav-navLinks">
            <li><a href="/index-new.html#problem">Problem</a></li>
            <li><a href="/index-new.html#solution">Solution</a></li>
            <li><a href="/pages/pricing.html">Pricing</a></li>
            <li class="dropdown" id="encav-toolsDropdown">
                <a href="#" class="dropdown-toggle">
                    Tools <i class="fas fa-chevron-down"></i>
                </a>
                <ul class="dropdown-menu">
                    <li><a href="https://cbam-tools.encarbonsys.com">CN Code Checker</a></li>
                    <li><a href="https://cbam-tools.encarbonsys.com/tools/emissions-calculator">Emissions Calculator</a></li>
                    <li><a href="https://cbam-tools.encarbonsys.com/tools/cbam-cost-estimator">CBAM Cost Estimator</a></li>
                </ul>
            </li>
            <li><a href="/cbam-blog/">Blog</a></li>
            <li><a href="/index-new.html#faq">FAQ</a></li>
            <li class="nav-cta-group" style="display:flex;align-items:center;gap:0.8rem;margin-left:1rem;">
                <a href="https://encam.encarbonsys.com/login" class="nav-login">Login</a>
                <a href="/index-new.html#cta" class="nav-cta">Get Started</a>
            </li>
        </ul>
    </div>
</nav>`;

    // Inject CSS into <head>
    document.head.insertAdjacentHTML('beforeend', NAV_CSS);

    // Inject navbar HTML
    const placeholder = document.getElementById('navbar-placeholder');
    if (placeholder) {
        placeholder.outerHTML = NAV_HTML;
    } else {
        // fallback: prepend to body
        document.body.insertAdjacentHTML('afterbegin', NAV_HTML);
    }

    // Wire up mobile toggle
    document.addEventListener('DOMContentLoaded', function () {
        initNavbar();
    });
    if (document.readyState !== 'loading') {
        initNavbar();
    }

    function initNavbar() {
        const mobileBtn = document.getElementById('encav-mobileBtn');
        const navLinks = document.getElementById('encav-navLinks');
        const toolsDrop = document.getElementById('encav-toolsDropdown');

        if (!mobileBtn || !navLinks) return;

        mobileBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            navLinks.classList.toggle('active');
        });

        if (toolsDrop) {
            toolsDrop.querySelector('.dropdown-toggle').addEventListener('click', function (e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault(); e.stopPropagation();
                    toolsDrop.classList.toggle('active');
                }
            });
        }

        document.addEventListener('click', function (e) {
            if (!navLinks.contains(e.target) && !mobileBtn.contains(e.target)) {
                navLinks.classList.remove('active');
                if (toolsDrop) toolsDrop.classList.remove('active');
            }
        });

        window.addEventListener('resize', function () {
            if (window.innerWidth > 768) {
                navLinks.classList.remove('active');
                if (toolsDrop) toolsDrop.classList.remove('active');
            }
        });

        // Highlight active link
        const currentPath = window.location.pathname;
        navLinks.querySelectorAll('a:not(.nav-cta)').forEach(function (link) {
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
        });
    }
})();
