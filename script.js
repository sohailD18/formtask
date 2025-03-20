function calculateAge() {
    const dob = document.getElementById('dob').value;
    if (dob) {
        const dobDate = new Date(dob);
        const today = new Date();
        let age = today.getFullYear() - dobDate.getFullYear();
        const monthDifference = today.getMonth() - dobDate.getMonth();
        if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < dobDate.getDate())) {
            age--;
        }
        document.getElementById('age').value = age;
    }
}

function validateForm() {
    const firstName = document.getElementById('first_name').value.trim();
    const dob = document.getElementById('dob').value;
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    const phone = document.getElementById('phone').value.trim();
    const file = document.getElementById('photo').files[0];

    const gender = document.querySelector('input[name="gender"]:checked');
    const state = document.getElementById('state').value;
    const course = document.getElementById('courses').value;

    const firstNameRegex = /^[A-Za-z]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
    const phoneRegex = /^[6-9]\d{9}$/;

    if (!firstNameRegex.test(firstName)) {
        alert('First name must contain only letters.');
        return false;
    }

    if (!dob) {
        alert('Please enter your date of birth.');
        return false;
    }

    const dobDate = new Date(dob);
    const today = new Date();
    let age = today.getFullYear() - dobDate.getFullYear();
    const monthDifference = today.getMonth() - dobDate.getMonth();
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < dobDate.getDate())) {
        age--;
    }
    if (age < 18) {
        alert("You must be at least 18 years old.");
        return false;
    }

    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return false;
    }

    if (!passwordRegex.test(password)) {
        alert('Password must be at least 8 characters long and contain letters, numbers, and special characters.');
        return false;
    }

    if (password !== confirmPassword) {
        alert('Password and Confirm Password must match.');
        return false;
    }

    if (!phoneRegex.test(phone)) {
        alert('Phone number must be 10 digits and start with 6, 7, 8, or 9.');
        return false;
    }

    if (!gender) {
        alert('Please select your gender.');
        return false;
    }

    if (!state) {
        alert('Please select your state.');
        return false;
    }

    if (!course) {
        alert('Please select a course.');
        return false;
    }

    if (file) {
        const fileSize = file.size / 1024; // Size in KB
        const fileType = file.type;
        if (fileSize > 200) {
            alert('File size must be less than 200KB.');
            return false;
        }
        if (!['image/jpeg', 'image/png'].includes(fileType)) {
            alert('Only .jpg and .png files are allowed.');
            return false;
        }
    }

    return true;
}
