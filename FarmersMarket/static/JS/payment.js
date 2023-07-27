// For UPI
document.getElementById('upi').addEventListener('change', function () {
  if (this.checked) {
    document.getElementById('upiid').style.display = 'block';
    document.getElementById('carddetails').style.display = 'none';
    document.getElementById('cod').style.display = 'none';
    document.getElementById('process').style.display = 'none';
    document.getElementById('done').style.display = 'block';
  } else {
    document.getElementById('upiid').style.display = 'none';
  }
});
// For Card
document.getElementById('paymentBycard').addEventListener('change', function () {
  if (this.checked) {
    document.getElementById('carddetails').style.display = 'block';
    document.getElementById('upiid').style.display = 'none';
    document.getElementById('cod').style.display = 'none';
    document.getElementById('process').style.display = 'none';
    document.getElementById('done').style.display = 'block';
  } else {
    document.getElementById('carddetails').style.display = 'none';
  }
});

// For COD
document.getElementById('codcheck').addEventListener('change', function () {
  if (this.checked) {
    document.getElementById('cod').style.display = 'block';
    document.getElementById('upiid').style.display = 'none';
    document.getElementById('carddetails').style.display = 'none';
    document.getElementById('process').style.display = 'block';
    document.getElementById('done').style.display = 'none';
  } else {
    document.getElementById('cod').style.display = 'none';
    document.getElementById('process').style.display = 'none';
    document.getElementById('done').style.display = 'block';
  }
});

document.getElementById('done').addEventListener('click', function () {
  window.location.href = '/';
})

// Generate a random math question
function generateCaptcha() {
  const num1 = Math.floor(Math.random() * 10);
  const num2 = Math.floor(Math.random() * 10);
  return `${num1} + ${num2}`;
}

const captchaSpan = document.getElementById('captcha');
const captchaInput = document.getElementById('captchaInput');
const submitBtn = document.getElementById('process');

// Display a random math question
captchaSpan.innerText = generateCaptcha();

submitBtn.addEventListener('click', function (event) {
  event.preventDefault();

  // Validate the user's answer
  const captchaAnswer = eval(captchaSpan.innerText);
  if (parseInt(captchaInput.value) === captchaAnswer) {
    // Correct answer
    window.location.href = '/';
    // submit the form or do other actions
  } else {
    // Incorrect answer
    alert('Incorrect captcha answer. Please try again.');
    // Generate a new captcha question
    captchaSpan.innerText = generateCaptcha();
    captchaInput.value = '';
  }
});
