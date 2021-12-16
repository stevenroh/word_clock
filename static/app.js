function update() {
  fetch('/leds').then((resp) => resp.json()).then(data => {
    console.log('update');

    const {leds, mode} = data;

    console.log(mode);
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

function sendAnimation(animation) {
  fetch(`/show?animation=${animation}`).then(res => {
    if (res.ok) {

    } else {
      console.log(res);
      alert('Error');
    }
  });
}