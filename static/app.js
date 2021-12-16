function update() {
  fetch('/leds').then((resp) => resp.json()).then(data => {
    console.log('update');

    const {leds, mode} = data;

    console.log(mode);

    document.querySelectorAll('.letter').forEach(el => el.classList.remove('on'));

    if (mode === 'time') {
      leds.forEach(led => {
        document.getElementById(`led-${led}`).classList.add("on");
      });
    }

    if (mode === 'animation') {
      leds.forEach((led, idx) => {
        console.log(led, idx)
        document.getElementById(`led-${idx}`).style.backgroundColor = `rgb(${led[0]}, ${led[1]}, ${led[2]})`;
        document.getElementById(`led-${idx}`).style.color = `rgb(${led[0]}, ${led[1]}, ${led[2]})`;
      });
    }
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
      window.location = '/'
    } else {
      console.log(res);
      alert('Error');
    }
  });
}


function enableClockMode() {
  fetch('/clock_mode').then(res => {
    if (res.ok) {
      window.location = '/'
    } else {
      console.log(res);
      alert('Error');
    }
  });
}

