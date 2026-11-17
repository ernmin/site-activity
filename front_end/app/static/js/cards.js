const cards = document.querySelectorAll('.card');
const track = document.querySelector('.carousel-track');
const scrollButtons = document.querySelectorAll('.carousel-button');

if (track && scrollButtons.length) {
  const updateScrollButtons = () => {
    const maxScroll = track.scrollWidth - track.clientWidth;
    scrollButtons.forEach(button => {
      const direction = Number(button.dataset.direction);
      button.disabled = direction < 0
        ? track.scrollLeft <= 0
        : track.scrollLeft >= maxScroll - 1;
    });
  };

  scrollButtons.forEach(button => {
    button.addEventListener('click', () => {
      const firstCard = track.querySelector('.card');
      if (!firstCard) return;

      const gap = parseFloat(getComputedStyle(track).columnGap) || 0;
      const distance = firstCard.getBoundingClientRect().width + gap;
      track.scrollBy({
        left: distance * Number(button.dataset.direction),
        behavior: 'smooth'
      });
    });
  });

  track.addEventListener('scroll', updateScrollButtons);
  window.addEventListener('resize', updateScrollButtons);
  updateScrollButtons();
}