function update() {
  fetch('/leds').then((resp) => resp.json()).then(leds => {
    console.log('update');

    document.querySelectorAll('.letter').forEach(el => el.classList.remove('on'));
    leds.forEach(led => {
      document.getElementById(`led-${led}`).classList.add("on");
    });
  });
}

function showLoader() {
  document.getElementById('loader').style.display = 'block';
}

function hideLoader() {
  document.getElementById('loader').style.display = 'none';
}

function sendTask(task) {
  showLoader();
  fetch(`/execute?task=${task}`).then(res => {
    if (res.ok) {
      hideLoader();
    } else {
      console.log(res);
      alert('Error');
    }
  });
}

function sendAnimation(animation, speed) {
  speedSec = speed / 1000;
  fetch(`/show?animation=${animation}&speed=${speedSec}`).then(res => {
    if (res.ok) {
      // window.location = '/'
    } else {
      console.log(res);
      alert('Error');
    }
  });
}


function enableClockMode() {
  fetch('/clock_mode').then(res => {
    if (res.ok) {
      // window.location = '/'
    } else {
      console.log(res);
      alert('Error');
    }
  });
}

