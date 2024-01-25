document.addEventListener('mousemove', (event) => {
  const follower = document.getElementById('custom-cursor');
  const mouseX = event.clientX;
  const mouseY = event.clientY;

  // Take into account the scroll position
  const scrollX = window.scrollX || window.pageXOffset;
  const scrollY = window.scrollY || window.pageYOffset;

  // Set the position of the follower element considering the scroll position
  follower.style.left = mouseX + scrollX + 'px';
  follower.style.top = mouseY + scrollY + 'px';
});

document.getElementById('menuButton').addEventListener('click', function () {
  const menu = document.getElementById('menu');
  menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
});