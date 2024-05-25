document.addEventListener('DOMContentLoaded', function() {
    const newsButton = document.getElementById('news-button');

    newsButton.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default link behavior
        window.location.href = '/news';  // Navigate to the news page
    });
});
