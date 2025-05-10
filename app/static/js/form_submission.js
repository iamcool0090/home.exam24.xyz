export async function submitContactForm(e) {
    e.preventDefault(); // Stop the default GET submission

    const form = document.getElementById('contact-form');
    const formData = new FormData(form);

    try {
        const response = await fetch('/contact', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            alert('Form submitted successfully!');
            form.reset();
        } else {
            console.log('Error submitting form:', response.statusText);
        }
    } catch (error) {
        alert('Something went wrong.');
        console.error(error);
    }
}
