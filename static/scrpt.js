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

win_x = (window.innerWidth * 0.95);
win_y = (window.innerHeight * 0.70);

document.addEventListener('DOMContentLoaded', function(){
  var rcb = document.getElementById('rcb');

  if (rcb){
    rcb.style.width = win_x + 'px';
    rcb.style.height = rcb.scrollHeight + 10 + 'px';
    rcb.style.backgroundColor = '#3c3b3d';
    rcb.style.borderRadius = '20px';
    rcb.style.boxShadow = '5px 5px 10px rgb(0, 0, 20)';
    rcb.style.marginLeft = 'auto';
    rcb.style.marginRight = 'auto';
    console.log("Yeah got it");
  }else{
    console.error("Fuck u!")
  }
  

  console.log(win_y);
});

