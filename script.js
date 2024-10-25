document.getElementById('image-upload').addEventListener('change', function(event) {
    const reader = new FileReader();
    reader.onload = function() {
        const profileImage = document.getElementById('profile-image');
        profileImage.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
});

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;

    if (name && email && message) {
        alert('Thank you, ' + name + '! Your message has been sent.');
    } else {
        alert('Please fill out all fields.');
    }
});
