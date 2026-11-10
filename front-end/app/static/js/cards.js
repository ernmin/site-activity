const cards = document.querySelectorAll('.card');

cards.forEach(card => {
  card.addEventListener('click', () => {
    // Smoothly scroll the clicked card into the center of the viewport
    card.scrollIntoView({
      behavior: 'smooth',
      block: 'nearest',   // Prevents the whole webpage from jumping up/down
      inline: 'center'    // Align the card perfectly to the horizontal center
    });
  });
});