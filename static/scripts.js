document.addEventListener('DOMContentLoaded', function() {
    const newsButton = document.getElementById('news-button');

    newsButton.addEventListener('click', function(event) {
        event.preventDefault();  // Prevent the default link behavior
        window.location.href = '/news';  // Navigate to the news page
    });
});
if (results.length === 0) {
    const noResultsMessage = document.createElement('li');
    noResultsMessage.textContent = 'No results found.';
    noResultsMessage.classList.add('no-results'); // Add class to style the message
    resultsList.appendChild(noResultsMessage);
}
